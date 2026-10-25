# Ejemplo: Proceso de ventas y pipeline de una firma contable ficticia

Empresa inventada: **Brújula Contadores** (6 personas; 62 clientes activos; ticket mensual promedio de unos USD 210). Todo lo siguiente es ficticio. Continúa el ejemplo de `oferta-y-propuesta-de-valor`: `OFE-01` (Paquete Tranquilidad, `ICP-01`), `OFE-02` (Paquete Consultorio, `ICP-02`), `PRO-03` (sin seguimiento sistemático), `BAC-03` y `OBJ-02` (siguiente paso fechado, de 36 % a 90 %).

## Turno 1

**Facilitador:** Vamos con `BAC-03`. ¿Cómo pasó tu última venta desde la primera señal hasta la activación del cliente, y dónde se detuvo la anterior?

## Turno 2

**Usuaria (socia fundadora):** La agencia de contenidos: un cliente nos recomendó, la asistente le contestó el mismo día, yo hice una reunión de 30 minutos, mandé propuesta a los dos días y a la semana firmó. La anterior fue una tienda de ropa: mandé propuesta, me dijeron que la veían y no volví a escribir.

**Facilitador:** Con esos recorridos propongo siete etapas, con regla de entrada y dato obligatorio. Las reglas son verificables: lo que el cliente hizo, no lo que sentimos.

## Turno 3: etapas y definiciones

| ID | Etapa | Regla de entrada | Dato obligatorio | Responsable | Tiempo máximo |
|---|---|---|---|---|---|
| `ETA-01` | Lead identificado | Cumple `ICP-01` o `ICP-02` y no cae en las exclusiones | Segmento y origen (recomendación, página, redes o contacto directo) | Asistente administrativa | Contactar en 2 días hábiles |
| `ETA-02` | Primer contacto | Hay contacto válido o respuesta | Contacto, fecha y canal | Asistente administrativa | 5 días hábiles para obtener respuesta; si no, nutrir |
| `ETA-03` | Oportunidad calificada | Puntaje BANT con `REG-01` cumplida | Dolor, actor (`ACT-01` identificado) y siguiente paso con fecha | Contadora senior | 3 días hábiles tras el contacto para agendar |
| `ETA-04` | Diagnóstico y solución | Reunión de 30 minutos realizada con `ACT-01` o `ACT-04` | Volumen aproximado de movimientos, situación con su contador actual y fecha deseada de inicio | Socia o socio con la contadora senior | 7 días hábiles |
| `ETA-05` | Propuesta presentada | Propuesta revisada por un socio, enviada y presentada con una siguiente acción acordada | Monto, fecha, paquete (`OFE-nn`) y fecha de seguimiento | Socia o socio de impuestos | 2 días hábiles tras la reunión |
| `ETA-06` | Negociación y decisión | El cliente respondió y se conocen condiciones, decisores y fecha esperada | Decisores, riesgo y fecha esperada | Socia o socio de impuestos | 14 días |
| `ETA-07` | Ganado o perdido | Contrato firmado o motivo de pérdida registrado | Valor mensual o motivo (frase del cliente) | Quien llevó la oportunidad | Registrar en 1 día hábil |

Umbral de estancamiento: 14 días sin avance (el mismo de la línea base, para comparar `KPI-07`). Motivos de pérdida: precio, no era el perfil, eligió a otro, momento, sin respuesta, otro. Ganado dispara el traspaso a incorporación del cliente.

## Turno 4: calificación (BANT simplificado)

**Facilitador:** ¿Qué tendría que ser cierto de una empresa para que valga la pena mandarle propuesta?

**Usuaria:** Que tenga un problema real con su contador o con sus impuestos, que pueda pagar al menos unos USD 150 al mes, que hable con quien decide y que quiera empezar en uno o dos meses.

| Criterio | Pregunta | Sí (2) | Parcial (1) | No (0) |
|---|---|---|---|---|
| Presupuesto | ¿Puede pagar al menos USD 150 al mes? | Rango dicho o claro por su facturación | Dudoso | Muy inferior |
| Autoridad | ¿Hablamos con quien decide? | Habla el decisor | Hay acceso | Sin acceso |
| Necesidad | ¿Hay un dolor concreto con su contador o impuestos? | Dolor reconocido (cierre tardío, multa, sin respuesta) | Interés general | Ninguno |
| Tiempo | ¿Quiere empezar en uno o dos meses? | Fecha o motivo para actuar | Sin fecha | Sin urgencia |

`REG-01` calificada (pasa a `ETA-03`): Necesidad en Sí y total de 5 o más sobre 8. `REG-02` nutrir: total de 3 o 4, o Necesidad en Parcial con total de 5 o más (por ejemplo 1+2+2+2 = 7: hay presupuesto, acceso y fecha, pero el dolor no está claro), con revisión en 30 a 60 días hasta aclarar la necesidad. `REG-03` descartar: Necesidad en No o total de 2 o menos, o cae en una exclusión de `ICP-01`. Preguntas MEDDICC opcionales (solo si hay varios socios decidiendo o un ticket mayor a USD 400 al mes): métricas, comprador económico, criterios de decisión, proceso de decisión, dolor, campeón y competencia.

## Turno 5: prueba con casos reales

| Oportunidad | Resultado | Etapa | ¿Una sola etapa? | Ajuste |
|---|---|---|---|---|
| `OPO-01` Agencia de contenidos (9 personas; firmó en septiembre, fuera de la lista de cuentas) | Ganada, USD 210 al mes (firmada antes de definir `OFE-01`) | `ETA-07` | Sí | Ninguno |
| `OPO-02` Comercio minorista pequeño (una de las 7 perdidas por perfil) | Perdida: no era el perfil (exclusión de facturación formal) | `ETA-07` | Sí | Debió descartarse en `ETA-01` con `REG-03`; se agrega la revisión de exclusiones en `ETA-01` |
| `OPO-03` Estudio de animación (12 personas; una de las 11 oportunidades abiertas, fuera de la lista de cuentas) | Abierta: propuesta presentada, siguiente acción una llamada el viernes 30 de octubre de 2026 | `ETA-05` | Sí | Ninguno |

**Nota de definiciones.** En la línea base de la etapa 0, "oportunidad" es una reunión realizada; en este pipeline, "Oportunidad calificada" (`ETA-03`) se alcanza antes de la reunión. Para que `KPI-04`, `KPI-05` y `KPI-07` sigan siendo comparables, se conserva la definición de la línea base (reunión realizada, es decir `ETA-04` o posterior) y las calificadas se miden como un indicador nuevo. Decisión `DEC-04`.

## Turno 6: manual y prueba de la persona nueva

El manual corto de dos páginas incluye ICP, oferta, las siete etapas, la regla BANT, las reglas fijas (siguiente paso con fecha, motivo de pérdida, avance solo cuando el cliente hace algo) y la hoja de seguimiento mínima. La analista de impuestos, que no participó, lo lee y lo explica: ubica bien `OPO-01` y `OPO-03`, pero confunde `ETA-03` con `ETA-04`.

**Facilitador:** Eso indica una definición floja, no un problema de la analista. Propongo agregar un ejemplo a cada etapa: `ETA-03` es "tiene dolor y presupuesto, aún no hubo reunión"; `ETA-04` es "la reunión ya se hizo".

Decisión `DEC-03`: el equipo adopta las siete etapas, `REG-01` a `REG-03` y el umbral de 14 días. Datos pendientes: contar el valor de `KPI-07` y `KPI-12` a los 30 días de uso (**Pendiente por validar** que `OBJ-02` se alcance). Hasta que exista el registro de la etapa 4, se usa una hoja de cálculo con una fila por oportunidad y las columnas del manual.

**Facilitador:** Siguiente paso (**Recomendación**): `crm-y-tableros` (etapa 4, Próximamente: todavía no está disponible). Mientras tanto, la hoja de cálculo mínima alcanza, y yo puedo ayudarte a construir los campos como borrador. ¿Empezamos con la hoja?

## Qué quedó claro del ejemplo

- Cada regla de entrada se puede verificar con un dato anotado.
- La calificación BANT quedó escrita con una regla de decisión y MEDDICC solo se usa en ventas complejas.
- La prueba con tres oportunidades reales mostró un ajuste (exclusiones en `ETA-01`).
- La prueba de la persona nueva reveló una definición floja y se corrigió con ejemplos.
- La siguiente etapa (CRM) está Próximamente, y el ejemplo lo dice con honestidad y propone un mínimo viable en una hoja.
