# Registro mínimo viable en una hoja de cálculo

Organización: ___  Fecha: ___  Versión: borrador 1

No es una herramienta recomendada: es un formato. Sirve para empezar hoy y como maqueta si más adelante el equipo adopta otra herramienta (el diccionario de datos es la especificación).

## 1. Hojas del archivo

| Hoja | Qué guarda | Quién la edita |
|---|---|---|
| Oportunidades | Una fila por oportunidad, con los campos `CAM-01` a `CAM-23` | Responsables de cada oportunidad |
| Prospección | Una fila por contacto de prospección: fecha, canal, cuenta, si respondió, resultado | Quien prospecta |
| Cuentas | Lista de cuentas objetivo (`CUE-nn`) con su nivel | Dueño de la calidad |
| Listas | Valores permitidos: etapas, orígenes, resultados, motivos | Solo el dueño de la calidad |
| Tablero | Fórmulas y gráficos de `TAB-01` a `TAB-05` | Dueño de la calidad |

## 2. Configuración paso a paso

1. Crea la hoja Oportunidades con una columna por campo, en el orden del diccionario. Congela la fila de títulos.
2. En la hoja Listas escribe cada lista cerrada; en Oportunidades, aplica validación de datos tipo lista a etapa, origen, resultado, motivo de pérdida y necesidad.
3. Valida las fechas (fecha del siguiente paso, último contacto) con formato de fecha.
4. Marca por formato condicional: siguiente paso con fecha anterior a hoy (rojo) y último contacto con más días que el umbral (amarillo).
5. Crea tres vistas filtradas: "Vencidos" (siguiente paso anterior a hoy), "Mis oportunidades" (por responsable) y "Sin siguiente paso".
6. Protege las columnas de fórmulas y la hoja Listas.
7. Guarda una copia de seguridad semanal con fecha en el nombre.

## 3. Fórmulas de referencia (en palabras)

| Indicador | Cómo se calcula en la hoja |
|---|---|
| Estancada (`KPI-07`) | Hoy menos último contacto es mayor que el umbral, o la fecha del siguiente paso está vacía |
| Higiene (`KPI-12`) | Filas abiertas con responsable, etapa, importe y siguiente paso con fecha, dividido entre filas abiertas |
| Oportunidad a venta (`KPI-05`) | Ganadas entre cerradas, con la definición de oportunidad de la línea base |
| Ciclo (`KPI-06`) | Mediana de (fecha de cierre menos fecha de reunión realizada) de las ganadas |
| Ticket promedio (`KPI-09`) | Suma de importes de ganadas entre número de ganadas |

## 4. Límites de la hoja (cuándo reconsiderar)

| Señal | Qué significa |
|---|---|
| Varias personas editan a la vez y se pisan | Se necesita edición concurrente con historial |
| Más de ___ oportunidades abiertas | La hoja se vuelve lenta de revisar |
| Se necesitan recordatorios o formularios conectados | Considerar una herramienta con automatizaciones |

Si se migra, se lleva el diccionario de datos, las listas y las reglas `AUT-nn`; no se cambian definiciones al migrar.

## 5. Hoja equivalente a la tabla de campos

Orden de columnas de la hoja Oportunidades: ___ (copia de la tabla de `assets/campos-minimos-crm.md`).
