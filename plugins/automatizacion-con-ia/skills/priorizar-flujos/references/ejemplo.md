# Ejemplo: Priorizar flujos en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa los ejemplos anteriores: las cinco oportunidades `OPO-01` a `OPO-05` ya tienen un reto (`RET-01` completo; `RET-02` a `RET-05` en versión breve: reto, objetivo con línea base y dueño).

## Turno 1

**Usuaria:** Ya tenemos los cinco retos definidos. ¿Cuál automatizamos primero?

**Facilitador:** Antes de elegir, armemos el inventario para que la decisión sea comparable. ¿Quiénes del equipo participarán en el puntaje?

## Turno 2

**Usuaria:** La jefa de recepción, la administradora, una odontóloga, la auxiliar de esterilización y yo.

**Facilitador:** Perfecto, el puntaje lo acuerdan ustedes y yo les propongo uno con su justificación. Primero el inventario.

| ID | Flujo | Reto | Disparadores | Pasos | Decisiones | Resultado | Dueño | Frecuencia | Esfuerzo | Horas/mes |
|---|---|---|---|---|---|---|---|---|---|---|
| `FLU-01` | Agendar citas | `RET-01` | Llega una solicitud por llamada, mensaje o formulario | Leer, identificar al paciente, revisar disponibilidad, registrar, confirmar | Qué hacer si el motivo parece una urgencia | Cita registrada y confirmada | Jefa de recepción | ~40/día | 0,1 h | ~88 |
| `FLU-02` | Recordatorios y confirmaciones | `RET-02` | Se acerca una cita | Buscar el contacto, avisar, registrar la respuesta, liberar el hueco si cancela | A quién llamar de nuevo | Cita confirmada o hueco liberado | Jefa de recepción | ~35/día | ~0,05 h | ~39 |
| `FLU-03` | Preautorización con aseguradoras | `RET-03` | Se agenda un tratamiento cubierto por seguro | Reunir datos y documentos, enviar la solicitud, seguir la respuesta, corregir si la devuelven | Cómo tratar los requisitos distintos de cada aseguradora | Preautorización aprobada | Administradora | ~25/semana | 0,5 h | ~50 |
| `FLU-04` | Cotización de planes de tratamiento | `RET-04` | El odontólogo propone un tratamiento de varias sesiones | Revisar el diagnóstico, definir sesiones y materiales, calcular el presupuesto, presentar alternativas | Qué alternativa recomendar y qué descuento ofrecer | Plan y presupuesto entregados | Odontólogo tratante | ~6/semana | 2 h | ~48 |
| `FLU-05` | Seguimiento postratamiento | `RET-05` | Pasan unos días de un tratamiento | Llamar, preguntar cómo va, detectar señales de complicación, reagendar si hace falta | Si la persona necesita una revisión pronto | Paciente contactado y registro del estado | Odontólogo tratante | ~8/semana | 0,5 h | ~16 |

Horas por mes: frecuencia mensual por esfuerzo (22 días hábiles al mes, 4 semanas). Frecuencias y esfuerzos, salvo los de `FLU-01` (medidos), son Dicho por participante.

## Turno 3

**Facilitador:** Esta es mi propuesta de puntaje (Inferencia de la IA). Recuerden que en Riesgo y control, 5 significa bien controlado. ¿Estás de acuerdo con estos puntajes, o qué cambiarías y por qué?

| ID | Valor | Idoneidad | Preparación | Riesgo y control | Total | Justificación breve |
|---|---|---|---|---|---|---|
| `FLU-01` | 5 | 4 | 3 | 4 | 16 | Es el flujo con más horas al mes; reglas claras con algo de interpretación; un error se ve en la agenda si una persona revisa |
| `FLU-02` | 4 | 5 | 2 | 4 | 15 | Tarea repetitiva y de alto efecto en los huecos de la agenda, pero los datos de contacto están incompletos y repartidos |
| `FLU-03` | 4 | 2 | 3 | 3 | 12 | Cada aseguradora pide requisitos distintos y hay muchas excepciones; un error retrasa el tratamiento pero se corrige |
| `FLU-04` | 3 | 2 | 3 | 2 | 10 | Cada plan es distinto; qué alternativa recomendar y el presupuesto son decisión clínica y comercial |
| `FLU-05` | 2 | 2 | 3 | 1 | 8 | Pocos casos; una señal de complicación no detectada tiene consecuencia en la salud difícil de revertir |

**Usuaria (equipo):** Estamos de acuerdo, salvo el valor de `FLU-02`: creemos que es 3 porque ahorra tiempo de recepción pero el efecto en los huecos todavía no se ha medido. Lo dejamos en 3.

**Facilitador:** Anotado: puntajes acordados por el equipo, con `FLU-02` en valor 3 en lugar del 4 que propuse (total 14). Los extremos tienen su nota: el 5 de `FLU-01` (88 horas por mes, medido en 20 solicitudes) y el 1 de `FLU-05` (consecuencia en la salud difícil de revertir).

## Turno 4

Factibilidad = promedio de idoneidad, preparación y riesgo y control. Coordenadas: x = (factibilidad − 1) / 4, y = (valor − 1) / 4. Puntajes finales acordados.

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
| Pilotos estratégicos | `FLU-03` | Valor 4, pero la idoneidad es 2: falta saber si los requisitos de cada aseguradora se pueden ordenar | Revisar 30 solicitudes devueltas antes de diseñar |
| Requiere bases | `FLU-02` | Estaba en Victorias rápidas en el mapa, pero la preparación es 2: los datos de contacto están incompletos y repartidos | Completar y centralizar los datos de contacto (dueña: jefa de recepción) |
| Asistir no automatizar | `FLU-04` | La alternativa y el presupuesto son una decisión clínica y comercial; riesgo y control 2 con valor 3 | La IA podría preparar un borrador con el historial del paciente; decide el odontólogo |
| No automatizar | `FLU-05` | Valor 2 y riesgo y control 1 | Se mantiene humano; se puede simplificar el registro del seguimiento |

**Decisión `DEC-01`** (decidió el equipo): `FLU-01` es el caso piloto candidato. **Línea base inicial** (`HAL-01`, medido en 20 solicitudes): unos 6 minutos por solicitud, unas 40 solicitudes al día, unas 88 horas por mes; citas con error, unas 4 de cada 100 (**Supuesto** `SUP-01`, pendiente de contar una semana).

Sin elegir tecnología. **Siguiente paso sugerido:** `mapear-proceso-actual` para documentar cómo se registra hoy una solicitud de cita, con pasos, decisiones y responsables.

## Lo que se ve en este ejemplo

- Cada flujo tiene un reto definido antes de puntuarse.
- Los puntajes de la IA se presentaron como propuesta; el equipo cambió uno (`FLU-02`, de 4 a 3) y quedó como acuerdo.
- El mapa dejó a `FLU-02` en Victorias rápidas, pero el orden de decisión lo movió a Requiere bases por la preparación.
- `FLU-04` y `FLU-05` no se automatizan, y eso es un resultado válido de la priorización.
- El 5 y el 1 llevan nota que los justifica.
