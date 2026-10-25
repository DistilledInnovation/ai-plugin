# Ejemplo: Diagnóstico comercial de una firma contable ficticia

Empresa inventada: **Brújula Contadores** (6 personas: 2 socios, 2 contadoras, 1 analista de impuestos y 1 asistente administrativa; 62 clientes activos con un ticket mensual promedio de unos USD 210, o sea unos USD 13.000 al mes en ingresos recurrentes). Todo lo siguiente es ficticio. Continúa el ejemplo de `facilitador-aceleracion-comercial`: modalidad A, etapa 0, con `HAL-01` a `HAL-03` y el supuesto `SUP-01`.

## Turno 1

**Usuaria (socia fundadora):** Ya conté mis contactos de los últimos seis meses. Quiero saber por qué no crecemos más rápido.

**Facilitador:** Perfecto, vamos a medirlo antes de opinar. Para saber en qué paso se cae el embudo, ¿cuántas de esas 84 personas llegaron a una reunión con ustedes?

## Turno 2

**Usuaria:** Unas 42. A 24 les mandamos propuesta y se firmaron 9. De las 42 reuniones, hoy 11 siguen abiertas (3 con propuesta y 8 sin propuesta todavía). Lo saqué de mi hoja de seguimiento y de los correos.

**Facilitador:** Con esas cifras armo el embudo. Defino los términos para que todos cuenten lo mismo: lead es una persona o empresa que pide información; oportunidad es una reunión realizada; propuesta es un documento con precio enviado; ganada es un contrato firmado.

| Etapa | Cantidad | Tasa de paso | Calidad del dato |
|---|---|---|---|
| Leads | 84 | n/a | Contada |
| Oportunidades (reunión realizada) | 42 | 50 % | Contada |
| Propuestas | 24 | 57 % | Contada |
| Ganadas | 9 | 42,9 % de las propuestas cerradas (9 de 21) | Contada |
| Perdidas | 22 (12 con propuesta y 10 sin propuesta) | n/a | Contada; motivo registrado solo en las 12 con propuesta |
| Abiertas hoy (dentro de las 42) | 11 (3 con propuesta y 8 sin propuesta) | n/a (no entran en las tasas de cierre) | Contada; 4 tienen siguiente paso fechado |

Las 42 reuniones se reparten en 9 ganadas, 22 perdidas y 11 abiertas, así que hay 31 oportunidades cerradas y la tasa de cierre de oportunidades es 9 / 31 = 29,0 %. Lead a venta: 9 / 84 = 10,7 %. Ciclo mediano entre la reunión y la firma: 21 días (estimado de los correos, calidad Estimada). Canal de los leads: 54 recomendaciones, 18 formulario de la página y 12 redes sociales (`HAL-02`).

## Turno 3

**Facilitador:** Faltan los motivos de pérdida. De las 12 propuestas que se perdieron, ¿qué te dijo cada cliente?

**Usuaria:** Revisé: en 7 no eran el perfil (negocios muy pequeños o sin facturación formal, sobre todo comercios, que solo querían alguien que les firmara); en 3 eligieron a otro por precio; en 2 nunca respondieron después de la propuesta. De las 10 perdidas sin propuesta no anoté el motivo. Y de las 11 abiertas, solo en 4 quedó una fecha de seguimiento.

**Facilitador:** Esto cambia `SUP-01`: el problema no parece ser la cantidad de contactos sino a quién se le manda propuesta y qué pasa después (**Hecho**: los motivos vienen de lo que dijo el cliente, registrados por la socia). Propongo estos problemas prioritarios; son hipótesis hasta que las verifiquemos.

| ID | Problema | Evidencia | Hipótesis de causa (**Supuesto**) |
|---|---|---|---|
| `PRO-01` | Se envían propuestas a quien no es el perfil: 7 de 12 propuestas perdidas | `HAL-04` | No hay criterio de calificación antes de la propuesta |
| `PRO-02` | Dependencia de una persona y de un canal: 64 % de recomendaciones y 7 de 9 cierres por la socia fundadora | `HAL-02`, `HAL-03` | La venta no está escrita ni repartida |
| `PRO-03` | Sin seguimiento sistemático: solo 4 de 11 oportunidades abiertas con siguiente paso fechado y 2 propuestas perdidas sin respuesta | `HAL-05` | No hay regla ni lugar para el seguimiento |

## Turno 4

**Facilitador:** ¿Qué te gustaría lograr en seis meses para estos tres problemas?

**Usuaria:** Pasar de 62 a 80 clientes en doce meses sin bajar el ticket, que no todo dependa de mí y que no se nos olvide ninguna propuesta.

**Facilitador:** Lo convierto en metas medibles; propongo plazos y tú los ajustas.

| ID | Meta | Línea base | Meta | Plazo |
|---|---|---|---|---|
| `OBJ-01` | Lead a venta (`KPI-04` y `KPI-05` sirven de apoyo) | 10,7 % (9/84) | 15 % | 6 meses |
| `OBJ-02` | Oportunidades abiertas con siguiente paso fechado (`KPI-12`) | 36 % (4/11) | 90 % | 3 meses |
| `OBJ-03` | Ventas cerradas por alguien distinto de la socia fundadora | 22 % (2/9) | 50 % | 6 meses |
| `OBJ-04` | Clientes activos | 62 | 80 | 12 meses |

**Línea base de KPIs (resumen):** `KPI-01` 84 leads en 6 meses (54, 18 y 12 por canal); `KPI-02` No medido (no hay criterio de perfil); `KPI-03` No medido; `KPI-04` 50 %; `KPI-05` 29,0 % (9 ganadas de 31 oportunidades cerradas; las 11 abiertas no entran), con propuesta a ganada de 42,9 % (9 de 21 propuestas cerradas); `KPI-06` 21 días (estimado); `KPI-07` 5 de 11 oportunidades abiertas sin avance en más de 14 días (45 %; definición de oportunidad: reunión realizada); `KPI-08` No medido; `KPI-09` USD 195 por mes (9 ganadas); `KPI-10` no existe forecast; `KPI-11` No medido; `KPI-12` 36 %; `KPI-13` ingresos recurrentes de unos USD 13.000 al mes, margen por segmento No medido.

**Madurez (propuesta, a confirmar por el equipo):** segmentación 1, oferta 2, proceso 1, datos y herramientas 2, equipo 2, demanda 2, gestión 1.

## Inventario de herramientas y canales (`assets/inventario-de-herramientas.md`)

| Canal o herramienta | Para qué se usa | Quién la usa | Qué dato guarda | ¿Se actualiza? |
|---|---|---|---|---|
| Hoja de seguimiento de contactos | Anotar contactos y propuestas | Asistente administrativa | Fecha, canal y estado | A veces |
| Correo | Enviar propuestas y dar seguimiento | Socios | Texto de cada propuesta, sin estructura | Siempre, pero no se consulta como registro |
| Agenda compartida | Reuniones | Socios y contadoras | Fecha y participantes | Siempre |
| Formulario de la página | Recibir consultas | Asistente administrativa | Datos de contacto | Siempre |
| Recomendaciones de clientes | Llegada de leads | Socia fundadora | Nada (de memoria) | Nunca |

Hecho: no hay un único registro; el estado de cada oportunidad vive en la hoja, en el correo y en la memoria de la socia (`HAL-09`). No se evalúa ni se recomienda ningún producto.

## Turno 5: backlog

| ID | Acción | Etapa | Problema | Impacto | Esfuerzo | Responsable | Fecha objetivo |
|---|---|---|---|---|---|---|---|
| `BAC-01` | Definir quién es el cliente ideal y a quién no se le manda propuesta | 1 | `PRO-01` | Alto | Bajo | Socia fundadora | Semana 3 |
| `BAC-02` | Escribir el argumento de venta común | 2 | `PRO-02` | Alto | Medio | Socio de impuestos | Semana 4 |
| `BAC-03` | Definir etapas con criterios y exigir siguiente paso fechado | 3 | `PRO-03` | Alto | Bajo | Asistente administrativa | Semana 5 |
| `BAC-04` | Registrar el motivo de cada pérdida | 3 | `PRO-01` | Medio | Bajo | Asistente administrativa | Semana 2 |

Decisión `DEC-01`: la socia fundadora y el socio de impuestos acuerdan `PRO-01` a `PRO-03` y `OBJ-01` a `OBJ-04`; la línea base queda registrada con `KPI-02`, `KPI-03`, `KPI-08` y `KPI-11` como datos que faltan (la asistente empezará a anotarlos desde la semana 2). Riesgo `RIE-01`: si la socia fundadora está de viaje, las oportunidades abiertas se detienen; mitigación: el socio de impuestos recibe las reuniones nuevas desde la semana 3.

**Facilitador:** Siguiente paso (**Recomendación**): `segmentacion-e-icp`, porque `BAC-01` ataca el problema con más evidencia. ¿Seguimos ahora con eso?

## Qué quedó claro del ejemplo

- Las definiciones se escribieron antes de contar.
- Los motivos de pérdida vinieron de lo que dijo el cliente y desmontaron el supuesto inicial.
- Cada meta tiene línea base y plazo, y los datos faltantes tienen responsable.
- No se recomendó ninguna herramienta.
