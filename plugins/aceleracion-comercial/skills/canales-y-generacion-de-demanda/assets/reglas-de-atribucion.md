# Reglas de atribución

Organización: ___  Fecha: ___  Versión: borrador 1  Dueño de las reglas: ___

Una regla escrita evita discutir el origen de cada lead y permite comparar canales.

## 1. Reglas (`REA-nn`)

| ID | Regla | Ejemplo | Dónde se anota |
|---|---|---|---|
| REA-01 | Cada lead tiene un solo origen (el primer contacto) | Llegó por recomendación y luego llenó el formulario: origen = recomendación | `CAM-04` |
| REA-02 | Si llegó por recomendación, se anota quién recomendó | | `CAM-22` |
| REA-03 | Si el primer contacto fue una respuesta a una campaña, el origen es el canal de la campaña (`CAN-nn`) | | `CAM-04` |
| REA-04 | Un lead sin origen conocido se marca "Sin origen" y se cuenta como error de higiene | | `CAM-04`, `HIG-nn` |
| REA-05 | Los canales adicionales con los que tuvo contacto se anotan como nota, no cambian el origen | | Notas |

## 2. Qué no resuelve esta atribución

Dice qué canal trajo al lead, no cuál lo convenció; si se necesita más detalle, se agrega una pregunta en la llamada de calificación ("¿cómo nos conociste?") y se anota.

## 3. Cómo se calcula por canal

| Indicador | Fórmula |
|---|---|
| Leads por canal (`KPI-01`) | Leads únicos del periodo con ese origen |
| Calidad por canal (`KPI-02`) | Leads del canal que cumplen el perfil / leads evaluados del canal × 100 |
| Costo por oportunidad (`KPI-11`) | Inversión comercial atribuible al canal / oportunidades generadas por el canal |

## 4. Revisión

Cada ___ se revisa si las reglas se cumplen (porcentaje de leads con origen) y si hace falta ajustarlas: ___

## 5. Pendientes por validar

- ___
