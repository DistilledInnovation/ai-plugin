import json
import re
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "scripts"))
import empaquetar  # noqa: E402

FIXTURE = AQUI / "fixtures" / "repo_valido"


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.raiz = Path(self._tmp.name) / "repo"
        shutil.copytree(FIXTURE, self.raiz)
        self.destino = Path(self._tmp.name) / "dist"
        self.destino.mkdir()
        self.plugin = self.raiz / "plugins" / "demo"
        self.skill = self.plugin / "skills" / "skill-demo"


class PruebasZips(Base):
    def test_zip_skill_raiz_es_carpeta(self):
        ruta = empaquetar.zip_skill(self.skill, self.destino, "0.1.0")
        self.assertEqual(ruta, self.destino / "skill-demo-v0.1.0.zip")
        with zipfile.ZipFile(ruta) as z:
            nombres = z.namelist()
        self.assertTrue(nombres[0].startswith("skill-demo/"), nombres)
        self.assertIn("skill-demo/SKILL.md", nombres)
        self.assertTrue(all(n.startswith("skill-demo/") for n in nombres), nombres)

    def test_zip_plugin_tiene_manifest_en_raiz_y_no_evals(self):
        ruta = empaquetar.zip_plugin(self.plugin, self.destino)
        self.assertEqual(ruta, self.destino / "demo-v0.1.0.plugin")
        with zipfile.ZipFile(ruta) as z:
            nombres = z.namelist()
        self.assertIn(".claude-plugin/plugin.json", nombres)
        self.assertIn("skills/skill-demo/SKILL.md", nombres)
        self.assertFalse([n for n in nombres if n.startswith("evals/")], nombres)

    def test_zip_determinista(self):
        a = empaquetar.zip_skill(self.skill, self.destino, "0.1.0").read_bytes()
        (self.skill / "SKILL.md").touch()
        b = empaquetar.zip_skill(self.skill, self.destino, "0.1.0").read_bytes()
        self.assertEqual(a, b)
        p1 = empaquetar.zip_plugin(self.plugin, self.destino).read_bytes()
        p2 = empaquetar.zip_plugin(self.plugin, self.destino).read_bytes()
        self.assertEqual(p1, p2)
        with zipfile.ZipFile(self.destino / "skill-demo-v0.1.0.zip") as z:
            self.assertTrue(all(i.date_time == (1980, 1, 1, 0, 0, 0) for i in z.infolist()))


class PruebasCopiarPegar(Base):
    def crear_skills(self, n, tam=3000, desc="Descripción corta de la skill."):
        base = self.plugin / "skills"
        for i in range(n):
            nombre = f"paso-{i:02d}"
            carpeta = base / nombre
            (carpeta / "references").mkdir(parents=True)
            cuerpo = ("Texto de relleno para la skill. " * 200)[:tam]
            (carpeta / "SKILL.md").write_text(
                f"---\nname: {nombre}\ndescription: {desc} Úsala cuando pruebes.\n---\n\n# {nombre}\n\n{cuerpo}\n",
                encoding="utf-8",
            )
            (carpeta / "references" / "ejemplo.md").write_text(f"Ejemplo de {nombre}\n", encoding="utf-8")

    def preparar_compartido(self):
        (self.raiz / "compartido").mkdir(exist_ok=True)
        (self.raiz / "compartido" / "reglas.md").write_text("Una pregunta por turno.\n", encoding="utf-8")

    def test_copiar_pegar_12_skills_max_10_archivos(self):
        self.crear_skills(12)
        self.preparar_compartido()
        ruta = empaquetar.paquete_copiar_pegar(self.plugin, self.raiz, self.destino)
        self.assertEqual(ruta, self.destino / "demo-copiar-pegar-v0.1.0.zip")
        with zipfile.ZipFile(ruta) as z:
            nombres = z.namelist()
            instr = z.read("INSTRUCCIONES.md").decode("utf-8")
            conocimiento = [n for n in nombres if n != "INSTRUCCIONES.md"]
            self.assertLessEqual(len(nombres), 10, nombres)
            self.assertLessEqual(len(instr), 8000)
            self.assertTrue(all(re.match(r"^\d\d-.+\.md$", n) for n in conocimiento), nombres)
            self.assertIn("Una pregunta por turno.", instr)
            self.assertIn("consulta el archivo de conocimiento correspondiente", instr)
            self.assertIn("paso-00: Descripción corta", instr)
            todo = "".join(z.read(n).decode("utf-8") for n in conocimiento)
            for i in range(12):
                self.assertIn(f"# paso-{i:02d}", todo)
                self.assertIn(f"Ejemplo de paso-{i:02d}", todo)
            # orden alfabetico y grupos contiguos
            posiciones = [todo.index(f"# paso-{i:02d}\n") for i in range(12)]
            self.assertEqual(posiciones, sorted(posiciones))

    def test_copiar_pegar_determinista_byte_a_byte(self):
        self.crear_skills(5)
        self.preparar_compartido()
        a = empaquetar.paquete_copiar_pegar(self.plugin, self.raiz, self.destino).read_bytes()
        (self.plugin / "skills" / "paso-00" / "SKILL.md").touch()
        otro = self.destino.parent / "dist2"
        otro.mkdir()
        b = empaquetar.paquete_copiar_pegar(self.plugin, self.raiz, otro).read_bytes()
        self.assertEqual(a, b)

    def test_incluye_proceso_del_facilitador(self):
        self.crear_skills(2)
        self.preparar_compartido()
        fac = self.plugin / "skills" / "facilitador-demo"
        fac.mkdir()
        (fac / "SKILL.md").write_text(
            "---\nname: facilitador-demo\ndescription: Orquesta. Úsala cuando empieces.\n---\n\n# F\n\n"
            "## Cuándo\nNO\n\n## Proceso (pasos)\n1. Diagnostica el punto de partida.\n\n## Entregables\nOTRO\n",
            encoding="utf-8",
        )
        ruta = empaquetar.paquete_copiar_pegar(self.plugin, self.raiz, self.destino)
        with zipfile.ZipFile(ruta) as z:
            instr = z.read("INSTRUCCIONES.md").decode("utf-8")
        self.assertIn("1. Diagnostica el punto de partida.", instr)
        self.assertNotIn("OTRO", instr)

    def test_recorta_indice_a_nombres_si_excede(self):
        self.crear_skills(12, tam=100, desc="d" * 900)
        self.preparar_compartido()
        ruta = empaquetar.paquete_copiar_pegar(self.plugin, self.raiz, self.destino)
        with zipfile.ZipFile(ruta) as z:
            instr = z.read("INSTRUCCIONES.md").decode("utf-8")
        self.assertLessEqual(len(instr), 8000)
        self.assertNotIn("ddddd", instr)
        self.assertIn("paso-11", instr)

    def test_excede_aun_sin_descripciones_lanza(self):
        self.crear_skills(2)
        (self.raiz / "compartido").mkdir(exist_ok=True)
        (self.raiz / "compartido" / "enorme.md").write_text("x" * 9000, encoding="utf-8")
        with self.assertRaises(ValueError):
            empaquetar.paquete_copiar_pegar(self.plugin, self.raiz, self.destino)

    def test_sin_skills_genera_solo_instrucciones(self):
        shutil.rmtree(self.plugin / "skills")
        self.preparar_compartido()
        ruta = empaquetar.paquete_copiar_pegar(self.plugin, self.raiz, self.destino)
        with zipfile.ZipFile(ruta) as z:
            self.assertEqual(z.namelist(), ["INSTRUCCIONES.md"])


class PruebasTodoEnUno(Base):
    def preparar(self, n=3):
        (self.raiz / "compartido").mkdir(exist_ok=True)
        (self.raiz / "compartido" / "reglas.md").write_text("Una pregunta por turno.\n", encoding="utf-8")
        (self.plugin / "README.md").write_text("# Demo Metodología\n\nTexto.\n", encoding="utf-8")
        base = self.plugin / "skills"
        nombres = ["facilitador-demo"] + [f"paso-{i:02d}" for i in range(n)]
        for nombre in nombres:
            carpeta = base / nombre
            (carpeta / "references").mkdir(parents=True)
            (carpeta / "assets").mkdir()
            extra = "## Proceso\n\nPregunta una cosa a la vez.\n\n## Otra\n\nNo va.\n" if nombre.startswith("facilitador") else ""
            (carpeta / "SKILL.md").write_text(
                f"---\nname: {nombre}\ndescription: Sirve para {nombre}. Úsala cuando digas \"quiero {nombre}\".\n---\n\n# {nombre}\n\n{extra}",
                encoding="utf-8",
            )
            (carpeta / "references" / "ejemplo.md").write_text(f"Ejemplo de {nombre}\n", encoding="utf-8")
            (carpeta / "assets" / "plantilla.md").write_text(f"Plantilla de {nombre}\n", encoding="utf-8")
        (self.plugin / "evals" / "x.json").write_text("{}", encoding="utf-8")
        return nombres

    def generar(self):
        return empaquetar.paquete_todo_en_uno(self.plugin, self.raiz, self.destino)

    def test_raiz_unica_con_skill_md(self):
        self.preparar()
        ruta = self.generar()
        self.assertEqual(ruta, self.destino / "demo-todo-en-uno-v0.1.0.zip")
        with zipfile.ZipFile(ruta) as z:
            nombres = z.namelist()
        self.assertTrue(all(n.startswith("demo/") for n in nombres), nombres)
        self.assertIn("demo/SKILL.md", nombres)

    def test_frontmatter_solo_name_y_description_y_limite(self):
        self.preparar()
        with zipfile.ZipFile(self.generar()) as z:
            texto = z.read("demo/SKILL.md").decode("utf-8")
        self.assertLessEqual(len(texto), 20000)
        m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
        claves = [l.split(":", 1)[0] for l in m.group(1).split("\n")]
        self.assertEqual(claves, ["name", "description"])
        self.assertIn("name: demo", m.group(1))
        desc = m.group(1).split("description: ", 1)[1]
        self.assertLessEqual(len(desc), 1024)
        self.assertIn("Úsala cuando", desc)
        self.assertIn("Una pregunta por turno.", texto)
        self.assertIn("Pregunta una cosa a la vez.", texto)
        self.assertNotIn("No va.", texto)

    def test_todas_las_skills_en_tabla_y_en_references(self):
        nombres = self.preparar(4)
        with zipfile.ZipFile(self.generar()) as z:
            texto = z.read("demo/SKILL.md").decode("utf-8")
            archivos = z.namelist()
        for n in nombres:
            self.assertIn(f"| `{n}` |", texto)
            self.assertIn(f"`references/{n}/SKILL.md`", texto)
            for rel in ("SKILL.md", "references/ejemplo.md", "assets/plantilla.md"):
                self.assertIn(f"demo/references/{n}/{rel}", archivos)
        self.assertFalse([a for a in archivos if "evals" in a])

    def test_recorta_descripciones_si_excede(self):
        self.preparar(40)
        for p in (self.plugin / "skills").glob("paso-*/SKILL.md"):
            t = p.read_text(encoding="utf-8")
            p.write_text(t.replace("Sirve para", "Sirve " + "para mucho " * 30 + "para"), encoding="utf-8")
        with zipfile.ZipFile(self.generar()) as z:
            self.assertLessEqual(len(z.read("demo/SKILL.md").decode("utf-8")), 20000)

    def test_determinista_y_solo_texto(self):
        self.preparar()
        a = self.generar().read_bytes()
        otro = self.destino / "otro"
        otro.mkdir()
        b = empaquetar.paquete_todo_en_uno(self.plugin, self.raiz, otro).read_bytes()
        self.assertEqual(a, b)
        with zipfile.ZipFile(self.generar()) as z:
            for n in z.namelist():
                z.read(n).decode("utf-8")
                self.assertFalse(re.search(r"(^|/)(\.terminos-prohibidos\.txt|\.fuentes-locales\.md|dist)(/|$)", n))


class PruebasCli(Base):
    def test_cli_escribe_dist(self):
        self.assertEqual(empaquetar.main(["x", str(self.raiz)]), 0)
        nombres = sorted(p.name for p in (self.raiz / "dist").iterdir())
        self.assertEqual(
            nombres,
            [
                "demo-copiar-pegar-v0.1.0.zip",
                "demo-todo-en-uno-v0.1.0.zip",
                "demo-v0.1.0.plugin",
                "skill-demo-v0.1.0.zip",
            ],
        )

    def test_cli_aborta_si_no_valida(self):
        (self.skill / "SKILL.md").write_text("sin frontmatter", encoding="utf-8")
        self.assertEqual(empaquetar.main(["x", str(self.raiz)]), 1)
        self.assertFalse((self.raiz / "dist").exists())


if __name__ == "__main__":
    unittest.main()
