---
type: llm
weight: 2
---

The user asked to finish ("Finalizar"), so the agent delivers the final result in Spanish using this structure: el diagnóstico de etapa (etapa, evidencia como Hecho, supuestos, incertidumbre principal), el bloque YAML de estado del proyecto (etapa, reto, actores, evidencia, supuestos, siguiente_skill) y un resumen en máximo cinco puntos. It must clearly separate facts (Hecho, backed by what the user said or evidence) from assumptions (Supuesto) and pending items (Pendiente por validar), tag claims with their origin, use stable IDs (for example HAL-01, SUP-01, DEC-01), and not invent data the user did not provide: missing information shows up as a gap or a provisional draft marked as such. If it includes a Mermaid diagram it must also include an equivalent table. It ends by suggesting the next skill with a one-line reason: identificar-reto (the stage is preparation: no reto yet and no customer evidence) or alinear-equipo.
