# Ejemplo: Canales y generación de demanda de una firma contable ficticia

Empresa inventada: **Brújula Contadores** (6 personas; 62 clientes activos; ticket mensual promedio de unos USD 210). Todo lo siguiente es ficticio. Continúa el ejemplo de `kit-comercial-y-entrenamiento`: `MSG-01` y `MSG-02`, `GUI-01` a `GUI-05`, `CAD-01` a `CAD-03`, `OBC-01` a `OBC-04`, `DEC-06`, `HAL-02` (54 de 84 leads por recomendación), `PRO-02` (dependencia de referidos y de la socia), `OBJ-01` y `OBJ-04`, `ICP-01`, `CUE-01` a `CUE-10` (todas cuentas sin contactar), `SUP-02` y `PRU-01`. Fecha de inicio: lunes 30 de noviembre de 2026.

## Turno 1

**Facilitador:** Vamos con la etapa 6. ¿Cómo llegaron tus últimos clientes y qué porcentaje viene de cada origen?

## Turno 2

**Usuaria (socia fundadora):** De los 84 leads de los seis meses: 54 por recomendación, 18 por el formulario de la página y 12 por redes. De los 9 clientes nuevos, 6 vinieron por recomendación, 2 por la página y 1 por redes. Lo saco de la columna de origen que la asistente llena desde el 26 de octubre y de la hoja anterior.

**Facilitador:** Anoto el origen real (**Hecho**, hojas de seguimiento; la columna de origen de la hoja anterior es **Estimada** para los 84):

| Origen | Leads | Ganados | Lead a venta | Calidad del dato |
|---|---|---|---|---|
| Recomendación | 54 | 6 | 11,1 % | Contada para ganados, estimada para leads |
| Formulario de la página | 18 | 2 | 11,1 % | Contada |
| Redes | 12 | 1 | 8,3 % | Contada |
| Total | 84 | 9 | 10,7 % | Contada |

Los tres orígenes convierten parecido; lo que cambia es el volumen y la dependencia de uno solo (`PRO-02`). **Supuesto** (**Pendiente por validar**): con pocos datos por origen no hay diferencia real entre canales.

## Turno 3: plan de canales

**Facilitador:** ¿Cuántas horas por semana y cuánto dinero puedes dedicar a esto de forma sostenida, sin descuidar los cierres del día 8?

**Usuaria:** Seis horas por semana: cuatro de la asistente administrativa y dos mías. Hasta USD 150 al mes; sin anuncios pagos por ahora.

| ID | Canal | ¿El `ICP-01` busca o pregunta aquí? | Papel | Decisión | Motivo |
|---|---|---|---|---|---|
| `CAN-01` | Recomendaciones de clientes actuales | Sí: 6 de 9 ganados vinieron por recomendación (**Hecho**) | Generar y convertir | Priorizar | Mayor evidencia y costo bajo; hoy es pasivo |
| `CAN-02` | Alianzas con asesores legales y consultores de marketing que atienden agencias | Quizá: `ACT-04` influenciador (**Supuesto**) | Generar | Probar en pequeño | Sin evidencia propia todavía |
| `CAN-03` | Contacto directo a la lista de cuentas (`CUE-01` a `CUE-10` y diez más del perfil) | Parcial: dos ganados llegaron por la página, ninguno por contacto directo | Generar | Priorizar con experimento | Es el único canal que se controla por completo |
| `CAN-04` | Formulario de la página | Sí: 18 leads y 2 ganados | Convertir | Mantener, sin esfuerzo nuevo | Funciona, solo se afina el mensaje con la hoja comercial |
| `CAN-05` | Redes | Poco: 12 leads y 1 ganado | Generar | Pausar | La calidad del lead es la más baja y consume horas |

Prioridad: `CAN-01`, `CAN-03` y `CAN-02` (en pequeño). Decisión `DEC-07`: el plan queda así y `CAN-05` se pausa hasta el reporte de experimentos. Cada lead entra a la hoja con origen, fecha y responsable (`CAM-04`).

Meta de demanda (**Supuesto**): para pasar de 62 a 80 clientes (`OBJ-04`) hay que sumar 18 netos y reponer unas 10 bajas en 12 meses (5 bajas en 6 meses, `HAL-01`): unas 28 ventas. Con una conversión de lead a venta de 15 % (`OBJ-01`), eso pide unos 187 leads en 12 meses, o 16 por mes (hoy son 14). La meta de demanda es modesta si la conversión mejora; si no mejora, hace falta más volumen.

## Turno 4: calendario semanal (6 horas)

| Día | Actividad | Canal | Responsable | Volumen | Tiempo |
|---|---|---|---|---|---|
| Lunes | Cinco contactos a la lista de cuentas con borradores revisados por la socia | `CAN-03` | Asistente administrativa | 5 contactos | 1 h |
| Martes | Cinco contactos y registro en la hoja Prospección | `CAN-03` | Asistente administrativa | 5 contactos | 1 h |
| Miércoles | Pedir recomendación a clientes por llamada breve (`MSG-02`) | `CAN-01` | Socia fundadora | 3 clientes | 1 h |
| Jueves | Seguimiento de respuestas, agendar reuniones y registrar | `CAN-03` | Asistente administrativa | Todas las respuestas | 1 h |
| Viernes | Revisión de números de la semana, borradores de la próxima y 2 llamadas de recomendación | `CAN-01` | Socia y asistente | 2 clientes | 2 h (1 h cada una) |

Riesgo `RIE-05`: la prospección compite con el cierre del día 8 (`RIE-02`); mitigación: del día 5 al 8 de cada mes se pausa el contacto directo y se mantiene solo el seguimiento de respuestas.

## Turno 5: experimentos (Tablero de Validación)

Cada experimento se registra en el Tablero de Validación de `probar-y-aprender` (hipótesis, métrica, umbral y decisión). Métricas fijadas el lunes 30 de noviembre, **antes** de lanzar.

| Experimento | Prueba y supuesto | Hipótesis | Muestra y fechas | Métrica y umbral | Regla de decisión |
|---|---|---|---|---|---|
| `EXP-01` | `PRU-02`, `SUP-04` (las agencias y estudios responden a un mensaje directo con el dato del día 8) | `MSG-01` por correo y llamada a cuentas del `ICP-01` | 20 cuentas (`CUE-01` a `CUE-10` y diez más), del 1 al 18 de diciembre | Al menos 4 respuestas de 20 (20 %) y al menos 2 reuniones realizadas | Cumple: escalar a 10 contactos por semana. 1 reunión: ajustar el mensaje una vez. 0: detener |
| `EXP-02` | `PRU-03`, `SUP-05` (si se pide una recomendación concreta, los clientes entregan un contacto) | Llamada breve a clientes activos del perfil con `MSG-02` | 20 clientes, del 30 de noviembre al 23 de diciembre | Al menos 6 de 20 (30 %) entregan un contacto | Cumple: dejarlo en la rutina. 3 a 5: ajustar el momento de la petición. Menos de 3: detener |
| `EXP-03` | `PRU-04` (una alianza produce leads) | Conversaciones con 3 aliados (un estudio jurídico, una consultora de marketing y un asesor financiero) | 3 conversaciones en diciembre, revisión el 8 de enero | Al menos 1 lead recomendado en 6 semanas | Cumple: ampliar a 3 aliados más |

Se agrega el cierre retrospectivo de `PRU-01` (precio): seis propuestas de `OFE-01` desde el 2 de noviembre; métrica fijada antes: al menos 2 de las 6 avanzan sin descuento de más de 10 %. Revisión el lunes 23 de noviembre: 3 de 6 cumplieron (**Hecho**, n = 6). `SUP-02` queda **sostenida con una muestra pequeña**, sin generalizarla.

## Turno 6: atribución (extracto)

| ID | Regla |
|---|---|
| `REA-01` | Un solo origen por lead: el primer contacto |
| `REA-02` | Si es recomendación, se anota quién recomendó (`CAM-22`) |
| `REA-03` | Si responde a una campaña, el origen es el canal de la campaña (`CAN-nn`) |
| `REA-04` | Sin origen conocido se marca "Sin origen" y es un error de higiene |

Caso real: la agencia de marketing de `OPO-05` entró por recomendación y luego llenó el formulario; el origen es recomendación (primer contacto), el formulario va como nota.

## Turno 7: reporte de experimentos (martes 23 de diciembre de 2026)

| Experimento | Métrica y umbral (fijado antes) | Resultado | ¿Cumplió? | Esfuerzo | Decisión |
|---|---|---|---|---|---|
| `EXP-01` | 4 de 20 respuestas y 2 reuniones | 7 respuestas de 20 (35 %) y 3 reuniones realizadas | Sí (**Hecho**, hoja Prospección) | 12 horas de la asistente | `DEC-08`: escalar a 10 contactos por semana desde el lunes 4 de enero |
| `EXP-02` | 6 de 20 entregan un contacto | 5 de 20 (25 %) entregaron 7 contactos | No (por un cliente) | 5 horas de la socia | `DEC-09`: ajustar una vez: pedirlo en la lectura trimestral y no por llamada breve; repetir en enero |
| `EXP-03` | 1 lead en 6 semanas | Pendiente (revisión el 8 de enero) | Pendiente por validar | 3 horas de la socia | Sin decisión todavía |

Aprendizaje (**Hecho**): el mensaje con el dato del día 8 genera respuestas; con 20 cuentas es una muestra pequeña. Explicación del `EXP-02` (**Supuesto**): los clientes entregan contactos cuando la persona está en una conversación y no a una petición suelta. Mejoras para la etapa 7 (`BAC-nn`): registrar el esfuerzo por canal en una hoja para medir `KPI-08` y `KPI-11`, y reevaluar `CAN-05` en marzo.

El mecanismo repetible queda así: un responsable por canal (asistente para `CAN-03`, socia para `CAN-01`), una rutina semanal de 6 horas y datos de efectividad de un ciclo. Riesgo `RIE-05` se mantiene bajo control porque la prospección se pausa del día 5 al 8.

**Facilitador:** Siguiente paso (**Recomendación**): `gobierno-comercial-y-forecast`, para que la revisión semanal, el forecast y el manual sostengan el sistema sin depender de mí. ¿Seguimos?

## Qué quedó claro del ejemplo

- El origen de los clientes salió de datos propios, con la calidad del dato declarada.
- Se priorizaron tres canales y se pausó uno con motivo.
- Cada experimento tuvo métrica y umbral fijados antes, y uno no cumplió y se registró sin dramatizar.
- La muestra pequeña se declaró y nadie prometió resultados.
- El calendario cabe en seis horas y protege el cierre del día 8.
