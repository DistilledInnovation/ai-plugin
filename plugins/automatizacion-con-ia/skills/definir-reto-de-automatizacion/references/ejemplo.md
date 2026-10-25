# Ejemplo: Definir el reto en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `descubrir-procesos`: la oportunidad `OPO-01` (registrar las solicitudes de cita sin teclear a mano y sin duplicados) vino de las señales `SEN-01` y `SEN-04`.

## Turno 1

**Usuaria:** Quiero encuadrar la de las citas. Mi socio ya dijo que lo resolvamos con un asistente de IA.

**Facilitador:** Perfecto, empecemos por `OPO-01`. Dejamos la herramienta para después y definimos primero el problema. ¿Qué situación concreta quieres cambiar y a quién le afecta?

## Turno 2

**Usuaria:** Recepción pasa horas registrando a mano las solicitudes de cita en la agenda, y a veces quedan citas duplicadas o con datos equivocados.

**Facilitador:** Separo lo que escuché: **síntoma**, horas registrando y citas duplicadas; **causa hipotética**, el registro a mano genera los errores (Supuesto, `SUP-01`); **evidencia**, 20 solicitudes medidas con unos 6 minutos de registro cada una (`HAL-01`). ¿Qué resultado medible quieres lograr y para cuándo?

## Turno 3

**Usuaria:** Bajar el tiempo de registro a la mitad y las citas con error a 1 de cada 100, antes de cerrar el trimestre.

**Facilitador:** De 6 a 3 minutos por solicitud es la meta de tiempo, con línea base medida. Los errores: la línea base de 4 de cada 100 es de recepción y nadie la ha contado (Pendiente por validar). Propongo contar una semana de citas corregidas antes de fijar la meta; mientras tanto la dejamos como borrador.

## Turno 4

**Facilitador:** Con eso redacto el reto sin solución adentro, y lo ajustamos: "¿Cómo podríamos registrar correctamente las solicitudes de cita que llegan por llamada, mensaje y formulario en la mitad del tiempo, para que recepción dedique su día a atender a los pacientes que llegan?". ¿Esta pregunta se puede responder de más de una forma, o aún suena a una solución?

**Usuaria:** Se puede resolver de varias formas, incluso con un formulario de horarios más claro.

**Facilitador:** Justo esa es la idea: el formulario también es una opción, y no hace falta IA para evaluarla.

## Turno 5

**Facilitador:** Antecedentes: ¿qué se intentó antes y cómo lo han resuelto otras organizaciones?

**Usuaria:** Hace un año pusimos un formulario en la página para pedir cita. Muchos pacientes siguen llamando o escribiendo. De otras clínicas no sé.

**Facilitador:** Anotado: formulario en la página, baja adopción (Dicho por participante); otras organizaciones, No sé.

## Turno 6

**Facilitador:** ¿Quiénes viven este problema y quién decide si se resuelve?

**Usuaria:** Lo vive recepción (2 personas) y también los pacientes. Decido yo, y la jefa de recepción es la dueña del proceso.

**Facilitador:** Por último, ¿qué debería cambiar si resolvemos esto y cómo lo notaríamos?

**Usuaria:** Que recepción atienda mejor a quienes llegan y que haya menos citas duplicadas. Lo que no debería empeorar es la confirmación al paciente: hoy se le responde el mismo día.

## Entregable: Scoping Canvas y reto

| Pregunta | Respuesta | Procedencia |
|---|---|---|
| 1. Problema | Recepción registra a mano unas 40 solicitudes de cita al día (unos 6 min cada una); quedan citas duplicadas o con datos equivocados | Evidencia (`HAL-01`); Dicho por participante |
| 2. Objetivo SMART | De 6 a 3 minutos por solicitud antes del cierre del trimestre; citas con error de 4 a 1 de cada 100 (línea base de errores pendiente de contar) | Evidencia; Supuesto (`SUP-01`) |
| 3. Pregunta | ¿Cómo podríamos registrar correctamente las solicitudes de cita que llegan por llamada, mensaje y formulario en la mitad del tiempo, para que recepción dedique su día a atender a los pacientes que llegan? | Recomendación |
| 4. Antecedentes | Formulario en la página hace un año, baja adopción; otras organizaciones: No sé | Dicho por participante |
| 5. Segmento | Recepción (2 personas), pacientes; decide Valeria; dueña del proceso: jefa de recepción | Dicho por participante |
| 6. Resultados | Mejor atención a quienes llegan, menos citas duplicadas; no debe empeorar la confirmación el mismo día | Dicho por participante |

`RET-01`, origen `OPO-01`. Riesgo `RIE-01`: un registro automático equivocado llega a la agenda sin que nadie lo revise → impacto: más citas duplicadas o a la hora equivocada → mitigación: revisión humana antes de confirmar mientras se mide el error. Pendiente por validar: contar una semana de citas con error (`SUP-01`).

**Recomendación: definir.** Las seis preguntas tienen respuesta, hay dueña del proceso y objetivo medible; el vacío (línea base de errores) se cierra con una semana de conteo. `DEC-01`: el reto no incluye tecnología (decide Valeria).

Las demás oportunidades (`OPO-02` a `OPO-05`) se encuadran en versión breve (reto, objetivo con línea base, dueño) como `RET-02` a `RET-05`, para pasar a priorizar.

**Siguiente paso sugerido:** `priorizar-flujos`, para decidir cuáles de los cinco conviene automatizar, asistir o dejar como están.

## Lo que se ve en este ejemplo

- La indicación de usar "un asistente de IA" no entró al reto: quedó fuera como una opción más.
- Se separaron síntoma, causa hipotética y evidencia, y la línea base de errores quedó pendiente en vez de inventarse.
- El reto admite más de una solución (incluso un formulario más claro).
- La recomendación (definir) viene con su porqué y el vacío que queda.
