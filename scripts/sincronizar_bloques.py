#!/usr/bin/env python3
"""Sincroniza bloques y archivos comunes de `compartido/` dentro de las skills.

Uso: python scripts/sincronizar_bloques.py [--verificar] [raiz]
Sin opciones reescribe los SKILL.md y copia los archivos compartidos;
con `--verificar` solo comprueba y sale con 1 si hay diferencias.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun  # noqa: E402

REGEX_INICIO = re.compile(r"<!-- inicio:([A-Za-z0-9_\-]+) -->")
ARCHIVO_COMPARTIDOS = "archivos-compartidos.json"


def cargar_bloques(carpeta: Path) -> dict[str, str]:
    carpeta = Path(carpeta)
    if not carpeta.is_dir():
        return {}
    return {
        p.stem: p.read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip()
        for p in sorted(carpeta.glob("*.md"))
    }


def aplicar_bloques(texto: str, bloques: dict[str, str]) -> str:
    """Reemplaza el contenido entre marcadores inicio/fin por el bloque comun."""
    salida: list[str] = []
    pos = 0
    while True:
        m = REGEX_INICIO.search(texto, pos)
        if m is None:
            salida.append(texto[pos:])
            break
        nombre = m.group(1)
        if nombre not in bloques:
            raise ValueError(f"bloque desconocido '{nombre}' (no existe en compartido/)")
        fin = f"<!-- fin:{nombre} -->"
        i_fin = texto.find(fin, m.end())
        if i_fin == -1:
            raise ValueError(f"falta el cierre '{fin}' del bloque '{nombre}'")
        salida.append(texto[pos:m.end()])
        salida.append("\n" + bloques[nombre] + "\n")
        salida.append(fin)
        pos = i_fin + len(fin)
    return "".join(salida)


def _validar_destino(d: str) -> list[str]:
    partes = d.split("/")
    if len(partes) < 3 or any(p in ("", ".", "..") or "\\" in p or Path(p).name != p for p in partes):
        raise ValueError(f"destino inválido '{d}' (use <plugin>/<skill>/<subcarpeta>)")
    return partes


def cargar_archivos_compartidos(raiz: Path) -> dict[str, list[str]]:
    raiz = Path(raiz)
    ruta = raiz / "compartido" / ARCHIVO_COMPARTIDOS
    if not ruta.is_file():
        return {}
    datos = json.loads(ruta.read_text(encoding="utf-8-sig"))
    if not isinstance(datos, dict):
        raise ValueError(f"{ARCHIVO_COMPARTIDOS} debe ser un objeto JSON")
    for origen, destinos in datos.items():
        if not (raiz / "compartido" / "archivos" / origen).is_file():
            raise ValueError(f"archivo compartido inexistente: compartido/archivos/{origen}")
        if not isinstance(destinos, list) or not all(isinstance(d, str) for d in destinos):
            raise ValueError(f"destinos inválidos para '{origen}' (se espera una lista de textos)")
        for d in destinos:
            _validar_destino(d)
    return datos


def _destinos(raiz: Path):
    """Itera (origen, destino, ruta relativa) de cada copia declarada."""
    for origen, destinos in cargar_archivos_compartidos(raiz).items():
        fuente = Path(raiz) / "compartido" / "archivos" / origen
        for d in destinos:
            partes = _validar_destino(d)
            plugin, skill, sub = partes[0], partes[1], "/".join(partes[2:])
            destino = Path(raiz) / "plugins" / plugin / "skills" / skill / sub / Path(origen).name
            yield fuente, destino


def copiar_archivos(raiz: Path) -> list[Path]:
    escritas: list[Path] = []
    for fuente, destino in _destinos(Path(raiz)):
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(fuente.read_bytes())
        escritas.append(destino)
    return escritas


def _skill_mds(raiz: Path) -> list[Path]:
    return [s / "SKILL.md" for p in comun.encontrar_plugins(raiz) for s in comun.encontrar_skills(p)]


def _rel(ruta: Path, raiz: Path) -> str:
    try:
        return Path(ruta).relative_to(raiz).as_posix()
    except ValueError:
        return Path(ruta).as_posix()


def aplicar_a_skills(raiz: Path) -> list[Path]:
    """Reescribe los SKILL.md desincronizados; devuelve los modificados."""
    raiz = Path(raiz)
    bloques = cargar_bloques(raiz / "compartido")
    cambiados: list[Path] = []
    for md in _skill_mds(raiz):
        original = md.read_text(encoding="utf-8").replace("\r\n", "\n")
        nuevo = aplicar_bloques(original, bloques)
        if nuevo != original:
            md.write_text(nuevo, encoding="utf-8", newline="\n")
            cambiados.append(md)
    return cambiados


def sincronizar(raiz: Path) -> list[Path]:
    raiz = Path(raiz)
    return aplicar_a_skills(raiz) + copiar_archivos(raiz)


def verificar(raiz: Path) -> list[str]:
    raiz = Path(raiz)
    mensajes: list[str] = []
    bloques = cargar_bloques(raiz / "compartido")
    for md in _skill_mds(raiz):
        texto = md.read_text(encoding="utf-8").replace("\r\n", "\n")
        try:
            if aplicar_bloques(texto, bloques) != texto:
                mensajes.append(f"{_rel(md, raiz)}: bloques comunes desincronizados (ejecute scripts/sincronizar_bloques.py)")
        except ValueError as e:
            mensajes.append(f"{_rel(md, raiz)}: {e}")
    try:
        for fuente, destino in _destinos(raiz):
            r = _rel(destino, raiz)
            if not destino.is_file():
                mensajes.append(f"{r}: falta la copia del archivo compartido (ejecute scripts/sincronizar_bloques.py)")
            elif destino.read_bytes() != fuente.read_bytes():
                mensajes.append(f"{r}: copia distinta de compartido/archivos/{fuente.name} (ejecute scripts/sincronizar_bloques.py)")
    except (ValueError, json.JSONDecodeError) as e:
        mensajes.append(f"compartido/{ARCHIVO_COMPARTIDOS}: {e}")
    return mensajes


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if a != "--verificar"]
    solo_verificar = len(args) != len(argv) - 1
    raiz = Path(args[0]).resolve() if args else Path(__file__).resolve().parent.parent
    try:
        if solo_verificar:
            mensajes = verificar(raiz)
            for m in mensajes:
                print(m)
            if mensajes:
                return 1
            print("OK: bloques y archivos sincronizados")
            return 0
        escritas = sincronizar(raiz)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    for ruta in escritas:
        print(f"actualizado: {_rel(ruta, raiz)}")
    print(f"OK: {len(escritas)} archivos actualizados")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
