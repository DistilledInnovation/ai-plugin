# Herramientas para la idempotencia y la confiabilidad

Nota de fuente: la exigencia de que toda operación repetible lleve clave idempotente, clasificación de reintentos y manejo de duplicados, con compensaciones, cola de errores y recuperación, proviene del diseño de implementación empresarial de Distilled Innovation; los criterios de calidad operativa (idempotencia de acciones, recuperación de errores, estado observable, trazabilidad de versiones y propiedad de incidentes) provienen de su oferta empresarial. Las estrategias de clave, reintento con espera creciente, cola de mensajes no procesados y conciliación son prácticas usadas ampliamente en integración de sistemas.

## 1. Dónde buscar operaciones repetibles

| Fuente | Qué buscar | Ejemplo típico |
|---|---|---|
| Pasos con `external_effect: true` | Todo envío, registro o modificación fuera del flujo | Enviar un mensaje, crear un registro en otro sistema |
| Entrada del flujo | El canal puede entregar dos veces lo mismo | Un formulario enviado dos veces, un mensaje reenviado por el canal |
| Esperas y avisos | Avisos que se disparan por tiempo | Recordatorio diario, aviso de vencimiento |
| Aprobaciones | Una persona responde dos veces o tarde | Doble clic, respuesta después del vencimiento |
| Reprocesamiento | Lo que se reintenta desde la cola de errores | Reenvío de una entrada fallida |

## 2. Estrategias de clave

| Estrategia | Cuándo sirve | Cuidado |
|---|---|---|
| Clave natural (campos del negocio) | El negocio ya define qué es "lo mismo": persona + horario, caso + día | Elegir campos estables; un dato que cambia (un nombre corregido) rompe la clave |
| Clave de operación generada | Cada solicitud tiene un identificador propio que viaja con la operación | Se genera una vez, al crear la operación, y se reutiliza en cada reintento |
| Clave con versión | La misma operación puede rehacerse legítimamente (una propuesta corregida) | La versión cambia solo por una decisión (por ejemplo, una corrección aprobada), nunca por un reintento |
| Sin clave (no aplica) | Pasos de solo lectura o decisiones humanas sin efecto | Declararlo con la razón |

**Alcance**: dentro de qué se compara la clave (un caso, una persona, un día, todo el sistema). **Retención**: cuánto se guarda la clave; al menos mientras pueda llegar una repetición (reintentos, reenvíos del canal, reprocesamientos). Ambos son decisiones con dueño.

## 3. Qué garantiza el destino

| El destino… | Patrón | Brecha que queda |
|---|---|---|
| Acepta una clave de operación | Enviar la clave en cada intento | Ninguna en la operación (verificar con una prueba) |
| Permite consultar antes de escribir | Constancia previa + consulta + escritura + confirmación | Una caída entre escribir y confirmar deja un caso incierto: conciliación |
| No permite ni lo uno ni lo otro | Constancia previa + revisión humana de los inciertos, o dejar el paso como tarea humana | Duplicado posible: se escribe como riesgo con dueño |

Nunca afirmes que una plataforma "garantiza que no se duplique" sin documentación vigente o una prueba: la garantía, cuando existe, suele depender del sistema de destino, no del orquestador.

## 4. Clasificación de errores

| Clase | Señales típicas | Qué se hace | Qué nunca se hace |
|---|---|---|---|
| Transitorio | Se sabe que la solicitud **no se procesó**: el destino la rechazó o la limitó antes de procesarla (límite de solicitudes, servicio no disponible), o no se pudo conectar. En operaciones sin efecto externo (por ejemplo, una llamada al modelo), una falta de respuesta también es transitoria | Reintentar con espera creciente (por ejemplo, 1, 2 y 4 minutos) hasta el tope del contrato; luego, a la cola | Reintentar sin tope ni espera |
| Permanente | Dato inválido, permiso denegado, regla de negocio incumplida, recurso inexistente | A la cola de revisión (negocio) o de errores (técnica) sin reintentar | Reintentar esperando otro resultado |
| Incierto | En una operación con efecto externo: el destino no responde, tiempo agotado después de enviar, respuesta perdida | Consultar el destino con la clave; si no es concluyente, revisión | Repetir el efecto a ciegas |

Los pasos con IA tienen además errores de forma (salida que no respeta los campos): se tratan como permanentes para ese intento y el caso pasa a revisión, salvo que el contrato permita un reintento.

## 5. Reintentos de la plataforma

Muchas plataformas traen reintentos automáticos en sus acciones o conectores, con valores por defecto (verificar en el perfil elegido y en la documentación vigente). Esos reintentos ocurren **dentro** de un paso y pueden repetir un efecto sin que el orquestador lo vea. Regla: para cada acción con efecto externo, configura el reintento de forma explícita con el valor del contrato y deja la configuración en el registro.

## 6. Compensaciones

| Tipo de efecto | Compensación habitual | Aprobación |
|---|---|---|
| Registro en otro sistema | Anular o corregir el registro, si el permiso existe; si el adaptador no puede borrar, lo hace una persona con su propio permiso | Según la matriz de aprobación |
| Mensaje enviado | No se puede deshacer: mensaje de aclaración con plantilla aprobada | Siempre humana |
| Cambio de estado interno | Volver al estado anterior con registro | Dueño del proceso |

Una compensación también puede fallar: tiene su propia clave y su propia entrada en el registro.

## 7. Cola de revisión y cola de errores

- **Cola de revisión** (negocio): casos que una persona del cliente decide. Dueño de negocio.
- **Cola de errores** (técnica, también llamada DLQ): entradas o efectos que fallaron por causas técnicas y no pudieron seguir. Dueño técnico.
- Cada cola: qué entra, dueño, frecuencia de revisión, antigüedad máxima con alerta, y cómo se reprocesa **con la misma clave**.
- Un elemento no se queda en la cola de errores indefinidamente: o se reprocesa, o pasa a revisión con su explicación, o se descarta con registro y aprobación.

## 8. Recuperación y conciliación

1. **Reinicio**: el orquestador retoma desde el último estado guardado; los pasos con efecto en estado "pendiente" se consultan antes de repetirse.
2. **Conciliación**: periódicamente se comparan las constancias con el sistema de destino (por ejemplo, cada día). Diferencias típicas: constancia sin efecto (falló después de guardar), efecto sin constancia (falló antes de confirmar), efecto duplicado. Cada diferencia va a revisión con dueño.
3. **Objetivo de recuperación**: en cuánto tiempo el servicio debe volver a funcionar y cuánto trabajo se puede rehacer a mano; decisión del cliente.
4. **Último recurso**: el modo manual (apagar la parte automatizada y operar como antes) con su responsable.

## 9. Lista de salida

| Comprobación | Sí / No |
|---|---|
| Toda operación repetible tiene `IDM-nn`, clave, alcance, constancia y retención | |
| Duplicados técnicos y de negocio están separados, y los de negocio siguen la regla del contrato | |
| Cada operación tiene errores clasificados en transitorio, permanente e incierto | |
| Los reintentos coinciden con el contrato y los de la plataforma están configurados de forma explícita | |
| Ningún resultado incierto se reintenta a ciegas | |
| Cada efecto tiene compensación o acción correctiva con aprobador | |
| Las colas tienen dueño, revisión, alerta por antigüedad y reprocesamiento con la misma clave | |
| Recuperación y conciliación definidas, con objetivo de tiempo como decisión | |
| Las brechas del destino están escritas sin garantías prestadas | |
| Cada operación tiene al menos una prueba de resiliencia negativa | |
