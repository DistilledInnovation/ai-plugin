#!/usr/bin/env python3
"""Empaquetador multiplataforma (solo biblioteca estandar).

Uso: python scripts/empaquetar.py [raiz]
Valida el repo (aborta si hay errores) y escribe en `dist/`:
- `<skill>-v<version>.zip` por skill (raiz `<skill>/SKILL.md`, para Claude.ai y ChatGPT),
- `<plugin>-v<version>.plugin` por plugin (sin `evals/`),
- `<plugin>-copiar-pegar-v<version>.zip` (INSTRUCCIONES.md + archivos de conocimiento).
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun  # noqa: E402
import sincronizar_bloques  # noqa: E402
import validar  # noqa: E402

FECHA_FIJA = (1980, 1, 1, 0, 0, 0)
MAX_INSTRUCCIONES = 8000
MAX_CONOCIMIENTO = 9  # + INSTRUCCIONES.md = 10 archivos

PREFIJO_FACILITADOR = "facilitador-"
CONSULTA = (
    "Cuando necesites el detalle de una skill, consulta el archivo de conocimiento "
    "correspondiente (los archivos `NN-*.md` adjuntos) antes de responder."
)


def _escribir(z: zipfile.ZipFile, arcname: str, datos: bytes) -> None:
    info = zipfile.ZipInfo(arcname, FECHA_FIJA)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    info.create_system = 3
    z.writestr(info, datos)


def _zip(destino: Path, entradas: list[tuple[str, bytes]]) -> Path:
    destino.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destino, "w") as z:
        for arcname, datos in sorted(entradas, key=lambda e: e[0]):
            _escribir(z, arcname, datos)
    return destino


def _archivos(carpeta: Path) -> list[Path]:
    return sorted(p for p in Path(carpeta).rglob("*") if p.is_file() and "__pycache__" not in p.parts)


def zip_skill(skill: Path, destino: Path, version: str) -> Path:
    skill = Path(skill)
    entradas = [(f"{skill.name}/{p.relative_to(skill).as_posix()}", p.read_bytes()) for p in _archivos(skill)]
    return _zip(Path(destino) / f"{skill.name}-v{version}.zip", entradas)


def _version(plugin: Path) -> str:
    datos = json.loads((Path(plugin) / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8-sig"))
    return datos["version"]


def zip_plugin(plugin: Path, destino: Path) -> Path:
    plugin = Path(plugin)
    entradas = []
    for p in _archivos(plugin):
        rel = p.relative_to(plugin)
        if rel.parts[0] == "evals":
            continue
        entradas.append((rel.as_posix(), p.read_bytes()))
    return _zip(Path(destino) / f"{plugin.name}-v{_version(plugin)}.plugin", entradas)


def _leer(ruta: Path) -> str:
    return Path(ruta).read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def _seccion_proceso(texto: str) -> str:
    """Contenido de la seccion `## Proceso...` hasta el siguiente `## `."""
    lineas = texto.split("\n")
    dentro, salida = False, []
    for linea in lineas:
        if linea.startswith("## "):
            if dentro:
                break
            dentro = linea.startswith("## Proceso")
            continue
        if dentro:
            salida.append(linea)
    return "\n".join(salida).strip()


def _cuerpo(skill: Path) -> str:
    """Texto de conocimiento de una skill: SKILL.md + references/ + assets/."""
    texto = _leer(skill / "SKILL.md").strip()
    partes = [f"# {skill.name}\n\n(Skill `{skill.name}`)\n\n" + _quitar_frontmatter(texto)]
    for sub in ("references", "assets"):
        base = skill / sub
        if base.is_dir():
            for p in _archivos(base):
                rel = p.relative_to(skill).as_posix()
                partes.append(f"## Archivo: {skill.name}/{rel}\n\n{_leer(p).strip()}")
    return "\n\n".join(partes) + "\n"


def _quitar_frontmatter(texto: str) -> str:
    m = re.match(r"^---\n.*?\n---\n?", texto, re.S)
    return texto[m.end():].strip() if m else texto


def _grupos(n: int, maximo: int) -> list[range]:
    """Reparte n elementos en <= maximo grupos contiguos y balanceados."""
    k = min(n, maximo)
    if k == 0:
        return []
    base, resto = divmod(n, k)
    grupos, inicio = [], 0
    for i in range(k):
        largo = base + (1 if i < resto else 0)
        grupos.append(range(inicio, inicio + largo))
        inicio += largo
    return grupos


def paquete_copiar_pegar(plugin: Path, raiz: Path, destino: Path) -> Path:
    plugin, raiz = Path(plugin), Path(raiz)
    skills = comun.encontrar_skills(plugin)
    grupos = _grupos(len(skills), MAX_CONOCIMIENTO)
    archivos: list[tuple[str, str]] = []  # (nombre de archivo, contenido)
    donde: dict[str, str] = {}
    for i, grupo in enumerate(grupos, start=1):
        primero, ultimo = skills[grupo[0]].name, skills[grupo[-1]].name
        sufijo = primero if primero == ultimo else f"{primero}-a-{ultimo}"
        nombre = f"{i:02d}-{sufijo}.md"
        archivos.append((nombre, "\n\n".join(_cuerpo(skills[j]) for j in grupo)))
        for j in grupo:
            donde[skills[j].name] = nombre

    bloques = sincronizar_bloques.cargar_bloques(raiz / "compartido")
    proceso = ""
    for s in skills:
        if s.name.startswith(PREFIJO_FACILITADOR):
            proceso = _seccion_proceso(_leer(s / "SKILL.md"))
            break

    def armar(con_descripciones: bool) -> str:
        partes = [f"# Instrucciones: {plugin.name}"]
        partes.extend(bloques[k] for k in sorted(bloques))
        if proceso:
            partes.append("## Proceso del facilitador\n\n" + proceso)
        if skills:
            lineas = []
            for s in skills:
                desc = comun.leer_frontmatter(_leer(s / "SKILL.md")).get("description", "")
                lineas.append(f"- {s.name}: {desc}" if con_descripciones else f"- {s.name}")
                lineas[-1] += f" (archivo: {donde[s.name]})"
            partes.append("## Skills disponibles\n\n" + CONSULTA + "\n\n" + "\n".join(lineas))
        return "\n\n".join(partes) + "\n"

    instrucciones = armar(True)
    if len(instrucciones) > MAX_INSTRUCCIONES:
        instrucciones = armar(False)
    if len(instrucciones) > MAX_INSTRUCCIONES:
        raise ValueError(
            f"INSTRUCCIONES.md de {plugin.name} excede {MAX_INSTRUCCIONES} caracteres ({len(instrucciones)})"
        )
    entradas = [("INSTRUCCIONES.md", instrucciones.encode("utf-8"))]
    entradas += [(n, c.encode("utf-8")) for n, c in archivos]
    return _zip(Path(destino) / f"{plugin.name}-copiar-pegar-v{_version(plugin)}.zip", entradas)


def main(argv: list[str]) -> int:
    raiz = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parent.parent
    errores = validar.validar_repo(raiz, comun.cargar_terminos(raiz))
    if errores:
        for e in errores:
            print(e)
        print("error: la validación falló; no se empaqueta", file=sys.stderr)
        return 1
    dist = raiz / "dist"
    dist.mkdir(exist_ok=True)
    generados: list[Path] = []
    try:
        for plugin in comun.encontrar_plugins(raiz):
            version = _version(plugin)
            generados.append(zip_plugin(plugin, dist))
            generados.append(paquete_copiar_pegar(plugin, raiz, dist))
            for skill in comun.encontrar_skills(plugin):
                generados.append(zip_skill(skill, dist, version))
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    for g in generados:
        print(f"generado: dist/{g.name}")
    print(f"OK: {len(generados)} paquetes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
