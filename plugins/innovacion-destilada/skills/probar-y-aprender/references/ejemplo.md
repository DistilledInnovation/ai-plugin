# Ejemplo: registrar resultados y decidir en una empresa de transporte ficticia

Empresa inventada: **Transportes Marea Azul** (carga refrigerada regional, 65 empleados, 22 camiones). Continúa el ejemplo de `validar-supuestos-y-mvp`. Todo es ficticio, incluidas las cifras.

Entrada: tarjeta `PRU-03` (prueba `SUP-05`: a los clientes les basta un aviso temprano). Mensaje de texto enviado a mano a 3 jefes de logística durante una semana de cargas reales. Métrica de éxito fijada antes: al menos 2 de los 3 dicen qué harán con la carga sin pedir más datos. Regla de Paula: con 2 o 3 continúa; con 1 itera; con 0 replantea.

## Turno 1: reunir y enlazar

**Facilitador:** Tengo la tarjeta `PRU-03` con su meta, fijada antes de probar. Primera pregunta: ¿qué resultado obtuviste, en números?

**Usuaria (Paula, gerente comercial):** Julio mandó 5 avisos en la semana. Solo uno de los tres clientes, Julián, dijo qué iba a hacer con la carga, y lo dijo en 4 minutos. Otro pidió más datos y el tercero ni lo leyó.

**Facilitador:** Siguiente pregunta: ¿cuántas personas participaron en realidad?

**Usuaria:** Los tres jefes de logística recibieron avisos, pero 3 de los 5 salieron de madrugada.

**Facilitador:** Siguiente pregunta: ¿dónde quedó el registro de ese resultado?

**Usuaria:** Julio anotó cada aviso con hora y mi llamada con cada cliente en una hoja de despacho. Tengo esa hoja.

## Turno 2: comparar

**Facilitador:** Entonces, como hecho: la meta era 2 de 3 y el resultado fue 1 de 3. No se alcanzó la meta. La evidencia es la hoja de despacho (Evidencia). Siguiente pregunta: ¿por qué crees que salió así?

**Usuaria:** El mensaje decía solo "frío fuera de rango". No decía cuánto ni qué hacer. Y los de madrugada nadie los vio.

**Facilitador:** Anoto esas dos explicaciones como Supuestos de Paula, pendientes de confirmar con otra prueba. Siguiente pregunta: ¿qué aprendiste que no sabías antes de probar?

**Usuaria:** Que un aviso no basta si no dice qué hacer, y que la hora del aviso importa.

## Turno 3: decidir

**Facilitador:** Las cuatro salidas posibles son perseverar, iterar, pivotar y detener. Tu regla de la tarjeta decía que con 1 de 3 se itera. Con este resultado, ¿qué decisión quieres tomar?

**Usuaria:** Iterar: el mensaje dirá la temperatura y qué hacer, y probamos solo con avisos de día para separar los dos efectos.

**Facilitador:** Registrado como `DEC-08`: iterar `PRU-03`, decidido por Paula. Razón (dicha por ella): el mensaje no decía qué hacer y la hora afectó la lectura. Siguiente pregunta: ¿qué hipótesis arriesgada es la siguiente que quieres probar?

**Usuaria:** La misma, con el mensaje mejorado. Después, `SUP-08`, el recargo.

## Turno 4: las seis métricas (un turno por pregunta, resumen)

**Facilitador:** Con una prueba ya hecha, miremos las seis métricas. Primera pregunta: ¿qué tan alineada está esta idea con la estrategia de tu empresa y con tus objetivos?

**Usuaria:** Mucho: este año queremos dejar de perder clientes por el frío.

*(Siguen, una por turno: Encaje Problema/Solución en dos turnos, Tracción, KPI, Viabilidad Económica en dos turnos y Encaje Producto/Mercado en tres. Paula responde con lo que tiene; donde no hay datos, queda sin datos.)*

## Entregable final

# Tablero de Validación: `CON-01`

Marea Azul, 2026-10-25, borrador 1.

**Momento 1: diseño**

| Prueba | Supuesto | Riesgo | Experimento | Muestra | Métrica de éxito | Meta fijada |
|---|---|---|---|---|---|---|
| PRU-03 | SUP-05 | Alto | Mensaje de texto a mano cuando el frío sale del rango | 3 jefes de logística, 1 semana | Al menos 2 de 3 dicen qué harán sin pedir más datos | Antes |

**Momento 2: resultado y decisión**

| Prueba | Resultado | Evidencia | ¿Se cumplió? (Hecho) | Explicación (Supuesto) | Aprendizaje | Decisión | Próximo paso |
|---|---|---|---|---|---|---|---|
| PRU-03 | 1 de 3 (Julián en 4 minutos); 5 avisos, 3 de madrugada | Hoja de despacho | No (1 frente a 2) | El mensaje no decía qué hacer; los avisos de madrugada no se leyeron | Un aviso sin instrucción no basta; la hora importa | `DEC-08` iterar | `PRU-04`: mensaje con temperatura e instrucción, solo avisos de día |

**Métricas de evaluación**

| Métrica | Dato | Estado | Procedencia |
|---|---|---|---|
| Afinidad Estratégica | Objetivo del año: dejar de perder clientes por el frío | Verde | Dicho por participante |
| Encaje Problema/Solución | Problema: 2 de 2 ex clientes citaron el frío (`HAL-06`). Solución: 1 de 3 decidió con el aviso (`PRU-03`) | Amarillo | Evidencia |
| Tracción | Nadie ha pagado todavía | Sin datos | Pendiente por validar |
| KPI | Sin medición de costo de adquisición ni retención | Sin datos | Pendiente por validar |
| Viabilidad Económica | Sin ingresos ni costos reales del servicio | Sin datos | Pendiente por validar |
| Encaje Producto/Mercado | Sin evidencia de captura de valor ni repetibilidad | Sin datos | Pendiente por validar |

**Bitácora**

| ID | Prueba y resultado | Decisión | Razón (dicha por Paula) | Decidió | Siguiente paso |
|---|---|---|---|---|---|
| DEC-08 | `PRU-03`: 1 de 3 frente a meta de 2 de 3 | Iterar | El mensaje no decía qué hacer y la hora afectó la lectura | Paula | `PRU-04`, luego `SUP-08` |

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RIE-05 | Dos explicaciones mezcladas (contenido y hora del aviso) | No se sabría cuál pesó | Probar solo avisos de día en `PRU-04` |

Pendientes por validar: las dos explicaciones de Paula; tracción, KPI, viabilidad y encaje producto/mercado.

Siguiente paso sugerido: volver a `validar-supuestos-y-mvp` para la tarjeta de `PRU-04`; cuando haya clientes que paguen, `modelo-de-negocio-y-escalamiento`.

## Lo que se ve en este ejemplo

- Una pregunta por turno, también al comparar y al decidir.
- La comparación con la meta es un hecho; la explicación de la persona es un supuesto.
- La decisión es de la persona, registrada con su razón (`DEC-08`).
- Las métricas sin datos se dejan sin datos: no se estiman.
- Un resultado negativo se convierte en la siguiente prueba, no en un fracaso.
