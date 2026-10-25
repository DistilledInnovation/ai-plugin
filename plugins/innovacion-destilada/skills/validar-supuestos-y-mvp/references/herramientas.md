# Herramientas para validar supuestos y diseñar el MVP

Nota de fuente: el libro (7.1.3) da la definición del Mínimo Producto Viable (o Mínima Propuesta de Valor Viable), la aclaración de que no es una versión inicial con poca funcionalidad, la gráfica basada en Henrik Kniberg y la consigna de definir método de prueba, criterios de éxito y alcance, con la opción de simular la solución completa o entregar la propuesta de valor a mano. En 8.1.1 y 8.1.2 pide priorizar los supuestos más riesgosos ("aquellos que si no son como creemos pueden hacer inviable nuestro modelo") y define la métrica de éxito. Del Anexo (capítulo 10) el libro solo trae índice. Las siete categorías de supuestos, la calificación, el catálogo de técnicas de experimento, la tarjeta de prueba y la regla de decisión son una **adaptación** de métodos publicados (Lean Startup; la tarjeta de prueba sigue el formato de David Bland y Alexander Osterwalder) y no una transcripción del libro.

## 1. Siete categorías de supuestos (adaptación)

Una categoría por turno. La frase del supuesto debe ser afirmativa y comprobable ("los clientes hacen X"), no una intención.

| Categoría | Pregunta guía (un turno) | Ejemplo ficticio |
|---|---|---|
| Problema | "¿Qué estás dando por cierto sobre el problema que, si fuera falso, tumbaría tu solución?" | El cliente sí pierde dinero cuando la carga llega tibia |
| Usuario | "¿Qué estás dando por cierto sobre quién es la persona que decide?" | Quien decide es el jefe de logística, no el dueño |
| Comportamiento | "¿Qué estás dando por cierto sobre lo que hará la persona al recibir tu solución?" | Lee el aviso y actúa en minutos |
| Propuesta de valor | "¿Qué estás dando por cierto sobre por qué tu solución es mejor que lo que hacen hoy?" | Prefieren un aviso a llamar al conductor |
| Factibilidad | "¿Qué estás dando por cierto sobre tu capacidad para entregarla?" | Podemos medir el frío todo el viaje |
| Adopción | "¿Qué estás dando por cierto sobre cómo empezarán a usarla?" | Aceptan probarla con una carga real |
| Viabilidad | "¿Qué estás dando por cierto sobre el dinero que entra y el que sale?" | Pagarían un recargo por el servicio |

Si la persona no sabe qué responder, repite la pregunta con un ejemplo de otra empresa, no del suyo. Cada supuesto con evidencia real se marca Hecho; el resto, Supuesto.

## 2. Calificar y priorizar (adaptación)

El libro pide empezar por los supuestos que, si no son como se cree, hacen inviable el modelo. Para ordenarlos se usan tres criterios, uno por turno:

| Criterio | Pregunta | Lectura |
|---|---|---|
| Impacto si es falso | "Si este supuesto fuera falso, ¿qué le pasaría a tu solución?" | Alto: la solución no se sostiene. Bajo: se corrige con poco |
| Certeza hoy | "¿Qué evidencia real tienes hoy de que es cierto?" | Sin evidencia, certeza baja |
| Costo de equivocarte | "¿Cuánto te costaría seguir adelante si estuvieras equivocado?" | Alto: dinero, tiempo o confianza difíciles de recuperar |

Cómo hacerlo:
1. Elegir 3 a 5 supuestos para calificar; no todos.
2. Preguntar los tres criterios, uno por turno, por supuesto.
3. Traducir las respuestas a alto, medio o bajo y mostrarlas como Inferencia de la IA para que la persona las corrija.
4. Ordenar: impacto alto, certeza baja y costo alto arriba.
5. Dejar que la persona elija con cuál empezar. La tabla ordena; no decide.

## 3. Técnicas de experimento (adaptación)

Regla del libro: elegir la técnica que conduzca **más rápidamente** a aprender sobre el supuesto más arriesgado. A veces basta con simular la solución completa o entregar la propuesta de valor de forma manual.

| Técnica | Sirve para probar | Cómo se hace | Costo |
|---|---|---|---|
| Entrevista de problema | Que el problema existe y duele | 5 a 8 conversaciones, sin presentar la solución | Muy bajo |
| Simulación manual | Que el servicio tiene valor | Una persona hace a mano lo que haría el sistema | Muy bajo |
| Concierge | Que el cliente quiere la propuesta de valor completa | Se entrega a mano a unos pocos clientes, con conversación | Bajo |
| Mago de Oz | Que la experiencia funciona, sin construir lo de atrás | La persona ve una interfaz simple; detrás, una persona lo opera | Bajo a medio |
| Página de humo | Que hay interés antes de construir | Una página o mensaje que ofrece el servicio y mide quién responde | Bajo |
| Preventa o carta de intención | Que están dispuestos a pagar | Se pide un compromiso (pago, firma) por algo que aún no existe | Bajo a medio |
| Prototipo probado | Que la solución se entiende y se usa | Dibujo, maqueta o demo navegable (ver `disenar-prototipo`) | Bajo a medio |

Cómo elegir:
1. Escribir el supuesto y qué señal observable lo confirmaría.
2. Preguntar "¿qué es lo más barato que podrías hacer esta semana para saber si ese supuesto es cierto?".
3. Escoger la técnica más barata que produzca esa señal; si dos sirven, la más rápida.
4. Marcar qué NO tiene, a propósito.
5. No elegir tecnología hasta que el experimento la exija.

## 4. La tarjeta de prueba (adaptación)

| Línea | Qué va | Error común |
|---|---|---|
| Creemos que… | El supuesto, como frase afirmativa | Escribir una meta ("queremos vender") |
| Para verificarlo, haremos… | El experimento mínimo | Describir el producto completo |
| Y mediremos… | La métrica con su unidad | "Interés" sin número |
| Acertamos si… | El umbral, decidido antes de ejecutar | Fijarlo después de ver el resultado |

Ejemplo de métrica de éxito del libro (8.1.2): si voy donde 100 clientes, al menos 50 deben comprarme. Si se cumple, se sigue validando la siguiente hipótesis; si no, se entiende por qué y se cambia el modelo.

Cómo completarla, un dato por turno:
1. Alcance: cuántas personas.
2. Método: paso a paso.
3. Criterio: qué resultado cuenta como acierto.
4. Regla de decisión: qué se hace si no se cumple.
5. Leer la tarjeta completa y pedir confirmación.

## 5. Regla de decisión (adaptación)

Se escribe antes de ejecutar para no moverla después. Cuatro salidas: continuar (se cumplió, siguiente supuesto), iterar (cerca del umbral, se ajusta y se repite), pivotar (lejos pero se entiende por qué, se cambia problema, segmento o solución) y detener (lejos y sin camino). La decisión final se registra como `DEC-nn` en `probar-y-aprender`.

## 6. El MVP según la gráfica de Kniberg (7.1.3)

La gráfica tiene dos filas. Fila "No de esta forma…": una rueda, luego un chasis, luego un carro (reacción del cliente: molesto, molesto, satisfecho). Fila "Sino de esta…": una patineta, luego una bicicleta, luego un carro (reacción: algo insatisfecho, conforme, satisfecho).

| Camino | 1 | 2 | 3 | Qué enseña |
|---|---|---|---|---|
| No de esta forma | Rueda | Chasis | Carro | Fragmentos que no resuelven nada hasta el final |
| Sino de esta | Patineta | Bicicleta | Carro | Cada entrega resuelve la necesidad completa (moverse) y mejora |

Cómo aplicarlo (adaptación):
1. Nombrar la necesidad completa en una frase ("moverse", "tener la ropa lista sin perder la tarde").
2. Preguntar cuál es la versión más simple que ya la cubre, aunque sea manual.
3. Revisar que no sea una pieza suelta: si el cliente no podría usarla para lo que necesita, es una rueda.
4. Definir qué sería la siguiente versión mejor y qué se aprende con la actual.
5. Recordar que un prototipo bonito no es un MVP: el MVP es el experimento que enseña.
