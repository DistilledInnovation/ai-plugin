# Ejemplo: sintetizar y redefinir el reto en una empresa de transporte ficticia

Empresa inventada: **Transportes Marea Azul** (carga refrigerada regional, 65 empleados, 22 camiones). Continúa el ejemplo de `investigar-y-empatizar`. Todo es ficticio.

Entrada: `RET-01` (hipótesis) "¿Cómo podemos lograr que los productores de alimentos frescos confíen en que su carga llega a tiempo y en buen estado, y lo puedan comprobar durante todo el viaje?"; `SUP-01` "se fueron por falta de visibilidad, no por precio"; evidencia `HAL-01` a `HAL-05` (5 entrevistas y 1 visita).

## Turno 1

**Facilitador:** Tengo tu plan con 5 entrevistas, 1 visita y 5 registros de evidencia. Primera pregunta: ¿qué fue lo que más te sorprendió porque no lo sabías antes?

**Usuaria (Paula):** Que el precio no era el problema. Y que ni siquiera querían ver el camión en el mapa: querían saber si el frío seguía bien.

## Turno 2

**Facilitador:** Con eso clasifico lo registrado (el hallazgo sintetizado recibe el siguiente `HAL-nn` libre y cita los registros que lo respaldan):

| ID | Tipo | Enunciado | Evidencia | Personas | Estado |
|---|---|---|---|---|---|
| HAL-06 | Hallazgo | Los dos ex clientes se fueron por la incertidumbre sobre el frío, no por el precio | HAL-01, HAL-02 | 2 de 2 ex clientes | Hecho (dicho por participante) |
| NEC-01 | Necesidad | Tener la certeza de que el frío se mantuvo durante todo el traslado | HAL-01, HAL-02, HAL-04 | 3 de 5 | Hecho |
| TEN-01 | Tensión | No hay forma de saber si el frío se cortó hasta que llega la carga tibia | HAL-01, HAL-02 | 2 de 5 | Hecho |
| TEN-02 | Tensión | Seguir la carga exige llamar al conductor cada dos horas y anotar en un cuaderno | HAL-03, HAL-05 | 1 visita + 1 dicho | Pendiente por validar (una sola observación) |

¿Esta clasificación refleja lo que viste?

**Usuaria:** Sí.

## Turno 3

**Facilitador:** ¿Qué cosas repitieron varias personas, y en qué casos dijeron una cosa y hicieron otra?

**Usuaria:** Lo del frío lo repitieron tres. El jefe de logística D decía que el rastreo en línea sería ideal, pero en la visita lo vi llamando al conductor y anotando en un cuaderno.

**Facilitador:** Anoto la contradicción `HAL-05`. Lectura posible (Inferencia de la IA): lo que pide ("rastreo") es una solución imaginada; lo que necesita es certeza sobre el frío y aviso temprano si algo falla. Pendiente por validar con más personas.

## Turnos 4 a 7 (resumen)

Mapa de Empatía del jefe de logística de un productor ("Julián", nombre ficticio): ve camiones llegando tarde y mercancía tibia (`HAL-02`); oye que los competidores ofrecen avisos (Supuesto); dice que el rastreo sería ideal pero hace llamadas y cuaderno (`HAL-05`); piensa y siente ansiedad por perder mercancía, temor a reclamos de sus compradores (Inferencia de la IA, Pendiente por validar).

Perfil del Cliente (con la evidencia entre paréntesis):

| Orden | Tarea | Dolor (durante la tarea) | Beneficio |
|---|---|---|---|
| 1ra | Asegurar que su carga llegue con el frío intacto (HAL-01, HAL-02) | 1er: no saber si se cortó el frío durante el traslado (TEN-01) | Enterarse a tiempo si algo sale mal (HAL-04, una sola persona: pendiente) |
| 2da | Coordinar la recepción con su comprador (HAL-03) | 2do: llamadas repetidas al conductor (TEN-02) | Confianza para recomendar el servicio |

## Turno 8: priorizar

**Facilitador:** ¿Cuál es la tarea más importante para esta persona y cuál es el dolor que más le pesa?

**Usuaria:** Asegurar que la carga llegue fría. Y el no enterarse hasta que ya llegó tibia.

## Turno 9: redefinir

**Facilitador:** Con la 1ra tarea y el 1er dolor, estos son los candidatos:
- `RET-02` (ayudar a que la tarea se satisfaga): ¿Cómo podemos ayudar a que el jefe de logística de un productor pueda asegurar que su carga llegue con el frío intacto?
- `RET-03` (mitigar el dolor durante la tarea): ¿Cómo podemos mitigar la incertidumbre sobre si se cortó el frío durante el traslado de la carga?

¿Cuál de estos retos refleja mejor lo que aprendimos?

**Usuaria:** El segundo. Es lo que me contaron los dos que se fueron.

## Entregable final

# Reto redefinido: Marea Azul

| | Reto | Estado |
|---|---|---|
| Inicial | `RET-01` ¿Cómo podemos lograr que los productores confíen en que su carga llega a tiempo y en buen estado, y lo puedan comprobar durante todo el viaje? | Hipótesis |
| Redefinido | `RET-03` ¿Cómo podemos mitigar la incertidumbre sobre si se cortó el frío durante el traslado de la carga? | Hipótesis informada por evidencia |

Resultado: **se ajusta**. La evidencia (`HAL-01`, `HAL-02`, `HAL-04`) mueve el foco de "ver el camino" a "tener certeza del frío". Decisión `DEC-01`. `RET-02` queda como alternativa descartada por ahora (`DEC-02`): su tarea es la misma, pero el dolor es lo que dijeron los dos clientes perdidos.

Lista de calidad: nombra al actor y el dolor; no lleva solución (no dice sensores, ni app, ni rastreo); se apoya en `HAL-01` y `HAL-02`; deja espacio a muchas soluciones.

| ID | Supuesto | Estado | Evidencia |
|---|---|---|---|
| SUP-01 | Se fueron por falta de visibilidad, no por precio | Se ajusta: el precio no pesó (2 de 2); lo que faltaba era certeza del frío, no ubicación | HAL-01, HAL-02 |
| SUP-02 | Los clientes hacen seguimiento manual frecuente | Pendiente por validar (1 visita) | HAL-03 |
| SUP-03 | Les basta con un aviso temprano si algo falla | Pendiente por validar (1 persona) | HAL-04 |

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RIE-01 | Que los hallazgos vengan de 5 personas | Reto demasiado estrecho | Validar con 3 clientes más y con recepción en el muelle antes de ideación |

Pendientes por validar: qué quiere saber exactamente la recepción en el muelle; qué es "aviso a tiempo" para cada cliente.

Siguiente paso sugerido: ideación (`facilitar-ideacion`), con `RET-03` como reto. Si esa skill aún no está disponible, actualizar el estado del proyecto con el facilitador. No se eligió tecnología.

## Lo que se ve en este ejemplo

- Una sola pregunta por turno.
- Las necesidades y tensiones citan los `HAL-nn` que las respaldan; lo que dijo una sola persona queda como pendiente.
- El reto nuevo usa el patrón textual del libro, nombra el dolor y no trae solución embebida.
- La comparación con el reto inicial muestra que se ajustó, y por qué.
