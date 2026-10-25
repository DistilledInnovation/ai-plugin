# Variante: matriz ponderada impacto / esfuerzo

Úsala cuando el equipo prefiera una lectura de **impacto contra esfuerzo** con pesos explícitos, en lugar del mapa Valor × Factibilidad con cinco cubetas. Las dos no se mezclan en un mismo ejercicio: elige una. Plantilla en `assets/matriz-ponderada.md`.

Nota de fuente: variante basada en prácticas de matrices de esfuerzo contra impacto con criterios ponderados, adaptada de forma genérica.

## Cuándo conviene

- El equipo ya tiene retos definidos y quiere ordenarlos por rendimiento.
- Se compara trabajo de distinta naturaleza (no solo flujos automatizables).
- Se quiere un índice numérico para ordenar una lista larga.

Si lo que importa es decidir **qué no automatizar** o **qué asistir**, usa las cinco cubetas: esta variante no distingue juicio humano ni riesgo.

## Criterios y pesos (escala 1 / 3 / 5)

| Dimensión | Criterio | Peso | 1 | 3 | 5 |
|---|---|---|---|---|---|
| Impacto | I1. Resultado de cara al reto | 0,6 | Logra menos de lo esperado | Logra lo esperado | Logra lo esperado y agrega valor |
| Impacto | I2. Objetivos y metas estratégicas | 0,4 | No aporta al propósito | Aporte indirecto | Aporte directo |
| Esfuerzo | E1. Tiempo | 0,4 | Rango corto | Rango medio | Rango largo |
| Esfuerzo | E2. Recursos técnicos y financieros | 0,6 | Ninguno adicional | Solo uno de los dos | Ambos |

Los rangos de E1 los define el equipo antes de puntuar (por ejemplo, 1 = hasta un mes, 3 = de uno a tres meses, 5 = más de tres) y se anotan en la plantilla.

## Cálculo

- **Impacto** = 0,6 × I1 + 0,4 × I2
- **Esfuerzo** = 0,4 × E1 + 0,6 × E2
- **Índice de prioridad** = Impacto / Esfuerzo (más alto = más rendimiento; ordena la lista)
- **Umbral = 3**: un impacto o esfuerzo de 3 o más es alto; menos de 3 es bajo.

## Cuadrantes

| Cuadrante | Impacto | Esfuerzo | Qué hacer |
|---|---|---|---|
| Victoria rápida | Alto | Bajo | Prioridad máxima |
| Mejora incremental | Bajo | Bajo | Si sobra capacidad |
| Gran apuesta | Alto | Alto | Planear con recursos y decisión explícita |
| Reconsiderar | Bajo | Alto | Replantear, dividir o descartar por ahora |

## Reglas de calidad

- **Puntúa por consenso del equipo**, no por promedio de opiniones.
- **Justifica los extremos** (1 o 5) en las notas.
- **Los puntajes de la IA son propuestas** (Inferencia de la IA) hasta que el equipo los confirme.
- **No priorices un reto sin definir.**
- El índice ordena; la decisión de qué hacer es del equipo y se registra como `DEC-nn`.

## Ejemplo con los flujos del ejemplo ficticio

Puntajes propuestos (pendientes de confirmar por el equipo):

| ID | Flujo | I1 | I2 | E1 | E2 | Impacto | Esfuerzo | Índice | Cuadrante |
|---|---|---|---|---|---|---|---|---|---|
| FLU-01 | Registrar pedidos | 5 | 3 | 1 | 3 | 4,2 | 2,2 | 1,9 | Victoria rápida |
| FLU-02 | Informar el estado de pedidos | 3 | 3 | 3 | 5 | 3,0 | 4,2 | 0,7 | Gran apuesta |
| FLU-04 | Cotizaciones a medida | 3 | 1 | 3 | 3 | 2,2 | 3,0 | 0,7 | Reconsiderar |

Lectura: el índice por sí solo no dice qué hacer con `FLU-02`: es una Gran apuesta porque requiere resolver antes dónde vive el estado del pedido (algo que las cubetas llaman Requiere bases). Por eso, cuando importa el riesgo o el juicio humano, conviene la clasificación en cinco cubetas.

## Cómo conversarlo

1. Confirma que cada fila tiene un reto definido.
2. Pregunta si el equipo acuerda los rangos de tiempo (E1).
3. Propón los cuatro puntajes por flujo con una línea de justificación y pide ajustes.
4. Muestra la tabla con índice y cuadrante, más el diagrama Mermaid con su tabla equivalente.
5. Pregunta: "¿Con cuál empezamos y qué queda en espera?". Registra la decisión.
