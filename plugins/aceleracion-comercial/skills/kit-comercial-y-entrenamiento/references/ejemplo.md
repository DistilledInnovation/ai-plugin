# Ejemplo: Kit comercial y entrenamiento de una firma contable ficticia

Empresa inventada: **Brújula Contadores** (6 personas; 62 clientes activos; ticket mensual promedio de unos USD 210). Todo lo siguiente es ficticio. Continúa el ejemplo de `crm-y-tableros`: registro en hoja de cálculo desde el 26 de octubre de 2026 (`DEC-05`), `ETA-01` a `ETA-07` con sus responsables, `REG-01` a `REG-03`, `OFE-01` (Paquete Tranquilidad, USD 240 al mes) y `OFE-02` (Paquete Consultorio, USD 190 al mes), `HAL-06` a `HAL-08`, `PRO-03`, `OBJ-03` (cierres por alguien distinto de la socia fundadora, de 22 % a 50 %), `PRU-01` y `SUP-02`. Fecha de inicio: lunes 2 de noviembre de 2026.

## Turno 1

**Facilitador:** Vamos con la etapa 5. ¿Qué le dijiste la última vez que un cliente te dijo que no, y qué habrías querido responder?

## Turno 2

**Usuaria (socia fundadora):** Una agencia me dijo "me sale más barato mi contador de siempre" y yo bajé el precio sin preguntar nada. Con una tienda de ropa, que dijo que lo consultaban con su socio, no volví a escribir. Y la asistente no sabe qué decir cuando alguien pregunta si hacemos nómina.

**Facilitador:** Anoto tres patrones (**Hecho**, dicho por la socia): bajar el precio sin preguntar, no dejar fecha después de "lo consulto con mi socio" y falta de respuesta clara sobre lo que no incluye la oferta. Propongo un kit pequeño con lo que ya existe: ICP, oferta, etapas y la evidencia `HAL-07` y `HAL-08`.

## Turno 3: playbook (extracto)

| ID | Etapa | Actor | Canal | Mensaje | Evidencia | Estado |
|---|---|---|---|---|---|---|
| `MSG-01` | `ETA-01` o `ETA-02` | `ACT-01` (socio gerente de una agencia) | Correo o mensaje | "Hola, soy de Brújula Contadores. Trabajamos con agencias y estudios creativos: entregamos el cierre contable el día 8 de cada mes y respondemos en un día hábil. ¿Te sirve una llamada de 20 minutos esta semana para ver cómo lo manejas hoy?" | 171 de 186 cierres a tiempo en tres meses (`HAL-08`) | **Hecho** (cierres); respuesta en un día hábil **Pendiente por validar** (no hay registro de consultas) |
| `MSG-02` | `ETA-02` | `ACT-01` referido por un cliente (`ACT-05`) | Llamada | "Nos dio tu contacto [referidor]; dice que te interesa ordenar tus números. ¿Te cuento en dos minutos qué hacemos?" | Dicho por el referidor | **Supuesto** |

Roles (de la etapa 3): la asistente administrativa lleva `ETA-01` a `ETA-02`, la contadora senior califica en `ETA-03`, la socia o el socio hacen el descubrimiento con la contadora, y los socios presentan y negocian. Regla de descuentos (`DEC-06`): solo un socio puede aprobar, hasta 10 % y a cambio de contrato de 12 meses; se anota en el registro (`CAM-17` en caso de pérdida).

## Turno 4: guiones

| ID | Conversación | Quién | Duración | Estructura |
|---|---|---|---|---|
| `GUI-01` | Contacto inicial | Asistente administrativa | 5 min | Motivo en una frase, una pregunta sobre cómo lo manejan hoy, propuesta de llamada |
| `GUI-02` | Calificación (BANT en conversación) | Contadora senior | 10 min | "¿Qué te frustra hoy con tu contador?" (necesidad), "¿Quién más decide?" (autoridad), "¿En qué rango estás pensando para esto?" (presupuesto), "¿Para cuándo lo quieres resuelto?" (tiempo) |
| `GUI-03` | Descubrimiento | Socio o socia con la contadora senior | 30 min | Volumen aproximado de movimientos, situación con su contador actual, fecha deseada de inicio |
| `GUI-04` | Presentación y cierre | Socio de impuestos o socia | 20 min | Resumen en palabras del cliente, qué incluye y qué no, precio, fecha de decisión y siguiente paso con fecha |
| `GUI-05` | Seguimiento | Quien lleva la oportunidad | 5 min | Aporte nuevo, pregunta por la decisión, siguiente paso |

Cada guion termina con "Entonces quedamos en que [quién] hace [qué] el [fecha]".

## Turno 5: cadencia

| ID | Día | Canal | Propósito | Si no responde |
|---|---|---|---|---|
| `CAD-01` | 0 | Reunión | Presentar propuesta y acordar fecha de respuesta | n/a |
| `CAD-01` | 2 | Correo | Resumen de la propuesta con una sola pregunta | Día 5 |
| `CAD-01` | 5 | Llamada breve (`GUI-05`) | Resolver dudas y ubicar al decisor | Día 9 |
| `CAD-01` | 9 | Correo | Aporte nuevo: qué cambiaría en fecha de cierre y respuesta | Día 14 |
| `CAD-01` | 14 | Llamada o correo | "¿Cierro esta conversación o prefieres retomarla más adelante?" | Día 16: perdida con motivo "sin respuesta"; si aplica, nutrir |

El umbral de 14 días coincide con la regla de estancamiento de la etapa 3. `CAD-02` (nutrir, `REG-02`): contactos a los 30, 60 y 90 días con un aporte distinto; a los 90 días se cierra. `CAD-03`: agradecer a quien recomendó dentro de dos días hábiles de contactar al lead. Revisión de la cadencia: mensual (`PRO-03` tenía 2 propuestas perdidas sin respuesta).

## Turno 6: matriz de objeciones

**Facilitador:** ¿Cuáles son las tres objeciones que más escuchas y qué prueba real tienes para cada una?

**Usuaria:** Que ya tienen contador y sale más barato; que lo van a consultar con su socio; y que no están seguros de si atrasaremos su cierre.

| ID | Tipo | Frase del cliente | Qué puede haber detrás (**Supuesto**) | Pregunta para entender | Respuesta honesta | Evidencia | Qué no hacer |
|---|---|---|---|---|---|---|---|
| `OBC-01` | Precio y alternativas | "Ya tengo contador y me sale más barato" | Compara solo precio mensual, no el costo de cierres tardíos | "¿Cuándo te entrega hoy el cierre y cuánto tardan en responderte?" | "Si hoy te entregan a tiempo y te responden, quizá no necesitas cambiar. Si no, nosotros entregamos el día 8 y respondemos en un día hábil." | `HAL-07` (6 de 9 cambiaron por demoras), `HAL-08` (92 % a tiempo); que el segmento pague USD 240 sigue **Pendiente por validar** al 6 de noviembre (`SUP-02`; `PRU-01` se revisa el 23 de noviembre) | Bajar el precio sin preguntar; criticar al contador actual |
| `OBC-02` | Urgencia | "Lo vemos en enero" | Sin dolor reciente o fecha clara | "¿Qué tendría que pasar antes para que lo veas antes?" | Se respeta la fecha y se agenda una cadencia `CAD-02`; no se crea urgencia falsa | Disparadores de compra observados (`HAL-06`: multa, financiamiento, contratación) **Dicho por participante**; costo de esperar **Pendiente por validar** | Inventar un plazo o una multa |
| `OBC-03` | Autoridad | "Tengo que consultarlo con mi socio" | `ACT-01` no es el único decisor | "¿Qué le va a preguntar tu socio? ¿Hacemos 20 minutos los tres?" | Se ofrece una reunión conjunta y se acuerda fecha | Mapa de actores (`ACT-01` a `ACT-04`) | Terminar sin fecha o sin hablar con el socio |
| `OBC-04` | Riesgo | "¿Y si se atrasan con mi cierre?" | Miedo a cambiar de contador y quedar peor; contrato de seis meses | "¿Qué te preocupa más: el atraso, un error o quedarte atado?" | "No prometemos cero errores. Prometemos el día 8 y una respuesta en un día hábil, y lo medimos." | `HAL-08`; una salida sin penalidad al tercer mes como forma de reducir el riesgo es una hipótesis (`SUP-03`, **Pendiente por validar**) | Prometer cero errores |

Las objeciones de urgencia y riesgo no tienen aún prueba propia suficiente: la respuesta lo dice con claridad. La conversación sobre qué no incluye (nómina) se resuelve con la sección "no incluye" de `OFE-01`, que ya existe.

## Turno 7: plan de entrenamiento y competencias

| ID | Semana | Tema | Conversación real que se ensaya | Competencia |
|---|---|---|---|---|
| `ENT-01` | 1 (2 al 6 de nov) | Calificación con `GUI-02` (asistente y contadora senior) | `OPO-02`: comercio que debió descartarse | `COM-01` |
| `ENT-02` | 2 (9 al 13 de nov) | Descubrimiento con `GUI-03` (contadora senior y analista de impuestos como observadora) | `OPO-03`: estudio de animación | `COM-02` |
| `ENT-03` | 3 (16 al 20 de nov) | Presentación y objeciones `OBC-01` y `OBC-03` (socio de impuestos y contadora senior; la socia hace de cliente) | Una de las 3 propuestas perdidas por precio (`HAL-04`) | `COM-03`, `COM-04` |
| `ENT-04` | 4 (23 al 27 de nov) | Seguimiento con `CAD-01` y registro (asistente y analista) | Las dos propuestas perdidas sin respuesta | `COM-05` |

Coaching quincenal los viernes 13 y 27 de noviembre: revisión de tres conversaciones reales cada vez, solo con permiso de quien participó (se pide al inicio de la llamada; si no, se revisan las notas). Cada ensayo se complementa con 15 minutos de simulación con un asistente de IA que hace de cliente; lo que dice la IA es **Inferencia de la IA** y la retroalimentación la confirma una persona. Competencias en tres niveles (`COM-01` calificar con BANT, `COM-02` descubrir, `COM-03` presentar valor con evidencia, `COM-04` manejar una objeción, `COM-05` dar seguimiento y registrar); la evaluación del lunes 30 de noviembre usa conversaciones reales de la hoja de revisión.

| Persona | Competencia | Nivel al 30 de noviembre | Evidencia |
|---|---|---|---|
| Contadora senior | `COM-01` | 3 | Calificó 3 de 3 llamadas con `GUI-02` y `REG-01` |
| Contadora senior | `COM-02` | 2 | Descubrimiento con apoyo del socio |
| Socio de impuestos | `COM-04` | 2 | Respondió `OBC-03` con fecha; no preguntó en `OBC-01` |
| Asistente administrativa | `COM-05` | 3 | Siguiente paso fechado en todas sus oportunidades |

## Turno 8: uso en ventas reales

Entre el 16 y el 27 de noviembre se revisaron 6 conversaciones reales (3 de calificación, 2 de presentación y 1 de seguimiento): 5 usaron el guion y terminaron con siguiente paso fechado; en 1 de presentación el cierre quedó sin fecha (**Hecho**, hoja de revisión). **Pendiente por validar:** que `OBJ-03` suba de 22 % a 50 %; se mide con ventas cerradas, no con simulaciones. Decisión `DEC-06`: el playbook versión 1, la regla de descuentos y el plan quedan adoptados; el dueño del kit es la contadora senior y se revisa cada mes con los motivos de pérdida. Riesgo `RIE-04`: que los guiones se lean como texto; mitigación: el coaching evalúa las preguntas hechas, no las frases dichas.

**Facilitador:** Siguiente paso (**Recomendación**): `canales-y-generacion-de-demanda`, porque el kit ya funciona y el 64 % de los leads sigue llegando por recomendaciones (`HAL-02`, `PRO-02`). ¿Seguimos?

## Qué quedó claro del ejemplo

- El kit salió de conversaciones reales y de la evidencia que ya existía (`HAL-07`, `HAL-08`).
- Dos objeciones quedaron con respuesta honesta y la evidencia que falta marcada como pendiente.
- La regla de descuentos y la cadencia cierran los dos huecos que se detectaron (`PRO-03`).
- La práctica usó casos reales del equipo, con permiso para revisar conversaciones.
- La mejora en ventas (`OBJ-03`) se declaró pendiente: la capacitación no se mide solo con simulaciones.
