# Herramientas para armar el canvas

Nota de fuente: los 12 bloques, sus títulos y sus preguntas guía provienen del Canvas de Automatización con IA de la metodología de Distilled Innovation (versión en español); las pautas de llenado, los estados de cada bloque y la vista A3 son una adaptación de este plugin.

## 1. Cómo se llena cada bloque (qué es una buena respuesta)

| Bloque | Una buena respuesta tiene | Señal de alerta |
|---|---|---|
| 1 Disparador y contexto | El evento que inicia el flujo, quién lo activa y el objetivo de negocio con su meta | Objetivo sin cifra ni dueño |
| 2 Flujo actual | Los pasos con ID, responsables, dolores y el resultado actual, en 4 a 6 líneas | Copiar toda la tabla del mapa |
| 3 Flujo futuro | Qué se elimina, qué se simplifica, qué se asiste, qué se automatiza y qué queda humano | Nombrar herramientas |
| 4 Capacidades | Verbos con su nivel de autoridad | "Usar un agente" sin capacidades |
| 5 Patrón | Una o varias casillas marcadas y 2 a 4 frases de justificación | Marcar "Agente" sin verificación previa |
| 6 Responsables y controles | Quién decide, aprueba, revisa excepciones y puede detener | Todo "el equipo" sin nombre de rol |
| 7 Sistemas, datos y herramientas | Datos y sistemas actuales en palabras funcionales; herramientas pendientes | Elegir una herramienta antes del MVP |
| 8 Riesgos | Riesgo → impacto → mitigación, enlazado a un guardrail | Riesgos genéricos ("puede fallar") |
| 9 Métricas | Línea base con procedencia → meta, y cómo se mide | Meta sin línea base |
| 10 Plan piloto | El experimento más pequeño: alcance, usuarios, duración, criterio de éxito, aprendizaje | Un piloto que ya es la solución completa |
| 11 Costo y esfuerzo | Bajo, Medio o Alto con factores, marcado como Supuesto | Cifras sin base |
| 12 Próximos pasos | Acción, responsable, fecha y dependencia | Acciones sin dueño |

## 2. Estados de un bloque

| Estado | Cuándo | Qué hacer |
|---|---|---|
| Completo | Viene de un entregable validado o de una respuesta confirmada | Citar los IDs |
| Provisional | Hay un borrador (por ejemplo, propuesto por la IA) sin confirmar | Aparece en "¿Qué falta?" |
| Pendiente | No hay material, o se decidió dejarlo para el MVP | Escribir el motivo y la skill que lo resuelve |

## 3. Bloque 11: costo y esfuerzo (clasificación inicial)

| Dimensión | Bajo | Medio | Alto |
|---|---|---|---|
| Esfuerzo de construcción | Pocas reglas o un solo paso con IA, sin conexiones nuevas | Varios pasos, reglas por escribir o una conexión nueva | Muchos pasos, varias conexiones o datos por limpiar |
| Costo operativo | Casi sin uso variable ni supervisión | Supervisión diaria o uso moderado | Uso intensivo o supervisión permanente |
| Mantenimiento | Reglas estables | Reglas o criterios que cambian por temporada | Cambios frecuentes o muchos casos de borde |

Son anclas para conversar, no una estimación. Explica los factores principales y marca todo como Supuesto hasta que el plan piloto lo afine. El retorno se calcula solo con datos; si no, "No sé". Una cuenta de apoyo útil: horas por mes de la línea base menos las horas por mes con la meta (por ejemplo, minutos por caso × casos por mes), marcada como **meta, no resultado**.

## 4. La vista A3

1. Una celda por bloque, en el orden del canvas (1 a 4, 5 a 8, 9 a 12).
2. Máximo unas 40 palabras por celda; los IDs reemplazan al texto repetido.
3. Los bloques Pendientes se escriben "Pendiente: motivo".
4. El Markdown es la fuente; la vista A3 se regenera cuando cambia el canvas.

## 5. Mantener el canvas vivo

| Cuándo | Qué se actualiza |
|---|---|
| Se valida o se rechaza un supuesto | Bloques 8, 9 y 12, y el estado de los bloques que dependían de él |
| Cambia el diseño del proceso | Bloques 3 a 6 y la versión |
| Termina el piloto | Bloques 9, 10 y 11 con resultados; los resultados se anotan aparte de las metas |
| Se aprueba | El pie (*Aprobado por*, *Fecha*) y la versión pasa de borrador a la siguiente |
