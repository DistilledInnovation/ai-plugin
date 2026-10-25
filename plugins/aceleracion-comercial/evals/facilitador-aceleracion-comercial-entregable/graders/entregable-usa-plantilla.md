---
type: llm
weight: 2
---

The user asked to finish ("Finalizar"), so the agent delivers in Spanish: a summary of at most five points, what is already clear, the main uncertainty, the diagnosed modality (A, structuring the sales of an existing business, because there are already paying customers) and the diagnosed stage (stage 0, diagnosis and baseline, because there are no numbers per stage or agreed priorities), and the project state (YAML or equivalent) with Hecho (30 contactos, 11 reuniones, 5 propuestas, 3 ventas, 8 clients, the owner closed everything) clearly separated from Supuesto and Pendiente por validar (why proposals fall, which numbers are unknown), tagged by origin and with stable IDs (for example HAL-01, SUP-01, DEC-01). It recommends the next skill `diagnostico-comercial` with a one-line reason, refers to the 4 to 7 stages by their skills if it mentions them, does not recommend specific tools, software or channels, and does not promise a percentage of improvement. If it includes a Mermaid diagram it also includes an equivalent table. Missing the modality, the stage, the Hecho/Supuesto separation or the next skill is a FAIL.
