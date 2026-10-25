# Ejemplo: validar supuestos y definir el MVP en una empresa de transporte ficticia

Empresa inventada: **Transportes Marea Azul** (carga refrigerada regional, 65 empleados, 22 camiones). Continúa el ejemplo de `disenar-prototipo`. Todo es ficticio, incluidas las cifras.

Entrada: `CON-01` "Aviso de frío y vista de la carga"; prototipo de simulación manual con su guion de prueba; supuestos `SUP-05` (a los clientes les basta un aviso temprano) y `SUP-06` (se puede medir el frío durante todo el viaje), ambos Pendientes por validar.

## Turno 1: supuestos nuevos (comportamiento)

**Facilitador:** Tengo `CON-01`, el prototipo y los supuestos `SUP-05` y `SUP-06`. Primera pregunta: ¿qué estás dando por cierto sobre lo que hará el cliente al recibir el aviso que, si fuera falso, tumbaría tu solución?

**Usuaria (Paula, gerente comercial):** Que va a leerlo y decidir qué hacer con la carga en pocos minutos. Si el aviso queda sin leer, no sirve de nada.

**Facilitador:** Anotado `SUP-07`: el jefe de logística lee el aviso y decide qué hacer en pocos minutos (Supuesto, dicho por participante). Siguiente pregunta: ¿qué estás dando por cierto sobre el dinero que entra y el que sale con este servicio?

**Usuaria:** Que pagarían un recargo por tener el aviso.

**Facilitador:** Anotado `SUP-08`: los clientes pagarían un recargo por el servicio (Supuesto, dicho por participante). Con eso hay cuatro supuestos.

## Turno 2: calificar (un criterio por turno, resumen)

**Facilitador:** Empecemos con `SUP-05`. Si este supuesto fuera falso, ¿qué le pasaría a tu solución?

**Usuaria:** Que el aviso no cambiaría nada y todo el concepto se cae.

**Facilitador:** Siguiente pregunta: ¿qué evidencia real tienes hoy de que es cierto?

**Usuaria:** Solo una conversación, con Julián, que dijo que le habría servido enterarse antes.

**Facilitador:** Siguiente pregunta: ¿cuánto te costaría seguir adelante si estuvieras equivocada?

**Usuaria:** Meses de trabajo y el dinero de armar el sistema.

*(Se repite el mismo orden de tres preguntas para `SUP-06`, `SUP-07` y `SUP-08`, un mensaje por pregunta.)*

## Turno 3: elegir el más riesgoso

**Facilitador:** Esta es mi lectura de tus respuestas, como Inferencia de la IA; corrígela donde no coincida:

| ID | Supuesto | Impacto si es falso | Certeza hoy | Costo de equivocarse |
|---|---|---|---|---|
| SUP-05 | A los clientes les basta un aviso temprano | Alto | Baja (1 conversación) | Alto |
| SUP-06 | Se puede medir el frío todo el viaje | Alto | Media (una prueba corta hecha por el taller) | Medio |
| SUP-07 | El jefe de logística decide en minutos | Medio | Baja | Bajo |
| SUP-08 | Pagarían un recargo | Medio | Baja | Medio |

¿Con cuál de estos supuestos quieres empezar a probar?

**Usuaria:** Con `SUP-05`: si no basta un aviso, lo demás no importa.

**Facilitador:** Registrado como `DEC-07`: se prueba primero `SUP-05`, decidido por Paula; `SUP-06`, `SUP-07` y `SUP-08` quedan en espera.

## Turno 4: la técnica

**Facilitador:** Ya tienes una simulación manual armada en la etapa anterior. ¿Qué es lo más barato que podrías hacer esta semana para saber si ese supuesto es cierto?

**Usuaria:** Usar esa simulación con cargas reales: Julio manda el mensaje de texto cuando un camión de verdad se acerque al límite de frío que el cliente fije, pero a mano, mirando un termómetro que ya tienen los conductores.

**Facilitador:** Es un concierge con simulación manual: nada de sistema. Lo que no tiene, a propósito: ningún sensor nuevo ni vista web.

## Turnos 5 a 8: alcance, método, criterio y regla (un dato por turno)

**Facilitador:** ¿A cuántas personas se lo vas a mostrar?

**Usuaria:** A tres jefes de logística de clientes actuales, durante una semana de cargas reales.

**Facilitador:** Siguiente pregunta: ¿cómo harías la prueba, paso a paso?

**Usuaria:** Cada cliente fija su rango de frío. Julio mira el termómetro del conductor cada hora y, si sale del rango, manda el mensaje con qué hacer. Yo llamo al cliente después a preguntarle qué decidió.

**Facilitador:** Siguiente pregunta: ¿qué resultado tendría que darte para que digas que acertaste?

**Usuaria:** Que al menos 2 de los 3 digan qué van a hacer con la carga sin pedir más datos.

**Facilitador:** Siguiente pregunta: si el resultado no llega a ese umbral, ¿qué harías?

**Usuaria:** Si es 1 de 3, cambio lo que dice el mensaje y repito. Si es 0 de 3, replanteo el concepto completo.

## Turno 9: la tarjeta

**Facilitador:** Esta es la tarjeta con tus palabras:

| | |
|---|---|
| **Creemos que…** | A los clientes les basta un aviso temprano para decidir qué hacer con la carga (`SUP-05`) |
| **Para verificarlo, haremos…** | Enviar a mano un mensaje de texto, cuando el frío salga del rango del cliente, a 3 jefes de logística durante una semana de cargas reales |
| **Y mediremos…** | Cuántos de los 3 dicen qué harán con la carga sin pedir más datos |
| **Acertamos si…** | Al menos 2 de los 3 lo hacen |

¿Esta tarjeta dice exactamente lo que quieres probar?

**Usuaria:** Sí, así está bien.

**Facilitador:** Registrada como `PRU-03`, prueba `SUP-05`.

## Turno 10: el MVP según Kniberg

**Facilitador:** Mira esta tabla: no de esta forma, una rueda, un chasis y luego un carro; sino de esta, una patineta, una bicicleta y luego un carro. ¿Qué versión de tu solución entregaría la necesidad completa, aunque sea de forma muy simple?

**Usuaria:** El mensaje a mano con la instrucción de qué hacer. Con eso el cliente ya sabe a tiempo y decide.

**Facilitador:** Eso cubre la necesidad completa (enterarse a tiempo y decidir), así que es una patineta: usable, manual y de la que aprendes. Un sensor sin aviso sería la rueda.

## Turno 11: riesgos y cierre

**Facilitador:** Veo un riesgo: si Julio está ocupado, el mensaje llega tarde y la prueba subestima el aviso. ¿Quién podría respaldar a Julio durante la semana de prueba?

**Usuaria:** Marcos, el otro despachador.

**Facilitador:** Anoto `RIE-04` con esa mitigación, propuesta por Paula. Siguiente pregunta: ¿cuándo vas a ejecutar esta prueba?

**Usuaria:** El martes.

## Entregable final

# Registro de supuestos y tarjeta de prueba: `CON-01`

Marea Azul, 2026-10-25, borrador 1.

| ID | Categoría | Supuesto | Impacto | Certeza | Costo | Estado | Procedencia |
|---|---|---|---|---|---|---|---|
| SUP-05 | Propuesta de valor | A los clientes les basta un aviso temprano | Alto | Baja | Alto | Priorizado (`DEC-07`) | Dicho por participante |
| SUP-06 | Factibilidad | Se puede medir el frío todo el viaje | Alto | Media | Medio | En espera | Supuesto |
| SUP-07 | Comportamiento | El jefe de logística decide en minutos | Medio | Baja | Bajo | En espera | Supuesto |
| SUP-08 | Viabilidad | Pagarían un recargo | Medio | Baja | Medio | En espera | Supuesto |

Calificación: Inferencia de la IA, corregida por Paula.

| | |
|---|---|
| **Creemos que…** | A los clientes les basta un aviso temprano (`SUP-05`) |
| **Para verificarlo, haremos…** | Mensaje de texto a mano a 3 jefes de logística durante una semana de cargas reales |
| **Y mediremos…** | Cuántos de los 3 dicen qué harán sin pedir más datos |
| **Acertamos si…** | Al menos 2 de los 3 |

| Si el resultado es… | Entonces… (decisión de Paula) |
|---|---|
| 2 o 3 de 3 | Continuar con `SUP-06` |
| 1 de 3 | Iterar: cambiar el mensaje y repetir |
| 0 de 3 | Replantear el concepto |

MVP (Kniberg): el aviso manual con instrucción es una patineta, no una rueda. Prueba `PRU-03`, ejecución el martes.

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RIE-04 | Que el mensaje llegue tarde si Julio está ocupado | La prueba subestima el aviso | Marcos, otro despachador, respalda a Julio |

Pendientes por validar: resultado de `PRU-03`; `SUP-06`, `SUP-07` y `SUP-08`.

Siguiente paso sugerido: `probar-y-aprender`, para registrar los resultados de `PRU-03` en el Tablero de Validación y decidir.

## Lo que se ve en este ejemplo

- Una pregunta por turno, también al calificar y al fijar alcance, método y criterio.
- La IA propone la calificación y la persona la corrige; la persona decide qué probar primero y qué hacer según el resultado.
- El umbral y la regla de decisión se escriben antes de ejecutar.
- El MVP se revisa con la tabla de Kniberg: la necesidad completa en la forma más simple, no una pieza suelta.
- Nada se da por hecho: el resultado queda Pendiente por validar.
