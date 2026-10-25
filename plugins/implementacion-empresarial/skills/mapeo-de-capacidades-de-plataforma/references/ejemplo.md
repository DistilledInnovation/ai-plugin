# Ejemplo: Mapeo de capacidades en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `arquitectura-de-implementacion`: el plan de implementación de `FLU-01` tiene diez componentes (`CMP-01` a `CMP-10`), las decisiones `DEC-14` (orquestador determinístico) y `DEC-15` (IA acotada), pendientes `DEC-11`, `DEC-12`, `DEC-13`, `DEC-16` y `DEC-17`, y catorce requisitos `REQ-01` a `REQ-14`. La plataforma seguía por decidir (`DEC-09`). Habla el líder técnico del proveedor de TI externo; aprueba Valeria (directora).

## Turno 1

**Líder técnico:** Valeria quiere hacerlo en Microsoft, porque ya pagan Microsoft 365 para correo y documentos. Si el día de mañana se cambian a otra nube, ¿esto se pasa solo?

**Facilitador:** No: no hay conversión automática entre plataformas. Si la clínica cambia, se vuelve a mapear cada requisito y se vuelve a aprobar; lo que se conserva es el contrato y la arquitectura lógica. Para registrar la elección: ¿la decidió Valeria, y miraron alguna alternativa?

## Turno 2

**Líder técnico:** La decidió Valeria el 11 de diciembre. Miramos por encima AWS y una opción en un servidor propio, pero nadie en la clínica podría mantener un servidor.

**Facilitador:** Queda como `DEC-18`, con esas alternativas y la razón. Que las licencias actuales incluyan flujos con conectores premium, Dataverse y Copilot Studio es Dicho por participante: lo dejo como pendiente de verificar con el administrador de licencias, porque condiciona varias opciones. Usé el perfil `references/perfiles/microsoft.md` (verificado el 2026-10-25). El requisito más difícil es `REQ-08`, registrar la cita sin duplicados: ¿el sistema de gestión acepta algún identificador de operación al crear una cita, o permite consultar si ya existe antes de crearla?

## Turno 3

**Líder técnico:** Según el proveedor del sistema, tiene una interfaz de programación para crear y consultar citas, pero no acepta ningún identificador propio. No lo hemos probado.

**Facilitador:** Entonces hay brecha. Opciones: (A) escribir antes una constancia en una tabla de Dataverse con clave única paciente + horario y consultar la cita en el sistema antes de crearla; (B) dejar el registro como tarea humana tras la aprobación. A conserva el ahorro de tiempo pero no es una garantía del sistema de destino: una caída entre crear la cita y guardar la constancia deja un caso dudoso que va a revisión. Ambas quedan por verificar contra la interfaz real. ¿Quién decide entre A y B, y quién aprueba el mapeo?

## Turno 4

**Líder técnico:** Elegimos A con B como respaldo. Valeria aprueba todo el mapa; el lunes 14 revisa. Finalizar.

**Facilitador:** Entrego el mapa.

## Entregable: decisiones nuevas en el registro

| ID | Decisión | Alternativas consideradas | Dueño | Fecha | Aprobación | Procedencia | Toca |
|---|---|---|---|---|---|---|---|
| `DEC-18` | Plataforma: perfil Microsoft (Copilot Studio, Dataverse y Power Automate) | AWS; autoalojado (descartado: nadie en la clínica puede operarlo) | Valeria | 2026-12-11 | Aprobada por Valeria | Decisión | Todo el mapa |
| `DEC-19` | `REQ-08`: constancia con clave única en Dataverse + consulta previa en el sistema de gestión; respaldo: registro manual tras la aprobación | Solo registro manual; confiar en el sistema de destino | Proveedor de TI | 2026-12-11 | Pendiente (Valeria, 2026-12-14) | Recomendación | `FUT-08`, `AT-06`, `RIE-07` |

Pendiente por validar: licencias para conectores premium, Dataverse y Copilot Studio (administrador de licencias de la clínica, para 2026-12-14).

## Entregable: mapa de capacidades (resumen)

Mapa `MAP-FLU-01-MS`, perfil Microsoft (`DEC-18`), perfil verificado el 2026-10-25. Archivo completo: `assets/capability-map.yaml`.

| Requisito | Opción elegida | Ajuste | Verificación | Brecha | Dueño | Aprobación |
|---|---|---|---|---|---|---|
| `REQ-01` Orquestación durable | Flujo de nube de Power Automate (el agente con orquestación generativa se descartó: no es motor durable) | configuration | verified (límite de 30 días por ejecución) | Baja: casos de más de 30 días pasan a revisión antes de vencer | Proveedor de TI | Aprobado |
| `REQ-02` Esperas con tiempo máximo | Espera con vencimiento dentro del flujo | configuration | to_verify | Media: plazo (`DEC-11`) y hora del aviso (`DEC-16`) sin decidir | Proveedor de TI | Pendiente |
| `REQ-03` Estado del caso | Tabla de casos en Dataverse | configuration | to_verify | Ninguna | Proveedor de TI | Aprobado |
| `REQ-04` Modelo acotado | Propuesta: herramienta de prompt o servicio aprobado | configuration / custom_build | to_verify | Media: modelo permitido sin decidir | Proveedor de TI | Pendiente |
| `REQ-05` Aprobaciones | Acciones de aprobación del flujo | native | to_verify | Baja: rol aprobador depende de `DEC-13` | Jefa de recepción | Aprobado |
| `REQ-06` Identidad | Entra ID, roles de Dataverse, identidad de servicio | configuration | to_verify | Ninguna | Proveedor de TI | Aprobado |
| `REQ-07` Secretos | Variables de entorno de tipo secreto con Azure Key Vault | configuration | verified | Ninguna | Proveedor de TI | Aprobado |
| `REQ-08` Cita sin duplicados | Constancia con clave única + consulta previa (`DEC-19`) | custom_build | to_verify | **Media** (ver abajo) | Proveedor de TI | Pendiente |
| `REQ-09` Propuesta sin duplicados | Constancia de envío con clave | configuration | to_verify | Media: mensajería sin elegir (`DEC-17`) | Proveedor de TI | Pendiente |
| `REQ-10` Evidencia y auditoría | Tabla de evidencias + auditoría de Dataverse | configuration | verified | Baja: retención (`DEC-12`) | Administradora | Aprobado |
| `REQ-11` Modo manual | Interruptor en tabla de configuración | configuration | to_verify | Ninguna | Jefa de recepción | Aprobado |
| `REQ-12` Minimizar datos al modelo | Enmascarar documento y teléfono antes del modelo | custom_build | to_verify | Media: se decide en seguridad | Administradora | Pendiente |
| `REQ-13` Adaptador del sistema de gestión | Conector personalizado, solo operaciones del contrato | custom_build | to_verify | Media: interfaz sin confirmar | Proveedor de TI | Aprobado |
| `REQ-14` Pruebas de aceptación | Entorno de prueba separado con datos ficticios | configuration | to_verify | Baja | Proveedor de TI | Aprobado |

### La brecha de `REQ-08` en detalle

```yaml
- requirement_id: REQ-08
  description: "Registrar la cita sin duplicados aunque FUT-08 se repita (clave patient_id + slot_id)."
  category: idempotency
  source_refs: [FUT-08, AT-06, RIE-07, CMP-07]
  options:
    - {option_id: OPC-A, description: "Constancia en Dataverse con clave única patient_id + slot_id antes de llamar al sistema de gestión, más consulta previa de la cita.", fit: custom_build, verification: to_verify}
    - {option_id: OPC-B, description: "FUT-08 como tarea humana tras la aprobación.", fit: native, verification: verified}
  decision: {status: decided, chosen_option: OPC-A, rationale: "Conserva el ahorro de tiempo; OPC-B es el respaldo.", decision_ref: DEC-19}
  gap: {exists: true, description: "El sistema de destino no garantiza la idempotencia; una caída entre crear la cita y guardar la constancia deja un caso dudoso.", severity: medium, mitigation: "Casos dudosos a revisión (ST-09) y conciliación con la consulta previa."}
  owner: Proveedor de TI
  approval_status: pending
  acceptance_check: "AT-06: reintentar el registro no duplica la cita."
```

Lo que **no** se escribió: "Power Automate garantiza que no se dupliquen citas". La garantía depende del sistema de destino, que no la ofrece; la opción reduce el riesgo y deja visible lo que no cubre. El diseño detallado de reintentos y conciliación queda para `idempotencia-y-confiabilidad` (Próximamente).

## Entregable: checklist de validación del perfil

| Paso | Comprobación | Resultado |
|---|---|---|
| 1 | Cada requisito tiene opción con ajuste y verificación | Sí |
| 2 | Aprobaciones, esperas y reintentos fuera de la orquestación generativa | Sí (`DEC-14`) |
| 3 | Ninguna espera supera el límite de 30 días, o la brecha está decidida | Sí (`REQ-01`) |
| 4 | Estado y evidencias en tablas, no en el historial de ejecuciones | Sí (`REQ-03`, `REQ-10`) |
| 5 | Secretos solo en el almacén de secretos | Sí (`REQ-07`) |
| 6 | Cada efecto externo con aprobación previa y clave de idempotencia | Sí en el diseño; `REQ-08` y `REQ-09` pendientes de aprobación |
| 7 | Todo lo "(verificar)" verificado o como brecha con dueño | Sí: doce opciones `to_verify`, cada una con dueño |
| 8 | Pruebas de aceptación ejecutables con datos ficticios | Planeado (`REQ-14`) |
| 9 | **Aprobación del mapa completo** | **Pendiente**: Valeria aprobó nueve requisitos el 2026-12-14; quedan `REQ-02`, `REQ-04`, `REQ-08`, `REQ-09` y `REQ-12` |

**Siguiente paso sugerido:** `integracion-segura-y-aprobaciones`, porque `REQ-04` (modelo permitido) y `REQ-12` (minimizar datos) se deciden con el modelo de amenazas, y la matriz de aprobación cierra el rol aprobador de `REQ-05`.

## Lo que se ve en este ejemplo

- La plataforma la eligió Valeria y quedó registrada con sus alternativas; el facilitador no recomendó ninguna.
- La pregunta "¿se pasa solo a otra nube?" se respondió sin rodeos: no hay conversión automática entre plataformas.
- Los límites citados (30 días por ejecución, retención del historial, almacén de secretos, auditoría) están verificados con fecha; el resto va como `to_verify`.
- La brecha de `REQ-08` se presenta con lo que la opción no cubre, en vez de dar por resuelta la idempotencia.
- Ningún mapeo se construye en `pending`, y la aprobación del mapa completo sigue abierta con lo que falta.
