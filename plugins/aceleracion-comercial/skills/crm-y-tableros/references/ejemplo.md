# Ejemplo: CRM y tableros de una firma contable ficticia

Empresa inventada: **Brújula Contadores** (6 personas; 62 clientes activos; ticket mensual promedio de unos USD 210). Todo lo siguiente es ficticio. Continúa el ejemplo de `proceso-de-ventas-y-pipeline`: `ETA-01` a `ETA-07`, estancamiento a 14 días, `REG-01` a `REG-03`, `DEC-03` y `DEC-04` (oportunidad de la línea base = reunión realizada, `ETA-04` o posterior), `KPI-01` a `KPI-13`, `OPO-01` a `OPO-03`, `HAL-09` (no hay un único registro), `OBJ-02` (siguiente paso fechado de 36 % a 90 %) y `BAC-03`. Fecha de inicio: lunes 26 de octubre de 2026.

## Turno 1

**Facilitador:** Vamos con la etapa 4. ¿Dónde está hoy el estado de cada oportunidad abierta y quién lo actualiza?

## Turno 2

**Usuaria (socia fundadora):** En una hoja que lleva la asistente administrativa, en mis correos y, la verdad, en mi cabeza. Hay 11 oportunidades abiertas y la hoja solo tiene la fecha de la propuesta.

**Facilitador:** Eso coincide con `HAL-09` (**Hecho**). Propongo no empezar por una herramienta sino por los campos: cada uno tiene que responder a una decisión o a un KPI. ¿Qué tienes que saber de una oportunidad para decidir qué hacer con ella hoy?

**Usuaria:** En qué etapa está, quién la lleva, qué va a pasar y cuándo, cuánto vale y de dónde vino.

## Turno 3: campos mínimos (`assets/campos-minimos-crm.md`)

Núcleo de 13 campos (`CAM-01` a `CAM-13`): identificador, cuenta, segmento o ICP, origen, responsable, etapa, contacto y actor, último contacto, siguiente paso, fecha del siguiente paso, importe mensual, fecha estimada de decisión y resultado. Medición (`CAM-14` a `CAM-17`): fecha de creación, **fecha de reunión realizada** (`CAM-15`), fecha de cierre y motivo de pérdida. Calificación (`CAM-18` a `CAM-20`): necesidad, puntaje BANT y dolor. Opcionales: paquete (`OFE-nn`), referidor y notas (descuentos aprobados y MEDDICC).

Por qué `CAM-15`: por `DEC-04`, los KPIs mantienen "reunión realizada" como definición de oportunidad; esa fecha permite calcular `KPI-04`, `KPI-05`, `KPI-06` y `KPI-07` de forma comparable, y las calificadas (`ETA-03`) se miden como indicador nuevo. Se quita del primer borrador el campo "tamaño de la empresa" porque ninguna decisión ni tablero lo usa todavía (**Recomendación**, la usuaria lo acepta).

## Turno 4: diccionario de datos (extracto)

| ID | Campo | Tipo | Valores permitidos | Obligatorio desde | Quién lo llena | Validación |
|---|---|---|---|---|---|---|
| `CAM-04` | Origen | Lista cerrada | recomendación, formulario de la página, redes, contacto directo, alianza | `ETA-01` | Asistente administrativa | Se queda el primer contacto |
| `CAM-06` | Etapa | Lista cerrada | `ETA-01` a `ETA-07` | `ETA-01` | Responsable | `ETA-03` exige `CAM-18` y `CAM-19` con `REG-01` cumplida |
| `CAM-10` | Fecha del siguiente paso | Fecha | Hoy o posterior | Siempre en abiertas | Responsable | No puede estar vacía |
| `CAM-17` | Motivo de pérdida | Lista cerrada + frase | precio, no era el perfil, eligió a otro, momento, sin respuesta, otro | `ETA-07` si se pierde | Responsable | Obligatorio al marcar perdida |

Higiene: `HIG-01` (campos completos en abiertas), `HIG-02` (sin duplicados), `HIG-03` (cerradas con resultado y motivo), `HIG-04` (estancadas con acción) y `HIG-05` (muestra mensual contra la realidad). Dueña de la calidad: la asistente administrativa; suplente: la contadora senior (`RIE-03`: si solo ella conoce el registro, un viaje o una licencia lo deja sin mantenimiento).

## Turno 5: migración (martes 27 de octubre) y hoja de cálculo

Se arma el archivo con las hojas Oportunidades, Prospección, Cuentas, Listas y Tablero (`assets/crm-en-hoja-de-calculo.md`), con listas desplegables y marca roja de siguiente paso vencido.

| Qué se migra | Cantidad | Calidad |
|---|---|---|
| Oportunidades abiertas (`OPO-03` a `OPO-13`), completas | 11 | Contada |
| Oportunidades cerradas (`OPO-01`, `OPO-02` y `OPO-14` a `OPO-42`), solo resultado, fechas y motivo si existe | 31 | Contada; 10 perdidas sin propuesta quedan "Sin registro" en el motivo (**Hecho**) |
| Duplicados detectados al migrar | 1 (la agencia de marketing de `OPO-05` aparecía por recomendación y por formulario) | Se unió y se conservó el primer contacto (recomendación) |

Importes de las 11 abiertas: tres con propuesta (`OPO-03` estudio de animación, USD 210; `OPO-04` consultorio odontológico, USD 190; `OPO-05` agencia de marketing, USD 210) suman USD 610 al mes; las ocho sin propuesta (`OPO-06` a `OPO-13`) llevan un importe estimado de USD 210 cada una (ticket promedio actual, **Supuesto**) y suman USD 1.680. Total abierto: USD 2.290 al mes. En la etapa `ETA-04` hay 8 oportunidades y en `ETA-05` hay 3.

## Turno 6: automatizaciones básicas

| ID | Qué hace | Lo que no hace |
|---|---|---|
| `AUT-01` | Marca en rojo y lista en "Vencidos" los siguientes pasos con fecha pasada | No escribe al cliente |
| `AUT-02` | Marca como estancada una oportunidad con más de 14 días sin contacto (el umbral de `ETA-nn`) | No la cierra |
| `AUT-03` | No deja pasar a `ETA-03` sin necesidad y puntaje BANT | No mueve etapas por su cuenta |
| `AUT-04` | Marca cuentas repetidas | No las une ni las borra |

Queda fuera por ahora el envío automático de mensajes al cliente (**Recomendación**, porque exige revisión humana y política de datos).

## Turno 7: tableros (`assets/tablero-comercial.md`)

**Facilitador:** ¿Qué pregunta quieres poder contestar cada lunes en cinco minutos?

**Usuaria:** Qué se nos está quedando sin siguiente paso y cuánto dinero hay en juego.

| ID | Tablero | Pregunta | Frecuencia |
|---|---|---|---|
| `TAB-01` | Actividad | ¿Qué vence esta semana y quién lo tiene? | Semanal |
| `TAB-02` | Pipeline | ¿Cuántas por etapa, cuánto valen y cuáles están estancadas? Hoy: 11 abiertas, USD 2.290 al mes y 5 estancadas (45 %, `KPI-07`) | Semanal |
| `TAB-03` | Eficiencia | ¿Cuánto convierte y en cuántos días? (`KPI-04` a `KPI-06`, `KPI-09`) | Mensual |
| `TAB-04` | Pronóstico | ¿Cuánto esperamos cerrar? (`KPI-10`, todavía sin forecast: lo hace la etapa 7) | Mensual |
| `TAB-05` | Calidad del registro | ¿Se puede confiar en los datos? (`KPI-12`) | Semanal |

`KPI-02`, `KPI-03`, `KPI-08` y `KPI-11` siguen **No medido**: `KPI-02` y `KPI-03` empiezan a calcularse con la hoja Prospección (desde el lunes 2 de noviembre); `KPI-08` y `KPI-11` necesitan el registro de esfuerzo de la etapa 6.

## Turno 8: guía de adopción y prueba

Rutina diaria de cinco minutos (revisar "Vencidos", anotar último contacto y siguiente paso después de cada contacto relevante). Capacitación de 30 minutos el martes 27 de octubre con tres oportunidades reales. Permisos: cada responsable edita sus filas; la asistente administrativa edita todo y la hoja Listas. Se pide no guardar documentos fiscales, claves ni datos bancarios de clientes.

| Fecha | Oportunidades abiertas | Con responsable, etapa, importe y siguiente paso fechado | `KPI-12` | Qué se hizo |
|---|---|---|---|---|
| Lunes 26 oct (antes de migrar) | 11 | 4 | 36 % (línea base) | Punto de partida |
| Lunes 2 nov | 11 | 9 | 82 % | `OPO-11` y `OPO-12` sin siguiente paso |
| Lunes 9 nov | 12 | 11 | 92 % | `OPO-12` se marcó perdida (sin respuesta); `OPO-11` tiene fecha; entraron `OPO-43` y `OPO-44` y una falta de fecha |

**Hecho:** la auditoría la hizo la asistente administrativa con la vista "Sin siguiente paso". **Pendiente por validar:** que `OBJ-02` (90 % durante tres meses) se sostenga y no sea solo el efecto de la primera semana. Una persona del equipo verifica `HIG-05` cada mes contra la realidad.

Decisión `DEC-05`: la hoja de cálculo es el registro oficial desde el lunes 26 de octubre de 2026; el correo y la memoria dejan de serlo. Se reconsidera una herramienta más completa solo si aparece una señal de la sección de límites (edición simultánea, volumen o integraciones).

**Facilitador:** Siguiente paso (**Recomendación**): `kit-comercial-y-entrenamiento`, porque ya se registra igual y falta que se converse y se dé seguimiento igual. ¿Seguimos?

## Qué quedó claro del ejemplo

- Los campos salieron de las decisiones y los KPIs, no de un catálogo; se quitó uno que nadie usaba.
- Se agregó la fecha de reunión realizada para que la línea base siga siendo comparable (`DEC-04`).
- Las automatizaciones solo avisan al equipo; ninguna escribe a un cliente.
- La hoja de cálculo alcanzó, con una condición explícita para reconsiderarla.
- La adopción se midió con una auditoría y se declaró lo que sigue pendiente.
