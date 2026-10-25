# Reglas de calificación

Organización: ___  Fecha: ___  ICP: ICP-__  Versión: borrador 1

Base: BANT simplificado. Para ventas complejas B2B (varios decisores, ciclo largo, ticket alto) se suman las preguntas MEDDICC como notas opcionales.

## 1. BANT simplificado

Sí = 2, Parcial = 1, No = 0.

| Criterio | Pregunta | Qué cuenta como Sí | Qué cuenta como Parcial | Qué cuenta como No |
|---|---|---|---|---|
| Presupuesto | | | | |
| Autoridad | | | | |
| Necesidad | | | | |
| Tiempo | | | | |

## 2. Regla de decisión (`REG-nn`)

| ID | Resultado | Condición | Siguiente acción |
|---|---|---|---|
| REG-01 | Calificada: pasa a ETA-03 | | |
| REG-02 | Nutrir | | |
| REG-03 | Descartar | | |

Los umbrales son una guía: se ajustan con los resultados y el cambio se registra como decisión (`DEC-nn`).

## 3. Preguntas MEDDICC opcionales

| Letra | Qué se averigua | Pregunta | Respuesta (notas de la oportunidad) |
|---|---|---|---|
| Métricas | Qué resultado medirán | | |
| Comprador económico | Quién controla el presupuesto | | |
| Criterios de decisión | Con qué comparan | | |
| Proceso de decisión | Pasos y fechas | | |
| Identificación del dolor | Qué cuesta no resolverlo | | |
| Campeón | Quién impulsa dentro de la cuenta | | |
| Competencia | Qué alternativas evalúan, incluida no hacer nada | | |

## 4. Diagrama de decisión (Mermaid con tabla equivalente)

```mermaid
flowchart TD
  A[Lead con respuesta] --> B[Puntaje BANT]
  B --> C{¿Necesidad en Sí y total suficiente?}
  C -- Sí --> D[Calificada: ETA-03]
  C -- Parcial --> E[Nutrir con fecha de revisión]
  C -- No --> F[Descartar con motivo]
```

Equivalente en tabla: la sección 2.

## 5. Revisión de la regla

Cada mes: ¿las oportunidades calificadas se ganan más que las no calificadas? Si no, la regla no discrimina y se ajusta.

| Mes | Calificadas ganadas / calificadas | No calificadas ganadas / no calificadas | Ajuste |
|---|---|---|---|
| | | | |
