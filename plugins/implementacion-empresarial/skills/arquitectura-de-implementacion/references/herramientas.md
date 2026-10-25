# Herramientas para la arquitectura de implementación

Nota de fuente: la arquitectura trazable al contrato, los límites de componentes y la regla de no elegir plataforma por defecto provienen del diseño de implementación empresarial de Distilled Innovation (skill de arquitectura); la distinción entre orquestación generativa y orquestador durable proviene de su oferta empresarial. Los catálogos y listas de este archivo son una adaptación de este plugin.

## 1. Componentes lógicos de referencia

| Componente | Responsabilidad | Límite típico ("no puede") | Cubre del contrato |
|---|---|---|---|
| Entrada | Recibe el evento o la solicitud y crea el caso | No decide nada sobre el contenido | Disparadores `event` y `manual` |
| Orquestador determinístico | Ejecuta los pasos en orden, guarda el estado, maneja esperas, reintentos, tiempos de espera y aprobaciones | No interpreta texto libre ni decide con criterio flexible | `steps`, `states`, `trigger`, `retry_policy` |
| Almacén de estado y evidencias | Guarda el estado de cada caso y las constancias | No ejecuta lógica de negocio | `states`, `evidence_requirements` |
| Componente de IA acotado | Lee texto libre, extrae o clasifica con salida estructurada | No escribe en sistemas, no aprueba, no envía, no llama herramientas que modifiquen | Pasos `ai_assisted`, `authority_level`, `guardrails` |
| Reglas | Aplica reglas fijas (cálculos, validaciones, plantillas) | No decide fuera de las reglas escritas | Pasos `deterministic`, `business_rules` |
| Bandeja de aprobaciones y cola de revisión | Muestra a la persona lo que debe aprobar o revisar y registra su decisión | No ejecuta el efecto: devuelve la decisión al orquestador | `approval_policies`, pasos `decision` y `human_task`, estados de falla |
| Adaptador (uno por sistema existente) | Traduce entre el flujo y un sistema existente; expone solo las operaciones que el contrato pide | No expone operaciones que el contrato no usa (por ejemplo, borrar) | Pasos con efecto externo, `idempotency` |
| Mensajería de salida | Envía mensajes a personas externas con plantillas aprobadas | No redacta libremente ni envía sin aprobación cuando el contrato la exige | Pasos que envían |
| Auditoría y observabilidad | Registra quién hizo qué y cuándo, métricas y alertas | No guarda más datos personales de los necesarios | `evidence_requirements`, `metrics` |
| Control de modo manual | Permite apagar la parte con IA y volver a operar como antes | No puede encenderse de nuevo sin quien tiene autoridad | Guardrail de falla del componente de IA |

## 2. Orquestador determinístico frente a orquestación generativa

| Necesidad del contrato | Orquestador determinístico | Orquestación generativa |
|---|---|---|
| Orden fijo de pasos | Garantizado por definición | El modelo decide en el momento; puede variar |
| Esperar horas o días (pasos `wait`) | Sí, con estado persistente y tiempo máximo | No es su función |
| Reanudar tras un reinicio | Sí, desde el último estado guardado | No garantizado |
| Aprobación antes del efecto externo | Se hace cumplir en el flujo | No se puede garantizar solo con instrucciones |
| Reintentos con límite | Configurables por paso | No garantizados |
| Conversación con una persona, elegir qué responder | Rígido | Adecuada |

Regla: lo que el contrato exige con garantías (orden, aprobaciones, reintentos, esperas, evidencia) va en el orquestador determinístico. La orquestación generativa puede atender una conversación y entregar al orquestador una solicitud estructurada, pero no maneja el estado del caso ni los efectos externos.

## 3. Cómo acotar un paso con IA

| Elemento | Regla |
|---|---|
| Entrada | Solo los datos que el paso necesita (minimización); los demás se omiten o se enmascaran |
| Instrucciones | Fijas y versionadas; el texto externo se trata como dato, nunca como instrucciones |
| Salida | Estructurada (campos con tipo) y validada por el orquestador antes de usarla |
| Herramientas | Ninguna que modifique sistemas |
| Si falla o duda | El caso va a la cola de revisión humana, no se reintenta sin límite |
| Evidencia | Se registra qué entró (o su referencia), qué salió y la versión de las instrucciones |

## 4. Clasificación de datos en las flechas

| Sensibilidad (del contrato) | Ejemplo genérico | Pregunta de arquitectura |
|---|---|---|
| `public` | Horario de atención publicado | Ninguna especial |
| `internal` | Tipo de cita, reglas de agenda | ¿Quién puede leerla? |
| `personal` | Contacto, horario aceptado | ¿Hace falta que llegue a este componente? |
| `sensitive` | Motivo de consulta, datos de salud | ¿Puede llegar al componente de IA? ¿Con qué autorización y qué enmascaramiento? |

## 5. Lista de salida

| Comprobación | Sí / No |
|---|---|
| Cada paso del contrato tiene componente que lo ejecuta | |
| Cada política de aprobación tiene dónde aprobarse y bloquea el efecto hasta aprobar | |
| Cada evidencia tiene componente que la produce y lugar donde se guarda | |
| Cada guardrail tiene componente que lo hace cumplir | |
| Cada prueba de aceptación tiene los componentes que intervienen | |
| Ningún componente queda sin elemento del contrato | |
| El orquestador determinístico es dueño del estado, esperas, reintentos y aprobaciones | |
| El componente de IA no tiene permisos de escritura ni herramientas que modifiquen | |
| Ningún camino llega a un efecto externo sin pasar por su aprobación | |
| Existe modo manual con responsable | |
| Ninguna plataforma, producto o proveedor está nombrado | |
| Cada decisión y valor del cliente está en el registro con dueño, fecha y aprobación | |
| El diagrama tiene tabla equivalente | |
| Sin credenciales, direcciones reales ni datos personales | |
