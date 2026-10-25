"""Utilidades comunes para los scripts del repo (solo biblioteca estandar)."""
from __future__ import annotations

import os
import re
import unicodedata
from pathlib import Path

ARCHIVO_TERMINOS = ".terminos-prohibidos.txt"
VARIABLE_TERMINOS = "TERMINOS_PROHIBIDOS"


def leer_frontmatter(texto: str) -> dict[str, str]:
    """Lee el bloque `---` inicial y devuelve un dict clave -> valor (texto).

    Tolera BOM y saltos CRLF. Lanza ValueError si no hay bloque de frontmatter.
    Soporta valores en una linea, entre comillas y bloques `>` / `|` o lineas
    de continuacion con sangria.
    """
    texto = texto.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    lineas = texto.split("\n")
    if not lineas or lineas[0].strip() != "---":
        raise ValueError("no hay bloque frontmatter (---) al inicio")
    datos: dict[str, str] = {}
    clave: str | None = None
    cerrado = False
    for linea in lineas[1:]:
        if linea.strip() == "---":
            cerrado = True
            break
        coincide = re.match(r"^([A-Za-z0-9_\-]+)\s*:\s*(.*)$", linea)
        if coincide and not linea[:1].isspace():
            clave, valor = coincide.group(1), coincide.group(2).strip()
            if valor in (">", "|", ">-", "|-", ">+", "|+"):
                valor = ""
            elif len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
                valor = valor[1:-1]
            datos[clave] = valor
        elif clave is not None and linea.strip():
            datos[clave] = (datos[clave] + " " + linea.strip()).strip()
    if not cerrado:
        raise ValueError("el bloque frontmatter no se cierra con ---")
    return datos


def encontrar_plugins(raiz: Path) -> list[Path]:
    base = Path(raiz) / "plugins"
    if not base.is_dir():
        return []
    return sorted(
        (p for p in base.iterdir() if (p / ".claude-plugin" / "plugin.json").is_file()),
        key=lambda p: p.name,
    )


def encontrar_skills(plugin: Path) -> list[Path]:
    base = Path(plugin) / "skills"
    if not base.is_dir():
        return []
    return sorted(
        (p for p in base.iterdir() if (p / "SKILL.md").is_file()),
        key=lambda p: p.name,
    )


def normalizar(texto: str) -> str:
    """Minusculas sin tildes (NFKD, descarta marcas combinantes)."""
    descompuesto = unicodedata.normalize("NFKD", texto)
    sin_marcas = "".join(c for c in descompuesto if not unicodedata.combining(c))
    return sin_marcas.lower()


def cargar_terminos(raiz: Path) -> list[str]:
    """Lee `.terminos-prohibidos.txt` o la variable TERMINOS_PROHIBIDOS."""
    archivo = Path(raiz) / ARCHIVO_TERMINOS
    if archivo.is_file():
        lineas = archivo.read_text(encoding="utf-8-sig").splitlines()
    else:
        lineas = os.environ.get(VARIABLE_TERMINOS, "").splitlines()
    terminos = []
    for linea in lineas:
        linea = linea.strip()
        if linea and not linea.startswith("#"):
            terminos.append(linea)
    return terminos
