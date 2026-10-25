# Herramientas para mapear el proceso actual

Nota de fuente: la tabla de pasos, el diagrama de flujo y la matriz RACI son prácticas estándar de documentación de procesos; los criterios de este plugin (proceso de hoy, tiempos separados de esperas, vacíos declarados y sin tecnología nueva) provienen de la metodología de Automatización con IA de Distilled Innovation.

## 1. Entrevista del caso reciente

Pide el último caso real, no el proceso "normal". Preguntas de apoyo (una por turno):

| Intención | Pregunta |
|---|---|
| Inicio | "¿Qué fue lo primero que pasó ese día?" |
| Siguiente paso | "¿Y después de eso, qué hiciste?" |
| Decisión | "¿Cómo supiste qué hacer ahí? ¿Alguien más lo habría decidido distinto?" |
| Espera | "¿En qué momento tuviste que esperar algo o a alguien?" |
| Excepción | "¿Qué habría pasado si la persona no hubiera respondido, o si el dato faltara?" |
| Fin | "¿Cómo supiste que el caso estaba cerrado?" |

Si hay un procedimiento escrito, compáralo con el caso: lo que difiere se anota como contradicción (el procedimiento dice A, el caso muestra B).

## 2. Cómo se escribe un paso

| Regla | Mal | Bien |
|---|---|---|
| Verbo + objeto | "Agenda" | "Revisar disponibilidad en la agenda" |
| Un verbo por paso | "Revisar y registrar la cita" | PAS-04 "Revisar disponibilidad" y PAS-07 "Registrar la cita" |
| Sin solución adentro | "Esperar el chatbot" | "Esperar la respuesta del paciente" |
| Dónde = lo que usan hoy | "En el sistema" | "En la agenda de la clínica" (el nombre que usa la persona) |

## 3. Del diagrama a la tabla

Cada flecha del diagrama es una fila de la tabla equivalente (desde, condición, hacia). Cada decisión tiene al menos dos salidas. Verifica que todos los `PAS-nn` y `EXC-nn` de la tabla aparezcan en el diagrama y al revés.

Formas Mermaid usadas: `([...])` inicio y fin, `[...]` actividad, `{...}` decisión, flecha con texto `-- Sí -->` para las condiciones. Si el diagrama pasa de unos 12 nodos, parte el proceso en subprocesos y mapea cada uno por separado.

## 4. Tiempos: trabajo contra espera

| Medida | Qué es | Para qué sirve |
|---|---|---|
| Tiempo de trabajo | Minutos en los que alguien está haciendo el paso | Calcula horas por mes y el ahorro posible |
| Tiempo de espera | Minutos u horas en que el caso está parado | Explica la demora que siente la persona atendida |

Una espera larga puede doler más al cliente que un paso lento, y no se arregla automatizando el paso. Medir 20 casos de forma sencilla (una marca de inicio y otra de fin) basta para pasar un dato de "dicho" a "medido".

## 5. Contradicciones

| Situación | Qué hacer |
|---|---|
| Dos personas ordenan distinto dos pasos | Registrar ambas versiones; preguntar al dueño cuál se espera, sin forzar |
| El procedimiento escrito no coincide con la práctica | Mapear la práctica y anotar la diferencia |
| Una persona dice "nunca pasa" y otra "pasa siempre" | Pendiente por validar; proponer contar una semana |

## 6. RACI paso a paso

1. Lista los pasos críticos (los que tienen consecuencia o decisión).
2. Para cada uno, pregunta primero por la A: "¿Quién responde si esto sale mal?".
3. Luego la R: "¿Quién lo hace?". Puede coincidir con la A, pero conviene verlo.
4. C e I solo si cambian lo que ocurre; no llenes toda la matriz.
5. Revisa: una A por paso, sin pasos huérfanos, sin una persona que sea A de todo por costumbre.
