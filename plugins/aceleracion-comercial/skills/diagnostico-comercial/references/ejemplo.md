# Ejemplo: Diagnóstico comercial de una firma contable ficticia

Empresa inventada: **Brújula Contadores** (6 personas: 2 socios, 2 contadoras, 1 analista de impuestos y 1 asistente administrativa; 62 clientes activos con un ticket mensual promedio de unos USD 210, o sea unos USD 13.000 al mes en ingresos recurrentes). Todo lo siguiente es ficticio. Continúa el ejemplo de `facilitador-aceleracion-comercial`: modalidad A, etapa 0, con `HAL-01` a `HAL-03` y el supuesto `SUP-01`.

## Turno 1

**Usuaria (socia fundadora):** Ya conté mis contactos de los últimos seis meses. Quiero saber por qué no crecemos más rápido.

**Facilitador:** Perfecto, vamos a medirlo antes de opinar. Para saber en qué paso se cae el embudo, ¿cuántas de esas 84 personas llegaron a una reunión con ustedes?

## Turno 2

**Usuaria:** Unas 42. De esas, a 24 les mandamos propuesta y se cerraron 9. Hoy hay 11 oportunidades abiertas. Lo saqué de mi hoja de seguimiento y de los correos.

**Facilitador:** Con esas cifras armo el embudo. Defino los términos para que todos cuenten lo mismo: lead es una persona o empresa que pide información; oportunidad es una reunión realizada; propuesta es un documento con precio enviado; ganada es un contrato firmado.

| Etapa | Cantidad | Tasa de paso | Calidad del dato |
|---|---|---|---|
| Leads | 84 | n/a | Contada |
| Oportunidades (reunión realizada) | 42 | 50 % | Contada |
| Propuestas | 24 | 57 % | Contada |
| Ganadas | 9 | 37,5 % (de las propuestas) | Contada |
| Abiertas hoy | 11 | n/a (aparte: no entran en las tasas, que usan solo oportunidades cerradas) | Contada; 4 tienen siguiente paso fechado |

Lead a venta: 9 / 84 = 10,7 %. Ciclo mediano entre la reunión y la firma: 21 días (estimado de los correos, calidad Estimada). Canal de los leads: 54 recomendaciones, 18 formulario de la página y 12 redes sociales (`HAL-02`).

## Turno 3

**Facilitador:** Faltan los motivos de pérdida. De las 15 propuestas que no se ganaron, ¿qué te dijo cada cliente?

**Usuaria:** Revisé: en 7 eran negocios muy pequeños, casi informales, que solo querían alguien que les firmara; en 5 eligieron a otro por precio; en 3 nunca respondieron después de la propuesta. Y de las 11 abiertas, solo en 4 quedó una fecha de seguimiento.

**Facilitador:** Esto cambia `SUP-01`: el problema no parece ser la cantidad de contactos sino a quién se le manda propuesta y qué pasa después (**Hecho**: los motivos vienen de lo que dijo el cliente, registrados por la socia). Propongo estos problemas prioritarios; son hipótesis hasta que las verifiquemos.

| ID | Problema | Evidencia | Hipótesis de causa (**Supuesto**) |
|---|---|---|---|
| `PRO-01` | Se envían propuestas a quien no es el perfil: 7 de 15 propuestas no ganadas | `HAL-04` | No hay criterio de calificación antes de la propuesta |
| `PRO-02` | Dependencia de una persona y de un canal: 64 % de recomendaciones y 7 de 9 cierres por la socia fundadora | `HAL-02`, `HAL-03` | La venta no está escrita ni repartida |
| `PRO-03` | Sin seguimiento sistemático: solo 4 de 11 oportunidades abiertas con siguiente paso fechado y 3 propuestas sin respuesta | `HAL-05` | No hay regla ni lugar para el seguimiento |

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

**Línea base de KPIs (resumen):** `KPI-01` 84 leads en 6 meses (54, 18 y 12 por canal); `KPI-02` No medido (no hay criterio de perfil); `KPI-03` No medido; `KPI-04` 50 %; `KPI-05` 21,4 % (9 ganadas de 42 reuniones cerradas); `KPI-06` 21 días (estimado); `KPI-07` 5 de 11 oportunidades abiertas sin avance en más de 14 días (45 %); `KPI-08` No medido; `KPI-09` USD 195 por mes (9 ganadas); `KPI-10` no existe forecast; `KPI-11` No medido; `KPI-12` 36 %; `KPI-13` ingresos recurrentes de unos USD 13.000 al mes, margen por segmento No medido.

**Madurez (propuesta, a confirmar por el equipo):** segmentación 1, oferta 2, proceso 1, datos y herramientas 2, equipo 2, demanda 2, gestión 1.

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
