---
type: llm
weight: 1
---

The user asked to finish ("Finalizar"), so the agent delivers the final result in Spanish using this structure: (1) a Mapa de Valor with the three parts (productos y servicios, aliviadores, creadores de beneficios), each element pointing to a task, pain or gain of the Perfil del Cliente; (2) an Encaje Problema-Solución checklist crossing the Perfil del Cliente (1ra tarea, 1er dolor, 2do dolor, 1er beneficio) with the Mapa de Valor, marking each as covered/partial/uncovered, naming the gaps (for example the surcharge or the 2do dolor if not covered) and stating that it is a fit on paper, a hypothesis, not market validation. It separates facts (Hecho, backed by what the user reported, e.g. 6 de 7 entrevistas) from assumptions (Supuesto) and pending items (Pendiente por validar), tags claims with their origin, uses stable IDs (for example PRS-01, ALI-01, CRB-01, SUP-01, DEC-01), does not pick a specific technology, and if it includes a Mermaid diagram also includes an equivalent table. It ends by suggesting the next step, validar-supuestos-y-mvp, with a one-line reason. Missing the Mapa de Valor or the encaje is a FAIL.
