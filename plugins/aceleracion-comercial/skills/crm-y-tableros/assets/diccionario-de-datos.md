# Diccionario de datos

Organización: ___  Fecha: ___  Versión: borrador 1  Dueño de la calidad del registro: ___

Es la especificación del registro: sirve igual para una hoja de cálculo o para una herramienta posterior.

## 1. Definición de cada campo

| ID | Campo | Tipo | Valores permitidos o formato | Obligatorio desde | Quién lo llena y cuándo | Regla de validación |
|---|---|---|---|---|---|---|
| CAM-01 | Identificador | Texto | `OPO-` + número consecutivo; nunca se reutiliza | ETA-01 | Quien crea la fila | Único |
| CAM-04 | Origen | Lista cerrada | ___ | ETA-01 | Quien recibe el lead | Un solo valor; se queda el primer contacto |
| CAM-06 | Etapa | Lista cerrada | `ETA-01` a `ETA-__` | ETA-01 | Responsable | Solo avanza si se cumple la regla de entrada |
| CAM-10 | Fecha del siguiente paso | Fecha | Fecha igual o posterior a hoy | Siempre | Responsable | No puede estar vacía en una oportunidad abierta |
| | | | | | | |

## 2. Listas cerradas

| Lista | Valores |
|---|---|
| Origen | ___ |
| Resultado | abierta, ganada, perdida, nutrir, descartada |
| Motivo de pérdida | ___ (por ejemplo: precio, no era el perfil, eligió a otro, momento, sin respuesta, otro) |
| Necesidad | Sí, Parcial, No |

## 3. Reglas de higiene (`HIG-nn`)

| ID | Regla | Cómo se comprueba | Frecuencia | Quién |
|---|---|---|---|---|
| HIG-01 | Toda oportunidad abierta tiene responsable, etapa, importe y siguiente paso con fecha | Filtro de campos vacíos (`KPI-12`) | Semanal | ___ |
| HIG-02 | Sin duplicados de cuenta | Revisión de cuentas repetidas | Semanal | ___ |
| HIG-03 | Toda oportunidad cerrada tiene resultado y fecha de cierre; toda perdida, motivo | Filtro de cerradas sin motivo | Semanal | ___ |
| HIG-04 | Ninguna oportunidad abierta supera el umbral de estancamiento sin acción | Filtro de último contacto | Semanal | ___ |
| HIG-05 | Una persona revisa una muestra contra la realidad (llamar o preguntar al responsable) | Muestra de ___ filas | Mensual | ___ |

## 4. Meta de calidad

`KPI-12` (porcentaje de oportunidades activas con responsable, etapa, importe y siguiente paso válidos): línea base ___ → meta ___ para ___ (**Supuesto** hasta medir).

## 5. Valores que se muestran como "Sin registro"

Qué hacer cuando un dato no se conoce: ___ (nunca se inventa).
