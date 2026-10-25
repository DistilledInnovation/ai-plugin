# Plan piloto

Flujo: ___ (`FLU-__`)  Versión: ___  Fecha: ___  Aprueba el plan: ___

Un piloto es el experimento más pequeño con personas reales que sigue enseñando algo. No es producción: tiene alcance, tiempo, usuarios y controles acotados.

## 1. Alcance, usuarios y duración (bloque 10 del canvas)

| Elemento | Respuesta |
|---|---|
| Qué entra (casos, canales, variantes, volumen estimado con su procedencia) | |
| Qué **no** entra y cómo se maneja (sigue como hoy, va a revisión, queda para otra etapa) | |
| Usuarios (quién opera, quién compara, quién revisa) | |
| Duración y fechas (las que no dio la persona, como Propuesta) | |
| Nivel de autoridad y guardrails que rigen (`GRD-__`) | |
| Modo manual de respaldo y quién puede activarlo | |

## 2. Línea base → meta (bloque 9 del canvas)

Cada métrica con su procedencia y dónde se mide. **Prototipo** es lo medido en pruebas con simulación; **piloto**, con personas reales y alcance acotado; **producción**, lo sostenido en el tiempo (no existe todavía).

| Métrica | Línea base (procedencia) | Meta | Prototipo (`PRU-__`) | Piloto (cómo se mide) | Producción |
|---|---|---|---|---|---|
| | | | | | Pendiente: se mide después de la etapa C |

## 3. Criterios de éxito y de parada

| Tipo | Criterio (umbral fijado antes de empezar) | Quién lo revisa |
|---|---|---|
| Éxito | | |
| Parada (detiene la parte con IA y vuelve al modo manual) | | |

Muestra: ___ casos esperados. Con pocos casos, la tasa es **indicativa, no concluyente**; dilo en el informe del piloto.

## 4. Qué aprenderemos

| Pregunta o supuesto | Cómo lo sabremos | Decisión que habilita |
|---|---|---|
| `SUP-__` | | |

## 5. Costo y esfuerzo (bloque 11 del canvas)

Resumen; el detalle está en `costo-y-esfuerzo.md`.

| Dimensión | Piloto | Si se amplía el alcance | Procedencia |
|---|---|---|---|
| Construir | Bajo, Medio o Alto | | Supuesto |
| Operar | | | Supuesto |
| Mantener | | | Supuesto |

## 6. Próximos pasos (bloque 12 del canvas)

| Acción | Responsable (rol) | Fecha (dada por la persona o Propuesta) | Dependencia |
|---|---|---|---|
| | | | |

## 7. Piloto, prototipo y producción

| | Prototipo | Piloto | Producción |
|---|---|---|---|
| Quién opera | El equipo de diseño o una persona que simula | Usuarios reales, alcance acotado | El equipo dueño, a escala |
| Datos | Ficticios o anonimizados | Reales, con autorización y controles | Reales, con gobierno completo |
| Controles | Los de la prueba | Aprobación humana y modo manual | Los del plugin Implementación Empresarial (seguridad, confiabilidad, observabilidad, recuperación) |
| Qué se concluye | Si un supuesto se sostiene | Si el flujo da valor con control | Valor sostenido y operación estable |

## 8. Puerta de entrada a la etapa C (Implementación Empresarial)

Quién decide: ___ (`DEC-__`). Resultado: **Pasa**, **Pasa con condiciones** o **No pasa todavía**.

| Condición | Cumple (Sí, Parcial o No) | Evidencia o pendiente |
|---|---|---|
| Los supuestos críticos tienen evidencia o una decisión explícita sobre el riesgo que queda | | |
| El piloto dio resultados reales frente a la meta (no solo cifras de prototipo) | | |
| Hay un dueño del flujo y quien aprueba el pase | | |
| Niveles de autoridad y guardrails vigentes; el modo manual de respaldo funciona | | |
| Datos sensibles identificados y autorización de uso confirmada | | |
| El `workflow-contract.yaml` cumple el esquema y se puede trazar al canvas | | |
| Costo y esfuerzo reevaluados con datos del piloto | | |
| Criterios de aceptación para producción definidos (qué más se exige además de lo del piloto) | | |

**Advertencia de portabilidad:** la especificación es portable como definición; la ejecución no tiene por qué ser idéntica en cada plataforma (transacciones, identidad, tiempos de espera, orquestación, costos y comportamiento del modelo). Nada de este plan promete conversión automática entre plataformas.
