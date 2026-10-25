import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "scripts"))
import validar  # noqa: E402

FIXTURE = AQUI / "fixtures" / "repo_valido"
SKILL_REL = "plugins/demo/skills/skill-demo"
SKILL_MD = SKILL_REL + "/SKILL.md"


class BaseRepo(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.raiz = Path(self._tmp.name) / "repo"
        shutil.copytree(FIXTURE, self.raiz)
        self.skill = self.raiz / SKILL_REL

    def errores(self, terminos=None):
        return validar.validar_repo(self.raiz, terminos or [])

    def afirmar_error(self, errores, ruta, palabra):
        self.assertTrue(
            any(ruta in e and palabra in e for e in errores),
            f"no hay error con {ruta!r} y {palabra!r}: {errores}",
        )

    def escribir_skill(self, nombre="skill-demo", descripcion=None, extra="", cuerpo="# Demo\n"):
        if descripcion is None:
            descripcion = "Guía de ejemplo. Úsala cuando haga falta."
        (self.skill / "SKILL.md").write_text(
            f"---\nname: {nombre}\ndescription: {descripcion}\n{extra}---\n{cuerpo}", encoding="utf-8"
        )


class PruebasValidarSkillsYRepo(BaseRepo):
    def test_repo_valido_sin_errores(self):
        self.assertEqual(self.errores(), [])

    def test_fixture_original_valido(self):
        self.assertEqual(validar.validar_repo(FIXTURE, []), [])

    def test_name_distinto_de_carpeta(self):
        self.escribir_skill(nombre="otra-cosa")
        self.afirmar_error(self.errores(), SKILL_MD, "name")

    def test_campo_extra_en_frontmatter(self):
        self.escribir_skill(extra="license: MIT\n")
        self.afirmar_error(self.errores(), SKILL_MD, "frontmatter")

    def test_sin_frontmatter(self):
        (self.skill / "SKILL.md").write_text("# sin bloque\n", encoding="utf-8")
        self.afirmar_error(self.errores(), SKILL_MD, "frontmatter")

    def test_description_sin_usala_cuando(self):
        self.escribir_skill(descripcion="Guía de ejemplo sin la frase obligatoria.")
        self.afirmar_error(self.errores(), SKILL_MD, "Úsala cuando")

    def test_description_mayor_1024(self):
        self.escribir_skill(descripcion="Úsala cuando " + "x" * 1030)
        self.afirmar_error(self.errores(), SKILL_MD, "1024")

    def test_description_exacta_1024_es_valida(self):
        base = "Úsala cuando "
        self.escribir_skill(descripcion=base + "x" * (1024 - len(base)))
        self.assertEqual(self.errores(), [])

    def test_skill_mayor_20000(self):
        self.escribir_skill(cuerpo="# Demo\n" + "a" * 20001)
        self.afirmar_error(self.errores(), SKILL_MD, "20000")

    def test_extension_no_permitida(self):
        (self.skill / "assets").mkdir()
        (self.skill / "assets" / "logo.png").write_bytes(b"\x89PNG")
        self.afirmar_error(self.errores(), SKILL_REL + "/assets/logo.png", "extensión")

    def test_gitkeep_vacio_permitido(self):
        (self.raiz / "plugins" / "demo" / "skills" / ".gitkeep").write_text("", encoding="utf-8")
        self.assertEqual(self.errores(), [])

    def test_extension_no_permitida_fuera_de_skills(self):
        (self.raiz / "plugins" / "demo" / "logo.png").write_bytes(b"\x89PNG")
        self.afirmar_error(self.errores(), "plugins/demo/logo.png", "extensión")

    def test_ruta_relativa_padre(self):
        self.escribir_skill(cuerpo="# Demo\nVer [más](../x.md)\n")
        self.afirmar_error(self.errores(), SKILL_MD, "../")

    def test_termino_prohibido_con_tildes(self):
        self.escribir_skill(cuerpo="# Demo\nCaso de LÁCTEOS ANDINOS en Bogotá.\n")
        self.afirmar_error(self.errores(["lacteos andinos"]), SKILL_MD, "prohibido")

    def test_termino_prohibido_coincide_solo_palabra_completa(self):
        self.escribir_skill(cuerpo="# Demo\nLa interacción de los usuarios es rica.\n")
        self.assertEqual(self.errores(["interaccion de los usuarios es ric"]), [])
        self.assertEqual(self.errores(["ric"]), [])

    def test_termino_prohibido_frase_con_salto_de_linea(self):
        self.escribir_skill(cuerpo="# Demo\nLácteos\nAndinos opera aquí.\n")
        self.afirmar_error(self.errores(["Lacteos Andinos"]), SKILL_MD, "prohibido")

    def test_termino_prohibido_en_docs_y_readme(self):
        (self.raiz / "docs").mkdir()
        (self.raiz / "docs" / "nota.md").write_text("Trabajamos con Lácteos Andinos.", encoding="utf-8")
        (self.raiz / "README.md").write_text("Lácteos Andinos", encoding="utf-8")
        errores = self.errores(["lacteos andinos"])
        self.afirmar_error(errores, "docs/nota.md", "prohibido")
        self.afirmar_error(errores, "README.md", "prohibido")

    def test_error_no_filtra_el_termino(self):
        self.escribir_skill(cuerpo="# Demo\nLácteos Andinos\n")
        self.assertFalse(any("andinos" in e.lower() for e in self.errores(["lacteos andinos"])))

    def test_falta_eval(self):
        (self.raiz / "plugins/demo/evals/skill-demo/prompt.md").unlink()
        self.afirmar_error(self.errores(), "plugins/demo/evals/skill-demo/prompt.md", "eval")

    def test_json_invalido(self):
        (self.skill / "assets").mkdir()
        (self.skill / "assets" / "x.json").write_text("{", encoding="utf-8")
        self.afirmar_error(self.errores(), SKILL_REL + "/assets/x.json", "JSON")

    def test_skill_con_bom_y_crlf_es_valida(self):
        contenido = "---\nname: skill-demo\ndescription: Guía. Úsala cuando haga falta.\n---\n# Demo\n"
        (self.skill / "SKILL.md").write_bytes(("\ufeff" + contenido.replace("\n", "\r\n")).encode("utf-8"))
        self.assertEqual(self.errores(), [])

    def test_plugin_sin_skills_es_advertencia_no_error(self):
        shutil.rmtree(self.skill)
        shutil.rmtree(self.raiz / "plugins/demo/evals/skill-demo")
        avisos = []
        self.assertEqual(validar.validar_repo(self.raiz, [], avisos), [])
        self.assertTrue(any("demo" in a and "skills" in a for a in avisos))

    def test_validar_skill_publica(self):
        self.assertEqual(validar.validar_skill(self.skill, []), [])


class PruebasManifiestos(BaseRepo):
    def escribir_json(self, ruta, datos):
        (self.raiz / ruta).write_text(json.dumps(datos), encoding="utf-8")

    def test_plugin_json_nombre_distinto(self):
        self.escribir_json(
            "plugins/demo/.claude-plugin/plugin.json",
            {"name": "otro", "version": "0.1.0", "description": "d"},
        )
        self.afirmar_error(self.errores(), "plugins/demo/.claude-plugin/plugin.json", "plugin.json")

    def test_plugin_json_version_no_semver(self):
        self.escribir_json(
            "plugins/demo/.claude-plugin/plugin.json",
            {"name": "demo", "version": "1.0", "description": "d"},
        )
        self.afirmar_error(self.errores(), "plugin.json", "semver")

    def test_plugin_json_sin_description(self):
        self.escribir_json(
            "plugins/demo/.claude-plugin/plugin.json", {"name": "demo", "version": "0.1.0"}
        )
        self.afirmar_error(self.errores(), "plugin.json", "description")

    def test_marketplace_sin_plugin(self):
        self.escribir_json(".claude-plugin/marketplace.json", {"name": "m", "plugins": []})
        self.afirmar_error(self.errores(), ".claude-plugin/marketplace.json", "marketplace")

    def test_marketplace_version_distinta(self):
        self.escribir_json(
            ".claude-plugin/marketplace.json",
            {"name": "m", "plugins": [{"name": "demo", "source": "./plugins/demo", "version": "9.9.9"}]},
        )
        self.afirmar_error(self.errores(), ".claude-plugin/marketplace.json", "version")

    def test_marketplace_source_incorrecto(self):
        self.escribir_json(
            ".claude-plugin/marketplace.json",
            {"name": "m", "plugins": [{"name": "demo", "source": "./demo", "version": "0.1.0"}]},
        )
        self.afirmar_error(self.errores(), ".claude-plugin/marketplace.json", "source")

    def test_json_invalido_en_plugin_json(self):
        (self.raiz / "plugins/demo/.claude-plugin/plugin.json").write_text("{", encoding="utf-8")
        self.afirmar_error(self.errores(), "plugins/demo/.claude-plugin/plugin.json", "JSON")


class PruebasCLI(BaseRepo):
    def correr(self):
        return subprocess.run(
            [sys.executable, str(AQUI.parent / "scripts" / "validar.py"), str(self.raiz)],
            capture_output=True,
            text=True,
        )

    def test_cli_ok(self):
        r = self.correr()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("OK: 1 skills", r.stdout)

    def test_cli_con_errores(self):
        self.escribir_skill(nombre="otra-cosa")
        r = self.correr()
        self.assertEqual(r.returncode, 1)
        self.assertIn(SKILL_MD + ": ", r.stdout)


class PruebasBloquesEnValidar(BaseRepo):
    def test_validar_reporta_bloque_desincronizado(self):
        (self.raiz / "compartido").mkdir()
        (self.raiz / "compartido" / "reglas.md").write_text("Una pregunta por turno.\n", encoding="utf-8")
        md = self.skill / "SKILL.md"
        md.write_text(
            md.read_text(encoding="utf-8") + "\n<!-- inicio:reglas -->\neditado a mano\n<!-- fin:reglas -->\n",
            encoding="utf-8",
        )
        self.afirmar_error(self.errores(), SKILL_MD, "desincronizado")


if __name__ == "__main__":
    unittest.main()
