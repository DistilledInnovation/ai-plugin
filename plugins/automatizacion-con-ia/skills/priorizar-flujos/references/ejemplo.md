# Ejemplo: Priorizar flujos en una distribuidora ficticia

Empresa inventada: **Distribuidora Rioclaro** (insumos de oficina y limpieza para empresas pequeñas; 85 empleados). Todo lo siguiente es ficticio. Continúa los ejemplos anteriores: las cinco oportunidades `OPO-01` a `OPO-05` ya tienen un reto (`RET-01` completo; `RET-02` a `RET-05` en versión breve: reto, objetivo con línea base y dueño).

## Turno 1

**Usuaria:** Ya tenemos los cinco retos definidos. ¿Cuál automatizamos primero?

**Facilitador:** Antes de elegir, armemos el inventario para que la decisión sea comparable. ¿Quiénes del equipo participarán en el puntaje?

## Turno 2

**Usuaria:** La jefa de Atención, el jefe de Bodega, la jefa de Cuentas por Cobrar, una persona de Ventas y yo.

**Facilitador:** Perfecto, el puntaje lo acuerdan ustedes y yo les propongo uno con su justificación. Primero el inventario.

| ID | Flujo | Reto | Disparadores | Pasos | Decisiones | Resultado | Dueño | Frecuencia | Esfuerzo | Horas/mes |
|---|---|---|---|---|---|---|---|---|---|---|
| `FLU-01` | Registrar pedidos | `RET-01` | Llega correo o mensaje con pedido | Leer, identificar cliente y productos, registrar, confirmar | Qué hacer si no hay stock | Pedido registrado y confirmado | Jefa de Atención | ~120/día | 0,1 h | ~264 |
| `FLU-02` | Informar el estado de pedidos | `RET-02` | Cliente pregunta por su pedido | Buscar en tres lugares, armar respuesta, responder | Qué decir si hay retraso | Cliente informado | Jefa de Atención | ~40/día | ~0,07 h | ~59 |
| `FLU-03` | Conciliar pagos con facturas | `RET-03` | Entra un pago | Cruzar con factura, detectar diferencia, resolver | Cómo tratar pagos parciales o descuentos | Factura conciliada | Jefa de Cuentas por Cobrar | ~25/semana | 0,5 h | ~50 |
| `FLU-04` | Cotizaciones a medida | `RET-04` | Cliente grande pide una oferta | Revisar historial, definir precios, armar oferta | Qué descuento ofrecer | Oferta enviada | Gerente de Ventas | ~6/semana | 2 h | ~48 |
| `FLU-05` | Aprobar crédito a clientes nuevos | `RET-05` | Cliente nuevo pide crédito | Reunir información de tres lados, evaluar, decidir | Aprobar, rechazar o pedir garantías | Crédito decidido | Gerente de Finanzas | ~8/semana | 1,5 h | ~48 |

Horas por mes: frecuencia mensual por esfuerzo (22 días hábiles al mes, 4 semanas). Frecuencias y esfuerzos, salvo los de `FLU-01` (medidos), son Dicho por participante.

## Turno 3

**Facilitador:** Esta es mi propuesta de puntaje (Inferencia de la IA). Recuerden que en Riesgo y control, 5 significa bien controlado. ¿Estás de acuerdo con estos puntajes, o qué cambiarías y por qué?

| ID | Valor | Idoneidad | Preparación | Riesgo y control | Total | Justificación breve |
|---|---|---|---|---|---|---|
| `FLU-01` | 5 | 4 | 3 | 4 | 16 | Es el flujo con más horas al mes; reglas claras con algo de interpretación; el error se detecta al confirmar si una persona revisa |
| `FLU-02` | 3 | 5 | 2 | 4 | 14 | Consulta repetitiva, pero la información está en tres lugares y no hay un estado único |
| `FLU-03` | 4 | 2 | 3 | 3 | 12 | Muchas excepciones (pagos parciales, descuentos); un error cuesta dinero pero se corrige |
| `FLU-04` | 3 | 2 | 3 | 2 | 10 | Cada oferta es distinta; el precio y el descuento son decisión comercial con efecto en el margen |
| `FLU-05` | 2 | 2 | 3 | 1 | 8 | Pocos casos; un error de crédito tiene consecuencia financiera difícil de revertir |

**Usuaria (equipo):** Estamos de acuerdo, salvo el valor de `FLU-02`: creemos que es 3 porque ahorra tiempo pero no cambia ventas. Lo dejamos en 3.

**Facilitador:** Anotado: puntajes acordados por el equipo. Los extremos tienen su nota: el 5 de `FLU-01` (264 horas por mes, medido en 20 pedidos) y el 1 de `FLU-05` (consecuencia financiera difícil de revertir).

## Turno 4

Factibilidad = promedio de idoneidad, preparación y riesgo y control. Coordenadas: x = (factibilidad − 1) / 4, y = (valor − 1) / 4.

| ID | Valor | Factibilidad | x | y |
|---|---|---|---|---|
| `FLU-01` | 5 | 3,67 | 0,67 | 1,00 |
| `FLU-02` | 3 | 3,67 | 0,67 | 0,50 |
| `FLU-03` | 4 | 2,67 | 0,42 | 0,75 |
| `FLU-04` | 3 | 2,33 | 0,33 | 0,50 |
| `FLU-05` | 2 | 2,00 | 0,25 | 0,25 |

```mermaid
quadrantChart
  title Mapa Valor x Factibilidad
  x-axis Factibilidad baja --> Factibilidad alta
  y-axis Valor bajo --> Valor alto
  quadrant-1 Victorias rápidas
  quadrant-2 Pilotos estratégicos o bases
  quadrant-3 Poco valor y difícil
  quadrant-4 Poco valor y fácil
  FLU-01: [0.67, 1.00]
  FLU-02: [0.67, 0.50]
  FLU-03: [0.42, 0.75]
  FLU-04: [0.33, 0.50]
  FLU-05: [0.25, 0.25]
```

| Cuadrante | Flujos |
|---|---|
| Victorias rápidas (valor ≥ 3 y factibilidad ≥ 3) | `FLU-01`, `FLU-02` |
| Pilotos estratégicos o bases (valor ≥ 3 y factibilidad < 3) | `FLU-03`, `FLU-04` |
| Poco valor y difícil | `FLU-05` |
| Poco valor y fácil | Ninguno |

## Entregable: cubetas

Con el orden de decisión (el mapa es provisional):

| Cubeta | Flujo | Por qué | Qué sigue |
|---|---|---|---|
| Victorias rápidas | `FLU-01` | Valor 5, factibilidad 3,67 y riesgo y control 4 | Caso piloto candidato |
| Pilotos estratégicos | `FLU-03` | Valor 4, pero la idoneidad es 2: falta saber si las excepciones se pueden clasificar | Revisar 30 casos de excepciones antes de diseñar |
| Requiere bases | `FLU-02` | Estaba en Victorias rápidas en el mapa, pero la preparación es 2: no existe un estado único del pedido | Resolver dónde vive el estado (dueño: jefe de Bodega) |
| Asistir no automatizar | `FLU-04` | El precio y el descuento son una decisión comercial; riesgo y control 2 con valor 3 | La IA podría preparar el historial del cliente; decide Ventas |
| No automatizar | `FLU-05` | Valor 2 y riesgo y control 1 | Se mantiene humano; se puede simplificar el reunir información |

**Decisión `DEC-01`** (decidió el equipo): `FLU-01` es el caso piloto candidato. **Línea base inicial** (`HAL-01`, medido en 20 pedidos): unos 6 minutos por pedido, unos 120 pedidos al día, unas 264 horas por mes; errores de código, unos 4 de cada 100 (**Supuesto** `SUP-01`, pendiente de contar una semana).

Sin elegir tecnología. **Siguiente paso sugerido:** `mapear-proceso-actual` (Próximamente) para documentar cómo se registra hoy un pedido, con pasos, decisiones y responsables. Mientras tanto, el facilitador puede acompañar esa conversación.

## Lo que se ve en este ejemplo

- Cada flujo tiene un reto definido antes de puntuarse.
- Los puntajes de la IA se presentaron como propuesta; el equipo cambió uno y quedó como acuerdo.
- El mapa dejó a `FLU-02` en Victorias rápidas, pero el orden de decisión lo movió a Requiere bases por la preparación.
- `FLU-04` y `FLU-05` no se automatizan, y eso es un resultado válido de la priorización.
- El 5 y el 1 llevan nota que los justifica.
