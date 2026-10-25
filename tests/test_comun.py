import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import comun  # noqa: E402


class PruebasComun(unittest.TestCase):
    def test_frontmatter_con_bom_y_crlf(self):
        texto = "\ufeff---\r\nname: a\r\ndescription: b\r\n---\r\n# x"
        self.assertEqual(comun.leer_frontmatter(texto), {"name": "a", "description": "b"})

    def test_frontmatter_ausente_lanza(self):
        with self.assertRaises(ValueError):
            comun.leer_frontmatter("# solo un título\n")

    def test_normalizar_tildes_y_mayusculas(self):
        self.assertEqual(comun.normalizar("LÁCTEOS Ñu"), "lacteos nu")

    def test_cargar_terminos_desde_env(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.dict(
            os.environ, {"TERMINOS_PROHIBIDOS": "uno\n\n# comentario\ndos words\n"}
        ):
            self.assertEqual(comun.cargar_terminos(Path(tmp)), ["uno", "dos words"])

    def test_cargar_terminos_desde_archivo(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.dict(
            os.environ, {"TERMINOS_PROHIBIDOS": "ignorado"}
        ):
            (Path(tmp) / ".terminos-prohibidos.txt").write_text("# c\n\nalfa\nbeta\n", encoding="utf-8")
            self.assertEqual(comun.cargar_terminos(Path(tmp)), ["alfa", "beta"])

    def test_encontrar_plugins_y_skills_ordenados(self):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            for nombre in ("zeta", "alfa"):
                (raiz / "plugins" / nombre / ".claude-plugin").mkdir(parents=True)
                (raiz / "plugins" / nombre / ".claude-plugin" / "plugin.json").write_text("{}")
            (raiz / "plugins" / "sin-manifiesto").mkdir()
            self.assertEqual([p.name for p in comun.encontrar_plugins(raiz)], ["alfa", "zeta"])
            for nombre in ("b", "a"):
                (raiz / "plugins" / "alfa" / "skills" / nombre).mkdir(parents=True)
                (raiz / "plugins" / "alfa" / "skills" / nombre / "SKILL.md").write_text("x")
            (raiz / "plugins" / "alfa" / "skills" / "vacia").mkdir()
            self.assertEqual(
                [s.name for s in comun.encontrar_skills(raiz / "plugins" / "alfa")], ["a", "b"]
            )


if __name__ == "__main__":
    unittest.main()
