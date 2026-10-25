# Herramientas para el plan piloto y la especificación

Nota de fuente: el plan piloto, la línea base → meta, la distinción entre prototipo, piloto y producción, y los bloques 9 a 12 del canvas provienen de la metodología de Distilled Innovation; la lista de validación del contrato, la puerta de entrada a la etapa C y la correspondencia entre canvas y contrato son una adaptación de este plugin.

## 1. Cómo acotar el piloto

| Pregunta | Regla |
|---|---|
| ¿Qué casos entran? | Los que la evidencia ya validó (por ejemplo, una variante del proceso). El resto sigue como hoy o va a revisión |
| ¿Cuántos usuarios? | Pocos y con comparación: una persona usa el flujo nuevo y otra sigue como hoy |
| ¿Cuánto dura? | Lo suficiente para tener casos que enseñen algo (de dos a cuatro semanas es un punto de partida, no una regla) |
| ¿Qué controles tiene? | Aprobación humana en todo efecto externo, modo manual de respaldo y alguien que puede apagar la parte con IA |
| ¿Cuándo se detiene? | Con criterios de parada escritos antes |

Un piloto que ya es la solución completa no es un piloto.

## 2. Prototipo, piloto y producción

| | Prototipo | Piloto | Producción |
|---|---|---|---|
| Para qué sirve | Probar un supuesto con la fidelidad más baja | Probar el flujo con personas reales y riesgo controlado | Operar con valor sostenido |
| Cifras que produce | Indicios (por ejemplo, minutos de aprobación en una hoja preparada a mano) | Resultados reales de alcance acotado | Resultados sostenidos y comparables en el tiempo |
| Cómo se rotulan | "Prototipo" | "Piloto" | "Producción" |
| Qué no se puede afirmar | Que funciona en la operación | Que escala o que el valor se sostiene | Nada fuera de lo medido |

Regla de redacción: nunca presentes una cifra de prototipo como resultado del piloto ni una del piloto como resultado de producción.

## 3. Criterios de éxito y de parada

| Tipo | Ejemplo genérico | Quién lo revisa |
|---|---|---|
| Éxito | El tiempo medio por caso baja a la meta en 20 casos medidos | Dueño del proceso |
| Éxito | Una revisión de muestra no encuentra casos críticos sin marcar | Quien responde por el criterio |
| Parada | Un caso crítico sin marcar: se detiene la parte con IA y se vuelve al modo manual | Dueño del proceso |
| Parada | Más de una cuarta parte de las propuestas se reescribe | Dueño del proceso y quien aprueba |

Con pocos casos, la tasa de errores es indicativa. Dilo, y no declares éxito o fracaso por una diferencia de uno o dos casos.

## 4. De dónde sale cada bloque (9 a 12)

| Bloque | Se alimenta de | Qué se agrega aquí |
|---|---|---|
| 9 Métricas y evaluación | Reto (línea base y meta), registro de evidencia | Separación prototipo, piloto y producción; cómo se mide en el piloto |
| 10 Plan piloto | Borrador del canvas, evidencia de las pruebas | Alcance acotado, criterios de éxito y parada, qué aprenderemos |
| 11 Costo y esfuerzo | Clasificación inicial del canvas | Construir, operar y mantener por alcance; qué lo cambia |
| 12 Próximos pasos | Pendientes y supuestos | Acción, rol responsable, fecha y dependencia |

## 5. De dónde sale cada parte del contrato

| Parte del contrato | Se alimenta de |
|---|---|
| `metadata` (nombre, dueño, objetivo, madurez, aviso de portabilidad) | Reto, canvas bloque 1, decisiones |
| `actors` | RACI y bloque 6 del canvas: personas, componente de IA, reglas |
| `states` | Flujo futuro (`FUT-nn`): cada paso deja el flujo en un estado, más los de espera y falla |
| `steps` (decisiones incluidas, con `kind: decision`) | `FUT-nn` y `CAP-nn`; disparador y entradas y salidas en palabras del negocio |
| `steps[].business_rules` y `required_knowledge` | Reglas de agenda, criterios y fuentes que el paso necesita |
| `steps[].authority_level` y `guardrails` | Escalera de autoridad y catálogo de guardrails |
| `steps[].idempotency` y `retry_policy` | Qué pasa si el paso se ejecuta dos veces o falla |
| `approval_policies` | Control humano de la escalera y guardrails de aprobación |
| `evidence_requirements` | La columna "qué se registra" de la escalera |
| `metrics` | Bloque 9 |
| `acceptance_tests` | Supuestos probados, guardrails y casos negativos |
| `required_capabilities` | Capacidades `CAP-nn` en palabras genéricas, nunca productos |
| `extensions` | Lo propio de este flujo que no cabe en lo anterior (por ejemplo, el alcance del piloto) |

## 6. Lista de validación del contrato

Con cualquier validador de JSON Schema Draft 2020-12 contra `workflow-contract.schema.json`, o a mano con esta lista:

1. Las claves de primer nivel `workflow_id`, `version`, `actors`, `states`, `steps`, `approval_policies` y `evidence_requirements` existen, y `version` es exactamente `"1.0"`.
2. Cada paso tiene `step_id`, `trigger`, `inputs`, `outputs`, `success_state`, `failure_state`, `idempotency` y `evidence`.
3. Cada `actor`, `success_state`, `failure_state`, `approval_policy` y `evidence` de un paso apunta a un ID que existe.
4. Todo paso con `external_effect: true` tiene una política de aprobación y una estrategia de idempotencia distinta de `not_applicable`.
5. Todo paso con IA declara su nivel de autoridad (los pilotos, 1 a 3) y sus guardrails.
6. Hay al menos un caso negativo en `acceptance_tests` por cada guardrail de impacto alto.
7. No hay credenciales, direcciones reales, nombres de productos ni datos personales.
8. Las claves están en inglés y las descripciones en español.

## 7. Advertencia de portabilidad

La **definición** del flujo es portable: describe qué hace, quién decide y qué evidencia deja. La **ejecución** no tiene por qué ser idéntica en cada plataforma: pueden diferir las transacciones, la identidad y los permisos, los tiempos de espera, la orquestación, los costos y el comportamiento del modelo. Cada implementación debe documentar sus desviaciones y correr pruebas de conformidad contra las `acceptance_tests`. No existe conversión automática entre plataformas ni equivalencia funcional que se pueda dar por supuesta.

## 8. Errores frecuentes

| Error | Cómo se evita |
|---|---|
| Un piloto que cubre todo el proceso | Acotarlo a la variante validada |
| Cifras de prototipo presentadas como resultados | Rotularlas "prototipo" |
| Contrato con herramientas o direcciones reales | Describir capacidades; lo concreto se decide en la etapa C |
| Pasos con efectos externos sin aprobación | Revisar el punto 4 de la lista |
| Costo en cifras inventadas | Bajo, Medio o Alto con factores; retorno "No sé" |
| Próximos pasos sin responsable | Cada acción con un rol y una fecha |
