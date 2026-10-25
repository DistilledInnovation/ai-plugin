# Rutas de implementación, revisión del contrato y puerta de entrada

Nota de fuente: las etapas C (implementar y transferir) y D (medir y mejorar), el contrato portable, el mapa de backends y los criterios de gobernanza provienen de la oferta empresarial de Distilled Innovation; las rutas, la lista de revisión y el registro de decisiones son una adaptación de este plugin.

## 1. Qué es el `workflow-contract` y por qué manda

El `workflow-contract` es la especificación portable del flujo que entrega `plan-piloto-y-especificacion` (plugin Automatización con IA), validada contra `workflow-contract.schema.json` (JSON Schema Draft 2020-12, un formato estándar para describir y validar estructuras de datos). Describe **qué hace** el flujo: actores, estados, pasos, disparadores, entradas y salidas, reglas, niveles de autoridad, guardrails, políticas de aprobación, idempotencia (qué pasa si un paso se ejecuta dos veces), evidencias, métricas y pruebas de aceptación. No dice **con qué** se construye.

Es la fuente de verdad de la implementación: lo que el contrato dice no se reinterpreta en silencio. Si la plataforma obliga a cambiar algo (por ejemplo, un tiempo de espera máximo), el cambio se registra como decisión y lo aprueba el dueño del contrato.

**Advertencia de portabilidad:** la definición es portable; la ejecución no tiene por qué ser idéntica en cada plataforma (transacciones, identidad, tiempos de espera, orquestación, costos y comportamiento del modelo). No hay conversión automática entre plataformas.

## 2. Lista de revisión del contrato

| Comprobación | Pasa si | Si no pasa |
|---|---|---|
| Claves obligatorias | Están `workflow_id`, `version` ("1.0"), `actors`, `states`, `steps`, `approval_policies` y `evidence_requirements` | Volver a `plan-piloto-y-especificacion` |
| Pasos completos | Cada paso tiene `trigger`, `inputs`, `outputs`, `success_state`, `failure_state`, `idempotency` y `evidence` | Volver al diseño con los pasos señalados |
| Referencias | Cada actor, estado, política y evidencia citada existe | Corregir con el dueño del contrato |
| Efectos externos | Todo paso con `external_effect: true` tiene `approval_policy` e idempotencia distinta de `not_applicable` | No se implementa ese paso hasta corregirlo |
| Caminos sin salida | Cada paso alcanza un estado de éxito o de falla; las ramas están declaradas | Corregir con el dueño del contrato |
| Valores "por definir" | Están identificados | Cada uno entra al registro de decisiones |
| Datos | Sin credenciales, direcciones reales ni datos personales; las entradas y salidas tienen sensibilidad | Quitar y avisar al dueño |
| Madurez | `pilot` o `production` para implementar en serio; `design` o `prototype` solo para arquitectura provisional | Registrar la limitación |

Un contrato con observaciones menores puede seguir si el dueño acepta corregirlas; queda como decisión con fecha.

## 3. Cómo leer la puerta de entrada a la etapa C

`plan-piloto-y-especificacion` evalúa la puerta con tres resultados posibles:

| Resultado | Qué se puede hacer |
|---|---|
| Pasa | Ruta completa |
| Pasa con condiciones | Ruta completa; cada condición entra al registro con dueño y fecha, y las que bloquean producción se revisan antes de `release-y-transferencia` |
| No pasa todavía | Solo arquitectura lógica provisional, marcada como tal; nada se construye ni se conecta a sistemas reales |

La puerta la decide quien tiene autoridad (rol del cliente), no el facilitador ni el equipo técnico.

## 4. Rutas en detalle

| Ruta | Cuándo | Recorrido | Qué no se hace |
|---|---|---|---|
| Volver al diseño | No hay contrato o no pasa la revisión | `plan-piloto-y-especificacion` | No se completa el contrato inventando pasos |
| Completa | Contrato listo; plataforma por decidir | Arquitectura → mapeo (el cliente elige plataforma) → seguridad e idempotencia → pruebas → release → operación | No se propone una plataforma "por defecto" |
| Completa con plataforma dada | El cliente ya opera una plataforma o tiene una restricción | Igual que la completa; la elección se registra como decisión con dueño | La arquitectura no se dibuja con productos: sigue siendo lógica |
| Revisión puntual | Hay una implementación y se pide revisar seguridad y aprobaciones | Reconstruir contrato y arquitectura mínima → `integracion-segura-y-aprobaciones` | No se aprueba una implementación sin contrato |
| Cambio controlado | Un flujo en operación necesita un cambio | Cambio al contrato con su dueño → skills afectadas → pruebas | No se cambia la plataforma sin pasar por el contrato |

## 5. Qué entra al registro de decisiones

| Tipo | Ejemplos | Quién suele decidir |
|---|---|---|
| Ruta y alcance | Ruta elegida, alcance de producción, qué variantes entran | Dueño del flujo |
| Plataforma | Perfil elegido (Microsoft, AWS, Google, autoalojado u otro) | Cliente (dirección o TI del cliente) |
| Arquitectura | Orquestador determinístico, límites de componentes, IA acotada | Equipo técnico, aprobado por el dueño |
| Mapeos | Cada requisito: opción elegida, brecha y cómo se cierra | Equipo técnico, aprobado por el cliente |
| Valores del cliente | Plazos, umbrales, retención, horarios, aprobadores suplentes | Dueño del proceso o responsable de datos |
| Seguridad | Modelos permitidos, datos que pueden salir, roles, acceso a secretos | Responsable de datos o de seguridad |
| Cambios al contrato | Ajustes que pide la plataforma | Dueño del contrato |

## 6. Glosario breve

| Término | En una línea |
|---|---|
| Orquestador determinístico | Componente que ejecuta los pasos en un orden fijo, guarda el estado y maneja esperas, reintentos y aprobaciones de forma predecible |
| Orquestación generativa | Un modelo de IA decide en el momento qué herramienta o tema usar; útil en la conversación, no es un motor durable |
| Idempotencia | Ejecutar dos veces la misma operación produce el mismo efecto que una sola vez |
| Mínimo privilegio | Cada componente y cada persona tiene solo los permisos que necesita |
| Perfil de plataforma | Guía de capacidades y preguntas de adaptación para una plataforma; no es un generador ni una promesa de equivalencia |
