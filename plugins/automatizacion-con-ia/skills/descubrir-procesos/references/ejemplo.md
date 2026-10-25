# Ejemplo: Descubrir procesos en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo del facilitador: Valeria, directora, no sabe qué automatizar y tiene un dato (`HAL-01`: unas 40 solicitudes de cita al día se registran a mano, unos 6 minutos cada una).

## Turno 1

**Usuaria:** Quiero entender dónde está el tiempo perdido de verdad. Tengo cuatro áreas: Recepción, Administración, Esterilización y los consultorios.

**Facilitador:** Perfecto, vamos por áreas. Para empezar con el contexto: ¿qué resultado del negocio te preocupa más este trimestre?

## Turno 2

**Usuaria:** Que los pacientes consigan cita rápido y que no falten. Hoy se quejan de que tardamos en responder y tenemos huecos en la agenda por pacientes que no avisan.

**Facilitador:** Anoto eso como el resultado que importa (Dicho por participante). Ahora el trabajo real: ¿me cuentas cómo fue la última solicitud de cita que llegó por mensaje, desde que entró hasta que quedó en la agenda?

## Turno 3

**Usuaria:** Llegó un mensaje de un paciente pidiendo "algo por la tarde la próxima semana para una limpieza". Recepción lo leyó, revisó la agenda del consultorio y de la higienista, le propuso dos horarios, esperó la respuesta, registró la cita y le confirmó. Esta semana a la agenda le quedaron dos citas duplicadas.

**Facilitador:** Gracias. Para la evidencia: ¿cuántas citas duplicadas o con datos equivocados ves por semana y cómo lo sabes?

## Turno 4

**Usuaria:** Recepción dice que unas 4 de cada 100, pero no lo han contado.

**Facilitador:** Lo anoto como Dicho por participante (`SUP-01`: error de unas 4 de cada 100 citas, pendiente por validar; se puede contar una semana de citas corregidas).

Para descomponer: de los pasos de la solicitud, ¿cuáles siguen reglas claras y cuáles requieren que alguien interprete?

**Usuaria:** Revisar la disponibilidad y registrar la cita es siempre igual. Interpretar es cuando el paciente escribe "por la tarde, cuando se pueda". Y si el motivo parece una urgencia, decide la odontóloga de turno.

## Turno 5

Valeria pide a un representante de cada área que llene una ficha de señal. Llegan cuatro más. Resumen de las siete fichas (ficticias):

| ID | Área | Situación (hecho) | Magnitud |
|---|---|---|---|
| `SEN-01` | Recepción | Registran a mano las solicitudes de cita que llegan por llamada, mensaje y formulario | Relevancia 5, urgencia 4; unas 40/día, unos 6 min cada una (medido en 20 solicitudes) |
| `SEN-02` | Recepción | Llaman a los pacientes para recordarles y confirmar su cita | Relevancia 3, urgencia 3; unas 35 llamadas al día, unos 3 min cada una (Dicho por participante) |
| `SEN-03` | Administración | Piden preautorización a las aseguradoras y a veces la devuelven por datos incompletos | Relevancia 4, urgencia 3; unas 25 solicitudes por semana, unos 30 min cada una (Dicho por participante) |
| `SEN-04` | Recepción | Al registrar una cita se confunden datos del paciente y quedan citas duplicadas | Relevancia 4, urgencia 4; unas 4 de cada 100 (No sé: no se ha contado) |
| `SEN-05` | Consultorios | Preparan por escrito el plan y el presupuesto de tratamientos de varias sesiones | Relevancia 3, urgencia 2; unas 6 por semana, unas 2 h cada una |
| `SEN-06` | Consultorios | Pacientes que no asisten dejan huecos que se avisan tarde a la lista de espera | Relevancia 3, urgencia 3; No sé la frecuencia |
| `SEN-07` | Odontólogos | Llamar a los pacientes unos días después de un tratamiento para ver cómo van | Relevancia 2, urgencia 2; unas 8 por semana, unos 30 min cada una |

## Turno 6

**Facilitador:** Al leerlas, veo dos pares que podrían ser el mismo problema: `SEN-01` con `SEN-04` (las citas duplicadas nacen al registrar a mano las solicitudes) y `SEN-02` con `SEN-06` (dos áreas lidiando con lo mismo: pacientes que no confirman y huecos en la agenda). ¿Son el mismo problema visto desde lados distintos?

**Usuaria:** Sí, ambos pares.

## Entregable: inventario de oportunidades

| ID | Oportunidad | Señales | Quién la vive | Frecuencia | Tiempo por vez | Relev. / Urg. | Evidencia | Primera lectura (provisional) |
|---|---|---|---|---|---|---|---|---|
| `OPO-01` | Registrar las solicitudes de cita sin teclear a mano y sin duplicados | `SEN-01`, `SEN-04` | Recepción | ~40 al día | ~6 min | 5 / 4 | **Hecho** (medido en 20 solicitudes); el error del 4 % es **Supuesto** (`SUP-01`) | Asistir o automatizar |
| `OPO-02` | Que los pacientes confirmen y no queden huecos en la agenda | `SEN-02`, `SEN-06` | Recepción, consultorios | ~35 al día | ~3 min | 3 / 3 | Dicho por participante; la frecuencia de los huecos, No sé | Simplificar (primero saber que los datos de contacto estén completos) |
| `OPO-03` | Preautorización con aseguradoras | `SEN-03` | Administración | ~25 por semana | ~30 min | 4 / 3 | Dicho por participante | Aún no se sabe |
| `OPO-04` | Plan y presupuesto de tratamiento | `SEN-05` | Consultorios | ~6 por semana | ~2 h | 3 / 2 | Dicho por participante | Asistir |
| `OPO-05` | Seguimiento después del tratamiento | `SEN-07` | Odontólogos | ~8 por semana | ~30 min | 2 / 2 | Dicho por participante | Mantener humano |

Descomposición de `OPO-01`: reglas claras (revisar disponibilidad, registrar la cita); interpretación (frases como "por la tarde, cuando se pueda"); juicio (qué hacer si el motivo parece una urgencia, decide la odontóloga de turno).

Pendientes por validar: contar una semana de citas duplicadas o corregidas (`SUP-01`); frecuencia real de los huecos por inasistencia; cuántos tipos distintos de rechazo hay en las preautorizaciones.

Sin elegir tecnología. **Siguiente paso sugerido:** `definir-reto-de-automatizacion` para `OPO-01`, la de mayor magnitud y con evidencia, y después encuadrar las demás de forma breve para poder priorizar.

## Lo que se ve en este ejemplo

- No se abrió con "¿qué quieres automatizar?": se empezó por el resultado de negocio.
- Se pidió el último caso real y luego la evidencia, y lo no medido quedó como Supuesto.
- Dos pares de señales de áreas distintas se agruparon con confirmación de la persona.
- La primera lectura es provisional y no incluye tecnología.
