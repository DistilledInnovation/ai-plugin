# Herramientas para el mapeo de capacidades

Nota de fuente: el mapa de capacidades (requisito, opciones, decisión, brecha, dueño y aprobación), los perfiles de plataforma y la regla de que cada mapeo es una decisión revisable provienen del diseño de implementación empresarial de Distilled Innovation; el mapa de backends por proveedor proviene de su oferta empresarial. La lista de extracción de requisitos y los criterios de ajuste son una adaptación de este plugin.

## 1. De dónde salen los requisitos

| Categoría (`category`) | Sale del contrato | Pregunta para el perfil |
|---|---|---|
| `orchestration` | `steps`, `trigger`, pasos `wait`, `retry_policy`, guardrail de modo manual | ¿Qué orquestador determinístico hay y cuánto puede durar una ejecución? |
| `state` | `states`, cola de revisión | ¿Dónde vive el estado del caso fuera del historial de ejecución? |
| `identity` | `actors`, `approver_role` | ¿Cómo se identifica a cada persona y a cada componente? |
| `secrets` | Conexiones a sistemas existentes | ¿Dónde se guardan y quién puede leerlos? |
| `approvals` | `approval_policies` (`on_timeout`, `on_rejection`) | ¿Cómo espera el flujo la aprobación y queda la identidad del aprobador? |
| `observability` | `evidence_requirements`, `metrics` | ¿Qué registros hay, cuánto se guardan, quién los ve? |
| `idempotency` | `idempotency` de cada paso con efecto externo | ¿El destino acepta una clave? ¿Se puede consultar antes de escribir? |
| `ai_model` | Pasos `ai_assisted`, `authority_level`, `guardrails` | ¿Qué modelos están permitidos y cómo se acota la salida? |
| `knowledge` | `required_knowledge` | ¿Hace falta recuperación de documentos? |
| `integration` | Sistemas que los pasos leen o modifican | ¿Hay conector o hay que construir un adaptador? |
| `data_protection` | `sensitivity` de entradas y salidas, guardrails de datos | ¿Qué datos pueden llegar al modelo y con qué tratamiento? |
| `acceptance_test` | `acceptance_tests` | ¿Se pueden ejecutar las pruebas, incluidas las negativas, en un entorno de prueba? |

Las ocho primeras más `acceptance_test` son obligatorias en todo mapa; las demás, cuando el contrato las pide.

## 2. Ajuste de una opción (`fit`)

| Valor | Significa | Ejemplo genérico |
|---|---|---|
| `native` | La plataforma lo hace tal cual, sin construir | Una acción de aprobación incluida en el orquestador |
| `configuration` | Se logra configurando piezas existentes | Una tabla con una clave única |
| `custom_build` | Hay que construir algo propio | Un adaptador para un sistema sin conector |
| `partial` | Cubre parte; queda brecha | Una espera con un máximo menor que el que pide el contrato |
| `not_available` | No existe en este perfil | — |
| `unknown` | No se sabe todavía | Antes de revisar la documentación vigente |

`verification`: `verified` solo si se confirmó en la documentación oficial vigente o en una prueba; si no, `to_verify`. Una opción `to_verify` puede elegirse, pero su brecha dice qué falta verificar y quién lo hace.

## 3. Estados de decisión y de aprobación

| Campo | Valores | Regla |
|---|---|---|
| `decision.status` | `proposed`, `decided`, `deferred` | Sin `chosen_option` no hay `decided` |
| `approval_status` | `pending`, `approved`, `rejected`, `needs_changes` | Nada se construye en `pending` ni en `rejected`; `needs_changes` dice qué cambiar |

## 4. Frases que no se escriben (y qué escribir en su lugar)

| No | Sí |
|---|---|
| "X equivale a Y de la otra nube" | "X cubre el requisito así…; queda esta brecha…" |
| "Se migra automáticamente" | "No hay conversión automática entre plataformas; se vuelve a mapear y a aprobar" |
| "Es igual que en el piloto" | "En el piloto se hizo así; en esta plataforma la opción es…, verificada / por verificar" |
| "La plataforma lo resuelve" | "La opción elegida es…, con ajuste…, dueño… y aprobación…" |

## 5. Mapa de orientación por proveedor

Solo para saber dónde buscar en cada perfil. **No es una tabla de equivalencias**: una celda no significa que dos piezas hagan lo mismo, y nada se traslada solo de una columna a otra.

| Capacidad | Microsoft | AWS | Google Cloud | Autoalojado |
|---|---|---|---|---|
| Agentes y modelos | Copilot Studio o servicios de IA aprobados | Bedrock | Gemini en Vertex AI | Entorno de agentes y modelo que elija el cliente |
| Orquestación durable | Power Automate | Step Functions (Standard) | Cloud Workflows | Motor de flujos que elija el cliente |
| Datos del proceso | Dataverse | Base de datos que elija el cliente (verificar) | Base de datos que elija el cliente (verificar) | Base de datos que elija el cliente |
| Aprobaciones | Acciones de aprobación del orquestador | Espera con token + experiencia propia | Devoluciones de llamada + experiencia propia | Tareas humanas del motor |
| Identidad y auditoría | Entra ID, auditoría de Dataverse | IAM, CloudTrail | IAM, registros de Cloud | Lo que configure el cliente |

Detalle, límites y estado de verificación en `perfiles/`.

## 6. Cómo comparar dos perfiles sin elegir por el cliente

1. Mapea los mismos `REQ-nn` contra cada perfil, en mapas separados.
2. Cuenta brechas por gravedad y opciones `to_verify`.
3. Presenta la comparación como insumo: "con A quedan estas brechas; con B, estas".
4. La elección la registra el cliente como decisión con alternativas, dueño, fecha y aprobación.
