# Perfil de plataforma: Microsoft (Copilot Studio + Dataverse + Power Automate)

Verificado: 2026-10-25 (lo confirmado en la documentación oficial de Microsoft en esa fecha). Lo marcado "(verificar)" no se confirmó y debe revisarse en la documentación vigente o con una prueba en el entorno del cliente antes de decidir.

No hay conversión automática entre plataformas. Este perfil es una guía de capacidades y preguntas de adaptación, no un generador ni una promesa de equivalencia funcional con otra plataforma. Cada mapeo que salga de aquí es una decisión que alguien aprueba.

## Piezas y su papel

| Pieza | Papel en una implementación gobernada | Estado |
|---|---|---|
| Copilot Studio | Agentes conversacionales. Con orquestación generativa, el agente elige temas, herramientas, otros agentes y fuentes de conocimiento según sus descripciones; la respuesta puede variar con el historial de la conversación y con el modelo configurado | Verificado: 2026-10-25 |
| Conocimiento de Copilot Studio | Fuentes para fundamentar respuestas: sitios públicos, documentos cargados en Dataverse, SharePoint, Dataverse y datos empresariales mediante conectores; SharePoint, Dataverse y conectores usan la autenticación del usuario (Microsoft Entra ID), de modo que cada persona solo ve lo que puede ver | Verificado: 2026-10-25 |
| Dataverse | Datos de negocio y estado del caso (tablas), con auditoría de cambios configurable | Verificado: 2026-10-25 (auditoría); diseño de tablas (verificar) |
| Power Automate (flujos de nube) | Orquestador determinístico: pasos en orden, esperas, aprobaciones, reintentos | Verificado: 2026-10-25 (límite de duración); resto (verificar) |

**Regla del perfil:** la orquestación generativa sirve para la conversación y para elegir herramientas; no es un motor durable. Aprobaciones, reintentos, esperas y procesos largos van en un orquestador determinístico (Power Automate o un componente equivalente que el cliente decida).

## Cobertura por tema

| Tema | Opciones habituales | Límites y preguntas de adaptación | Estado |
|---|---|---|---|
| Orquestación | Flujo de nube de Power Automate como orquestador; el agente de Copilot Studio solo como canal conversacional que entrega una solicitud estructurada | Una ejecución de flujo de nube dura como máximo 30 días, contando los pasos pendientes como aprobaciones; al cumplirse, los pasos pendientes vencen. ¿Algún caso del contrato puede esperar más? | Verificado: 2026-10-25 |
| Estado | Tabla de Dataverse por caso, con el estado del contrato (`ST-nn`) y las referencias a evidencias | La retención del historial de ejecuciones de un flujo es de 30 días: el estado y la evidencia no pueden depender de ese historial | Verificado: 2026-10-25 (retención del historial); diseño de tablas (verificar) |
| Modelo de IA | Una llamada acotada a un modelo desde el flujo (por ejemplo, una herramienta de prompt de Copilot Studio o un servicio de modelos aprobado por el cliente) con salida estructurada | ¿Qué modelos están permitidos por el cliente? ¿Dónde se procesan los datos? ¿Se puede obligar a una salida con campos? | (verificar) |
| Conocimiento | Fuentes de conocimiento de Copilot Studio cuando el paso necesita consultar documentos | Con orquestación generativa no se usan las fuentes de datos personalizadas ni Bing Custom Search como conocimiento; solo dentro de un nodo de respuestas generativas | Verificado: 2026-10-25 |
| Identidad | Microsoft Entra ID para personas; identidades de servicio y roles de seguridad de Dataverse para el flujo | ¿Con qué identidad corre cada conexión del flujo? ¿Quién es dueño de esa identidad? | Entra ID para conocimiento: Verificado: 2026-10-25; roles y conexiones (verificar) |
| Secretos | Variables de entorno de tipo secreto que referencian Azure Key Vault; el valor queda en el almacén y la variable solo guarda la referencia | Azure Key Vault es el único almacén de secretos soportado para variables de entorno; el almacén debe estar en el mismo inquilino. Las variables de texto no están cifradas: nunca guardes allí claves | Verificado: 2026-10-25 |
| Aprobaciones | Acciones de aprobación de Power Automate dentro del flujo; la aprobación queda con la identidad de quien aprueba | La espera de la aprobación cuenta para el límite de 30 días de la ejecución. Para esperas más largas, separar crear la aprobación y esperar la respuesta en flujos distintos | Límite: Verificado: 2026-10-25; patrón de dos flujos (verificar) |
| Observabilidad | Auditoría de Dataverse (cambios en registros, activada por tabla y columna); historial de ejecuciones del flujo; registros de uso del agente | La auditoría de Dataverse no cubre lecturas ni exportaciones (eso es otro registro de actividad); el historial de flujos se conserva 30 días | Auditoría: Verificado: 2026-10-25; registros del agente (verificar) |
| Idempotencia | Clave del contrato guardada en Dataverse antes del efecto; consulta previa en el sistema de destino; claves alternativas únicas en tablas de Dataverse | ¿El sistema de destino acepta una clave de idempotencia? Si no, ¿se puede consultar antes de escribir? | (verificar) |
| Prueba de aceptación | Entornos separados de Power Platform para pruebas, con datos ficticios; ejecutar las pruebas `AT-nn` del contrato | ¿Las pruebas negativas (instrucciones ocultas, duplicados) se pueden reproducir en el entorno de prueba? | (verificar) |

## Preguntas que siempre hay que hacer

1. ¿Qué licencias tiene el cliente para flujos con conectores premium, Dataverse y Copilot Studio? (Dicho por participante hasta verificar con el administrador de licencias.)
2. ¿Qué sistemas existentes tienen conector y cuáles necesitan un conector personalizado?
3. ¿Algún paso del contrato puede superar el límite de 30 días de una ejecución?
4. ¿Qué modelos de IA y qué regiones de procesamiento permite el cliente para los datos del contrato?
5. ¿Quién administra los entornos, las conexiones y el almacén de secretos?

## Checklist de validación

| Paso | Comprobación | Responsable | Hecho |
|---|---|---|---|
| 1 | Cada requisito del contrato tiene opción con ajuste y verificación | Equipo técnico | |
| 2 | Ningún paso con aprobación, espera o reintento depende de la orquestación generativa | Equipo técnico | |
| 3 | Ninguna espera del contrato supera el límite de duración de la ejecución, o la brecha está decidida | Equipo técnico | |
| 4 | Estado y evidencias en tablas, no en el historial de ejecuciones | Equipo técnico | |
| 5 | Secretos solo en el almacén de secretos; ningún valor en flujos, variables de texto ni exportaciones | Responsable de seguridad | |
| 6 | Cada efecto externo tiene aprobación antes del efecto y clave de idempotencia | Equipo técnico | |
| 7 | Todo lo marcado "(verificar)" se verificó o quedó como brecha con dueño | Equipo técnico | |
| 8 | Pruebas de aceptación del contrato ejecutables en un entorno de prueba con datos ficticios | Equipo técnico | |
| 9 | **Aprobación** del mapa completo por quien tiene autoridad del cliente, con fecha y decisión registrada | Dueño del flujo / cliente | |

Fuentes consultadas el 2026-10-25: documentación oficial de Microsoft sobre orquestación generativa y fuentes de conocimiento de Copilot Studio, límites de flujos de Power Automate, variables de entorno con secretos de Azure Key Vault y auditoría de Dataverse.
