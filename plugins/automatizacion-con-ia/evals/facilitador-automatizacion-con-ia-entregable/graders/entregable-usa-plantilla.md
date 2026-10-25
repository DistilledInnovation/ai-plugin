---
type: llm
weight: 2
---

The user asked to finish ("Finalizar"), so the agent delivers the final result in Spanish: a summary of at most five points, what is already clear, the main uncertainty, the diagnosed entry point (the user does not know what to automate, so entry point 1, stage A), the project state (YAML or equivalent) with Hecho (the 40 hours per month measured on a time sheet) clearly separated from Supuesto (the chatbot would solve everything) and Pendiente por validar (no process list, no talk with the team), tagged by origin and with stable IDs (for example HAL-01, SUP-01, DEC-01). It recommends the next skill `descubrir-procesos` with a one-line reason. It does not choose a technology or promise AI, and it states that the best answer may be not to automate, to simplify first, or to postpone. If it includes a Mermaid diagram it also includes an equivalent table. If it mentions skills that are not available yet (for example mapear-proceso-actual) it labels them as Próximamente and does not invent their templates. Missing the entry point, the Hecho/Supuesto separation or the next skill is a FAIL.
