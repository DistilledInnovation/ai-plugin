#!/usr/bin/env python3
"""Validador de skills, plugins y marketplace (solo biblioteca estandar).

Uso: python scripts/validar.py [raiz]
Imprime errores `ruta: mensaje`; exit 1 si hay errores, 0 y `OK: N skills` si no.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun  # noqa: E402
import sincronizar_bloques  # noqa: E402

REGEX_NOMBRE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REGEX_SEMVER = re.compile(r"^\d+\.\d+\.\d+(-[0-9A-Za-z.\-]+)?(\+[0-9A-Za-z.\-]+)?$")
EXTENSIONES_PERMITIDAS = {".md", ".txt", ".json", ".yaml", ".yml", ".csv"}
MAX_DESCRIPTION = 1024
MAX_SKILL = 20000
FRASE_USO = "Úsala cuando"
CAMPOS_FRONTMATTER = {"name", "description"}
RUTAS_TERMINOS = ("plugins", "docs", "README.md", "AGENTS.md")


def _rel(ruta: Path, base: Path | None) -> str:
    if base is None:
        return ruta.as_posix()
    try:
        return ruta.relative_to(base).as_posix()
    except ValueError:
        return ruta.as_posix()


def _leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8-sig", errors="replace")


def _archivos(carpeta: Path) -> list[Path]:
    return sorted(p for p in carpeta.rglob("*") if p.is_file())


def _coincide_termino(texto_normalizado: str, termino: str) -> bool:
    t = re.sub(r"\s+", " ", comun.normalizar(termino)).strip()
    if not t:
        return False
    return re.search(r"(?<!\w)" + re.escape(t) + r"(?!\w)", texto_normalizado) is not None


def _validar_archivo(ruta: Path, base: Path | None, terminos: list[str], revisar_padre: bool) -> list[str]:
    """Extension, JSON valido, terminos prohibidos y (opcional) rutas `../`."""
    errores: list[str] = []
    r = _rel(ruta, base)
    ext = ruta.suffix.lower()
    if ext not in EXTENSIONES_PERMITIDAS:
        errores.append(f"{r}: extensión no permitida '{ext or ruta.name}' (permitidas: {', '.join(sorted(EXTENSIONES_PERMITIDAS))})")
        return errores
    texto = _leer(ruta)
    if ext == ".json":
        try:
            json.loads(texto)
        except json.JSONDecodeError as e:
            errores.append(f"{r}: JSON inválido ({e.msg}, línea {e.lineno})")
    if revisar_padre and "../" in texto.replace("..\\", "../"):
        errores.append(f"{r}: referencia a ruta con ../ (no permitida)")
    errores.extend(_errores_terminos(r, texto, terminos))
    return errores


def _errores_terminos(r: str, texto: str, terminos: list[str]) -> list[str]:
    if not terminos:
        return []
    normal = re.sub(r"\s+", " ", comun.normalizar(texto))
    errores = []
    for termino in terminos:
        if _coincide_termino(normal, termino):
            errores.append(f"{r}: término prohibido detectado (caso real o cliente)")
            break  # no se imprime el termino para no filtrarlo en los logs
    return errores


def _validar_skill(skill: Path, terminos: list[str], base: Path | None) -> list[str]:
    errores: list[str] = []
    archivo = skill / "SKILL.md"
    r = _rel(archivo, base)
    if not archivo.is_file():
        return [f"{r}: falta SKILL.md"]
    texto = _leer(archivo)
    try:
        fm = comun.leer_frontmatter(texto)
    except ValueError as e:
        errores.append(f"{r}: frontmatter inválido ({e})")
        fm = None
    if fm is not None:
        extra = sorted(set(fm) - CAMPOS_FRONTMATTER)
        faltan = sorted(CAMPOS_FRONTMATTER - set(fm))
        if extra:
            errores.append(f"{r}: frontmatter con campos no permitidos: {', '.join(extra)}")
        if faltan:
            errores.append(f"{r}: frontmatter sin campos obligatorios: {', '.join(faltan)}")
        nombre = fm.get("name")
        if nombre is not None:
            if nombre != skill.name:
                errores.append(f"{r}: name '{nombre}' distinto de la carpeta '{skill.name}'")
            if not REGEX_NOMBRE.match(nombre):
                errores.append(f"{r}: name '{nombre}' no cumple kebab-case ^[a-z0-9]+(-[a-z0-9]+)*$")
        desc = fm.get("description")
        if desc is not None:
            if len(desc) > MAX_DESCRIPTION:
                errores.append(f"{r}: description de {len(desc)} caracteres supera el máximo de {MAX_DESCRIPTION}")
            if FRASE_USO not in desc:
                errores.append(f"{r}: description debe contener la frase '{FRASE_USO}'")
    if len(texto) > MAX_SKILL:
        errores.append(f"{r}: SKILL.md de {len(texto)} caracteres supera el máximo de {MAX_SKILL}")
    for ruta in _archivos(skill):
        errores.extend(_validar_archivo(ruta, base, terminos, revisar_padre=True))
    return errores


def validar_skill(skill: Path, terminos: list[str]) -> list[str]:
    return _validar_skill(Path(skill), terminos, None)


def _cargar_json(ruta: Path):
    try:
        return json.loads(_leer(ruta))
    except (json.JSONDecodeError, OSError):
        return None  # el error de JSON ya lo reporta _validar_archivo


def _validar_plugin(plugin: Path, raiz: Path) -> tuple[list[str], str | None]:
    errores: list[str] = []
    ruta = plugin / ".claude-plugin" / "plugin.json"
    r = _rel(ruta, raiz)
    datos = _cargar_json(ruta)
    if not isinstance(datos, dict):
        errores.append(f"{r}: plugin.json debe ser un objeto JSON válido")
        return errores, None
    if datos.get("name") != plugin.name:
        errores.append(f"{r}: plugin.json name '{datos.get('name')}' distinto de la carpeta '{plugin.name}'")
    version = datos.get("version")
    if not isinstance(version, str) or not REGEX_SEMVER.match(version):
        errores.append(f"{r}: plugin.json version '{version}' no es semver (X.Y.Z)")
    if not isinstance(datos.get("description"), str) or not datos["description"].strip():
        errores.append(f"{r}: plugin.json requiere description")
    return errores, version if isinstance(version, str) else None


def _validar_marketplace(raiz: Path, plugins: list[Path], versiones: dict[str, str | None]) -> list[str]:
    errores: list[str] = []
    if not plugins:
        return errores
    ruta = raiz / ".claude-plugin" / "marketplace.json"
    r = _rel(ruta, raiz)
    if not ruta.is_file():
        return [f"{r}: falta marketplace.json"]
    datos = _cargar_json(ruta)
    if not isinstance(datos, dict) or not isinstance(datos.get("plugins"), list):
        return [f"{r}: marketplace.json debe tener una lista 'plugins' (JSON válido)"]
    entradas = {e.get("name"): e for e in datos["plugins"] if isinstance(e, dict)}
    for plugin in plugins:
        e = entradas.get(plugin.name)
        if e is None:
            errores.append(f"{r}: marketplace no lista el plugin '{plugin.name}'")
            continue
        if e.get("source") != f"./plugins/{plugin.name}":
            errores.append(f"{r}: marketplace source de '{plugin.name}' debe ser './plugins/{plugin.name}'")
        if versiones.get(plugin.name) and e.get("version") != versiones[plugin.name]:
            errores.append(
                f"{r}: marketplace version '{e.get('version')}' de '{plugin.name}' distinta de plugin.json '{versiones[plugin.name]}'"
            )
    return errores


def validar_repo(raiz: Path, terminos: list[str], avisos: list[str] | None = None) -> list[str]:
    raiz = Path(raiz)
    errores: list[str] = []
    plugins = comun.encontrar_plugins(raiz)
    versiones: dict[str, str | None] = {}
    carpetas_skills: set[Path] = set()
    for plugin in plugins:
        e, version = _validar_plugin(plugin, raiz)
        errores.extend(e)
        versiones[plugin.name] = version
        skills = comun.encontrar_skills(plugin)
        if not skills and avisos is not None:
            avisos.append(f"{_rel(plugin, raiz)}: el plugin no tiene skills todavía")
        for skill in skills:
            carpetas_skills.add(skill)
            errores.extend(_validar_skill(skill, terminos, raiz))
            eval_prompt = plugin / "evals" / skill.name / "prompt.md"
            if not eval_prompt.is_file():
                errores.append(f"{_rel(eval_prompt, raiz)}: falta eval de la skill '{skill.name}'")
    errores.extend(_validar_marketplace(raiz, plugins, versiones))

    # Archivos de plugins fuera de las skills (ya validadas), y textos del repo.
    base_plugins = raiz / "plugins"
    if base_plugins.is_dir():
        for ruta in _archivos(base_plugins):
            if any(s in ruta.parents for s in carpetas_skills):
                continue
            errores.extend(_validar_archivo(ruta, raiz, terminos, revisar_padre=False))
    for nombre in RUTAS_TERMINOS[1:]:
        destino = raiz / nombre
        if destino.is_file():
            errores.extend(_errores_terminos(_rel(destino, raiz), _leer(destino), terminos))
        elif destino.is_dir():
            for ruta in _archivos(destino):
                if ruta.suffix.lower() in EXTENSIONES_PERMITIDAS:
                    errores.extend(_errores_terminos(_rel(ruta, raiz), _leer(ruta), terminos))

    errores.extend(sincronizar_bloques.verificar(raiz))
    vistos: set[str] = set()
    return [e for e in errores if not (e in vistos or vistos.add(e))]


def contar_skills(raiz: Path) -> int:
    return sum(len(comun.encontrar_skills(p)) for p in comun.encontrar_plugins(raiz))


def main(argv: list[str]) -> int:
    raiz = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parent.parent
    terminos = comun.cargar_terminos(raiz)
    avisos: list[str] = []
    errores = validar_repo(raiz, terminos, avisos)
    for a in avisos:
        print(f"ADVERTENCIA {a}", file=sys.stderr)
    if errores:
        for e in errores:
            print(e)
        return 1
    print(f"OK: {contar_skills(raiz)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
