import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "scripts"))
import sincronizar_bloques as sb  # noqa: E402

FIXTURE = AQUI / "fixtures" / "repo_valido"
SKILL_MD = "plugins/demo/skills/skill-demo/SKILL.md"
BLOQUES = {"reglas": "Una pregunta por turno."}


def con_marcadores(contenido="viejo"):
    return f"# T\n\n<!-- inicio:reglas -->\n{contenido}\n<!-- fin:reglas -->\n\nFin\n"


class PruebasAplicar(unittest.TestCase):
    def test_aplicar_reemplaza_contenido(self):
        salida = sb.aplicar_bloques(con_marcadores(), BLOQUES)
        self.assertEqual(salida, con_marcadores("Una pregunta por turno."))

    def test_aplicar_idempotente(self):
        una = sb.aplicar_bloques(con_marcadores(), BLOQUES)
        self.assertEqual(sb.aplicar_bloques(una, BLOQUES), una)

    def test_bloque_desconocido_lanza(self):
        with self.assertRaises(ValueError):
            sb.aplicar_bloques("<!-- inicio:zzz -->\nx\n<!-- fin:zzz -->\n", BLOQUES)

    def test_cierre_faltante_lanza(self):
        with self.assertRaises(ValueError):
            sb.aplicar_bloques("<!-- inicio:reglas -->\nx\n", BLOQUES)

    def test_cargar_bloques(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "a.md").write_text("Hola\n\n", encoding="utf-8")
            self.assertEqual(sb.cargar_bloques(Path(d)), {"a": "Hola"})


class BaseRepo(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.raiz = Path(self._tmp.name) / "repo"
        shutil.copytree(FIXTURE, self.raiz)
        (self.raiz / "compartido" / "archivos").mkdir(parents=True)
        (self.raiz / "compartido" / "reglas.md").write_text("Una pregunta por turno.\n", encoding="utf-8")
        (self.raiz / "compartido" / "archivos-compartidos.json").write_text("{}", encoding="utf-8")
        self.skill_md = self.raiz / SKILL_MD
        self.skill_md.write_text(
            self.skill_md.read_text(encoding="utf-8") + "\n" + con_marcadores(), encoding="utf-8"
        )


class PruebasVerificar(BaseRepo):
    def afirmar_ruta(self, msgs, ruta):
        self.assertEqual(len(msgs), 1, msgs)
        self.assertTrue(msgs[0].startswith(ruta + ":"), msgs)

    def test_verificar_detecta_edicion_manual(self):
        self.afirmar_ruta(sb.verificar(self.raiz), SKILL_MD)
        sb.sincronizar(self.raiz)
        self.assertEqual(sb.verificar(self.raiz), [])
        t = self.skill_md.read_text(encoding="utf-8").replace("Una pregunta", "Dos preguntas")
        self.skill_md.write_text(t, encoding="utf-8")
        self.afirmar_ruta(sb.verificar(self.raiz), SKILL_MD)
        sb.sincronizar(self.raiz)
        self.assertEqual(sb.verificar(self.raiz), [])

    def test_bloque_desconocido_se_reporta(self):
        t = self.skill_md.read_text(encoding="utf-8").replace("inicio:reglas", "inicio:otro").replace("fin:reglas", "fin:otro")
        self.skill_md.write_text(t, encoding="utf-8")
        msgs = sb.verificar(self.raiz)
        self.assertTrue(any(SKILL_MD in m and "otro" in m for m in msgs), msgs)


class PruebasArchivos(BaseRepo):
    def declarar(self, destinos):
        (self.raiz / "compartido" / "archivos" / "esquema.json").write_text('{"a": 1}\n', encoding="utf-8")
        (self.raiz / "compartido" / "archivos-compartidos.json").write_text(
            json.dumps({"esquema.json": destinos}), encoding="utf-8"
        )

    def test_copiar_archivos_crea_destino(self):
        self.declarar(["demo/skill-demo/assets"])
        escritas = sb.copiar_archivos(self.raiz)
        destino = self.raiz / "plugins/demo/skills/skill-demo/assets/esquema.json"
        self.assertEqual(escritas, [destino])
        self.assertEqual(destino.read_text(encoding="utf-8"), '{"a": 1}\n')

    def test_verificar_detecta_copia_distinta(self):
        self.declarar(["demo/skill-demo/assets"])
        sb.sincronizar(self.raiz)
        self.assertEqual(sb.verificar(self.raiz), [])
        copia = self.raiz / "plugins/demo/skills/skill-demo/assets/esquema.json"
        copia.write_text("{}", encoding="utf-8")
        msgs = sb.verificar(self.raiz)
        self.assertTrue(any("assets/esquema.json" in m for m in msgs), msgs)

    def test_verificar_detecta_copia_ausente(self):
        self.declarar(["demo/skill-demo/assets"])
        sb.aplicar_a_skills(self.raiz)
        msgs = sb.verificar(self.raiz)
        self.assertTrue(any("assets/esquema.json" in m for m in msgs), msgs)

    def test_archivo_compartido_inexistente_lanza(self):
        (self.raiz / "compartido" / "archivos-compartidos.json").write_text(
            json.dumps({"no-existe.json": ["demo/skill-demo/assets"]}), encoding="utf-8"
        )
        with self.assertRaises(ValueError):
            sb.cargar_archivos_compartidos(self.raiz)


if __name__ == "__main__":
    unittest.main()
