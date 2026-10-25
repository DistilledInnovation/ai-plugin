# Herramientas para pruebas y evaluación

Nota de fuente: las cuatro categorías obligatorias (funcional, seguridad, resiliencia y calidad de IA), los criterios de aceptación y la regla de no declarar lista una liberación sin criterios aprobados provienen del diseño de implementación empresarial de Distilled Innovation. Las métricas de calidad de IA (exactitud, relevancia, fundamentación en la evidencia, consistencia estructural, selección correcta de herramientas, tasa de escalamiento, sesgos y errores de extracción), la evaluación con casos positivos y negativos, la diferencia entre métricas de prototipo y resultados de producción, y la trazabilidad de cada requisito a su prueba provienen de su oferta empresarial (gobernanza y criterios de calidad).

## 1. Qué cubre cada categoría

| Categoría | Pregunta que responde | Casos típicos |
|---|---|---|
| Funcional | ¿Hace lo que dice el contrato, en cada rama? | Recorrido completo; cada rama y excepción; rechazo de una aprobación; vencimiento de una espera |
| Seguridad | ¿Cada control resiste el abuso que lo justifica? | Instrucciones ocultas; datos que no deben llegar al modelo; permisos que no deben existir; secretos en exportaciones; suplantación en aprobaciones |
| Resiliencia | ¿Qué pasa cuando algo se repite o falla? | Duplicados; tiempo agotado tras un efecto; reinicio en medio de una espera; reprocesamiento desde la cola de errores; conciliación; modo manual |
| Calidad de IA | ¿El componente de IA es lo bastante bueno, y falla de forma segura? | Métricas sobre un conjunto etiquetado; salida con formato roto; casos difíciles; sesgo |
| Desempeño (opcional) | ¿Aguanta el volumen y los tiempos del contrato? | Pico de solicitudes; tiempo hasta la primera respuesta |
| Usabilidad (opcional) | ¿Las personas aprueban y revisan sin errores? | Tiempo por aprobación; errores en la bandeja |

## 2. Métricas de calidad de IA

| Métrica | Qué mide | Cómo se mide | Cuándo no aplica |
|---|---|---|---|
| Exactitud | Respuestas correctas frente a la esperada | Proporción de campos o decisiones correctas en un conjunto etiquetado; en clasificaciones de riesgo, mirar sobre todo los casos que no deben perderse | Nunca, si hay un paso con IA |
| Relevancia | Si lo generado responde a lo que se pidió | Revisión de una muestra con una guía de puntuación | Cuando el modelo no genera texto para personas |
| Fundamentación en la evidencia | Si cada dato o afirmación sale de la entrada o de una fuente citada | Comprobar que cada valor aparece en el texto de entrada; nada inventado | Rara vez |
| Consistencia estructural | Si la salida respeta los campos y valores permitidos | Validar cada salida contra su forma; contar las que fallan y a dónde van | Rara vez |
| Selección de herramientas | Si el modelo elige la herramienta correcta | Casos con la herramienta esperada | Cuando el modelo no tiene herramientas |
| Tasa de escalamiento | Cuántos casos pasan a una persona | Proporción de casos enviados a revisión; muy alta quita valor, muy baja puede esconder errores | Rara vez |
| Sesgo | Si el resultado cambia por algo que no debería importar | Pares del mismo caso con distinta forma de escribir o rasgos irrelevantes; comparar resultados | Rara vez |
| Errores de extracción | Errores que pasan sin aviso | Campos equivocados que no se marcaron como dudosos | Cuando no hay extracción |

**Umbrales**: los decide el dueño del flujo con el equipo, antes de medir, según el costo del error y si hay una persona que revisa después. Un umbral alto en lo que no puede fallar (una urgencia perdida) y tolerante en lo que una persona corrige igual.

## 3. Conjuntos de datos

1. **Ficticios por defecto.** Escritos a mano o generados y revisados, con las variantes del contrato, casos límite (datos incompletos, formatos raros) y casos difíciles (ambiguos, con faltas).
2. **Etiquetados por el negocio.** La respuesta esperada la fija quien conoce el criterio (por ejemplo, quien aprobó los criterios de urgencia), no quien construye el flujo.
3. **Suficientes para decidir**, no para impresionar: decenas de casos bien elegidos suelen bastar para una primera puerta; anota el tamaño para no sobreinterpretar.
4. **Separados por propósito**: uno para medir calidad, otros para seguridad (instrucciones ocultas, datos sensibles) y resiliencia.
5. **Datos reales** solo con autorización registrada, anonimizados cuando se pueda, y nunca en pruebas negativas.

## 4. Criterios de aceptación por etapa

| Etapa | Qué demuestra | Ejemplos de criterio |
|---|---|---|
| Prototipo | Que la idea funciona en condiciones controladas | La tarea de prueba se completa; las personas entienden la propuesta |
| Piloto | Que funciona con casos reales acotados | Tiempo por caso y errores en la muestra del piloto, rotulados como piloto |
| Producción | Que se puede operar con seguridad y sin el equipo que lo construyó | Todas las categorías pasan; controles con prueba negativa; ningún duplicado; modo manual probado; alertas con dueño |
| Producción (valor) | Que entrega el valor prometido | Línea base → meta medidas en operación; no bloquea la salida, pero tiene dueño y fecha |

Un criterio no cumplido se puede **dispensar** solo con una decisión registrada de quien tiene autoridad (con la razón y lo que se hará después). Nunca se cambia el umbral después de ver el resultado sin registrarlo.

## 5. Regresión

| Cambio | Qué se vuelve a correr como mínimo |
|---|---|
| Instrucciones del modelo o modelo | Calidad de IA completa, instrucciones ocultas, datos hacia el modelo |
| Reglas o plantillas | Funcional de los pasos afectados; casos de datos cruzados entre personas |
| Definición del flujo | Funcional completo y resiliencia de los pasos tocados |
| Permisos o conexiones | Seguridad de permisos y secretos |

## 6. Lista de salida

| Comprobación | Sí / No |
|---|---|
| El `evaluation-plan.yaml` valida contra el esquema | |
| Las cuatro categorías tienen casos, con positivos y negativos | |
| Cada `AT-nn`, `CTL-nn`, `RES-nn`, `REQ-nn` y métrica tiene al menos un caso | |
| Los conjuntos de datos son ficticios (o autorizados) y los etiquetó el negocio | |
| Cada métrica de IA tiene umbral y conjunto, o la razón de no aplicar | |
| Los criterios separan piloto de producción y tienen aprobador | |
| Cada corrida tiene versiones y evidencia; cada defecto, dueño y nueva corrida | |
| Lo que no se puede probar antes de producción pasó a operación con dueño | |
| La puerta de pruebas está aprobada o pendiente con lo que falta | |
