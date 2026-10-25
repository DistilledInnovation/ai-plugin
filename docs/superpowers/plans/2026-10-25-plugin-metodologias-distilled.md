# Plugin de metodologías Distilled — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar `DistilledInnovation/ai-plugin` v1.0.0: un marketplace público con cuatro plugins de skills en español (Innovación Destilada, Automatización con IA, Implementación Empresarial, Aceleración Comercial), instalable por novatos en Claude, ChatGPT, Microsoft 365 Copilot, Amazon Quick, Gemini, Grok y OpenWork.

**Architecture:** Fuente única en formato Agent Skills (`SKILL.md` solo texto) organizada como marketplace de plugins de Claude. Tres scripts Python stdlib sincronizan bloques y archivos comunes, validan las reglas del spec y empaquetan zips por skill, `.plugin` por metodología y paquetes copiar-pegar. GitHub Actions valida en PR y publica Releases en tag.

**Tech Stack:** Markdown + Mermaid + YAML; Python 3.11+ (solo stdlib, pruebas con `unittest`); GitHub Actions; CLI `claude` (`plugin validate`, `plugin eval`, `--plugin-dir`).

**Spec:** `docs/superpowers/specs/2026-10-25-plugin-metodologias-distilled-design.md`

## Global Constraints

- Todo el contenido visible en español latinoamericano, tono de negocios cercano; identificadores y nombres de archivo en español kebab-case/snake_case.
- Frontmatter de `SKILL.md`: exactamente `name` y `description`; `name` = carpeta, regex `^[a-z0-9]+(-[a-z0-9]+)*$`.
- `description` ≤ 1.024 caracteres y contiene la frase `Úsala cuando`.
- `SKILL.md` ≤ 20.000 caracteres.
- Dentro de `plugins/` solo extensiones `.md .txt .json .yaml .yml .csv`.
- Ningún archivo de una skill referencia rutas con `../`.
- Cero nombres, personas, productos o datos de clientes reales — incluidos los casos del libro y de los documentos de `brainstorm/`. Ejemplos siempre con empresas ficticias.
- Sin secretos en el repo. `.terminos-prohibidos.txt` es local y está en `.gitignore`.
- Bloques comunes solo se editan en `compartido/`; dentro de las skills van entre `<!-- inicio:NOMBRE -->` y `<!-- fin:NOMBRE -->`.
- Archivos compartidos entre skills (esquemas, plantillas) solo se editan en `compartido/archivos/` y se declaran en `compartido/archivos-compartidos.json`; las copias deben ser idénticas.
- Todo `.json` dentro de `plugins/` debe ser JSON válido.
- Implementación Empresarial nunca afirma conversión automática entre plataformas, ni incluye credenciales, endpoints reales o datos personales.
- Paquete copiar-pegar: ≤ 10 archivos e `INSTRUCCIONES.md` ≤ 8.000 caracteres.
- Licencia: contenido CC BY 4.0 (atribución “Distilled Innovation”), `scripts/` MIT.
- Commits con `aleriospresidente@gmail.com` (verificar `git config user.email` antes de cada commit).
- Modelos de subagentes (CLAUDE.md de Boss): Tareas 1–3 implementador `haiku`; Tareas 4–11 y 14–15 implementador `sonnet` (prosa y lectura de fuentes); Tareas 12–13 implementador `opus` (seguridad, infraestructura y contratos: override de riesgo); revisores `sonnet` mínimo; revisión final de rama `opus`.

## Review Focus

- Zip de skill con la carpeta mal ubicada (archivos sueltos en la raíz) → Claude.ai/ChatGPT lo rechazan; la raíz del zip debe ser `<skill>/SKILL.md`. Prueba en Tarea 3.
- Término prohibido con mayúsculas o tildes distintas (“LÁCTEOS ANDINOS” vs “lacteos andinos”) → debe detectarse igual. Prueba en Tarea 1.
- `SKILL.md` guardado con BOM o saltos CRLF (editado en Windows) → el frontmatter debe leerse bien. Prueba en Tarea 1.
- Plugin con 12+ skills → el paquete copiar-pegar sigue en ≤ 10 archivos e instrucciones ≤ 8.000 caracteres. Prueba en Tarea 3.
- Bloque común editado a mano dentro de una skill → `validar.py` lo reporta y `sincronizar_bloques.py` lo restaura. Prueba en Tarea 2.

---

## Estructura de archivos

```text
AGENTS.md, CLAUDE.md, README.md, CHANGELOG.md, LICENSE, LICENSE-scripts, .gitignore
.claude-plugin/marketplace.json
compartido/reglas-facilitacion.md, compartido/etiquetas-y-trazabilidad.md, compartido/archivos/, compartido/archivos-compartidos.json
plugins/{innovacion-destilada,automatizacion-con-ia,implementacion-empresarial,aceleracion-comercial}/
  .claude-plugin/plugin.json · README.md · skills/<skill>/{SKILL.md,references/,assets/} · evals/<skill>/{prompt.md,graders/*.md}
scripts/comun.py · scripts/validar.py · scripts/sincronizar_bloques.py · scripts/empaquetar.py
tests/test_comun.py · tests/test_validar.py · tests/test_sincronizar.py · tests/test_empaquetar.py · tests/fixtures/
docs/instalacion/{claude,chatgpt,microsoft-365-copilot,amazon-quick,gemini,grok,openwork-opencode}.md · docs/guia-taller.md · docs/imagenes/*.png
.github/workflows/{validar.yml,publicar.yml}
```

---

### Task 1: Base del repo, utilidades comunes y validador

**Files:**
- Create: `.gitignore`, `LICENSE`, `LICENSE-scripts`, `scripts/comun.py`, `scripts/validar.py`, `tests/test_comun.py`, `tests/test_validar.py`, `tests/fixtures/repo_valido/…` (un plugin `demo` con una skill `skill-demo` y su eval), `.terminos-prohibidos.txt` (local, no se commitea)

**Interfaces:**
- Produces:
  - `comun.leer_frontmatter(texto: str) -> dict[str, str]` — tolera BOM y CRLF; lanza `ValueError` si no hay bloque `---`.
  - `comun.encontrar_plugins(raiz: Path) -> list[Path]` (carpetas `plugins/*` con `.claude-plugin/plugin.json`, orden alfabético).
  - `comun.encontrar_skills(plugin: Path) -> list[Path]` (carpetas `skills/*` con `SKILL.md`, orden alfabético).
  - `comun.normalizar(texto: str) -> str` — minúsculas sin tildes (NFKD, descarta marcas).
  - `comun.cargar_terminos(raiz: Path) -> list[str]` — lee `.terminos-prohibidos.txt` (una por línea, ignora vacías y `#`) o variable `TERMINOS_PROHIBIDOS` (separada por saltos de línea).
  - `validar.validar_skill(skill: Path, terminos: list[str]) -> list[str]`
  - `validar.validar_repo(raiz: Path, terminos: list[str]) -> list[str]` — incluye skills, manifiestos, evals, términos en `plugins/ docs/ README.md AGENTS.md` y (desde Tarea 2) bloques.
  - CLI: `python scripts/validar.py [raiz]` → imprime errores `ruta: mensaje`; exit 1 si hay errores, 0 y `OK: N skills` si no.

- [ ] **Step 1:** `.gitignore` con `dist/`, `__pycache__/`, `.terminos-prohibidos.txt`, `.fuentes-locales.md`, `.env`, `evals/results/`, `plugins/*/evals/results/`. Crear `.terminos-prohibidos.txt` local con los nombres de empresas, personas, productos y proyectos de clientes que aparecen en `../brainstorm/` (carpetas de clientes, sección 9 de la oferta, tabla de evidencias de Aceleración Comercial) y los casos del capítulo 9 del libro. Crear también `.fuentes-locales.md` (local) con las rutas absolutas de las fuentes de casos reales que da el controlador. Confirmar con `git check-ignore .terminos-prohibidos.txt .fuentes-locales.md`.
- [ ] **Step 2: Pruebas que fallan** en `tests/test_comun.py`: `test_frontmatter_con_bom_y_crlf` (`"﻿---\r\nname: a\r\ndescription: b\r\n---\r\n# x"` → `{"name":"a","description":"b"}`), `test_frontmatter_ausente_lanza`, `test_normalizar_tildes_y_mayusculas` (`normalizar("LÁCTEOS Ñu") == "lacteos nu"`), `test_cargar_terminos_desde_env`. En `tests/test_validar.py`, sobre copias temporales de `fixtures/repo_valido`: `test_repo_valido_sin_errores`, `test_name_distinto_de_carpeta`, `test_campo_extra_en_frontmatter`, `test_description_sin_usala_cuando`, `test_description_mayor_1024`, `test_skill_mayor_20000`, `test_extension_no_permitida` (`logo.png`), `test_ruta_relativa_padre` (`../x.md`), `test_termino_prohibido_con_tildes` (término `lacteos andinos`, texto “LÁCTEOS ANDINOS”), `test_falta_eval` (sin `evals/skill-demo/prompt.md`), `test_plugin_json_nombre_distinto`, `test_marketplace_sin_plugin`, `test_json_invalido` (`assets/x.json` con `{`). Cada prueba afirma que algún error contiene la ruta y una palabra clave (`name`, `frontmatter`, `Úsala cuando`, `1024`, `20000`, `extensión`, `../`, `prohibido`, `eval`, `plugin.json`, `marketplace`, `JSON`).
- [ ] **Step 3:** `python -m unittest discover -s tests -v` → FAIL (módulos inexistentes).
- [ ] **Step 4:** Implementar `comun.py` y `validar.py` (agrega `scripts/` a `sys.path` en las pruebas). Manifiestos: `plugin.json` requiere `name` (= carpeta), `version` semver, `description`; `marketplace.json` debe listar cada plugin con `"source": "./plugins/<name>"` y versión igual a la del `plugin.json`.
- [ ] **Step 5:** Pruebas → PASS.
- [ ] **Step 6:** Commit `chore: base del repo y validador de skills`.

### Task 2: Bloques y archivos comunes, y sincronizador

**Files:**
- Create: `compartido/reglas-facilitacion.md`, `compartido/etiquetas-y-trazabilidad.md`, `compartido/archivos/.gitkeep`, `compartido/archivos-compartidos.json` (`{}`), `scripts/sincronizar_bloques.py`, `tests/test_sincronizar.py`
- Modify: `scripts/validar.py` (llamar `verificar`)

**Interfaces:**
- Consumes: `comun.encontrar_plugins`, `comun.encontrar_skills`.
- Produces:
  - `cargar_bloques(carpeta: Path) -> dict[str, str]` (clave = nombre de archivo sin `.md`).
  - `aplicar_bloques(texto: str, bloques: dict[str, str]) -> str` — reemplaza el contenido entre `<!-- inicio:X -->` y `<!-- fin:X -->`; `ValueError` si `X` no existe o falta el cierre.
  - `cargar_archivos_compartidos(raiz: Path) -> dict[str, list[str]]` — lee `compartido/archivos-compartidos.json`: `{"<archivo en compartido/archivos/>": ["<plugin>/<skill>/<subcarpeta>", …]}`; `ValueError` si el archivo origen no existe.
  - `copiar_archivos(raiz: Path) -> list[Path]` — copia cada archivo a `plugins/<plugin>/skills/<skill>/<subcarpeta>/`; devuelve las rutas escritas.
  - `verificar(raiz: Path) -> list[str]` — rutas de `SKILL.md` con bloques desincronizados y de copias de archivos ausentes o distintas.
  - CLI: `python scripts/sincronizar_bloques.py` (reescribe) y `--verificar` (exit 1 si hay diferencias).

- [ ] **Step 1: Contenido de `compartido/`** — copiar las reglas comunes del spec §4 (una pregunta por turno; Hecho/Supuesto/Recomendación/Pendiente por validar; riesgo → impacto → mitigación y línea base → meta; no inventar, borrador provisional + vacíos; lo más simple primero; comandos “Muéstrame el avance”, “¿Qué falta?”, “Finalizar”; Markdown + Mermaid con tabla equivalente; sugerir siguiente skill). `etiquetas-y-trazabilidad.md`: tipos de procedencia (dicho por participante, evidencia, observación del facilitador, inferencia de la IA, supuesto, recomendación, decisión) e IDs estables (`RET-01`, `HAL-01`, `SUP-01`, `PRU-01`…). Cada bloque ≤ 1.500 caracteres.
- [ ] **Step 2: Pruebas que fallan:** `test_aplicar_reemplaza_contenido`, `test_aplicar_idempotente`, `test_bloque_desconocido_lanza`, `test_cierre_faltante_lanza`, `test_verificar_detecta_edicion_manual` (editar texto dentro del bloque en la fixture → `verificar` devuelve esa ruta; tras `aplicar` → lista vacía), `test_copiar_archivos_crea_destino`, `test_verificar_detecta_copia_distinta` (modificar la copia → `verificar` la reporta), `test_archivo_compartido_inexistente_lanza`, y en `test_validar.py` `test_validar_reporta_bloque_desincronizado`.
- [ ] **Step 3:** FAIL → implementar → PASS (`python -m unittest discover -s tests -v`).
- [ ] **Step 4:** Commit `feat: bloques y archivos comunes sincronizados en las skills`.

### Task 3: Empaquetador, manifiestos y CI

**Files:**
- Create: `scripts/empaquetar.py`, `tests/test_empaquetar.py`, `.claude-plugin/marketplace.json`, `plugins/<4>/.claude-plugin/plugin.json`, `.github/workflows/validar.yml`, `.github/workflows/publicar.yml`

**Interfaces:**
- Consumes: Tareas 1–2.
- Produces:
  - `zip_skill(skill: Path, destino: Path, version: str) -> Path` → `destino/<skill>-v<version>.zip`, raíz `<skill>/SKILL.md`.
  - `zip_plugin(plugin: Path, destino: Path) -> Path` → `destino/<plugin>-v<version>.plugin`, con `.claude-plugin/plugin.json` en la raíz, sin `evals/`.
  - `paquete_copiar_pegar(plugin: Path, raiz: Path, destino: Path) -> Path` → `destino/<plugin>-copiar-pegar-v<version>.zip` con `INSTRUCCIONES.md` (bloques de `compartido/` + sección “Proceso” del facilitador + índice `nombre: description` de cada skill + instrucción “consulta el archivo de conocimiento correspondiente”) y ≤ 9 archivos `NN-<nombre>.md` (skills concatenadas en orden alfabético, repartidas en grupos contiguos; incluye `references/` y `assets/` de cada una). Si `INSTRUCCIONES.md` excede 8.000 caracteres, recortar el índice a solo nombres; si aún excede, `ValueError`.
  - Zips deterministas (fecha fija `1980-01-01`, orden alfabético).
  - CLI: `python scripts/empaquetar.py` → valida primero (aborta si hay errores) y escribe todo en `dist/`.

- [ ] **Step 1: Pruebas que fallan:** `test_zip_skill_raiz_es_carpeta` (`namelist()[0]` empieza con `skill-demo/` y contiene `skill-demo/SKILL.md`), `test_zip_plugin_tiene_manifest_en_raiz_y_no_evals`, `test_zip_determinista` (dos ejecuciones → mismos bytes), `test_copiar_pegar_12_skills_max_10_archivos` (fixture generada con 12 skills de ~3.000 caracteres → ≤ 10 entradas e `INSTRUCCIONES.md` ≤ 8.000).
- [ ] **Step 2:** FAIL → implementar → PASS.
- [ ] **Step 3: Manifiestos.** `marketplace.json`: `name: "distilled-innovation"`, `owner: {name: "Distilled Innovation"}`, cuatro plugins con `source`, `description`, `version: "0.1.0"`. `plugin.json` de cada uno: `name`, `version: "0.1.0"`, `description` (español), `author: {name: "Distilled Innovation"}`, `license: "CC-BY-4.0"`, `keywords`. Carpeta `skills/` vacía con `.gitkeep`. Ajustar `validar.py` para aceptar plugins sin skills (avisa, no falla) hasta las tareas de contenido.
- [ ] **Step 4:** `claude plugin validate .` y `claude plugin validate plugins/innovacion-destilada` → sin errores.
- [ ] **Step 5: CI.** `validar.yml` (push/PR): Python 3.11, `TERMINOS_PROHIBIDOS: ${{ secrets.TERMINOS_PROHIBIDOS }}`, ejecutar pruebas, `sincronizar_bloques.py --verificar`, `validar.py`. `publicar.yml` (tag `v*`): lo mismo + `empaquetar.py` + `gh release create` adjuntando `dist/*`. Recordar a Boss crear el secreto `TERMINOS_PROHIBIDOS` en GitHub.
- [ ] **Step 6:** Commit `feat: empaquetador multiplataforma, manifiestos y CI`.

### Task 4: Repo AI-first y documentación de instalación

**Files:**
- Create: `AGENTS.md`, `CLAUDE.md` (contenido: `@AGENTS.md`), `CHANGELOG.md`, `docs/instalacion/*.md` (7), `docs/guia-taller.md`, `docs/imagenes/` (copiar los 4 PNG del libro y los 3 lienzos de `../brainstorm/Distilled-Skills/*.png`)
- Modify: `README.md`

- [ ] **Step 1: `AGENTS.md`** con: propósito; mapa del repo; anatomía de skill (spec §7, plantilla literal); reglas duras (Global Constraints); comandos (`python -m unittest discover -s tests`, `sincronizar_bloques.py`, `validar.py`, `empaquetar.py`, `claude plugin validate .`, `claude plugin eval plugins/<p>`); receta “agregar una skill” en 6 pasos; definición de terminado (pruebas + validar + eval pasa + revisión de términos).
- [ ] **Step 2: `README.md`** para clientes novatos: qué es (3 líneas), tabla “¿Qué asistente usas?” → enlace a `docs/instalacion/<plataforma>.md` con nivel (spec §5), catálogo de las cuatro metodologías con un diagrama Mermaid de cómo se encadenan (Innovación Destilada → Automatización con IA → Implementación Empresarial; Innovación Destilada → Aceleración Comercial) e indicando que Implementación Empresarial es para equipos técnicos, “Cómo empezar” con 3 frases de ejemplo, licencia y créditos. Sin jerga técnica en la primera pantalla.
- [ ] **Step 3: Guías por plataforma** — pasos numerados desde la perspectiva del usuario y del admin, tomados del spec §5. Marcar con “(verificar)” los pasos que la investigación no pudo confirmar (Grok chatbot, Gemini Gems, administración de Amazon Quick) y agregar fecha “Verificado: 2026-10-25”.
- [ ] **Step 4: `docs/guia-taller.md`** — checklist previo (admin carga el plugin, prueba con frase de ejemplo), guion de uso por bloque de taller (Sprint 1 descubrir/priorizar 6 h, Sprint 2 prototipar 6 h, cierre 2 h; sin nombres de clientes), y “qué te llevas para después”.
- [ ] **Step 5:** `python scripts/validar.py` → OK. Commit `docs: README, AGENTS.md y guías de instalación`.

---

### Tareas de contenido (5–15): procedimiento común

Cada tarea crea un conjunto de skills. Para **cada skill**:

1. Leer las fuentes indicadas. El libro está en `../Innovación Destilada 20190309/Innovación Destilada 20190309.md` (índice en líneas 25–82; buscar los títulos en negrita como `**4.1.2` o `10.5`). Borradores en `../brainstorm/Distilled-Skills/`.
2. Crear `plugins/<p>/skills/<skill>/SKILL.md` con la anatomía del spec §7: frontmatter (description = qué hace + “Úsala cuando…” + 3–5 frases reales del usuario), bloques `<!-- inicio:reglas-facilitacion -->` y `<!-- inicio:etiquetas-y-trazabilidad -->` vacíos, *Cuándo usarla / cuándo no*, *Antes de empezar*, *Proceso* (pasos numerados, una pregunta por turno, con preguntas guía textuales), *Entregables* (apuntando a `assets/`), *Criterio de salida*, *Siguiente paso sugerido*.
3. `assets/`: plantillas Markdown rellenables de cada entregable; diagramas como Mermaid + tabla equivalente.
4. `references/ejemplo.md`: recorrido completo con una empresa **ficticia** (nombre inventado, sector, cifras plausibles) mostrando entrada del usuario, preguntas y entregable final. `references/herramientas.md` cuando la skill enseña técnicas (cómo aplicarlas paso a paso).
5. `evals/<skill>/prompt.md` (mensaje de un novato + contexto ficticio) y `graders/` con 3 criterios: activa la skill correcta, hace una sola pregunta principal en el primer turno, el entregable usa la plantilla y separa Hecho/Supuesto. Seguir el formato de `claude plugin eval --help`; en la Tarea 5 confirmar el formato con una corrida real y ajustar el procedimiento si difiere.

**Verificación por tarea:**
- `python scripts/sincronizar_bloques.py && python scripts/validar.py` → `OK`.
- `claude plugin validate plugins/<p>` → sin errores.
- `claude plugin eval plugins/<p> --case "<skill>*"` para las skills de la tarea → todas pasan, y el brazo con plugin supera al brazo sin plugin.
- Revisor (`sonnet`): compara cada skill con la fila correspondiente del spec §6 (columna “qué se agrega”) y con la fuente; falla si falta un elemento listado o si aparece un nombre real.
- Commit `feat(<p>): skills <lista>`.

### Task 5: Innovación Destilada — facilitador, alinear equipo, identificar reto

**Files:** `plugins/innovacion-destilada/skills/{facilitador-innovacion-destilada,alinear-equipo,identificar-reto}/…`, `plugins/innovacion-destilada/README.md`, evals.

- `facilitador-innovacion-destilada`: base borrador `skills/12-…`; diagnostica la etapa (Validar/Innovar/Escalar), mantiene un bloque YAML de estado del proyecto (`etapa, reto, actores, evidencia, supuestos, siguiente_skill`), muestra el diagrama de proceso del spec §6.1 y la tabla de orígenes del Design Thinking (de `historia-design-thinking.png`, verificando años contra el libro línea ~419) como contexto opcional.
- `alinear-equipo`: borrador 01 + libro §3.1–3.2 y anexos 10.1–10.3 (Línea de tiempo, Modelo de Negocio Personal, Círculo Dorado, MEGA). Assets: `acuerdo-de-equipo.md`, `circulo-dorado.md`, `mega.md`.
- `identificar-reto`: borrador 02 + libro §4.1.1 (11 preguntas “¿Cómo podemos…?”, Lienzo de Modelo de Negocio, Fuerzas del entorno, Canvas de Propuesta de Valor). Assets: `ficha-de-reto.md`, `lienzo-modelo-de-negocio.md`.
- `plugins/innovacion-destilada/README.md`: qué es la metodología, diagrama, lista de skills y frase de arranque de cada una.

### Task 6: Innovación Destilada — empatizar y redefinir

**Files:** `skills/{investigar-y-empatizar,sintetizar-y-redefinir-reto}/…`

- `investigar-y-empatizar`: borrador 03 + libro §4.1.2 y anexos de Perfil de Usuario, Entrevistas, Diario, Sesión participativa, Collage, Mapa Mental. Incluir la escalera de profundidad (tabla 3×3 de `empatizar-herramientas.png`: dicen-piensan/entrevistas/explícito; hacen-usan/observación/observable-tácito; saben-sienten-sueñan/técnicas generativas/latente) para elegir técnica. Assets: `plan-de-investigacion.md`, `guia-de-entrevista.md`, `perfil-de-usuario.md`, `diario-de-usuario.md`.
- `sintetizar-y-redefinir-reto`: borrador 04 + libro §5.1. Hallazgos/Necesidades/Tensiones, Mapa de Empatía, Perfil del Cliente, los dos patrones de reformulación textuales. Assets: `sintesis.md`, `mapa-de-empatia.md`, `perfil-del-cliente.md`, `reto-redefinido.md`.

### Task 7: Innovación Destilada — idear, concepto, prototipar

**Files:** `skills/{facilitar-ideacion,construir-concepto-fuerte,disenar-prototipo}/…`

- `facilitar-ideacion`: borrador 05 + libro §6.1 completo. Agenda de sesión (Tiempo, Actividad, Objetivos y reglas, Preguntas o comentarios, Encargados, Materiales), Principios de Participación, “ideas con vida” (Visibles, Implementables, Diferentes, Ambiciosas), calentamiento, y en `references/herramientas.md` cada técnica paso a paso (Esquema del Proceso, Dramatización, Historieta, Sombreros, ¿Qué tal si…?, 6-5-3, SCAMPER con sus 7 verbos), brain-writing y votación. Modo “taller en vivo” (el asistente cronometra y guía) y modo “individual”.
- `construir-concepto-fuerte`: borrador 06 + plantilla `templates/concepto-fuerte.md` + libro §6.1.4 (empaquetamiento).
- `disenar-prototipo`: borrador 07 + libro §7.1. Mapa de Valor, Encaje Problema-Solución (checklist Mapa de Valor ↔ Perfil del Cliente), prototipos rápidos, Pitch con A.I.D.A. (leer el libro para las 4 letras). Assets: `mapa-de-valor.md`, `encaje-problema-solucion.md`, `pitch-aida.md`, `guion-de-prueba.md`.

### Task 8: Innovación Destilada — escalar y transversal

**Files:** `skills/{validar-supuestos-y-mvp,probar-y-aprender,modelo-de-negocio-y-escalamiento,innovacion-abierta-y-ecosistema}/…`

- `validar-supuestos-y-mvp`: borrador 08 + tabla “No de esta forma / Sino de esta” (de `producto-minimo-viable.png`) + tarjeta de prueba. Assets: `registro-de-supuestos.md`, `tarjeta-de-prueba.md`.
- `probar-y-aprender`: borrador 09 + `templates/tablero-validacion.md` + libro §8.1.2–8.1.3 (6 métricas).
- `modelo-de-negocio-y-escalamiento`: borrador 10 + libro §8.1.1; definir los 9 bloques con preguntas guía; tránsito Product/Market Fit → Business Model Fit.
- `innovacion-abierta-y-ecosistema`: borrador 11 + libro §1.2–1.3; definición y pregunta práctica de cada uno de los 7 patrones y 7 prácticas.
- Al cerrar: `claude plugin eval plugins/innovacion-destilada` completo; subir `plugin.json` y marketplace a `0.5.0`.

### Task 9: Automatización con IA — facilitador y etapa A

**Files:** `plugins/automatizacion-con-ia/skills/{facilitador-automatizacion-con-ia,descubrir-procesos,definir-reto-de-automatizacion,priorizar-flujos}/…`, `plugins/automatizacion-con-ia/README.md`

Fuentes: `../brainstorm/Distilled-Skills/automatizacion-de-procesos-con-ia/`, `prompt_maestro_canvas_automatizacion_IA.md`, `AI_Distilled_Innovation_Enterprise_Offering.md` §3–4, `AI_Automation_Consultancy_Framework_Spec.md`, y como inspiración (sin copiar nombres) los módulos de mapeo, scoping y priorización en la exportación de Notion del caso real de taller (ruta en `.fuentes-locales.md`).

- `facilitador-automatizacion-con-ia`: protocolo de apertura del prompt maestro (resumen ≤ 5 puntos, qué está claro, incertidumbre principal, primera pregunta); 4 puntos de entrada (no sabe qué automatizar / caso definido / tiene prototipo / ya opera); diagrama del spec §6.2; “Regla final” (puede ser mejor no automatizar). Remite a `identificar-reto` y `investigar-y-empatizar` de Innovación Destilada cuando el reto es difuso.
- `descubrir-procesos`: guía de entrevista (nunca abrir con “¿qué quieres automatizar?”; orden contexto → observar trabajo → evidencia → descomponer), ficha de señal (Contexto, Situación, Magnitud con relevancia/urgencia 1–5, Intención), agrupación de señales del mismo problema. Assets: `guia-de-entrevista-de-proceso.md`, `ficha-de-senal.md`, `inventario-de-oportunidades.md`.
- `definir-reto-de-automatizacion`: Scoping Canvas de 6 preguntas (oportunidad, objetivo SMART, “¿Cómo podríamos…?”, antecedentes, segmento, resultados esperados) + recomendación definir/refinar/dividir.
- `priorizar-flujos`: inventario (Flujo, Disparadores, Pasos, Decisiones, Resultado, Dueño, Frecuencia, Esfuerzo h/ejecución) → mapa Valor × Factibilidad (Mermaid `quadrantChart` + tabla) → 5 cubetas (Victorias rápidas, Pilotos estratégicos, Requiere bases, Asistir no automatizar, No automatizar). Variante en `references/`: matriz ponderada impacto/esfuerzo escala 1/3/5 (I1 0.6, I2 0.4, E1 0.4, E2 0.6; índice = impacto/esfuerzo; umbral 3; cuadrantes Victoria rápida, Mejora incremental, Gran apuesta, Reconsiderar). Regla: puntajes de la IA son propuestas; el equipo decide.

### Task 10: Automatización con IA — diseño (etapa B, parte 1)

**Files:** `skills/{mapear-proceso-actual,disenar-proceso-futuro,elegir-patron-y-autonomia,canvas-de-automatizacion}/…`

- `mapear-proceso-actual`: fusiona borradores 02 y 03. Tabla de pasos, Mermaid, RACI, tiempos/volúmenes/excepciones, `proceso-actual.yaml`.
- `disenar-proceso-futuro`: borrador 04 (sin herramientas ni proveedores); opciones por actividad eliminar/simplificar/asistir/automatizar/mantener humano; comparación As-Is vs To-Be sin inventar cifras.
- `elegir-patron-y-autonomia`: árbol de decisión para los 5 patrones (determinística, flujo con IA, copiloto/asistente, agente autónomo, híbrido), escalera de autoridad 0–5 (Sin IA, Asesor, Redactor, Ejecutor controlado, Operador autónomo, Sistema autónomo adaptativo; pilotos 1–3), catálogo de guardrails (condición de riesgo → límite requerido). Aquí sí se permite hablar de capacidades técnicas genéricas, no de proveedores.
- `canvas-de-automatizacion`: 12 bloques con títulos y preguntas textuales de `Canvas-Automatización-IA.png` (ver la imagen), encabezado Flujo/Equipo/Fecha/Versión, pie Aprobado por/Fecha/Notas; se llena conversacionalmente reutilizando los entregables previos; vista A3 en Markdown (tabla 4×3) + versión YAML.

### Task 11: Automatización con IA — validación y continuidad

**Files:** `skills/{supuestos-y-riesgos,prototipos-y-tarjetas-de-prueba,plan-piloto-y-especificacion,crear-skill-de-flujo}/…`

- `supuestos-y-riesgos`: borrador 05 + guardrails de la Tarea 10 (referenciar por nombre de skill, no por ruta).
- `prototipos-y-tarjetas-de-prueba`: borrador 06 + tarjeta de prueba (Creemos que… / Para verificarlo, haremos… / Y mediremos… / Acertamos si…; nivel crítico, costo, tipo, evidencia, confiabilidad, decisión iterar/escalar/pausar/descartar/redefinir reto); tipos de prueba (entrevista, smoke test, conserje, mago de Oz, prototipo clicable, demo funcional, piloto operativo, experimento de proceso); ejemplo ficticio donde la prueba resulta “falsa” y revela variantes del proceso.
- `plan-piloto-y-especificacion`: borrador 07 + bloques 9–12 del Canvas; costo/esfuerzo Bajo/Medio/Alto para construir, operar y mantener; especificación portable (metadatos, actores, pasos, decisiones, esquemas de entrada/salida, reglas, conocimiento requerido, controles, pruebas de aceptación) con advertencia de que portabilidad ≠ ejecución idéntica; distinguir piloto de producción. Patrón de pipeline de vigilancia del spec §6.2 en `references/patrones-de-solucion.md`.
- `crear-skill-de-flujo`: de `prompt-spanish-create-workflow-skill.md`; entrevista breve, separa pasos de lectura vs. que modifican sistemas, nunca guarda credenciales, prueba con ejemplo seguro, produce un `SKILL.md` válido según este mismo estándar (frontmatter, “Úsala cuando”).
- `plan-piloto-y-especificacion` entrega la especificación como `workflow-contract.yaml` siguiendo `assets/workflow-contract.schema.json`. Crear ese esquema en `compartido/archivos/workflow-contract.schema.json` (JSON Schema Draft 2020-12; requeridos `workflow_id`, `version` = `"1.0"`, `actors`, `states`, `steps`, `approval_policies`, `evidence_requirements`; cada paso requiere `step_id`, `trigger`, `inputs`, `outputs`, `success_state`, `failure_state`, `idempotency`, `evidence`; `extensions` libre) y registrarlo en `archivos-compartidos.json` con destino `automatizacion-con-ia/plan-piloto-y-especificacion/assets`. Las claves del esquema quedan en inglés por ser contrato técnico; las descripciones (`description`) en español.
- Al cerrar: eval completo del plugin; versión `0.8.0`.

### Task 12: Implementación Empresarial — contrato, arquitectura y capacidades

**Files:** `plugins/implementacion-empresarial/skills/{facilitador-implementacion-empresarial,arquitectura-de-implementacion,mapeo-de-capacidades-de-plataforma,integracion-segura-y-aprobaciones}/…`, `plugins/implementacion-empresarial/README.md`, `compartido/archivos/capability-map.schema.json`, `compartido/archivos-compartidos.json`

Fuentes: `../brainstorm/Distilled-Skills/2026-10-17-ai-magic-flow-enterprise-pack-b-design.md` y `2026-10-18-ai-magic-flow-enterprise-pack-b.md` (skills 08–10, esquemas, plantillas, perfiles), `AI_Distilled_Innovation_Enterprise_Offering.md` §6–7 y §10 (mapa de backends, rol de los MCPs, gobernanza). El ejemplo de Pack B se reemplaza por un caso **ficticio** (radar de señales regulatorias de una empresa inventada) que se usa de forma coherente en todas las skills del plugin.

- Público: equipo de TI/implementación y consultores; el tono sigue en español claro, pero puede usar términos técnicos con una línea de explicación.
- Registrar `workflow-contract.schema.json` también con destino `implementacion-empresarial/arquitectura-de-implementacion/assets`.
- `facilitador-implementacion-empresarial`: si no hay `workflow-contract`, remite a `plan-piloto-y-especificacion`; mantiene `registro-de-decisiones.md` (decisión, alternativas, dueño, fecha, aprobación); toda configuración específica del cliente se registra como decisión, nunca como valor implícito.
- `arquitectura-de-implementacion` (Pack B 08): arquitectura lógica trazable paso a paso al contrato, límites de componentes, sin plataforma por defecto; orquestador determinístico para aprobaciones, reintentos y procesos largos (la orquestación generativa no es un motor durable). Asset: `plan-de-implementacion.md`.
- `mapeo-de-capacidades-de-plataforma` (Pack B 09): `capability-map.yaml` según `assets/capability-map.schema.json` (crear en `compartido/archivos/`; por requisito: `requirement_id`, `options`, `decision`, `gap`, `owner`, `approval_status`). `references/perfiles/{microsoft,aws,google,self-hosted}.md`: cada uno cubre orquestación, estado, identidad, secretos, aprobaciones, observabilidad, idempotencia y prueba de aceptación; contiene literalmente “No hay conversión automática” y una checklist de validación con aprobación; lleva “Verificado: 2026-10-25”.
- `integracion-segura-y-aprobaciones` (Pack B 10): modelo de amenazas, mínimo privilegio, secretos fuera de artefactos, matriz de aprobación humana para acciones de impacto, auditoría, anonimizar antes de enviar datos a un modelo. Asset: `revision-de-amenazas-y-aprobaciones.md`.
- Graders adicionales de esta tarea: la respuesta no inventa equivalencias entre plataformas y pide aprobación explícita para cada mapeo.

### Task 13: Implementación Empresarial — confiabilidad, pruebas, release y operación

**Files:** `skills/{idempotencia-y-confiabilidad,pruebas-y-evaluacion,release-y-transferencia,operacion-y-aseguramiento-continuo}/…`, `compartido/archivos/evaluation-plan.schema.json`

- `idempotencia-y-confiabilidad` (Pack B 11): por operación repetible, clave idempotente, alcance, retención, clasificación de reintentos (transitorio/permanente), compensación, cola de errores y recuperación. Asset: `registro-de-idempotencia.md`.
- `pruebas-y-evaluacion` (Pack B 12): `evaluation-plan.yaml` según `assets/evaluation-plan.schema.json` (crear en `compartido/archivos/`; `test_categories` debe incluir `functional`, `security`, `resilience`, `ai_quality`); casos positivos y negativos; métricas de calidad de IA de la oferta §10 (exactitud, groundedness, consistencia estructural, selección de herramientas, tasa de escalamiento). Asset: `registro-de-evidencia-de-pruebas.md`.
- `release-y-transferencia` (Pack B 13): prohíbe declarar listo sin dueños, aprobación y rollback. Assets: `preparacion-de-release.md` (contiene “aprobación” y “rollback”), `runbook-de-transferencia.md`.
- `operacion-y-aseguramiento-continuo` (Pack B 14, etapa D de la oferta): observabilidad, alertas, KPIs de valor diferenciando prototipo vs. producción, costos por caso, control de cambios, recertificación periódica, backlog de mejoras que vuelve a `disenar-proceso-futuro`.
- Al cerrar: `claude plugin eval plugins/implementacion-empresarial` completo; versión `0.8.0`; revisor `opus` (override de riesgo) confirma que ningún perfil promete conversión automática ni trae credenciales o endpoints.

### Task 14: Aceleración Comercial — facilitador y etapas 0–3

**Files:** `plugins/aceleracion-comercial/skills/{facilitador-aceleracion-comercial,diagnostico-comercial,segmentacion-e-icp,oferta-y-propuesta-de-valor,proceso-de-ventas-y-pipeline}/…`, `plugins/aceleracion-comercial/README.md`

Fuente: `../brainstorm/Distilled-Skills/metodologia_aceleracion_comercial_distilled_innovation.md`. Quitar etiquetas [OFICIAL]/[PROPUESTO]/[CASOS] y la tabla de casos; aplicar las decisiones del spec §10 (BANT con MEDDICC opcional, CRM agnóstico con versión en hoja de cálculo, sección “Cómo te ayuda la IA aquí” con revisión humana, cronograma 8–12 semanas como referencia).

- `facilitador-aceleracion-comercial`: modalidades A (estructurar ventas de negocio existente), B (validar y lanzar oferta nueva → remite a Innovación Destilada), C (colectivos o sectores); diagrama de 8 etapas con ciclos 7→1, 7→3, 7→4.
- Una skill por etapa 0–3 con las salidas y criterio de salida de la tabla de la fuente; `oferta-y-propuesta-de-valor` reutiliza por nombre `sintetizar-y-redefinir-reto` y `disenar-prototipo` (Perfil del Cliente, Mapa de Valor, pitch A.I.D.A.); `proceso-de-ventas-y-pipeline` incluye el ejemplo B2B de 7 etapas con reglas de entrada.

### Task 15: Aceleración Comercial — etapas 4–7

**Files:** `skills/{crm-y-tableros,kit-comercial-y-entrenamiento,canales-y-generacion-de-demanda,gobierno-comercial-y-forecast}/…`

- Salidas y criterios de salida según la tabla de etapas de la fuente; `gobierno-comercial-y-forecast` incluye la tabla de rituales (diaria, semanal, quincenal, mensual, trimestral), los 13 KPIs con fórmulas en `references/kpis.md` y el “manual del sistema comercial” de transferencia; `canales-y-generacion-de-demanda` reutiliza por nombre `probar-y-aprender` (Tablero de Validación).
- Al cerrar: eval completo del plugin; versión `0.9.0`.

### Task 16: Paquetes multiplataforma, prueba en plataformas y release 1.0.0

**Files:** Modify `CHANGELOG.md`, versiones en `plugin.json` ×4 y `marketplace.json`; `docs/instalacion/*.md` según hallazgos.

- [ ] **Step 1:** `python scripts/empaquetar.py` → `dist/` con 41 zips de skill, 4 `.plugin`, 4 paquetes copiar-pegar; revisar a mano un `INSTRUCCIONES.md` por metodología (se entiende solo, en español, sin rutas rotas).
- [ ] **Step 2: Prueba en Claude Code:** `claude --plugin-dir plugins/innovacion-destilada -p "Tenemos un reto: los clientes abandonan la compra en línea. ¿Por dónde empezamos?"` → activa `facilitador-innovacion-destilada` o `identificar-reto` y hace una sola pregunta. Repetir con una frase por plugin.
- [ ] **Step 3: Prueba manual (Boss o facilitador)**: subir un zip de skill a Claude.ai y a ChatGPT Skills; cargar un paquete copiar-pegar en un Gem de Gemini. Registrar resultado y fecha en cada guía de `docs/instalacion/`.
- [ ] **Step 4:** Revisión de rama completa (`opus`): spec vs. repo, búsqueda final de términos prohibidos (`validar.py` con la lista local completa) y lectura de muestra de skills por tono y calidad.
- [ ] **Step 5:** Versiones a `1.0.0`, `CHANGELOG.md`, commit, `git tag v1.0.0`; push y Release **solo con aprobación de Boss** (es publicación externa).
