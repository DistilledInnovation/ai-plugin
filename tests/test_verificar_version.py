import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "scripts"))
import verificar_version  # noqa: E402

FIXTURE = AQUI / "fixtures" / "repo_valido"


class PruebasVersion(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.raiz = Path(self._tmp.name) / "repo"
        shutil.copytree(FIXTURE, self.raiz)
        self.plugin_json = self.raiz / "plugins" / "demo" / ".claude-plugin" / "plugin.json"

    def test_coincide_con_y_sin_v(self):
        self.assertEqual(verificar_version.verificar("v0.1.0", self.raiz), [])
        self.assertEqual(verificar_version.verificar("0.1.0", self.raiz), [])

    def test_difiere_en_plugin_json(self):
        errores = verificar_version.verificar("v0.2.0", self.raiz)
        self.assertTrue(any("plugin.json" in e for e in errores), errores)

    def test_difiere_en_marketplace(self):
        mk = self.raiz / ".claude-plugin" / "marketplace.json"
        if not mk.is_file():
            mk.parent.mkdir(exist_ok=True)
            mk.write_text(json.dumps({"plugins": [{"name": "demo", "version": "0.0.9"}]}), encoding="utf-8")
        else:
            d = json.loads(mk.read_text(encoding="utf-8"))
            for p in d["plugins"]:
                p["version"] = "0.0.9"
            mk.write_text(json.dumps(d), encoding="utf-8")
        errores = verificar_version.verificar("v0.1.0", self.raiz)
        self.assertTrue(any("marketplace.json" in e for e in errores), errores)

    def test_cli_codigos_de_salida(self):
        self.assertEqual(verificar_version.main(["x", "v0.1.0", str(self.raiz)]), 0)
        self.assertEqual(verificar_version.main(["x", "v9.9.9", str(self.raiz)]), 1)
        self.assertEqual(verificar_version.main(["x", ""]), 2)


if __name__ == "__main__":
    unittest.main()
