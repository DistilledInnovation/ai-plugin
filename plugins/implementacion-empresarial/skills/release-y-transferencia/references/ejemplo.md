# Ejemplo: Release y transferencia en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `pruebas-y-evaluacion`: el plan `EVP-FLU-01` de `FLU-01` (agendar citas) tiene su puerta de pruebas aprobada por Valeria el 2027-01-11 (`DEC-31`), con las versiones flujo 0.4, reglas de agenda v1 (enero), plantillas v1 e instrucciones del modelo v2 (`DEC-30`). `TC-15` (muestra semanal de lo aprobado) y `CA-07` (valor en producción) pasaron a operación. Siguen abiertas, según el registro: `DEC-12` y `DEC-25` (retención), `DEC-20` y `DEC-21` (datos y modelo permitido), `DEC-24` (revisión legal), la autorización de datos reales (condición de `DEC-08`) y la rotación de secretos. La clínica no tiene equipo de TI: el proveedor de TI externo construyó el flujo. Participan el líder técnico del proveedor y, desde el turno 3, la jefa de recepción.

## Turno 1

**Líder técnico:** Valeria aprobó la puerta de pruebas el lunes. ¿Lo declaramos listo y salimos el lunes 18?

**Facilitador:** Todavía no: la puerta de pruebas dice que el flujo funciona en el entorno de prueba, no que se puede operar con datos reales. En el registro hay decisiones que bloquean la salida: modelo permitido y datos hacia él (`DEC-20`, `DEC-21`), revisión legal (`DEC-24`), retención (`DEC-12`, `DEC-25`), autorización de datos reales y rotación de secretos. ¿Cuáles de ellas ya se cerraron?

## Turno 2

**Líder técnico:** El 12 la administradora aprobó el modelo con la evidencia del contrato con el proveedor de nube (`DEC-20` y `DEC-21`) y autorizó los datos reales. El asesor legal entregó su revisión el mismo día con dos condiciones: avisar a los pacientes cómo se tratan sus datos, en el formulario y en el primer mensaje, y guardar las evidencias dos años. La administradora fijó esa retención. La de las claves y la rotación de secretos las cerramos mañana.

**Facilitador:** Registrado. La condición legal cambia el formulario y la plantilla de la propuesta, así que lo que saldría ya no es lo que se probó: el cambio de plantilla lo propone el proveedor y lo aprueba la jefa de recepción (matriz de `DEC-22`), y se repiten `TC-01`, `TC-06` y `TC-10` antes de salir. Ahora el rollback: volver atrás de forma controlada si algo sale mal. Si el primer día algo sale mal, ¿quién decide volver atrás, y con qué señal?

## Turno 3

**Jefa de recepción:** Yo. Si veo una cita duplicada o un mensaje con datos de otro paciente, apago todo.

**Facilitador:** "Apagar todo" tiene tres niveles y conviene usar el justo. Si falla la lectura o la marca de urgencia, nivel 1: apagas la parte con IA y todo va a tu cola. Si un cambio reciente de reglas, plantillas o instrucciones empeora las cosas, nivel 2: se restaura la versión anterior aprobada. Si sale algo equivocado hacia un paciente (una cita duplicada, datos de otra persona), nivel 3: se desactiva el flujo y recepción trabaja como antes del piloto, con los casos en curso en tu cola. Los niveles 1 y 3 los decides tú, sin pedir permiso. Un rollback que no se ensayó no cuenta. ¿Podemos ensayar los tres niveles el miércoles en el entorno de prueba, con tus dos recepcionistas?

## Turno 4

**Jefa de recepción:** El miércoles, sí.

**Líder técnico:** Y después de salir, el soporte lo damos nosotros, como hasta ahora.

**Facilitador:** "Como hasta ahora" no es un acuerdo: la clínica necesita saber qué incluye, en qué horario y en cuánto tiempo responden según la gravedad. Lo dejo como `DEC-35`, para que Valeria lo firme junto con la salida. ¿Qué día revisa Valeria la checklist completa?

**Líder técnico:** El viernes 15. Finalizar.

**Facilitador:** Entrego la preparación de release; la actualizo con el ensayo y la revisión del viernes.

## Entregable: preparación de release

Flujo: Agendar citas (`FLU-01`). Release: `REL-01`. Plan de evaluación: `EVP-FLU-01`. Salida prevista: 2027-01-18. Prepara: líder técnico del proveedor de TI. Aprueba la salida: Valeria (directora).

**Estado al 2027-01-11: No listo.** Falta: cerrar `DEC-25` y la rotación de secretos, probar la plantilla con el aviso legal, ensayar el rollback, firmar el acuerdo de soporte y la aprobación de salida.

### 1. Qué se libera

| Elemento | Se libera | Probado | ¿Coinciden? | Aprobación y regresión |
|---|---|---|---|---|
| Definición del flujo | 0.4 | 0.4 | Sí | — |
| Reglas de agenda | v1 (enero) | v1 | Sí | — |
| Plantillas | **v2** (aviso de tratamiento de datos) | v1 | **No** | Jefa de recepción, 2027-01-13; regresión `EVI-13` |
| Formulario de entrada | v2 (mismo aviso) | v1 | **No** | Idem; `TC-01` con el formulario nuevo |
| Instrucciones del modelo | v2 | v2 | Sí | `DEC-30` |
| Modelo | El aprobado en `DEC-21` | El candidato de `REQ-04` | Sí (es el mismo) | `DEC-21` |
| Configuración | Reintentos explícitos (`DEF-01`), alertas, interruptor | Idem | Sí | — |

### 2. Entradas

| Entrada | Estado | Referencia |
|---|---|---|
| Puerta de pruebas | Aprobada | `DEC-31` |
| Datos y modelo permitido | Cerradas el 2027-01-12 | `DEC-20`, `DEC-21` (administradora) |
| Revisión legal y de cumplimiento | Entregada el 2027-01-12, con dos condiciones | `DEC-24`; aviso: `DEC-32`; retención: `DEC-12` |
| Retención de evidencias | Dos años (condición legal) | `DEC-12` (administradora, 2027-01-12) |
| Retención de claves | Cerrada el 2027-01-13 | `DEC-25` (administradora) |
| Autorización de datos reales | Concedida el 2027-01-12 | Condición de `DEC-08` (administradora) |
| Reglas de agenda de enero escritas | Sí | Condición de `DEC-08`; reglas v1 |
| Rotación de secretos | Cada seis meses; la ejecuta el proveedor de TI | `DEC-33` (administradora, 2027-01-13) |
| Pendientes que pasan a operación | `TC-15` (muestra semanal), `CA-07` (valor), revisión trimestral de permisos (`DEC-23`) | Dueñas: jefa de recepción y administradora |

### 3. Dueños

| Qué | Dueño | Suplente | Del cliente o tercero |
|---|---|---|---|
| Proceso, reglas y plantillas | Jefa de recepción | Valeria | Cliente |
| Datos, retención y auditoría | Administradora | Valeria | Cliente |
| Aprobaciones del día a día (`APR-01` a `APR-04`) | Recepcionista de turno (`DEC-13`) | Jefa de recepción | Cliente |
| Cola de revisión | Jefa de recepción | Recepcionista de turno | Cliente |
| Cola de errores y alertas técnicas | Proveedor de TI | — (según acuerdo) | Tercero, acuerdo `DEC-35` |
| Interruptor de modo manual | Jefa de recepción | Valeria | Cliente |
| Conciliación diaria (`DEC-27`) | Proveedor de TI la ejecuta; jefa de recepción resuelve | Recepcionista de turno | Ambos |
| Soporte técnico | Proveedor de TI | — | Acuerdo `DEC-35` |

### 4. Rollback

| Nivel | Qué hace | Disparadores verificables | Decide | Casos en curso | Tiempo objetivo | Ensayo |
|---|---|---|---|---|---|---|
| 1 | Apaga la IA (`CMP-10`); toda solicitud nueva va a la cola de revisión | Una urgencia sin marcar; una instrucción oculta obedecida; tasa de escalamiento por encima de 26 % en un día (el doble de la medida en pruebas) | Jefa de recepción, sin permiso previo | Siguen; los nuevos van a revisión | 1 minuto | 2027-01-13: 1 minuto (jefa de recepción) |
| 2 | Restaura la versión anterior aprobada de reglas, plantillas o instrucciones | Un cambio publicado empeora una métrica del plan de evaluación | Jefa de recepción (reglas y plantillas); Valeria y administradora (instrucciones) | Siguen con la versión restaurada | 30 minutos | 2027-01-13: instrucciones v2 → v1 en 15 minutos (proveedor de TI); cómo se restaura una versión en la plataforma, verificado en el entorno de prueba |
| 3 | Desactiva el flujo; recepción agenda como antes del piloto, en el sistema de gestión y por la mensajería institucional | Una cita duplicada confirmada; un mensaje con datos de otro paciente; servicio caído más de 4 horas hábiles (`DEC-28`) | Jefa de recepción, sin permiso previo | Pasan a la cola de revisión con su estado; recepción los termina a mano | 15 minutos | 2027-01-13: 10 minutos; 4 casos en curso pasaron a la cola (jefa de recepción y proveedor de TI) |

Aviso de un rollback: la jefa de recepción avisa a Valeria y al proveedor de TI por el canal acordado en `DEC-35`; queda registrado como incidente (`INC-nn`). Plan de rollback: `DEC-34`.

### 5. Plan de salida

| Elemento | Respuesta |
|---|---|
| Ventana | Lunes 2027-01-18, a las 8:00, con la jefa de recepción y el líder técnico presentes |
| Salida gradual | Semana 1: solo el formulario. Desde el 2027-01-25, también los mensajes, si en la semana 1 no hubo incidentes altos y la cola de revisión respetó sus 4 horas hábiles |
| Comunicación | Recepción avisa a los pacientes que pidan cita por teléfono que también pueden usar el formulario; aviso de tratamiento de datos en el formulario y el primer mensaje (`DEC-32`) |
| Acompañamiento reforzado | Dos semanas: revisión diaria de colas, alertas e incidentes a las 17:30; soporte presente en horario de recepción. Cierre: diez días hábiles sin incidentes altos y colas dentro de su antigüedad máxima |

## Actualización tras la revisión del viernes 2027-01-15

**Estado: Aprobado.** `EVI-13` (2027-01-13): `TC-01`, `TC-06` y `TC-10` pasaron con plantillas y formulario v2. Rollback ensayado en sus tres niveles el 2027-01-13. Acuerdo de soporte firmado.

### Checklist de salida

| # | Comprobación | Resultado | Evidencia |
|---|---|---|---|
| 1 | Puerta de pruebas aprobada y ninguna decisión bloqueante abierta | Sí | `DEC-31`; `DEC-12`, `DEC-20`, `DEC-21`, `DEC-24`, `DEC-25`, `DEC-33` cerradas |
| 2 | Lo que se libera coincide con lo probado | Sí, tras la regresión | `EVI-13` |
| 3 | Dueños y suplentes | Sí | Sección 3 |
| 4 | **Rollback** por niveles con disparadores y quién decide | Sí | `DEC-34` |
| 5 | **Rollback** ensayado | Sí | Ensayo del 2027-01-13 |
| 6 | Runbook revisado por quien opera | Sí | Revisado por la jefa de recepción el 2027-01-14 |
| 7 | Capacitación | Sí | Dos recepcionistas, jefa de recepción y administradora, 2027-01-14 |
| 8 | Secretos en el almacén, con rotación | Sí | `REQ-07`, `DEC-33` |
| 9 | Alertas llegan a su dueño | Sí | `EVI-10`, ensayo |
| 10 | Contrato con madurez `production` | Sí | `DEC-37` |
| 11 | **Aprobación** de salida del cliente | Sí | `DEC-36` |

### Decisiones nuevas

| ID | Decisión | Dueño | Fecha | Aprobación |
|---|---|---|---|---|
| `DEC-32` | Aviso de tratamiento de datos en el formulario y en el primer mensaje (condición de `DEC-24`) | Valeria | 2027-01-12 | Aprobada; plantilla y formulario v2 aprobados por la jefa de recepción el 2027-01-13 |
| `DEC-33` | Rotación de secretos cada seis meses, ejecutada por el proveedor de TI y registrada | Administradora | 2027-01-13 | Aprobada |
| `DEC-34` | Plan de rollback en tres niveles, con disparadores, quién decide y tiempos | Jefa de recepción | 2027-01-13 | Aprobada por Valeria |
| `DEC-35` | Acuerdo de soporte técnico del proveedor de TI: horario de recepción; respuesta en 1 hora hábil (alta), 4 horas hábiles (media) y 2 días hábiles (baja); incluye la cola de errores, la conciliación y la rotación de secretos; no incluye cambios de reglas ni mejoras | Valeria | 2027-01-15 | Aprobada; vigencia de seis meses, revisión en la recertificación |
| `DEC-36` | **Salida a producción de `REL-01`** el 2027-01-18, gradual (formulario primero) | Valeria | 2027-01-15 | Aprobada |
| `DEC-37` | Contrato a madurez `production`: aprobador "Recepcionista de turno", plazo de espera de 48 horas, aviso a las 18:00, reintentos de `DEC-26` y retención de `DEC-12` | Jefa de recepción (dueña del contrato) | 2027-01-15 | Aprobada |

## Entregable: runbook (extracto)

| Alerta | Umbral | Llega a | Primera acción | Escalar a |
|---|---|---|---|---|
| Cola de revisión antigua | Un caso con más de 4 horas hábiles (`DEC-27`) | Jefa de recepción | Asignar a la recepcionista de turno | Valeria, si se repite tres días |
| Cola de errores | Un elemento con más de 2 horas hábiles | Proveedor de TI | Reprocesar con la misma clave (`IDM-01`) | Al cumplir un día, caso en la cola de revisión |
| Diferencia en la conciliación | Cualquier diferencia | Jefa de recepción | Revisar la agenda; compensación según el registro de idempotencia | Proveedor de TI |
| Fallas del modelo | Más de 5 en una hora | Proveedor de TI | Revisar; si siguen, rollback nivel 1 | Jefa de recepción |
| Límite por contacto | Un contacto supera el límite (`CTL-10`) | Jefa de recepción | Revisar si es un abuso | Administradora |

Rollback paso a paso, contactos por rol, tareas periódicas y dónde está cada artefacto: en el runbook completo, que usa `assets/runbook-de-transferencia.md`. Ningún secreto aparece en él: dice que viven en el almacén de secretos (`REQ-07`) y que los administra el proveedor de TI sin leer sus valores en producción.

## Entregable: checklist de transferencia (extracto)

| Ámbito | Antes | Después |
|---|---|---|
| Administración de entornos | Proveedor de TI | Valeria es la dueña; el proveedor de TI administra por el acuerdo `DEC-35` |
| Almacén de secretos | Proveedor de TI | Igual, con la rotación de `DEC-33`; la administradora revisa los accesos cada tres meses (`DEC-23`) |
| Cuentas de los desarrolladores | Acceso de administración en producción | Retiradas; queda una cuenta de soporte con permisos mínimos |
| Interruptor de modo manual | Proveedor de TI (pruebas) | Jefa de recepción |
| Acta de aceptación | — | Firmada por Valeria el 2027-01-15, con pendientes: `TC-15`, `CA-07`, falsas alarmas de `MET-02` (dueñas: jefa de recepción y odontóloga coordinadora clínica) |

**Siguiente paso sugerido:** `operacion-y-aseguramiento-continuo`, desde el 2027-01-18: observabilidad y alertas en marcha, medición de `CA-07` frente a la línea base, la muestra semanal de `TC-15` y la recertificación.

## Lo que se ve en este ejemplo

- La puerta de pruebas aprobada no se confundió con "listo": la salida esperó a cerrar las decisiones de datos, cumplimiento y retención.
- La condición legal cambió una plantilla después de las pruebas; se aprobó y se volvió a probar, porque se libera lo que se probó.
- "Apago todo" se convirtió en tres niveles de rollback con disparadores verificables y quién decide sin pedir permiso, y se ensayaron.
- El soporte "como hasta ahora" pasó a ser un acuerdo escrito con alcance, horario y tiempos.
- La aprobación de salida fue de Valeria, no del equipo técnico; el estado fue "No listo" hasta tener dueños, aprobación y rollback.
- La transferencia retiró los accesos de administración de quien construyó y dejó el interruptor en manos de la clínica.
