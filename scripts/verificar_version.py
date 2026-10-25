#!/usr/bin/env python3
"""Verifica que la version de un tag coincida con los manifiestos (solo biblioteca estandar).

Uso: python scripts/verificar_version.py <tag> [raiz]
El tag puede llevar una `v` inicial (`v0.1.0`). Compara contra `version` en cada
`plugins/*/.claude-plugin/plugin.json` y en cada plugin de `.claude-plugin/marketplace.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun  # noqa: E402


def _json(ruta: Path):
    return json.loads(Path(ruta).read_text(encoding="utf-8-sig"))


def verificar(tag: str, raiz: Path) -> list[str]:
    raiz = Path(raiz)
    esperada = tag[1:] if tag.startswith("v") else tag
    errores: list[str] = []
    for plugin in comun.encontrar_plugins(raiz):
        ruta = plugin / ".claude-plugin" / "plugin.json"
        version = _json(ruta).get("version")
        if version != esperada:
            errores.append(f"{ruta.relative_to(raiz).as_posix()}: version {version!r} != tag {esperada!r}")
    ruta = raiz / ".claude-plugin" / "marketplace.json"
    if ruta.is_file():
        for entrada in _json(ruta).get("plugins", []):
            version = entrada.get("version")
            if version != esperada:
                errores.append(
                    f".claude-plugin/marketplace.json: {entrada.get('name')} version {version!r} != tag {esperada!r}"
                )
    return errores


def main(argv: list[str]) -> int:
    if len(argv) < 2 or not argv[1].strip():
        print("uso: verificar_version.py <tag> [raiz]", file=sys.stderr)
        return 2
    raiz = Path(argv[2]).resolve() if len(argv) > 2 else Path(__file__).resolve().parent.parent
    errores = verificar(argv[1].strip(), raiz)
    for e in errores:
        print(e)
    if errores:
        print("error: la versión del tag no coincide con los manifiestos", file=sys.stderr)
        return 1
    print(f"OK: todos los manifiestos están en {argv[1].strip().lstrip('v')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
