# Ejemplo: Definir el reto en una distribuidora ficticia

Empresa inventada: **Distribuidora Rioclaro** (insumos de oficina y limpieza para empresas pequeñas; 85 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `descubrir-procesos`: la oportunidad `OPO-01` (registrar pedidos sin teclear a mano y sin errores de código) vino de las señales `SEN-01` y `SEN-04`.

## Turno 1

**Usuaria:** Quiero encuadrar la de los pedidos. Mi gerente general ya dijo que lo resolvamos con un asistente de IA.

**Facilitador:** Perfecto, empecemos por `OPO-01`. Dejamos la herramienta para después y definimos primero el problema. ¿Qué situación concreta quieres cambiar y a quién le afecta?

## Turno 2

**Usuaria:** Atención al Cliente pasa horas copiando pedidos de correos y chats al sistema de pedidos, y a Bodega le llegan pedidos con códigos equivocados.

**Facilitador:** Separo lo que escuché: **síntoma**, horas copiando y errores de código; **causa hipotética**, el copiado a mano genera los errores (Supuesto, `SUP-01`); **evidencia**, 20 pedidos medidos con unos 6 minutos de captura cada uno (`HAL-01`). ¿Qué resultado medible quieres lograr y para cuándo?

## Turno 3

**Usuaria:** Bajar el tiempo de captura a la mitad y los errores a 1 de cada 100, antes de cerrar el trimestre.

**Facilitador:** De 6 a 3 minutos por pedido es la meta de tiempo, con línea base medida. Los errores: la línea base de 4 de cada 100 es de Bodega y nadie la ha contado (Pendiente por validar). Propongo contar una semana de devoluciones antes de fijar la meta; mientras tanto la dejamos como borrador.

## Turno 4

**Facilitador:** Con eso redacto el reto sin solución adentro, y lo ajustamos: "¿Cómo podríamos registrar correctamente los pedidos que llegan por correo y chat en la mitad del tiempo, para que el equipo de Atención dedique su día a resolver los casos difíciles?". ¿Esta pregunta se puede responder de más de una forma, o aún suena a una solución?

**Usuaria:** Se puede resolver de varias formas, incluso con un formulario para los clientes.

**Facilitador:** Justo esa es la idea: el formulario también es una opción, y no hace falta IA para evaluarla.

## Turno 5

**Facilitador:** Antecedentes: ¿qué se intentó antes y cómo lo han resuelto otras organizaciones?

**Usuaria:** Hace un año hicimos una plantilla de correo para que los clientes escribieran el pedido en columnas. Casi nadie la usó. De otras empresas no sé.

**Facilitador:** Anotado: plantilla de correo, baja adopción (Dicho por participante); otras organizaciones, No sé.

## Turno 6

**Facilitador:** ¿Quiénes viven este problema y quién decide si se resuelve?

**Usuaria:** Lo vive Atención (9 personas) y Bodega. Decido yo, y la jefa de Atención es la dueña del proceso.

**Facilitador:** Por último, ¿qué debería cambiar si resolvemos esto y cómo lo notaríamos?

**Usuaria:** Que Atención atienda más casos difíciles y que Bodega reciba menos pedidos con error. Lo que no debería empeorar es la confirmación al cliente: hoy responden el mismo día.

## Entregable: Scoping Canvas y reto

| Pregunta | Respuesta | Procedencia |
|---|---|---|
| 1. Problema | Atención copia unos 120 pedidos al día al sistema (unos 6 min cada uno); Bodega recibe pedidos con códigos equivocados | Evidencia (`HAL-01`); Dicho por participante |
| 2. Objetivo SMART | De 6 a 3 minutos por pedido antes del cierre del trimestre; errores de 4 a 1 de cada 100 pedidos (línea base de errores pendiente de contar) | Evidencia; Supuesto (`SUP-01`) |
| 3. Pregunta | ¿Cómo podríamos registrar correctamente los pedidos que llegan por correo y chat en la mitad del tiempo, para que Atención dedique su día a resolver los casos difíciles? | Recomendación |
| 4. Antecedentes | Plantilla de correo en columnas hace un año, baja adopción; otras organizaciones: No sé | Dicho por participante |
| 5. Segmento | Atención (9 personas), Bodega; decide Daniela; dueña del proceso: jefa de Atención | Dicho por participante |
| 6. Resultados | Más casos difíciles atendidos, menos pedidos con error; no debe empeorar la confirmación el mismo día | Dicho por participante |

`RET-01`, origen `OPO-01`. Riesgo `RIE-01`: una captura automática equivocada llega a Bodega sin que nadie la revise → impacto: más pedidos erróneos → mitigación: revisión humana antes de confirmar mientras se mide el error. Pendiente por validar: contar una semana de pedidos con error (`SUP-01`).

**Recomendación: definir.** Las seis preguntas tienen respuesta, hay dueña del proceso y objetivo medible; el vacío (línea base de errores) se cierra con una semana de conteo. `DEC-01`: el reto no incluye tecnología (decide Daniela).

Las demás oportunidades (`OPO-02` a `OPO-05`) se encuadran en versión breve (reto, objetivo con línea base, dueño) como `RET-02` a `RET-05`, para pasar a priorizar.

**Siguiente paso sugerido:** `priorizar-flujos`, para decidir cuáles de los cinco conviene automatizar, asistir o dejar como están.

## Lo que se ve en este ejemplo

- La indicación de usar "un asistente de IA" no entró al reto: quedó fuera como una opción más.
- Se separaron síntoma, causa hipotética y evidencia, y la línea base de errores quedó pendiente en vez de inventarse.
- El reto admite más de una solución (incluso un formulario).
- La recomendación (definir) viene con su porqué y el vacío que queda.
