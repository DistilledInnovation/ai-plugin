# Perfil de plataforma: Google Cloud (Gemini en Vertex AI + Cloud Workflows)

Verificado: 2026-10-25 (lo confirmado en la documentación oficial de Google Cloud en esa fecha). Lo marcado "(verificar)" no se confirmó y debe revisarse en la documentación vigente o con una prueba en el proyecto del cliente antes de decidir.

No hay conversión automática entre plataformas. Este perfil es una guía de capacidades y preguntas de adaptación, no un generador ni una promesa de equivalencia funcional con otra plataforma. Cada mapeo que salga de aquí es una decisión que alguien aprueba.

## Piezas y su papel

| Pieza | Papel en una implementación gobernada | Estado |
|---|---|---|
| Cloud Workflows | Orquestador determinístico; una ejecución dura como máximo un año | Verificado: 2026-10-25 |
| Gemini en Vertex AI | Modelos de IA; un flujo puede llamarlos con un conector de Vertex AI o con una solicitud HTTP; la cuenta de servicio del flujo necesita el rol de usuario de Vertex AI | Verificado: 2026-10-25 |
| Secret Manager | Almacén de secretos; Workflows tiene un conector para leerlos | Verificado: 2026-10-25 |
| Almacén de datos del proceso | Base de datos que el cliente decida (por ejemplo, Firestore o Cloud SQL) | (verificar) |

**Regla del perfil:** el orden, las esperas, las aprobaciones y los reintentos viven en Workflows; la IA se llama como un paso acotado del flujo, no como el orquestador.

## Cobertura por tema

| Tema | Opciones habituales | Límites y preguntas de adaptación | Estado |
|---|---|---|---|
| Orquestación | Un flujo de Workflows con un paso por paso del contrato | Duración máxima de una ejecución: un año. ¿Hay pasos que conviene separar en flujos distintos? | Verificado: 2026-10-25 |
| Estado | Variables de la ejecución para el estado en curso; base de datos para el estado de negocio y las evidencias | ¿Qué estado necesita sobrevivir al fin de la ejecución? | (verificar) |
| Modelo de IA | Conector de Vertex AI (método de generación de contenido) dentro del flujo, con salida estructurada | ¿Qué modelos y regiones permite el cliente? ¿Cómo se valida la salida antes de usarla? | Conector: Verificado: 2026-10-25; modelos y regiones (verificar) |
| Conocimiento | Búsqueda o recuperación de Vertex AI, o fuentes propias | ¿Hace falta conocimiento en el paso, o basta con reglas? | (verificar) |
| Identidad | Cuenta de servicio por flujo con roles mínimos; IAM para personas | ¿Quién administra las cuentas de servicio y revisa sus roles? | Rol para Vertex AI: Verificado: 2026-10-25; resto (verificar) |
| Secretos | Secret Manager leído con su conector en tiempo de ejecución | Nunca en la definición del flujo ni en sus argumentos | Verificado: 2026-10-25 |
| Aprobaciones | Devoluciones de llamada (callbacks): el flujo crea un punto de devolución y espera a que una solicitud lo reanude; la documentación lo presenta para interacción humana, como revisar un pedido | El tiempo de espera por defecto es de 12 horas y al vencer se produce un error que hay que manejar; el punto de devolución solo vale para la ejecución que lo creó. La experiencia de aprobación se construye aparte y debe registrar la identidad de quien aprueba | Verificado: 2026-10-25; experiencia de aprobación (verificar) |
| Observabilidad | Registros de ejecución que Workflows envía a Cloud Logging; Secret Manager deja registros de auditoría de acceso; Cloud Audit Logs para las operaciones sobre los flujos | ¿Qué registros de acceso a datos están activados y por cuánto tiempo se guardan? | Registros de ejecución y de Secret Manager: Verificado: 2026-10-25; Cloud Audit Logs de Workflows, retención y configuración (verificar) |
| Idempotencia | Clave del contrato guardada en la base de datos antes del efecto; escritura condicional o consulta previa en el sistema de destino | ¿El sistema de destino acepta una clave de idempotencia? | (verificar) |
| Prueba de aceptación | Proyecto de prueba separado, datos ficticios, pruebas `AT-nn` del contrato | ¿Cómo se simulan las devoluciones de llamada y los vencimientos? | (verificar) |

## Preguntas que siempre hay que hacer

1. ¿Qué proyectos y regiones usa el cliente, y dónde pueden procesarse los datos del contrato?
2. ¿Qué modelos de Gemini están permitidos?
3. ¿Dónde aprueban las personas y cómo se identifica a quien aprueba al reanudar el flujo?
4. ¿Algún paso puede esperar más de lo que permite el tiempo de espera configurado?
5. ¿Quién administra IAM, Secret Manager y los registros de auditoría?

## Checklist de validación

| Paso | Comprobación | Responsable | Hecho |
|---|---|---|---|
| 1 | Cada requisito del contrato tiene opción con ajuste y verificación | Equipo técnico | |
| 2 | Cada espera de aprobación tiene tiempo máximo explícito y manejo del vencimiento igual al `on_timeout` del contrato | Equipo técnico | |
| 3 | La reanudación de una aprobación registra quién aprobó y no se puede hacer sin autenticación | Responsable de seguridad | |
| 4 | Evidencias en almacenamiento propio con retención decidida | Equipo técnico | |
| 5 | Cuenta de servicio con roles mínimos; el paso de IA sin permisos de escritura | Responsable de seguridad | |
| 6 | Secretos solo en Secret Manager; ninguno en definiciones, argumentos ni registros | Responsable de seguridad | |
| 7 | Todo lo marcado "(verificar)" se verificó o quedó como brecha con dueño | Equipo técnico | |
| 8 | Pruebas de aceptación del contrato ejecutables con datos ficticios | Equipo técnico | |
| 9 | **Aprobación** del mapa completo por quien tiene autoridad del cliente, con fecha y decisión registrada | Dueño del flujo / cliente | |

Fuentes consultadas el 2026-10-25: documentación oficial de Google Cloud sobre cuotas y devoluciones de llamada de Workflows, acceso a modelos Gemini desde un flujo con Vertex AI, panorama de seguridad de Workflows y registros de auditoría de Secret Manager.
