# Perfil de plataforma: autoalojado (self-hosted)

Verificado: 2026-10-25 (revisión del patrón). Este perfil describe un patrón, no un producto: los componentes los elige y opera el cliente, así que cada afirmación sobre un componente concreto queda "(verificar)" hasta confirmarla con su documentación y con una prueba en la infraestructura del cliente.

No hay conversión automática entre plataformas. Este perfil es una guía de capacidades y preguntas de adaptación, no un generador ni una promesa de equivalencia funcional con otra plataforma. Cada mapeo que salga de aquí es una decisión que alguien aprueba.

## Cuándo se elige

Cuando el cliente tiene restricciones o preferencias de operación propia: los datos no pueden salir de su infraestructura, ya opera servidores y bases de datos, o quiere evitar depender de un proveedor de nube. Es una decisión del cliente con costo de operación propio: alguien tiene que mantener, respaldar y vigilar cada pieza.

## El patrón

| Pieza | Papel | Qué decide el cliente |
|---|---|---|
| Entorno de ejecución de agentes | Ejecuta las llamadas acotadas a un modelo y, si hace falta, la conversación | Cuál usar y qué modelo (local o externo) |
| Motor de flujos (orquestador determinístico) | Pasos en orden, estado persistente, esperas, tareas humanas, aprobaciones, reintentos y efectos externos con evidencia | Cuál usar |
| Base de datos | Estado del caso, evidencias, claves de idempotencia | Cuál usar y cómo se respalda |
| Integraciones | Adaptadores a los sistemas existentes, por interfaces de programación o por servidores MCP (Model Context Protocol, un protocolo abierto para conectar asistentes de IA con herramientas y datos) | Cuáles exponer y con qué permisos |

Una combinación posible, entre otras: un motor de flujos expuesto como servidor MCP (por ejemplo, el runtime de flujos que usa Distilled Innovation, Workflows MCP) con una base de datos SQLite. Es opcional, no una dependencia obligatoria, y antes de tratarlo como listo para producción empresarial hay que cerrar las brechas de la sección "Brechas típicas" (verificar con su documentación vigente).

**Regla del perfil:** el motor de flujos es el orquestador; el entorno de agentes no maneja estado ni efectos externos por su cuenta.

## Cobertura por tema

| Tema | Opciones habituales | Límites y preguntas de adaptación | Estado |
|---|---|---|---|
| Orquestación | Motor de flujos con estado persistente | ¿Reanuda tras un reinicio? ¿Cuánto puede durar una espera? | (verificar) según el motor elegido |
| Estado | Base de datos del motor o del cliente | Una base de un solo archivo puede limitar la concurrencia de escritura; ¿alcanza para el volumen? ¿Cómo se respalda? | (verificar) |
| Modelo de IA | Modelo local o servicio externo aprobado, llamado como paso acotado | Si el modelo es externo, los datos salen de la infraestructura: decisión explícita del responsable de datos | (verificar) |
| Conocimiento | Repositorio propio de fuentes, si el paso lo necesita | ¿Quién mantiene las fuentes y su procedencia? | (verificar) |
| Identidad | Inicio de sesión único (SSO) y control de acceso por roles (RBAC) para personas; identidades separadas por servicio | Hay que construir o integrar lo que una nube trae resuelto | (verificar) |
| Secretos | Gestor de secretos que el cliente opere; nunca en archivos de configuración del repositorio ni en la base de datos del flujo | ¿Quién rota los secretos y quién puede leerlos? | (verificar) |
| Aprobaciones | Tareas humanas del motor de flujos, con identidad de quien aprueba | ¿Dónde aprueban las personas y cómo se autentica la aprobación? | (verificar) |
| Observabilidad | Registros, métricas y alertas que el cliente opere; auditoría en la base de datos | ¿Dónde se guardan, por cuánto tiempo y quién las mira? | (verificar) |
| Idempotencia | Claves del contrato guardadas en la base antes del efecto; restricción de unicidad | ¿El motor reintenta solo? ¿Cómo distingue un reintento de un caso nuevo? | (verificar) |
| Prueba de aceptación | Entorno de prueba separado con datos ficticios; pruebas `AT-nn` del contrato | ¿Se pueden simular caídas y reinicios? | (verificar) |

## Brechas típicas antes de producción

Lo que una nube administrada suele resolver y en autoalojado hay que decidir y construir: aislamiento de identidades, autenticación de las interfaces, SSO y RBAC, gestión de secretos, contenedores o empaquetado, respaldos y recuperación, observabilidad, seguridad de red, políticas de datos y una evaluación de privacidad que vaya más allá de buscar patrones con expresiones regulares. Cada una entra al mapa como requisito con dueño.

## Preguntas que siempre hay que hacer

1. ¿Quién opera cada pieza a las tres de la mañana cuando falla?
2. ¿El modelo de IA corre dentro de la infraestructura o es un servicio externo?
3. ¿Cómo se respalda y se restaura la base de datos, y cada cuánto se prueba?
4. ¿Cómo se autentican las personas que aprueban?
5. ¿Qué capacidades del motor de flujos están probadas y cuáles son promesas?

## Checklist de validación

| Paso | Comprobación | Responsable | Hecho |
|---|---|---|---|
| 1 | Cada requisito del contrato tiene opción con ajuste y verificación | Equipo técnico | |
| 2 | El motor de flujos reanuda un caso tras un reinicio (probado, no supuesto) | Equipo técnico | |
| 3 | Cada brecha típica tiene decisión y dueño | Equipo técnico | |
| 4 | Secretos fuera del código, de la configuración versionada y de la base de datos del flujo | Responsable de seguridad | |
| 5 | Respaldo y restauración probados | Operación del cliente | |
| 6 | Si el modelo es externo, la salida de datos está aprobada por el responsable de datos | Responsable de datos | |
| 7 | Todo lo marcado "(verificar)" se verificó o quedó como brecha con dueño | Equipo técnico | |
| 8 | Pruebas de aceptación del contrato ejecutables con datos ficticios, incluidas caídas | Equipo técnico | |
| 9 | **Aprobación** del mapa completo por quien tiene autoridad del cliente, con fecha y decisión registrada | Dueño del flujo / cliente | |
