# Herramientas para supuestos y riesgos

Nota de fuente: el enfoque de supuestos falsables, la calificación de impacto e incertidumbre y el registro de riesgos provienen de la metodología de validación de Distilled Innovation; las escalas, la matriz y el enlace entre autonomía y riesgo son una adaptación de este plugin.

## 1. Cómo redactar un supuesto falsable

Estructura: **Creemos que** [quién o qué] **[resultado]** bajo [condición]. **Lo sabremos porque** [señal observable]. **Es falso si** [umbral].

| Mal redactado | Por qué no sirve | Bien redactado |
|---|---|---|
| "La automatización va a ser mejor" | No hay señal ni umbral | "Creemos que recepción tarda menos de 3 minutos por solicitud con el flujo nuevo; lo sabremos cronometrando 20 solicitudes; es falso si el promedio supera los 3 minutos" |
| "A los pacientes les va a gustar" | Nadie podría desmentirlo | "Creemos que 6 de cada 10 pacientes aceptan uno de los tres horarios propuestos en su primera respuesta; es falso si menos de 5 de cada 10 lo hacen" |
| "La IA entiende los mensajes" | Sin criterio de qué es entender | "Creemos que en al menos 24 de 30 mensajes reales se pueden leer nombre, documento y motivo sin volver a preguntar; es falso si son menos" |

Prueba rápida de falsabilidad: pregunta "¿qué tendríamos que ver para decir que esto no es cierto?". Si nadie sabe contestar, reescribe.

## 2. Los siete tipos y preguntas para encontrarlos

| Tipo | Pregunta para encontrar supuestos | Ejemplo genérico |
|---|---|---|
| Deseabilidad | ¿Quién tiene que querer usar o aceptar esto? | Los usuarios responden a mensajes más estructurados |
| Valor | ¿Dónde está el beneficio y cuánto vale? | La línea base de errores es la que dice el equipo |
| Factibilidad técnica | ¿Puede un componente hacer esto con la calidad necesaria? | Un paso puede leer texto libre con pocas fallas |
| Datos | ¿Existen los datos, completos y accesibles? | Las solicitudes traen la información necesaria |
| Viabilidad económica | ¿El costo de construir y operar cabe en lo que se espera ganar? | La revisión diaria de casos dudosos es asumible |
| Seguridad y cumplimiento | ¿Qué podría exponerse o incumplirse? | Un componente no aprobado nunca ve datos personales |
| Adopción | ¿El equipo cambiará su forma de trabajar? | Quien aprueba lo hace con atención, no por inercia |

## 3. Escalas de 1 a 5

| Nota | Impacto si es falso | Incertidumbre |
|---|---|---|
| 1 | Casi no cambia nada | Está medido y confirmado |
| 2 | Molesta, se corrige fácil | Hay evidencia sólida, aunque de otro contexto |
| 3 | Afecta una meta secundaria o genera retrabajo | Hay evidencia parcial o dicha por varias personas |
| 4 | Afecta una meta principal o la confianza del equipo | Lo dice una persona o se recuerda; nadie lo contó |
| 5 | Pone en riesgo a personas, datos sensibles o el flujo completo | No hay evidencia alguna |

Criticidad = impacto × incertidumbre (de 1 a 25). Desempates: primero lo que bloquea a otros supuestos, luego lo que afecta seguridad o datos personales, luego lo más barato de probar.

## 4. Impacto y probabilidad de un riesgo

| Nivel | Impacto | Probabilidad (siempre Supuesto sin datos) |
|---|---|---|
| Bajo | Se corrige en el momento, sin efecto externo | Es raro que ocurra |
| Medio | Retrabajo o una queja que se resuelve | Ocurre de vez en cuando |
| Alto | Daño a una persona, a datos sensibles o a la confianza; difícil de deshacer | Ocurre con frecuencia o no hay forma de detectarlo |

Un riesgo de impacto alto tiene guardrail y responsable aunque su probabilidad sea baja.

## 5. Autonomía y supuestos

Regla de enlace: cada subida de nivel en la escalera de autoridad (por ejemplo, de 2 a 3) pide (a) la métrica y el umbral de `elegir-patron-y-autonomia`, (b) los supuestos de datos, valor y adopción que sostienen esa capacidad, y (c) un guardrail activo por cada riesgo de impacto alto. Si algún supuesto sigue sin evidencia, el nivel no sube.

## 6. Errores frecuentes

| Error | Cómo se evita |
|---|---|
| Mezclar supuestos con tareas ("hay que escribir las reglas") | Las tareas van al plan; el supuesto es "las reglas caben en una hoja y no cambian cada semana" |
| Calificar con entusiasmo | Pide la evidencia: "¿lo contaron?" |
| Un solo tipo de supuesto (todos técnicos) | Revisar la cobertura por tipo |
| Mitigaciones sin responsable | Todo riesgo lleva un rol con nombre |
| Probar lo fácil en vez de lo crítico | Ordenar por criticidad y dependencia |
