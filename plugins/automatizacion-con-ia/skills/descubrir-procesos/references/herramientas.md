# Herramientas para descubrir procesos

Nota de fuente: el orden de la entrevista (contexto, trabajo real, evidencia, descomposición) sigue la secuencia de descubrimiento de la metodología de Automatización con IA; la ficha de señal y la agrupación de reportes son una adaptación genérica de prácticas de captura de señales internas en talleres de innovación. Los pasos son una guía, no una camisa de fuerza.

## 1. Entrevista de proceso

Objetivo: ver el trabajo como ocurre. Guía completa en `assets/guia-de-entrevista-de-proceso.md`.

**Cómo aplicarla:**
1. Empieza por el contexto del negocio: qué resultado importa y qué se interpone. Esto evita buscar automatizaciones que no mueven nada.
2. Pide el último caso real, desde que llegó hasta que se resolvió. Registra pasos, personas, herramientas y excepciones tal como se cuentan.
3. Pregunta por frecuencia, duración, costo y variabilidad. Si no hay dato, acuerda una forma barata de medir (contar una semana, cronometrar 20 casos).
4. Descompón: ¿qué pasos son reglas, cuáles requieren interpretar, cuáles juicio, cuáles relación con personas?
5. Cierra preguntando con quién más conviene hablar.

Una entrevista por rol distinto. Con tres a cinco personas de áreas diferentes suele aparecer el patrón.

## 2. Ficha de señal (captura de señales internas)

Formato corto para que cualquier persona reporte un problema sin necesidad de entrevista. Cuatro partes: contexto, situación, magnitud, intención (`assets/ficha-de-senal.md`).

**Reglas:**
- **Hechos antes que soluciones**: la situación cuenta qué pasó; la intención dice qué resultado se quiere, no qué herramienta.
- **Un ejemplo concreto** por ficha. Si hay dos problemas, son dos fichas.
- **"No sé" es válido** en cualquier casilla de magnitud. Una ficha con huecos honestos vale más que una con cifras inventadas.
- **Magnitud con dos escalas de 1 a 5**: relevancia (cuánto afecta el resultado) y urgencia (cuánto puede esperar). Son percepciones de quien reporta, no mediciones; se contrastan con frecuencia y tiempo cuando hay datos.

**Modo asíncrono:** la ficha se puede enviar a varias personas por correo o chat y recoger por escrito. Al recibirlas, no las juzgues: agrúpalas.

## 3. Agrupar señales del mismo problema

Dos fichas de áreas distintas pueden describir el mismo problema con palabras diferentes ("los pacientes llaman a preguntar si su cita sigue en pie" y "pasamos el día contestando consultas de confirmación").

**Cómo aplicarlo:**
1. Lee todas las fichas y ordénalas por proceso o tarea.
2. Pregúntate para cada par: ¿es el mismo trabajo? ¿es el mismo resultado que falla? Si ambas respuestas son sí, es el mismo problema.
3. Propón el grupo a la persona y pide confirmación. Pregunta guía: "¿Estas dos situaciones son el mismo problema visto desde lados distintos?".
4. Crea una oportunidad (`OPO-nn`) con todas las señales del grupo. Conserva los IDs de señal: nunca los reutilices.
5. Promedia relevancia y urgencia solo si las personas están de acuerdo en que describen lo mismo; si difieren mucho, anota por qué.

Si dos fichas se parecen pero el resultado que falla es distinto, déjalas separadas. Mejor dos oportunidades pequeñas que una mezcla.

## 4. Señales internas y fuerzas externas

- **Señales internas** (zoom in): lo que viven las personas en su trabajo (fichas de señal, entrevistas, observación).
- **Fuerzas externas** (zoom out): lo que cambia afuera y presiona al proceso (pacientes que esperan respuestas más rápidas, regulaciones, competidores).

Una oportunidad con respaldo en ambas (algo duele adentro y el entorno lo vuelve más urgente) suele merecer más atención. Anota la fuente de cada una y no inventes tendencias: si no hay dato, es **Supuesto**.

## 5. Primera lectura de cada oportunidad

Para cada oportunidad, antes de priorizar, pregunta con qué opción se resolvería con menos cambio:

| Opción | Cuándo suena razonable |
|---|---|
| Eliminar | El paso no cambia ninguna decisión ni resultado |
| Simplificar | El paso existe por costumbre, duplicación o formularios largos |
| Asistir | Una persona sigue decidiendo, pero con ayuda para preparar o revisar |
| Automatizar | Reglas claras, buen volumen y consecuencias controladas |
| Mantener humano | Es trabajo de relación o de juicio con consecuencias altas |

Es una recomendación provisional. Marca "aún no se sabe" sin culpa.
