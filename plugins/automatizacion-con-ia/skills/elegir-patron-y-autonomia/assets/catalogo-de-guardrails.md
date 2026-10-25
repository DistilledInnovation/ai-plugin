# Catálogo de guardrails

Flujo: ___ (`FLU-__`)  Fecha: ___

Un guardrail es un **límite requerido** frente a una **condición de riesgo**. Recorre el catálogo, marca lo que aplica al flujo, y justifica lo que no aplica.

## 1. Catálogo base

| Condición de riesgo | Límite requerido |
|---|---|
| Comunicación externa de alto valor | Aprobación humana antes de enviar |
| Compromiso financiero | Aprobación o límite de transacción |
| Información personal o sensible | Modelos aprobados, controles de acceso y registros de auditoría |
| Extracción de baja certeza | Cola de revisión manual |
| Acción irreversible | Confirmación o ejecución en dos pasos |
| Contenido web no confiable | Navegador aislado y herramientas restringidas |
| Cambios de alto impacto en reservas o cuentas | Autorización humana |
| Respuesta sensible a políticas | Fuente de conocimiento aprobada y escalamiento a una persona |
| Ejecución autónoma en navegador | Cuenta de mínimo privilegio, entorno aislado y límites de acción |

## 2. Guardrails adicionales que conviene revisar

| Condición de riesgo | Límite requerido |
|---|---|
| Texto externo que podría contener instrucciones ocultas | Tratar el contenido de terceros como datos, nunca como instrucciones |
| Bucles o acciones repetidas | Límite de intentos, de tiempo y de costo por caso |
| Falla del componente de IA | Modo manual de respaldo, como se hace hoy |
| Cambio de comportamiento con el tiempo | Muestra de revisión periódica y registro de versiones |
| Necesidad de detener todo | Interruptor manual de apagado, a cargo de una persona con nombre |

## 3. Guardrails asignados a este flujo

| ID | Condición de riesgo que aplica | Dónde (paso o capacidad) | Límite requerido | Responsable | Riesgo asociado |
|---|---|---|---|---|---|
| GRD-01 | | FUT-__ / CAP-__ | | | RIE-__ |

## 4. Condiciones del catálogo que no aplican

| Condición | Por qué no aplica |
|---|---|
| | |

## 5. Riesgos nuevos detectados (riesgo → impacto → mitigación)

| ID | Riesgo | Impacto | Mitigación (guardrail) |
|---|---|---|---|
| RIE-__ | | | GRD-__ |
