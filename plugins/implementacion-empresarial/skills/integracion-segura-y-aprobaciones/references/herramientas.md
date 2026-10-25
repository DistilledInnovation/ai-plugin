# Herramientas para la integración segura y las aprobaciones

Nota de fuente: el modelo de amenazas, el mínimo privilegio, los secretos fuera de los artefactos, la matriz de aprobación y la auditoría provienen del diseño de implementación empresarial de Distilled Innovation; los criterios de seguridad y privacidad (clasificación de fuentes, permisos mínimos, residencia de datos, minimización, retención, controles de salida, revisión humana de acciones de alto impacto) y el patrón "anonimizar antes del modelo" provienen de su oferta empresarial y de Automatización con IA. Las categorías de amenazas siguen una clasificación usada ampliamente en seguridad (suplantación, alteración, repudio, fuga de información, denegación de servicio y elevación de privilegios), a la que este plugin suma categorías propias de los flujos con IA.

## 1. Catálogo de amenazas

| Categoría | Qué es, en una línea | Pregunta en el flujo | Controles típicos |
|---|---|---|---|
| Suplantación | Alguien o algo se hace pasar por otro | ¿Puede alguien aprobar en nombre de otro? ¿Puede un mensaje fingir ser de otra persona? | Identidad en cada aprobación; asociar respuestas al caso por datos verificados |
| Alteración | Se modifica un dato o una regla sin autorización | ¿Quién puede cambiar las reglas, plantillas o instrucciones? | Cambios con aprobación y versión; registro de cambios |
| Repudio | Alguien niega haber hecho algo y no hay cómo probarlo | ¿Queda quién aprobó y cuándo? | Auditoría con identidad, hora y versión |
| Fuga de información | Un dato llega a quien no debe | ¿Una persona puede recibir datos de otra? ¿Los registros guardan datos de más? | Plantillas con datos del caso confirmado; minimización en registros |
| Denegación de servicio | El flujo deja de funcionar o se satura | ¿Qué pasa si llegan cien solicitudes falsas? ¿Si el modelo no responde? | Límites de entrada; modo manual; cola de revisión |
| Elevación de privilegios | Un componente hace más de lo que debería | ¿El componente de IA o una identidad de servicio puede escribir o borrar? | Mínimo privilegio; identidades separadas |
| Instrucciones ocultas | Texto externo trae órdenes para el modelo ("ignora lo anterior y…") | ¿Qué hace el flujo si un mensaje trae instrucciones? | El texto externo es dato; instrucciones fijas; salida estructurada validada; la IA sin herramientas que escriban |
| Exceso de autonomía | La IA actúa sobre sistemas o personas sin control | ¿Algún camino llega a un efecto externo sin aprobación? | Aprobación antes del efecto; nivel de autoridad del contrato |
| Salida no validada | Se usa lo que devuelve el modelo sin comprobar | ¿Qué pasa si el modelo inventa un campo o un horario? | Validar forma y valores; ante duda, revisión humana |
| Fuga al modelo | Datos sensibles llegan a un modelo o a un proveedor no autorizado | ¿Qué datos salen hacia el modelo y dónde se procesan? | Minimizar, enmascarar o anonimizar; modelos permitidos por decisión; autorización del responsable de datos |

## 2. Mínimo privilegio: cómo revisarlo

1. Lista cada permiso que tiene cada rol y cada identidad de servicio.
2. Para cada permiso, encuentra el paso del contrato que lo usa. Si no hay, se quita.
3. Separa lectura de escritura: un componente que solo consulta no necesita escribir.
4. Ningún componente tiene permiso de borrar si el contrato no tiene un paso que borre.
5. Cada identidad de servicio es de un solo componente; no se comparten.
6. Se fija quién revisa los permisos y cada cuánto (decisión del cliente).

## 3. Minimizar y anonimizar antes del modelo

| Técnica | Qué hace | Cuándo sirve | Límite |
|---|---|---|---|
| Omitir | No enviar el dato | El paso no lo necesita | Ninguno |
| Enmascarar con marca | Reemplazar el dato por una marca (`{DOCUMENTO}`, `{TELEFONO}`) antes de enviarlo; el valor real se conserva fuera del modelo | Datos con forma reconocible (números de documento, teléfonos, correos) | Las reglas por patrones no detectan todo; nombres y texto libre se escapan |
| Seudonimizar | Reemplazar por un identificador estable que solo el flujo puede revertir | Cuando el modelo necesita distinguir personas sin conocerlas | La tabla de correspondencia es un secreto más |
| Generalizar | Enviar una categoría en vez del dato ("adulto", "mañana") | Cuando basta el rango | Pierde detalle |
| Dejar sin anonimizar (decisión) | Enviar el dato real porque el paso lo necesita | Solo con modelo permitido, autorización del responsable de datos y registro de la decisión | Riesgo residual explícito |

Regla: la detección automática de datos personales es probabilística; no se confía solo en ella. Se combina con omitir lo innecesario y con una prueba con datos ficticios que contengan los casos difíciles.

## 4. Matriz de aprobación: acciones que suelen faltar

El contrato cubre las aprobaciones de los pasos del flujo. La operación suma otras acciones de impacto:

| Acción | Por qué es de impacto | Quién suele aprobar |
|---|---|---|
| Cambiar reglas, plantillas o criterios | Cambia lo que el flujo hace con personas | Dueño del proceso o de los criterios |
| Cambiar el modelo, su versión o sus instrucciones | Cambia el comportamiento de la IA | Dueño del flujo y responsable de datos |
| Conceder o ampliar accesos | Abre la puerta a usos no previstos | Responsable de seguridad |
| Encender la parte con IA tras un apagado | El apagado tuvo una razón | Dueño del proceso |
| Exportar evidencias o registros | Pueden contener datos personales | Responsable de datos |

Apagar la parte con IA **no** requiere aprobación previa: debe poder hacerse de inmediato y se registra.

## 5. Qué registra la auditoría

| Campo | Ejemplo genérico |
|---|---|
| Quién | Rol e identidad de la persona o del componente |
| Qué | Acción y caso (por referencia) |
| Cuándo | Fecha y hora |
| Con qué versión | Versión de reglas, plantillas e instrucciones del modelo |
| Decisión | Aprobó, rechazó, corrigió |
| Qué no | Copias completas de mensajes o datos de salud; se guarda la referencia |

## 6. Lista de salida

| Comprobación | Sí / No |
|---|---|
| Cada límite y flujo de datos revisado con el catálogo | |
| Cada amenaza con control, riesgo residual y dueño | |
| Cada permiso responde a un paso del contrato | |
| El componente de IA no escribe en sistemas ni llama herramientas que modifiquen | |
| Ningún secreto en artefactos; se sabe dónde vive cada uno | |
| Cada paso con IA tiene su tabla de datos hacia el modelo y modelo permitido por decisión | |
| Cada acción de impacto en la matriz, con aprobador distinto de quien la produce | |
| Auditoría definida, con retención como decisión | |
| Cada control tiene prueba, incluida una negativa | |
| Riesgos residuales aceptados por quien tiene autoridad | |
