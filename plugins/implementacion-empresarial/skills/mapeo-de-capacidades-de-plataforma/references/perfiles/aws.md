# Perfil de plataforma: AWS (Amazon Bedrock + AWS Step Functions)

Verificado: 2026-10-25 (lo confirmado en la documentación oficial de AWS en esa fecha). Lo marcado "(verificar)" no se confirmó y debe revisarse en la documentación vigente o con una prueba en la cuenta del cliente antes de decidir.

No hay conversión automática entre plataformas. Este perfil es una guía de capacidades y preguntas de adaptación, no un generador ni una promesa de equivalencia funcional con otra plataforma. Cada mapeo que salga de aquí es una decisión que alguien aprueba.

## Piezas y su papel

| Pieza | Papel en una implementación gobernada | Estado |
|---|---|---|
| AWS Step Functions (flujos Standard) | Orquestador determinístico: hasta un año de duración, ejecución exactamente una vez por paso (salvo los reintentos que se definan), historial de ejecución consultable 90 días después de terminar | Verificado: 2026-10-25 |
| AWS Step Functions (flujos Express) | Alto volumen y corta duración: hasta cinco minutos, ejecución al menos una vez (asíncronos); no admiten el patrón de espera con token de devolución | Verificado: 2026-10-25 |
| Amazon Bedrock | Modelos de IA; Step Functions tiene una integración optimizada para invocar modelos de Bedrock sin código intermedio | Verificado: 2026-10-25 |
| Amazon Bedrock Guardrails | Filtros de información sensible que detectan datos personales en la entrada o en la respuesta y los bloquean o enmascaran; la detección es probabilística | Verificado: 2026-10-25 |
| Almacén de datos del proceso | Base de datos que el cliente decida (por ejemplo, DynamoDB o RDS) | (verificar) |

**Regla del perfil:** para pasos con efectos que no deben repetirse, aprobaciones y esperas largas se usan flujos Standard; los Express solo para tramos cortos e idempotentes. La IA se invoca como un paso acotado del flujo, no como el orquestador.

## Cobertura por tema

| Tema | Opciones habituales | Límites y preguntas de adaptación | Estado |
|---|---|---|---|
| Orquestación | Máquina de estados Standard con un estado por paso del contrato | El tipo de flujo no se puede cambiar después de crear la máquina de estados. ¿Hay tramos de alto volumen que justifiquen Express? | Verificado: 2026-10-25 |
| Estado | Estado interno persistente del flujo Standard entre transiciones, más una base de datos para el estado de negocio y las evidencias | El historial de ejecución se borra a los 90 días: la evidencia del contrato no puede depender de él | Verificado: 2026-10-25 (historial); base de datos (verificar) |
| Modelo de IA | Integración optimizada de Step Functions con Bedrock para invocar un modelo con salida estructurada | El cuerpo de la solicitud tiene un tamaño máximo; para entradas grandes se usa almacenamiento intermedio. ¿Qué modelos y regiones permite el cliente? | Integración: Verificado: 2026-10-25; modelos y regiones (verificar) |
| Conocimiento | Bases de conocimiento de Bedrock o fuentes propias del cliente | ¿Hace falta conocimiento en el paso, o basta con reglas? | (verificar) |
| Identidad | Roles de IAM: uno por máquina de estados y por función, con permisos mínimos | ¿Quién administra los roles y cómo se revisan? | (verificar) |
| Secretos | Un gestor de secretos (por ejemplo, AWS Secrets Manager) leído en ejecución; nunca en la definición del flujo | ¿Rotación de secretos y quién puede leerlos? | (verificar) |
| Aprobaciones | Patrón de devolución con token (`.waitForTaskToken`): el flujo se detiene hasta que alguien devuelve el resultado con ese token; solo en flujos Standard | Definir siempre un tiempo máximo de espera; la experiencia de aprobación (bandeja, correo, aplicación) se construye aparte y debe registrar la identidad del aprobador | Patrón: Verificado: 2026-10-25; experiencia de aprobación (verificar) |
| Observabilidad | AWS CloudTrail registra las llamadas a la API de Step Functions (quién, desde dónde, cuándo); registros de ejecución en CloudWatch Logs | El historial de eventos de CloudTrail cubre 90 días; para más tiempo hace falta un registro continuo (trail). Los eventos de datos no se registran por defecto y tienen costo adicional | Verificado: 2026-10-25 |
| Idempotencia | Iniciar una ejecución Standard con el mismo nombre que una en curso no crea otra; escrituras condicionales en la base de datos con la clave del contrato | La protección por nombre aplica a la ejecución, no a los efectos dentro de ella: cada efecto externo necesita su propia clave | Nombre de ejecución: Verificado: 2026-10-25; escrituras condicionales (verificar) |
| Prueba de aceptación | Cuenta o entorno de prueba separado, datos ficticios, pruebas `AT-nn` del contrato | ¿Cómo se simulan las devoluciones de aprobación y los fallos del sistema de destino? | (verificar) |

## Preguntas que siempre hay que hacer

1. ¿Qué cuentas y regiones usa el cliente, y dónde pueden procesarse los datos del contrato?
2. ¿Qué modelos de Bedrock están habilitados y aprobados?
3. ¿Dónde vive la experiencia de aprobación para las personas y cómo se identifica a quien aprueba?
4. ¿Quién administra IAM, el gestor de secretos y los registros de auditoría?
5. ¿Qué sistemas existentes necesitan una integración propia?

## Checklist de validación

| Paso | Comprobación | Responsable | Hecho |
|---|---|---|---|
| 1 | Cada requisito del contrato tiene opción con ajuste y verificación | Equipo técnico | |
| 2 | Pasos con aprobaciones, esperas o efectos que no deben repetirse en flujos Standard | Equipo técnico | |
| 3 | Cada espera con token tiene tiempo máximo y camino de vencimiento igual al `on_timeout` del contrato | Equipo técnico | |
| 4 | Evidencias en almacenamiento propio, no solo en el historial de ejecución | Equipo técnico | |
| 5 | Roles de IAM con permisos mínimos por componente; el paso de IA sin permisos de escritura | Responsable de seguridad | |
| 6 | Secretos en el gestor de secretos; ninguno en definiciones, parámetros ni registros | Responsable de seguridad | |
| 7 | Filtros de información sensible configurados y probados con datos ficticios, sin confiar solo en ellos (son probabilísticos) | Responsable de datos | |
| 8 | Todo lo marcado "(verificar)" se verificó o quedó como brecha con dueño | Equipo técnico | |
| 9 | **Aprobación** del mapa completo por quien tiene autoridad del cliente, con fecha y decisión registrada | Dueño del flujo / cliente | |

Fuentes consultadas el 2026-10-25: documentación oficial de AWS sobre tipos de flujo de Step Functions, integración con Bedrock, patrón de devolución con token, registro de llamadas con CloudTrail y filtros de información sensible de Bedrock Guardrails.
