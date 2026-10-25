# Herramientas para diseñar el proceso futuro

Nota de fuente: la escalera de opciones (eliminar, simplificar, asistir, automatizar, mantener humano), la descripción de capacidades por verbo y la separación entre diseño funcional y decisión técnica provienen de la metodología de Automatización con IA de Distilled Innovation; el catálogo de capacidades y las plantillas son una adaptación de este plugin.

## 1. Catálogo de capacidades funcionales

Descríbelas por lo que hacen, no por cómo se hacen. Cada una es una hipótesis hasta probarla.

| Capacidad | Qué hace | Entra | Sale | Pregunta de riesgo |
|---|---|---|---|---|
| Clasificar | Asigna una categoría | Texto, documento o dato | Categoría y nivel de certeza | ¿Qué pasa si se equivoca de categoría? |
| Extraer | Saca datos concretos de un texto o documento | Texto libre o archivo | Campos estructurados | ¿Y si el dato no está o es ambiguo? |
| Resumir | Condensa información larga | Documentos, historial | Resumen con sus fuentes | ¿Puede omitir algo que importa? |
| Validar | Comprueba reglas o coincidencias | Datos | Pasa, no pasa o duda | ¿Qué hacemos con los casos dudosos? |
| Recuperar | Encuentra información relevante en lo que ya existe | Pregunta o contexto | Fragmentos con su origen | ¿Es la fuente vigente y aprobada? |
| Recomendar | Sugiere una opción con criterios | Datos y reglas | Opción y motivo | ¿Quién decide si se sigue la sugerencia? |
| Redactar | Prepara un borrador de texto | Datos y plantilla | Borrador | ¿Quién lo revisa antes de enviarlo? |
| Registrar | Deja constancia o actualiza un registro | Datos aprobados | Registro actualizado | ¿Se puede deshacer? |
| Notificar | Avisa a una persona | Evento | Aviso | ¿A quién y con qué urgencia? |
| Calcular o priorizar | Aplica fórmulas o reglas de orden | Datos | Resultado ordenado | ¿Las reglas son estables? |

Muchas de estas capacidades se cumplen con reglas simples (validar, calcular, registrar, notificar). La IA se justifica sobre todo donde hay texto libre o criterio flexible (clasificar, extraer, resumir, redactar). Esa distinción se resuelve en `elegir-patron-y-autonomia`, no aquí.

## 2. Preguntas para cada actividad

| Opción | Preguntas de apoyo |
|---|---|
| Eliminar | ¿Quién usa el resultado de este paso? ¿Qué se rompe si no existe? ¿Existe por una regla vieja o un error de otro paso? |
| Simplificar | ¿Se pueden unificar canales o formatos? ¿Se pide algún dato dos veces? ¿Una regla clara quitaría una decisión? |
| Asistir | ¿Quién decide hoy? ¿Qué información le falta o le sobra? ¿Qué le prepararía el apoyo? |
| Automatizar | ¿Las reglas son estables? ¿Cómo se detecta un error? ¿Se puede deshacer? ¿Qué casos pasan a una persona? |
| Mantener humano | ¿Hay empatía, juicio clínico o legal, o consecuencia grave? ¿Qué parte se puede simplificar sin quitar la decisión? |

## 3. Diseñar las excepciones

1. Parte de las excepciones del As-Is (`EXC-nn`).
2. Para cada una decide: **se evita** (el diseño la elimina), **se detecta** (el sistema la marca y la manda a una persona) o **se mantiene** (como hoy).
3. Define quién recibe lo que se marca y en cuánto tiempo se espera una respuesta.
4. Toda decisión con duda, certeza baja o consecuencia alta pasa a una persona. Esa regla se afina en `elegir-patron-y-autonomia` con los guardrails.

## 4. Cómo escribir la comparación sin inventar cifras

| Situación | Cómo se escribe |
|---|---|
| Hay línea base medida y meta del reto | "Hoy: 6 min por caso (medido). Meta del reto: 3 min. Se comprobará midiendo 20 casos." |
| Hay línea base dicha, sin medir | "Hoy: unas 4 de cada 100 (Dicho por participante, pendiente de contar)." |
| No hay dato | "No sé. Medir: ..." |
| Mejora cualitativa esperada | "Hipótesis: el paciente recibe horarios en la primera respuesta." |

Nunca escribas "ahorrará 50 %" si nadie lo midió ni lo fijó como meta.

## 5. Validar el diseño

Muestra el To-Be a quien opera el flujo, no solo al dueño. Pregunta: "¿Qué parte no funcionaría un lunes con mucho trabajo?". Las objeciones se anotan como supuestos a probar o como cambios al diseño, con quién las dijo.
