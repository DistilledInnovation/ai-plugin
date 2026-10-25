# Ejemplo: Operación y aseguramiento continuo en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `release-y-transferencia`: `REL-01` de `FLU-01` (agendar citas) salió a producción el 2027-01-18 (`DEC-36`), primero solo por formulario; el contrato está en madurez `production` (`DEC-37`); el soporte técnico lo da el proveedor de TI con un acuerdo escrito (`DEC-35`); el rollback tiene tres niveles (`DEC-34`). Pasaron a operación: la muestra semanal de lo aprobado (`TC-15`, `CTL-08`), las falsas alarmas de urgencia por encima del umbral (`MET-02`, dispensadas en `DEC-31`) y el valor en producción (`CA-07`). Metas del contrato (`RET-01`): de 6 a 3 minutos por solicitud y de unas 4 a 1 cita con error por cada 100. Revisión mensual del 2027-02-19; participan el líder técnico del proveedor de TI y la jefa de recepción.

## Turno 1

**Líder técnico:** Llevamos un mes en producción. Valeria quiere saber si funcionó.

**Facilitador:** Para responderle sin mezclar etapas, cada cifra tiene que decir de dónde sale. ¿Con qué cifras cuentan hoy y cómo se midieron: el tiempo por solicitud se cronometró en producción, o es el 3,4 del piloto?

## Turno 2

**Líder técnico:** La jefa cronometró 40 solicitudes la semana del 8 de febrero: 3,2 minutos en promedio. Entraron 318 solicitudes al flujo; 211 terminaron en cita confirmada, y la conciliación encontró 2 citas con error.

**Facilitador:** Entonces: 3,2 minutos es Hecho de producción (40 solicitudes, una semana), todavía por encima de la meta de 3; 2 citas con error en 211 (0,9 por cada 100) cumple la meta, pero con una muestra que todavía es chica. Ninguna de las dos se mezcla con el piloto. Para el costo por caso: ¿la factura del mes permite separar lo que consume este flujo, o hay que repartirla?

## Turno 3

**Líder técnico:** El proveedor de nube factura el consumo por servicio, y el modelo y la mensajería vienen separados. Las licencias de Microsoft 365 ya las pagaba la clínica.

**Facilitador:** Bien: sumo el consumo atribuible y dejo las licencias fuera, explicando por qué. El soporte del acuerdo es un monto fijo y lo informo aparte. Ahora lo que más enseña un mes de operación es la cola. Jefa, de lo que llegó a tu cola de revisión este mes, ¿qué fue lo que más se repitió?

## Turno 4

**Jefa de recepción:** Los controles de tratamiento, que el flujo no atiende, y pacientes que piden por el formulario y además llaman por teléfono. Por eso pasó lo de la cita doble del 3 de febrero.

**Líder técnico:** Y Valeria pregunta si nosotros podemos encargarnos de todo esto mes a mes. Finalizar.

**Facilitador:** Entrego la revisión del mes con el plan de operación.

## Entregable: plan de operación y revisión del período

Flujo: Agendar citas (`FLU-01`). Release vigente: `REL-01` (con `CAM-01` a `CAM-04`). En producción desde: 2027-01-18. Período: 2027-01-18 al 2027-02-19. Dueña del flujo: jefa de recepción. Soporte técnico: proveedor de TI (`DEC-35`). Aprueba: Valeria. Plan de operación aprobado por Valeria el 2027-01-18 (`DEC-38`).

### 1. Etapa y límites

| Etapa | Criterios verificables | ¿Rige hoy? |
|---|---|---|
| Piloto | Variante A, una recepcionista, dos semanas, cifras indicativas | No: cerrado el 2026-11-27 |
| Producción | `DEC-36` aprobada; dueños y suplentes; rollback ensayado; alertas con dueño; contrato en `production` (`DEC-37`) | **Sí** |
| Servicio gestionado | Acuerdo escrito que cubra informes mensuales, mejoras incluidas, recertificación a cargo del proveedor y disponibilidad acordada | **No**: hoy hay soporte técnico (`DEC-35`), no un servicio gestionado |

Valeria pidió que el proveedor "se encargue de todo mes a mes". Eso es un servicio gestionado y necesita un acuerdo nuevo que diga qué incluye; queda como `DEC-39`, Pendiente. Aunque se contrate, siguen siempre en la clínica: las decisiones del registro, las aprobaciones del día a día, los datos y el interruptor de modo manual.

| Actividad | Clínica | Proveedor de TI hoy (`DEC-35`) | Con un servicio gestionado (`DEC-39`, propuesta) |
|---|---|---|---|
| Cola de revisión y aprobaciones | Sí | — | — |
| Cola de errores, conciliación, rotación de secretos | Revisa | Ejecuta | Ejecuta |
| Informe mensual de KPIs y costo por caso | Hoy lo arma el proveedor sin acuerdo | No incluido | Incluido |
| Mejoras de configuración | Aprueba | No incluido | Un número de horas al mes |
| Recertificación | Responsable | No incluido | La ejecuta; la clínica aprueba |

### 2. Observabilidad y alertas

| ID | Alerta | Umbral | Llega a | Primera acción | Probada |
|---|---|---|---|---|---|
| `ALE-01` | Cola de revisión antigua | Un caso con más de 4 horas hábiles | Jefa de recepción | Asignar a la recepcionista de turno | Sí (ensayo) |
| `ALE-02` | Cola de errores antigua | Más de 2 horas hábiles | Proveedor de TI | Reprocesar con la misma clave | Sí |
| `ALE-03` | Diferencia de conciliación | Cualquiera | Jefa de recepción | Revisar la agenda; compensación del registro de idempotencia | Sí (`INC-02`) |
| `ALE-04` | Fallas del modelo | Más de 5 en una hora | Proveedor de TI | Revisar; si siguen, rollback nivel 1 | Sí |
| `ALE-05` | Tasa de escalamiento diaria | Más de 26 % | Jefa de recepción | Revisar la muestra del día; rollback nivel 1 si hay errores de lectura | Sí |
| `ALE-06` | Fallas de envío de la mensajería | Más de 3 en 15 minutos | Proveedor de TI y jefa de recepción | Pausar envíos; los casos esperan en revisión | Nueva (`MEJ-03`), aprobada, por publicar |

Las métricas no guardan datos de pacientes: cuentan casos por estado y por versión de reglas, plantillas e instrucciones.

### 3. KPIs de valor

| ID | Indicador | Línea base | Piloto | Meta | Producción | ¿Cumple? |
|---|---|---|---|---|---|---|
| `KPI-01` | Minutos de trabajo por solicitud (variante A) | 6 (`HAL-01`, 20 solicitudes de todas las variantes; Hecho) | 3,4 (20 solicitudes; piloto) | 3 | **3,2** (40 solicitudes cronometradas por la jefa, 2027-02-08 a 2027-02-12; Hecho) | No todavía |
| `KPI-02` | Citas con error por cada 100 | Unas 4 (`SUP-01`, Dicho por participante) | 1 en 94 (piloto) | 1 | **0,9** (2 en 211 citas confirmadas; conciliación y revisión de la jefa) | Sí, indicativo: muestra de un mes |
| `KPI-03` | Confirmación el mismo día | El mismo día (Dicho por participante) | — | No empeora | 203 de 211 (96 %) | Sí |
| `KPI-04` | Adopción: solicitudes que entran por el flujo | — | — | Sin meta | 318 de unas 820 solicitudes de cita del período (39 %); el resto, por teléfono (fuera de alcance) | — |

Resultados del período (Hecho, producción): 318 solicitudes; 272 de la variante A y 46 de las variantes B, C y D (28 de control de tratamiento), que fueron a revisión como prevé el contrato. De las 272: 211 citas confirmadas, 9 urgencias derivadas, 37 enviadas a revisión por baja certeza (13,6 %) y 15 sin respuesta del paciente al cierre.

**Calidad de IA en producción**

| Indicador | Cómo se mide | Resultado | Referencia |
|---|---|---|---|
| Solicitudes con algún dato corregido por recepción (`APR-04`) | Correcciones registradas en la bandeja | 17 de 272 (6 %); la mitad, el tipo de cita | `MET-01` (97 % en pruebas) |
| Urgencias perdidas | Muestra semanal de 20 casos revisada por la odontóloga (`TC-15`), 4 semanas | 0 de 80 | `MET-02` |
| Falsas alarmas de urgencia | La misma muestra | 28 % | Por debajo del 30 % del plan: la dispensa de `DEC-31` se cierra |
| Tasa de escalamiento | Casos de la variante A a revisión por baja certeza | 13,6 % | `MET-05` (13 % en pruebas) |
| Aprobado sin revisar de verdad (`RIE-04`) | Muestra semanal de 20 propuestas aprobadas, revisada por la jefa (`CTL-08`) | 1 error aprobado en 80 | Se sigue cada semana |

### 4. Costo por caso

| Componente | Monto del período | Atribución | Procedencia |
|---|---|---|---|
| Consumo de plataforma (flujo y tablas) | US$ 23 | Por servicio en la factura | Evidencia (factura de enero y febrero, prorrateada al período por el proveedor de TI) |
| Modelo | US$ 9 | Separado en la factura | Evidencia |
| Mensajería | US$ 29 | Separado en la factura | Evidencia |
| **Total atribuible** | **US$ 61** | | |
| **Costo por solicitud** | **US$ 0,19** (61 / 318) | | Cálculo |
| Licencias que la clínica ya pagaba | No se incluyen | Existían antes del flujo | Dicho por participante |
| Soporte técnico (`DEC-35`) | Monto fijo mensual, informado aparte | No depende del volumen | Evidencia (acuerdo) |
| Horas de recepción | 17 horas (318 × 3,2 minutos) frente a unas 32 con el proceso anterior (318 × 6 minutos) | | Inferencia: depende de que los 3,2 minutos de la muestra representen el mes |

### 5. Bitácora de cambios del período

| ID | Fecha | Tipo | Qué cambió | Aprueba | Pruebas repetidas | Antes → después | Estado |
|---|---|---|---|---|---|---|---|
| `CAM-01` | 2027-01-25 | Flujo | Se suman los mensajes (salida gradual cumplida: semana 1 sin incidentes altos) | Valeria (plan de `DEC-36`) | — (probado en `EVP-FLU-01`) | Formulario → formulario y mensajes | Publicado |
| `CAM-02` | 2027-02-05 | Emergencia (después de `INC-02`) | Disparador del rollback nivel 3: "una cita duplicada **creada por el flujo**" | Valeria (propuso la jefa de recepción) | Ensayo de lectura del runbook | `DEC-34` v1 → v2 | Publicado |
| `CAM-03` | 2027-02-08 | Plantillas | Propuesta con "llegue 10 minutos antes" | Valeria (propuso la jefa de recepción, matriz de `DEC-22`) | `TC-01`, `TC-06`, `TC-10` (`EVI-14`) | v2 → v3 | Publicado |
| `CAM-04` | 2027-02-15 | Reglas | Reglas de agenda de febrero | Valeria (propuso la jefa) | `TC-01`, `TC-05` (`EVI-15`) | v1 → v2 | Publicado |

### 6. Incidentes

| ID | Fecha | Qué pasó | Casos | Qué se hizo | Causa | Dueño | Mejora |
|---|---|---|---|---|---|---|---|
| `INC-01` | 2027-01-27 | La mensajería no respondió de 10:10 a 12:05 | 14 propuestas fallidas o inciertas | Fueron a revisión; recepción confirmó con 3 pacientes antes de reenviar las inciertas; ningún duplicado (`IDM-04`) | Falla del servicio de mensajería (Evidencia: aviso del servicio) | Proveedor de TI | `MEJ-03` |
| `INC-02` | 2027-02-03 | La conciliación encontró una cita doble | 1 | La jefa verificó en 20 minutos que la otra cita se había agendado a mano por teléfono, fuera del flujo; anuló la sobrante y se envió un mensaje de aclaración aprobado. No activó el nivel 3: el flujo no la creó | Duplicado de negocio entre canales | Jefa de recepción | `MEJ-02`, `CAM-02` |

El acompañamiento reforzado se cerró el 2027-02-01: diez días hábiles sin incidentes altos (`INC-01` fue de severidad media).

### 7. Recertificación

| Elemento | Qué se revisa | Responsable | Próxima fecha |
|---|---|---|---|
| Calidad de IA | `DS-01` a `DS-05` con las versiones vigentes, más 30 solicitudes recientes anonimizadas con autorización de la administradora | Proveedor de TI; aprueban Valeria y la administradora | 2027-04-19 |
| Permisos | Revisión trimestral (`DEC-23`) | Administradora | 2027-04-19 |
| Secretos | Rotación semestral (`DEC-33`) | Proveedor de TI | 2027-07-13 |
| Retención y auditoría | `DEC-12`, `DEC-25` | Administradora | 2027-04-19 |
| Perfil de plataforma | Volver a verificar lo que se usó del perfil Microsoft (verificado el 2026-10-25), con fecha nueva | Proveedor de TI | 2027-04-19 |
| Contrato | Describe lo que de verdad ocurre | Jefa de recepción | 2027-04-19 |
| Acuerdo de soporte | Vigencia de seis meses (`DEC-35`) y decisión de servicio gestionado (`DEC-39`) | Valeria | 2027-04-19 |

### 8. Backlog de mejoras

| ID | Mejora | Evidencia | Impacto esperado | Va a | Dueño | Estado |
|---|---|---|---|---|---|---|
| `MEJ-01` | Atender la variante B (control de tratamiento) | 28 de 46 casos fuera de alcance en la cola | Menos trabajo manual en la cola | **`disenar-proceso-futuro`**: reabre los datos que pide la variante B (`DEC-06`) y vuelve por la cadena hasta el contrato | Jefa de recepción | Propuesta |
| `MEJ-02` | Pacientes que piden por formulario y además llaman | `INC-02`; casos en la cola | Menos duplicados de negocio | **`disenar-proceso-futuro`**: el teléfono está fuera del flujo; decidir cómo se registra una llamada en la misma lista | Jefa de recepción | Propuesta |
| `MEJ-03` | Alerta específica de la mensajería | `INC-01` | Detectar la caída en minutos | Control de cambios (`ALE-06`) | Proveedor de TI | Aprobada, por publicar |
| `MEJ-04` | Campo "tipo de cita" con opciones en el formulario | La mitad de las correcciones de `APR-04`; `KPI-01` | Acercar `KPI-01` a 3 minutos | Control de cambios (formulario v3), con la regresión de `TC-01` y `TC-27` | Jefa de recepción | Propuesta |
| `MEJ-05` | Reagendar y cancelar (`FLU-02`) | 19 pedidos en la cola del mes | Flujo nuevo | `disenar-proceso-futuro` para `FLU-02`, fuera del alcance de `FLU-01` | Valeria | Para priorizar |

### 9. Decisiones y pendientes

| ID | Decisión o pendiente | Dueño | Fecha | Aprobación |
|---|---|---|---|---|
| `DEC-38` | Plan de operación: alertas `ALE-01` a `ALE-05`, revisión mensual de KPIs, muestra semanal (`TC-15`) y recertificación trimestral | Valeria | 2027-01-18 | Aprobada |
| `DEC-39` | ¿Servicio gestionado del proveedor de TI? Requiere un acuerdo con las filas de la sección 1 | Valeria | Para la recertificación del 2027-04-19 | Pendiente |
| `DEC-40` | `CA-07`: la meta de errores se cumple (indicativo); la de tiempo no, se vuelve a medir cuatro semanas después de `MEJ-04` | Valeria | 2027-02-19 | Aprobada |

**Siguiente paso sugerido:** `disenar-proceso-futuro` (Automatización con IA) para `MEJ-01` y `MEJ-02`, con la evidencia de este mes; `MEJ-03` y `MEJ-04` siguen por el control de cambios, y esta skill vuelve en la revisión de marzo.

## Lo que se ve en este ejemplo

- Cada cifra dice si es de la línea base, del piloto o de producción, con su muestra; 3,2 minutos no se redondeó a "meta cumplida".
- El costo por caso usa la factura del cliente, dice qué incluye y deja fuera, con su razón, las licencias que ya existían.
- La muestra semanal que no se podía probar antes de salir se hizo en operación y cerró la dispensa de falsas alarmas.
- Un incidente reveló un disparador de rollback mal escrito; se corrigió con la bitácora, no de palabra.
- Las mejoras que cambian el diseño (variante B, el teléfono) vuelven a `disenar-proceso-futuro`; las de configuración van al control de cambios.
- "Que se encarguen de todo" se separó del soporte actual: un servicio gestionado requiere un acuerdo con criterios verificables, y las decisiones siguen en la clínica.
