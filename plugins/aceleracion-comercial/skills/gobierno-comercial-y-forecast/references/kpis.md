# Los 13 KPIs del sistema comercial

Los mismos 13 indicadores de la línea base de `diagnostico-comercial` (`KPI-01` a `KPI-13`), con las fórmulas o definiciones operativas de la metodología. Las fórmulas se mantienen exactas; las demás columnas indican cómo medirlos con el registro de la etapa 4.

## Regla de medición

Comparar periodos equivalentes y cohortes cuando sea posible; documentar qué significa "conversión", por cuál denominador se divide y si los indicadores reportados son actividad, resultados o impacto. No convertir porcentajes promocionales en garantías. Un indicador sin dato se muestra "No medido".

## 1. Tabla de KPIs

| ID | Dimensión | KPI | Fórmula o definición operacional | Tipo |
|---|---|---|---|---|
| KPI-01 | Demanda | Leads por canal | Nuevos leads únicos recibidos en el periodo, segmentados por fuente | Actividad |
| KPI-02 | Calidad | % de leads ICP | Leads que cumplen perfil / leads evaluados × 100 | Resultado |
| KPI-03 | Activación | Tasa de respuesta | Prospectos que responden / prospectos contactados × 100 | Actividad |
| KPI-04 | Conversión | Lead a oportunidad | Oportunidades nuevas / leads elegibles del periodo × 100 (definir cohorte) | Resultado |
| KPI-05 | Conversión | Oportunidad a venta | Oportunidades ganadas / oportunidades cerradas × 100 | Resultado |
| KPI-06 | Velocidad | Duración del ciclo | Días entre creación/fecha de calificación y cierre (definición consistente) | Resultado |
| KPI-07 | Salud del pipeline | Oportunidades estancadas | Oportunidades sin siguiente paso o sin avance más allá del umbral acordado | Resultado |
| KPI-08 | Productividad | Actividades útiles por persona | Contactos/reuniones/propuestas según la etapa y la calidad | Actividad |
| KPI-09 | Valor | Ticket promedio ganado | Valor total ganado / número de negocios ganados | Resultado |
| KPI-10 | Previsibilidad | Error del forecast | Diferencia entre ventas previstas y realizadas, con método explícito | Resultado |
| KPI-11 | Eficiencia | Costo por oportunidad | Inversión comercial atribuible / oportunidades generadas | Resultado |
| KPI-12 | Adopción | Higiene del registro | % oportunidades activas con responsable, etapa, importe y siguiente paso válidos | Actividad |
| KPI-13 | Resultados | Ingresos y margen | Ventas y contribución por segmento, canal y periodo | Impacto |

Notas: "persona" sustituye a "comercial" y "responsable" a "owner" para el equipo que no tiene una función comercial exclusiva. El tipo (actividad, resultado o impacto) es la clasificación recomendada para reportar; ajústala si el equipo define otra.

## 2. Cómo medirlos con el registro

| ID | Campos o fuentes (`CAM-nn`, hojas) | Ritual donde se lee | Responsable sugerido | Trampa común |
|---|---|---|---|---|
| KPI-01 | `CAM-04`, `CAM-14` | Semanal (canales), mensual | Quien registra los leads | Contar el mismo lead dos veces por canales distintos (regla de atribución) |
| KPI-02 | `CAM-03` ("Fuera de perfil") | Semanal | Quien califica | Evaluar solo los leads que parecen buenos |
| KPI-03 | Hoja Prospección (contactados y respondieron) | Semanal | Quien prospecta | Contar como respuesta un rechazo automático o un "no gracias" sin distinguirlo |
| KPI-04 | `CAM-14`, `CAM-15` | Mensual | Responsable comercial | Dividir por todos los leads cuando la cohorte aún no tuvo tiempo de avanzar |
| KPI-05 | `CAM-13`, `CAM-15` | Mensual | Responsable comercial | Incluir las abiertas en el denominador |
| KPI-06 | `CAM-15`, `CAM-16` (o `CAM-14`) | Mensual | Responsable comercial | Cambiar el punto de inicio entre periodos (se anota la definición y no se cambia) |
| KPI-07 | `CAM-08`, `CAM-10` | Semanal | Responsable comercial | Dejar abiertas por inercia las oportunidades muertas |
| KPI-08 | Hoja Prospección, `CAM-15`, propuestas | Quincenal y mensual | Responsable comercial | Contar actividad sin calidad (llamadas sin respuesta) |
| KPI-09 | `CAM-11`, `CAM-13` | Mensual | Dirección | Mezclar importes mensuales con importes anuales |
| KPI-10 | Forecast y ventas reales | Mensual | Dirección | Medirlo sin escribir el método del pronóstico |
| KPI-11 | Hoja de esfuerzo y gasto por canal | Mensual | Dirección | Olvidar el costo de horas internas (se declara el costo por hora como **Supuesto**) |
| KPI-12 | `HIG-nn` | Semanal | Dueño de la calidad del registro | Llenar campos con datos inventados para subir el indicador |
| KPI-13 | `CAM-03`, `CAM-04`, `CAM-11`, costos del servicio | Mensual y trimestral | Dirección | Reportar ingresos sin contribución cuando todavía no se mide el costo de servir |

## 3. Cómo usarlos en las reuniones

| Ritual | KPIs que se miran | Pregunta |
|---|---|---|
| Semanal | `KPI-01`, `KPI-02`, `KPI-03`, `KPI-07`, `KPI-12` | ¿Entra demanda de calidad y se mueve el pipeline? |
| Quincenal | `KPI-08` y las objeciones registradas | ¿Qué conducta entrenamos? |
| Mensual | `KPI-04`, `KPI-05`, `KPI-06`, `KPI-09`, `KPI-10`, `KPI-11` | ¿Convertimos mejor, más rápido y a menor costo? |
| Trimestral | `KPI-13` por segmento y canal, tendencias de todos | ¿Dónde invertimos y qué etapa se reabre? |

## 4. Líneas base y metas

Cada indicador parte de la línea base de la etapa 0 (con su calidad de dato: contada, estimada o No medido) y de metas con plazo (`OBJ-nn`). Las metas son hipótesis, no promesas; en ciclos largos se usan indicadores adelantados (reuniones, propuestas y siguientes pasos fechados).
