# Ejemplo: Pruebas y evaluación en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `idempotencia-y-confiabilidad`: `FLU-01` (agendar citas) tiene contrato con seis pruebas de aceptación (`AT-01` a `AT-06`), mapa `MAP-FLU-01-MS` en la plataforma Microsoft (`DEC-18`), diez controles de seguridad (`CTL-01` a `CTL-10`), un registro de idempotencia con ocho operaciones (`IDM-01` a `IDM-08`) y once pruebas de resiliencia (`RES-01` a `RES-11`), y el cambio de reintentos `DEC-26`. Según el registro de decisiones, la jefa de recepción ya fijó el plazo de espera (`DEC-11`: 48 horas) y la hora del aviso (`DEC-16`: 18:00), y Valeria eligió la mensajería institucional (`DEC-17`, 2026-12-21). Las decisiones llegaron hasta `DEC-28`. Habla el líder técnico del proveedor de TI.

## Turno 1

**Líder técnico:** Con el registro de idempotencia listo, ¿cómo probamos todo esto antes de salir?

**Facilitador:** Ya hay mucho escrito para probar: seis pruebas de aceptación del contrato, diez controles con su prueba y once pruebas de resiliencia; falta decidir contra qué se aprueba. ¿Quién firma que el flujo está listo para producción, y qué necesita ver para firmarlo?

## Turno 2

**Líder técnico:** Firma Valeria. La administradora dijo que ella quiere ver con sus ojos que ningún documento ni teléfono llega al modelo.

**Facilitador:** Entonces fijo los criterios antes de probar y separados por etapa. El del piloto (3 minutos o menos por solicitud) no se cumplió y Valeria lo dispensó en `DEC-08`: queda así, sin reescribirlo. Para producción propongo cinco criterios adicionales, uno por categoría y uno de operación, con la administradora como coaprobadora de seguridad y calidad de IA. La meta de valor (3 minutos y 1 cita con error por cada 100) se mide en producción y no bloquea la salida. Para medir la IA hacen falta solicitudes ficticias con su respuesta correcta, y esa respuesta no la puede escribir quien construye. ¿La escriben la jefa de recepción para los datos y el tipo de cita, y la odontóloga coordinadora clínica para las urgencias?

## Turno 3

**Líder técnico:** Sí, las dos. La odontóloga pidió una cosa: que ninguna urgencia se escape, aunque haya falsas alarmas.

**Facilitador:** Queda como umbral de `MET-02`: 12 de 12 urgencias marcadas, con hasta 30 % de falsas alarmas, porque una persona decide igual (`GRD-05`). Para la extracción de `FUT-01`, recepción revisa los datos antes de usarlos (`APR-04`), así que el umbral puede ser menos estricto. ¿Qué porcentaje de campos correctos le parece aceptable a la jefa de recepción?

## Turno 4

**Líder técnico:** Ella dice 95 %: con menos, corrige más de lo que corregía antes. Corremos la primera semana de enero. Finalizar.

**Facilitador:** Entrego el plan; lo actualizo con los resultados de la corrida.

## Entregable: plan de evaluación (resumen)

Plan `EVP-FLU-01`, etapa objetivo `production`. Archivo completo: `assets/evaluation-plan.yaml` (valida contra `assets/evaluation-plan.schema.json`). Entorno de prueba separado, datos ficticios. Plan y criterios aprobados por Valeria el 2026-12-22 (`DEC-29`).

**Categorías:** `functional`, `security`, `resilience`, `ai_quality`.

**Conjuntos de datos (todos ficticios)**

| ID | Contenido | Casos | Etiqueta |
|---|---|---|---|
| `DS-01` | Variante A por mensaje y formulario, con faltas y datos incompletos | 60 | Jefa de recepción |
| `DS-02` | Variantes B, C y D | 20 | Jefa de recepción |
| `DS-03` | Motivos de consulta, 12 urgencias, cada uno en dos o tres formas de escribir | 40 | Odontóloga coordinadora clínica |
| `DS-04` | Instrucciones ocultas | 10 | Administradora |
| `DS-05` | Documentos y teléfonos en formatos raros | 15 | Administradora |
| `DS-06` | Fichas, agenda y citas del sistema de gestión de prueba | 50 | Jefa de recepción |

**Métricas de calidad de IA**

| ID | Métrica | Umbral | Conjunto |
|---|---|---|---|
| `MET-01` | Exactitud de `FUT-01` | 95 % o más de campos correctos (Decisión de la jefa de recepción) | `DS-01` |
| `MET-02` | Exactitud de urgencias en `FUT-04` | 12 de 12 marcadas; falsas alarmas hasta 30 % (Decisión de la odontóloga) | `DS-03` |
| `MET-03` | Fundamentación en la evidencia | 100 %: ningún dato inventado | `DS-01` |
| `MET-04` | Consistencia estructural | 100 % de salidas válidas o enviadas a revisión | `DS-01` |
| `MET-05` | Tasa de escalamiento | 20 % o menos en `DS-01`; 100 % en `DS-02` | `DS-01`, `DS-02` |
| `MET-06` | Sesgo por forma de escribir | La misma marca en 95 % o más de las versiones | `DS-03` |
| `MET-07` | Errores de extracción sin aviso | 2 o menos de 60 | `DS-01` |
| `MET-08` | Selección de herramientas | No aplica: la IA no tiene herramientas (`DEC-15`) | — |
| `MET-09` | Relevancia | No aplica: los mensajes al paciente usan plantillas fijas | — |

**Criterios de aceptación**

| ID | Etapa | Criterio | Aprueba |
|---|---|---|---|
| `CA-01` | Piloto | 3 minutos o menos por solicitud: **dispensado** (`DEC-08`, el piloto dio 3,4) | Valeria |
| `CA-02` | Producción | Funcional: `AT-01`, `AT-04`, `AT-05` y las ramas del contrato | Valeria |
| `CA-03` | Producción | Seguridad: cada control probable antes de producción pasa su prueba negativa | Valeria y administradora |
| `CA-04` | Producción | Resiliencia: `RES-01` a `RES-11`, ningún duplicado | Valeria |
| `CA-05` | Producción | Calidad de IA: `MET-01` a `MET-07` con la versión que se publica | Valeria y administradora |
| `CA-06` | Producción | Operación: modo manual y alertas con dueño | Jefa de recepción |
| `CA-07` | Producción (valor) | 3 minutos y 1 de cada 100, en las primeras cuatro semanas; no bloquea la salida | Valeria |

**Casos:** 30 (`TC-01` a `TC-30`): 6 funcionales, 9 de seguridad, 11 de resiliencia y 4 de calidad de IA; 9 positivos y 21 negativos.

**Trazabilidad requisito → prueba (resumen)**

| Elemento | Casos | Brecha |
|---|---|---|
| `AT-01` a `AT-06` | `TC-01`, `TC-07`, `TC-28`, `TC-03`, `TC-04`, `TC-19` | Ninguna |
| `CTL-01` a `CTL-10` | `TC-07` a `TC-14`, `TC-30` | `CTL-08` (muestra semanal de lo aprobado) solo se puede hacer con casos reales: `TC-15` pasa a operación con la jefa de recepción como dueña |
| `RES-01` a `RES-11` | `TC-03`, `TC-16` a `TC-25` | Ninguna |
| `REQ-01` a `REQ-14` | Cada `acceptance_check` del mapa tiene caso (`REQ-14` es el entorno mismo) | Ninguna |
| Métricas del contrato | Tiempo por solicitud y citas con error: `CA-07` | Se miden en producción |

## Actualización tras la corrida (2027-01-04 a 2027-01-08)

### Registro de evidencia de pruebas (extracto)

Versiones: flujo 0.3 (0.4 tras `DEF-01`), reglas de agenda v1 (enero), plantillas v1, instrucciones del modelo v1 (v2 tras `DEF-02`), modelo candidato de `REQ-04`. Evidencia guardada en la carpeta de evidencias del entorno de prueba, con capturas y el registro de cada caso.

| ID | Fecha | Casos | Resultado | Ejecutó | Observación | Defecto |
|---|---|---|---|---|---|---|
| `EVI-01` | 2027-01-04 | `TC-01` a `TC-03`, `TC-12` | Pasó | Proveedor de TI; aprobaciones de dos recepcionistas | Recorrido completo en 6 minutos de reloj; aprobaciones con identidad personal | — |
| `EVI-02` | 2027-01-04 | `TC-04` | Pasó | Proveedor de TI | 20 de 20 a la cola de revisión | — |
| `EVI-03` | 2027-01-05 | `TC-05`, `TC-06`, `TC-26` | Pasó | Proveedor de TI y jefa de recepción | Aviso a las 18:00; apagado inmediato; encendido sin la jefa rechazado | — |
| `EVI-04` | 2027-01-05 | `TC-07`, `TC-08`, `TC-30` | Pasó | Proveedor de TI; la administradora revisó lo enviado al modelo | Ningún documento ni teléfono en el registro de llamadas | — |
| `EVI-05` | 2027-01-05 | `TC-09` a `TC-11`, `TC-13` | Pasó | Proveedor de TI y administradora | Borrado e historia clínica rechazados por permisos | — |
| `EVI-06` | 2027-01-06 | `TC-16`, `TC-17` | Pasó | Proveedor de TI | Tres intentos registrados en `TC-17` | — |
| `EVI-07` | 2027-01-06 | `TC-18`, `TC-19`, `TC-20` | **Falló** `TC-20` | Proveedor de TI | `TC-18`: la mensajería no permite consultar el estado de un envío (Evidencia): el envío incierto va a revisión, como prevé `IDM-04`. `TC-20`: al simular el tiempo agotado se crearon **dos** citas | `DEF-01` |
| `EVI-08` | 2027-01-07 | `TC-22` a `TC-25` | Pasó | Proveedor de TI | — | — |
| `EVI-09` | 2027-01-07 | `TC-20`, `TC-21` (regresión) | Pasó | Proveedor de TI | Con flujo 0.4: una sola cita; ninguna acción con efecto externo reintenta sola | — |
| `EVI-10` | 2027-01-07 | `TC-14` | Pasó tras corregir | Proveedor de TI | El límite actuó, pero la alerta no llegaba a la jefa; corregido el destinatario | `DEF-03` |
| `EVI-11` | 2027-01-08 | `TC-27` | Pasó con instrucciones v2 | Proveedor de TI | v1: `MET-01` 91 % (tipo de cita confundido entre limpieza y control). v2: 97 % | `DEF-02` |
| `EVI-12` | 2027-01-08 | `TC-28`, `TC-29`, `TC-07` (regresión v2) | Pasó | Proveedor de TI; la odontóloga revisó las marcas | 12 de 12 urgencias; 9 falsas alarmas de 28 (32 % → ver nota); `MET-06` 96 % | — |

Nota sobre `EVI-12`: las falsas alarmas dieron 32 %, por encima del 30 % acordado. No se movió el umbral en silencio: la odontóloga revisó los 9 casos, dijo que 3 eran dudosos de verdad y propuso dejarlos como falsas alarmas aceptables; Valeria dispensó ese punto con la razón por escrito (`DEC-31`), y la tasa se vuelve a revisar en operación.

### Métricas de calidad de IA (resultado)

| Métrica | Umbral | Resultado | Cumple |
|---|---|---|---|
| `MET-01` | 95 % | 97 % (v2) | Sí |
| `MET-02` | 12 de 12; falsas alarmas hasta 30 % | 12 de 12; 32 % | Sí en urgencias; falsas alarmas dispensadas (`DEC-31`) |
| `MET-03` | 100 % | 100 % | Sí |
| `MET-04` | 100 % | 100 % (3 salidas rotas simuladas, las 3 a revisión) | Sí |
| `MET-05` | 20 % o menos; 100 % en `DS-02` | 13 %; 100 % | Sí |
| `MET-06` | 95 % | 96 % | Sí |
| `MET-07` | 2 o menos de 60 | 1 | Sí |

### Defectos

| ID | Descripción | Dueño | Corrección | Aprobación | Nueva corrida | Estado |
|---|---|---|---|---|---|---|
| `DEF-01` | La acción que crea la cita tenía activa la política de reintentos por defecto; con el tiempo agotado repitió la creación (`RIE-09` confirmado) | Proveedor de TI | Reintentos desactivados de forma explícita en las acciones con efecto externo (flujo 0.4) | No requiere: ajusta la configuración al contrato | `EVI-09` | Cerrado |
| `DEF-02` | Exactitud de 91 % por confusión entre tipos de cita | Proveedor de TI | Instrucciones v2 con la lista de tipos de cita de las reglas de agenda | `DEC-30`: Valeria y la administradora (matriz de `DEC-22`), con `TC-07` y `TC-28` repetidas | `EVI-11`, `EVI-12` | Cerrado |
| `DEF-03` | La alerta del límite por contacto no llegaba a la jefa | Proveedor de TI | Destinatario corregido | No requiere | `EVI-10` | Cerrado |

### Decisiones nuevas

| ID | Decisión | Dueño | Fecha | Aprobación |
|---|---|---|---|---|
| `DEC-29` | Plan `EVP-FLU-01` y criterios `CA-01` a `CA-07` | Valeria | 2026-12-22 | Aprobada |
| `DEC-30` | Instrucciones del modelo v2 (lista de tipos de cita) | Valeria y administradora | 2027-01-07 | Aprobada, con regresión `EVI-12` |
| `DEC-31` | Puerta de pruebas aprobada: `CA-02` a `CA-06` cumplidos; falsas alarmas de `MET-02` en 32 % dispensadas con revisión en operación; `TC-15` pasa a operación | Valeria, con la administradora en `CA-03` y `CA-05` | 2027-01-11 | Aprobada |

Con `TC-11`, `TC-19` y `TC-20` en verde, el proveedor de TI marcó como verificadas las opciones de `REQ-08` y `REQ-13`, y Valeria las aprobó en el mapa el 2027-01-08 (junto con `DEC-19`).

**Lo que la puerta de pruebas no decide:** la salida a producción. Siguen abiertos `DEC-21` (modelo permitido con datos reales), `DEC-24` (revisión legal), `DEC-12` y `DEC-25` (retención) y la autorización de datos reales (`DEC-08`).

**Siguiente paso sugerido:** `release-y-transferencia`, para preparar la salida con dueños, aprobación y rollback probado, y cerrar las decisiones que todavía la bloquean.

## Lo que se ve en este ejemplo

- Los criterios se fijaron antes de probar y por etapa; el del piloto quedó como dispensado, sin reescribirlo.
- Las respuestas esperadas las escribieron la jefa de recepción y la odontóloga, no el proveedor que construye.
- Dos métricas no aplicaban y se dijo por qué, en vez de omitirlas.
- La prueba de resiliencia encontró el duplicado que el registro de idempotencia había previsto como riesgo; se corrigió y se volvió a correr.
- El cambio de instrucciones pasó por la matriz de aprobación y repitió las pruebas de seguridad y urgencias.
- Un umbral no alcanzado (falsas alarmas) se dispensó con decisión y razón, no moviendo la cifra.
- La puerta de pruebas se separó de la salida a producción, que todavía tiene decisiones abiertas.
