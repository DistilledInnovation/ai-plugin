# Trazabilidad contrato → componentes

Flujo: ___ (`FLU-__`)  Contrato (fecha): ___  Plan de implementación (versión): ___

Regla: cada elemento del contrato tiene al menos un componente responsable; cada componente responde al menos a un elemento del contrato. Lo que no cumple va a la sección 6.

## 1. Pasos

| Paso | Tipo | Efecto externo | Componente que ejecuta | Componentes de apoyo | Aprobación (política) | Idempotencia | Evidencia | Estado al terminar (éxito / falla) |
|---|---|---|---|---|---|---|---|---|
| `FUT-__` | deterministic / ai_assisted / decision / wait / human_task | Sí / No | | | `APR-__` o No aplica | | `EVD-__` | `ST-__` / `ST-__` |

## 2. Políticas de aprobación

| Política | Pasos | Rol aprobador | Dónde se aprueba (componente) | Qué bloquea hasta aprobar | Si nadie responde |
|---|---|---|---|---|---|
| `APR-__` | | | | | |

## 3. Evidencias

| Evidencia | Qué se registra | Componente que la produce | Dónde se guarda | Retención (decisión) |
|---|---|---|---|---|
| `EVD-__` | | | | `DEC-__` |

## 4. Guardrails

| Guardrail | Qué limita | Componente que lo hace cumplir | Cómo se comprueba |
|---|---|---|---|
| `GRD-__` | | | |

## 5. Pruebas de aceptación

| Prueba | Pasos cubiertos | Componentes que intervienen | Positiva / negativa |
|---|---|---|---|
| `AT-__` | | | |

## 6. Brechas y preguntas

| Tipo | Elemento | Descripción | Qué se hace | Decisión |
|---|---|---|---|---|
| Elemento sin componente / Componente sin elemento | | | | `DEC-__` |
