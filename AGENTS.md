# AGENTS.md

Contrato para los agentes (y personas) que mantienen este repositorio. Todo el contenido visible va en español latinoamericano, tono de negocios cercano. Los identificadores y nombres de archivo van en español (`kebab-case` o `snake_case`).

## Propósito

Empaquetar las metodologías de Distilled Innovation como **skills** (formato abierto Agent Skills, `SKILL.md`) para que los clientes las usen dentro de su propio asistente de IA. Hay cuatro plugins: Innovación Destilada, Automatización con IA, Implementación Empresarial y Aceleración Comercial. Una sola fuente, publicada para todas las plataformas.

Diseño completo (autoridad): `docs/superpowers/specs/2026-10-25-plugin-metodologias-distilled-design.md`.

## Mapa del repo

```text
ai-plugin/
├── AGENTS.md / CLAUDE.md          # este contrato (CLAUDE.md solo dice @AGENTS.md)
├── README.md                      # para clientes novatos
├── CHANGELOG.md                   # cambios en español
├── .claude-plugin/marketplace.json
├── compartido/                    # única fuente de bloques y archivos que se copian a las skills
│   ├── reglas-facilitacion.md
│   ├── etiquetas-y-trazabilidad.md
│   ├── archivos/                  # archivos completos compartidos (esquemas, plantillas)
│   └── archivos-compartidos.json  # qué archivo va a qué skill
├── plugins/<metodologia>/
│   ├── .claude-plugin/plugin.json
│   ├── skills/<skill>/{SKILL.md, references/, assets/}
│   └── evals/<skill>/{prompt.md, graders/}   # no se empaqueta
├── scripts/                       # sincronizar_bloques.py, validar.py, empaquetar.py, verificar_version.py
├── tests/                         # pruebas con unittest (solo biblioteca estándar)
├── docs/{instalacion/, guia-taller.md, imagenes/, superpowers/}
└── .github/workflows/             # validar.yml (cada cambio), publicar.yml (tag v*)
```

## Anatomía de una skill

````markdown
---
name: priorizar-flujos
description: Ayuda a un equipo a inventariar sus procesos y elegir cuáles conviene automatizar, asistir con IA o dejar humanos, con un mapa Valor × Factibilidad. Úsala cuando el usuario diga "qué procesos automatizo", "priorizar flujos", "por dónde empezar con IA" o comparta una lista de tareas repetitivas.
---
# Priorizar flujos
<!-- inicio:reglas-facilitacion --> … <!-- fin:reglas-facilitacion -->
## Cuándo usarla / cuándo no
## Antes de empezar (qué pedir al usuario)
## Proceso (pasos numerados, una pregunta por turno)
## Entregables (usa assets/…)
## Criterio de salida
## Siguiente paso sugerido
````

Cada skill incluye un bloque `etiquetas-y-trazabilidad` (también sincronizado), plantillas rellenables en `assets/` y un recorrido con empresa **ficticia** en `references/ejemplo.md`.

## Reglas duras

- Frontmatter de `SKILL.md`: exactamente `name` y `description`. `name` = nombre de la carpeta, regex `^[a-z0-9]+(-[a-z0-9]+)*$`.
- `description` de 1.024 caracteres o menos, con la frase `Úsala cuando` y 3 a 5 frases reales del usuario.
- `SKILL.md` de 20.000 caracteres o menos (límite de Microsoft 365). Lo largo va en `references/`.
- Dentro de `plugins/` solo extensiones `.md .txt .json .yaml .yml .csv`. Las imágenes viven en `docs/imagenes/`.
- Ningún archivo de una skill usa rutas con `../`: cada skill es autocontenida.
- Cero nombres, personas, productos o datos de clientes reales, tampoco los casos del libro ni de los borradores. Ejemplos siempre con empresas ficticias.
- Sin secretos en el repo. `.terminos-prohibidos.txt` es local y está en `.gitignore`; en CI llega por el secreto `TERMINOS_PROHIBIDOS`.
- Los bloques comunes solo se editan en `compartido/`; dentro de las skills van entre `<!-- inicio:NOMBRE -->` y `<!-- fin:NOMBRE -->`. Los archivos compartidos solo se editan en `compartido/archivos/` y se declaran en `compartido/archivos-compartidos.json`.
- Todo `.json` dentro de `plugins/` es JSON válido.
- Implementación Empresarial nunca afirma conversión automática entre plataformas ni incluye credenciales, endpoints reales o datos personales.
- Paquete todo-en-uno (`<plugin>-todo-en-uno-v*.zip`): una sola skill `<plugin>/` con `SKILL.md` de 20.000 caracteres o menos (descripción de 1.024 o menos) y `references/<skill>/`; es el camino principal de instalación para interfaces web.
- Paquete copiar-pegar: 10 archivos o menos e `INSTRUCCIONES.md` de 8.000 caracteres o menos.
- Licencia: contenido CC BY 4.0 (atribución "Distilled Innovation"); `scripts/` MIT.
- Commits con `aleriospresidente@gmail.com` (revisar `git config user.email` antes de cada commit). Nunca confirmar `.terminos-prohibidos.txt`, `.fuentes-locales.md`, `.superpowers/` ni `dist/`.

## Comandos

```bash
python3 -m unittest discover -s tests          # pruebas
python3 scripts/sincronizar_bloques.py         # copia compartido/ dentro de las skills
python3 scripts/sincronizar_bloques.py --verificar
python3 scripts/validar.py                     # reglas duras
python3 scripts/empaquetar.py                  # genera dist/ (todo-en-uno por metodología, zips por skill, .plugin, copiar-pegar)
python3 scripts/verificar_version.py v0.1.0    # el tag coincide con los manifiestos
claude plugin validate .                       # valida marketplace y plugins
claude plugin eval plugins/<plugin>            # evals (agregar --case "<skill>*" para una skill)
```

## Receta: agregar una skill

1. Crear `plugins/<plugin>/skills/<skill>/SKILL.md` con la anatomía de arriba (nombre en kebab-case, sin números) y los dos bloques compartidos vacíos entre sus marcadores.
2. Escribir `assets/` (plantillas Markdown rellenables; diagramas como Mermaid más tabla equivalente) y `references/ejemplo.md` con una empresa ficticia.
3. Crear `plugins/<plugin>/evals/<skill>/prompt.md` (mensaje de un novato con contexto ficticio) y `graders/` con tres criterios: activa la skill correcta, hace una pregunta principal en el primer turno (a lo sumo, dos seguimientos cortos del mismo punto), el entregable usa la plantilla y separa Hecho de Supuesto.
4. Ejecutar `python3 scripts/sincronizar_bloques.py` y luego `python3 scripts/validar.py`.
5. Ejecutar `claude plugin validate .` y `claude plugin eval plugins/<plugin> --case "<skill>*"`; el brazo con plugin debe superar al brazo sin plugin.
6. Actualizar el catálogo en `README.md`, `CHANGELOG.md` y, si cambia el comportamiento, la versión en `plugin.json` y `marketplace.json`.

## Definición de terminado

- `python3 -m unittest discover -s tests` pasa.
- `python3 scripts/sincronizar_bloques.py --verificar`, `python3 scripts/validar.py` y `claude plugin validate .` pasan.
- Los evals de las skills tocadas pasan y el brazo con plugin supera al brazo sin plugin.
- Revisión de términos: la lista local `.terminos-prohibidos.txt` no produce coincidencias (la corre `validar.py`).
- Cambios documentados en `CHANGELOG.md`.

## Publicar

Con la versión actualizada en los cuatro `plugin.json` y en `marketplace.json`, crear el tag `vX.Y.Z`. `publicar.yml` falla si el secreto `TERMINOS_PROHIBIDOS` está vacío o si la versión del tag no coincide, y si todo pasa publica la Release con los paquetes de `dist/`.

Formato de evals confirmado: cada caso es una carpeta `plugins/<plugin>/evals/<caso>/` con `prompt.md` (frontmatter `max_turns: 6` y `allowed_tools: [Read, Glob, Grep, Skill]`, luego el mensaje del usuario) y `graders/*.md` (frontmatter `type: tool_used` + `tool: Skill` para la activación, o `type: llm` + `weight` para criterios juzgados). Los casos son carpetas hermanas, no anidadas (una carpeta dentro de otro caso no se descubre). Por skill hay dos: `evals/<skill>/` (primer turno de un novato: graders `activa-la-skill` y `una-sola-pregunta`) y `evals/<skill>-entregable/` (el mensaje trae todos los datos y termina en "Finalizar": graders `activa-la-skill` y `entregable-usa-plantilla`); `--case "<skill>*"` corre ambos. Con ablación (por defecto) `tool_used: Skill` solo indica que el plugin se activó y no suma al puntaje. Comando: `claude plugin eval plugins/<plugin> --case "<skill>*" -j 3 --no-publish --max-cost-usd 3 --trust-plugin --runs 3`.
