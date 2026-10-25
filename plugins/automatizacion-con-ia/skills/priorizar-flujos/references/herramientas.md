# Herramientas para priorizar flujos

Nota de fuente: el inventario, las cuatro dimensiones (valor, idoneidad, preparación, riesgo y control), el mapa de dos ejes y las cinco cubetas siguen la práctica del Workflows Prioritization Canvas de la metodología de Automatización con IA; los umbrales y el orden de decisión son una adaptación pensada para este plugin.

## 1. Inventario de flujos

Describe el trabajo antes de puntuarlo: la descripción pesa más que el puntaje.

| Columna | Qué se anota | Ayuda |
|---|---|---|
| Flujo | Nombre corto del proceso | Verbo + objeto: "Agendar citas" |
| Disparadores | Qué inicia el flujo | Llega un correo, vence un plazo, un cliente pregunta |
| Pasos | Secuencia de alto nivel (5 a 8) | Sin entrar al detalle de pantallas |
| Decisiones | Puntos donde alguien decide algo | Quién decide y con qué criterio |
| Resultado | Qué queda al terminar | Cita registrada, preautorización aprobada |
| Dueño | Quién responde por el resultado | Una persona o un rol |
| Frecuencia | Veces por día, semana o mes | Con dato o "No sé" |
| Esfuerzo (h/ejecución) | Horas-persona por vez | Con dato o "No sé" |

**Horas por mes** = frecuencia mensual × esfuerzo. Con "No sé", propón una forma barata de medir y deja la celda como Pendiente por validar.

## 2. Qué mira cada criterio

| Criterio | Sub-criterios que ayudan a puntuar |
|---|---|
| Valor de negocio | Impacto en metas, tiempo o costo ahorrado, ingresos que habilita, experiencia de clientes o empleados, reducción de riesgo, importancia estratégica |
| Idoneidad para automatizar | Repetición, estabilidad del proceso, calidad medible, tasa de excepciones, consistencia del resultado |
| Preparación | Disponibilidad de datos, acceso a sistemas, dueño del proceso, factibilidad de integración, disposición del equipo a adoptarlo |
| Riesgo y control | Consecuencia de fallar, detectabilidad, reversibilidad, privacidad y cumplimiento, seguridad, controlabilidad |

No hace falta una columna por sub-criterio: úsalos como preguntas para justificar el puntaje.

### Anclas sugeridas (1 / 3 / 5)

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Valor de negocio | Ahorra poco y no mueve una meta | Ahorro o mejora visible en un área | Mueve una meta importante o libera mucho tiempo |
| Idoneidad | Cada caso es distinto, muchas excepciones | Reglas claras con excepciones frecuentes | Pasos estables y pocas excepciones |
| Preparación | Faltan datos, acceso o dueño | Datos disponibles pero dispersos | Datos, acceso, dueño y equipo listos |
| Riesgo y control | Error grave, difícil de ver o de deshacer | Error con costo, pero detectable y corregible | Error de consecuencia pequeña, visible y reversible |

### Dirección de "Riesgo y control"

Es el criterio que más confunde: **un puntaje alto es bueno**. Mide qué tan bien controlado está el riesgo, no qué tan riesgoso es. Un proceso que paga a proveedores sin revisión tendría 1 (alto riesgo, poco control); el mismo proceso con una persona que aprueba cada pago tendría 4. Al presentar los puntajes, escribe siempre "5 = bien controlado".

## 3. Puntuar como equipo

1. Presenta tu propuesta de puntaje con una línea de justificación por criterio y márcala como **Inferencia de la IA**.
2. Pide al equipo que ajuste. Cuando haya desacuerdo de dos o más puntos, pregunta qué evidencia ve cada persona; el desacuerdo suele revelar un dato faltante.
3. Acuerda el puntaje por consenso (no promedio de opiniones) y cambia la procedencia a **Acordado por el equipo**.
4. Justifica por escrito todo 1 o 5.

## 4. Mapa Valor × Factibilidad

- **Valor**: puntaje de Valor de negocio.
- **Factibilidad**: promedio de Idoneidad, Preparación y Riesgo y control.
- Posición en el diagrama: x = (factibilidad − 1) / 4 y y = (valor − 1) / 4.
- Un valor o una factibilidad de 3 o más se considera alto; es una guía que el equipo puede ajustar si lo registra.

El mapa **no** decide la cubeta: muestra una posición provisional. Dos flujos en el mismo cuadrante pueden terminar en cubetas distintas (uno sin datos va a Requiere bases; otro con juicio humano esencial, a Asistir).

## 5. Las cinco cubetas con ejemplos genéricos

| Cubeta | Señales típicas | Ejemplo genérico |
|---|---|---|
| Victorias rápidas | Valor alto, todo listo, error acotado | Clasificar correos entrantes por tema |
| Pilotos estratégicos | Valor alto, pero no se sabe si funcionará o se necesita una capacidad nueva | Resolver las excepciones frecuentes de preautorización |
| Requiere bases | La información vive en varios lugares, el proceso cambia cada vez o nadie es dueño | Enviar recordatorios cuando los datos de contacto no están completos en un solo lugar |
| Asistir no automatizar | Una persona decide con consecuencias, aunque la IA pueda preparar | Preparar el borrador de una oferta personalizada |
| No automatizar | Poco valor, riesgo alto sin control o trabajo de relación | Decisiones sensibles con pocas repeticiones |

Para cada flujo en **Requiere bases**, anota cuál es la base que falta y quién la resuelve: eso es el siguiente paso, y a veces el mayor valor es resolver la base sin automatizar nada.

## 6. Evitar filtros absolutos

No uses reglas como "lo mensual nunca vale la pena automatizar", "solo se automatiza lo de bajo riesgo" o "la IA debe acertar el 80 %". Evalúa en cambio la economía (horas por mes y costo), la consecuencia de fallar, la reversibilidad, la detectabilidad, los controles necesarios, el esfuerzo de construcción y el costo de operar.

## 7. De la cubeta al siguiente paso

1. Elige un caso piloto candidato (generalmente una Victoria rápida o un Piloto estratégico con buen dueño).
2. Registra la línea base inicial: frecuencia, tiempo por vez, errores, con su procedencia.
3. Para los flujos en Requiere bases, abre una tarea de base con dueño y fecha.
4. Para Asistir no automatizar, anota qué prepararía la IA y qué decide la persona.
5. Registra la decisión como `DEC-nn`.
