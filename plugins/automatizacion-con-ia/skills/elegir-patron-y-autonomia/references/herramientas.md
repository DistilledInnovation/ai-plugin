# Herramientas para elegir patrón y autonomía

Nota de fuente: el árbol de decisión, la separación entre modo de interacción, modo de razonamiento y autoridad de ejecución, la escalera de autoridad de 0 a 5 y el catálogo de guardrails provienen del marco de consultoría de Automatización con IA de Distilled Innovation; las explicaciones y plantillas son una adaptación de este plugin.

## 1. Las tres decisiones separadas

| Decisión | Pregunta | Opciones |
|---|---|---|
| Modo de interacción | ¿Cómo se inicia y cómo se usa? | Conversacional, por eventos, programado, embebido en otra tarea |
| Modo de razonamiento | ¿Cómo se decide qué hacer? | Reglas, IA acotada en pasos fijos, agente que elige el siguiente paso |
| Autoridad de ejecución | ¿Qué puede hacer sin permiso? | Recomendar, redactar, ejecutar con aprobación, ejecutar dentro de límites, actuar con autonomía |

Un flujo programado (sin conversación) con IA acotada y autoridad 2 es perfectamente válido; un copiloto conversacional con autoridad 1 también. El patrón no define la autoridad.

## 2. Capacidades técnicas genéricas (qué se puede pedir sin nombrar productos)

| Capacidad | En lenguaje simple | Se usa para |
|---|---|---|
| Entender texto libre | Leer un mensaje o documento y sacar sentido | Clasificar, extraer, resumir |
| Salida estructurada | Que la respuesta venga en campos fijos, no en párrafos | Pasar datos a otro paso sin errores de formato |
| Recuperar información | Buscar en una fuente aprobada antes de responder | Responder con base en documentos propios |
| Redactar con plantilla | Rellenar un texto fijo con datos del caso | Mensajes repetitivos sin IA |
| Llamar a una herramienta | Ejecutar una acción acotada (consultar, registrar) | Pasos que tocan otros sistemas |
| Pedir aprobación | Detenerse hasta que una persona acepte | Modelo de control, a cualquier nivel |
| Cola de revisión | Apartar los casos dudosos para una persona | Baja certeza, excepciones |
| Registro de acciones | Dejar constancia de qué se hizo y por qué | Auditoría y corrección |
| Entorno aislado | Limitar a qué puede acceder el sistema | Contenido no confiable, ejecución autónoma |

Todas son capacidades **genéricas**. Cuál producto las ofrece, o si hace falta alguno, se decide en la especificación.

## 3. Cuándo cada patrón es la respuesta correcta

| Situación típica | Patrón probable | Por qué |
|---|---|---|
| Aplicar una tarifa, buscar un registro, calcular una fecha | Determinística | Una regla siempre da la misma respuesta |
| Clasificar mensajes de texto libre y pasarlos a un paso fijo | Flujo con IA | El orden es fijo; solo un paso entiende texto libre |
| Preparar un resumen de un historial para quien decide | Copiloto o flujo con IA con autoridad 1 o 2 | La decisión sigue siendo de la persona |
| Investigar una pregunta abierta con pasos que dependen de lo encontrado | Agente autónomo, con límites | El camino no se puede fijar |
| Un flujo con pasos de reglas, un paso de lectura y un paso de decisión humana | Híbrido | Cada parte con su patrón |

Antes de elegir un agente: ¿un flujo con ramas lo cubre? ¿Las ramas se pueden enumerar? Si sí, no hace falta.

## 4. Cómo asignar el nivel de autoridad

1. Empieza en el nivel más bajo que haga útil la capacidad (por lo general 1 o 2).
2. Pregunta tres cosas: ¿es reversible?, ¿es detectable?, ¿cuánto cuesta el error?
3. Si es irreversible o cuesta mucho, el tope es el nivel 2 (la persona aprueba) o la ejecución en dos pasos.
4. Define la métrica que permitirá subir (por ejemplo, tasa de errores durante un periodo) y quién decide.
5. Anota el nivel por capacidad: un mismo flujo puede mezclar un paso en nivel 3 y otro en nivel 1.

## 5. Cómo asignar los guardrails

1. Recorre el catálogo base y marca las condiciones que aplican.
2. Para cada una, escribe el límite en términos del flujo ("la recepcionista aprueba antes de enviar") y el responsable.
3. Si una condición no aplica, escribe por qué (por ejemplo, "la acción se puede deshacer").
4. Si una condición aplica y no hay límite posible, el nivel de autoridad baja.
5. Los riesgos nuevos se registran como riesgo → impacto → mitigación, con el guardrail como mitigación.

## 6. Señales de que se está sobrediseñando

| Señal | Qué hacer |
|---|---|
| Se pide un agente para un proceso con pasos fijos | Verificar el flujo con ramas |
| Se pide IA para una regla | Volver a reglas |
| Todo el flujo está en nivel 4 desde el primer día | Bajar a 1 a 3 y definir la evidencia para subir |
| "El agente decidirá" sin decir quién responde | Volver al control humano |
| Se nombra un producto para resolver la decisión | Quitarlo: la herramienta se elige después |
