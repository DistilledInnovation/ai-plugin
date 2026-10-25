# Herramientas para construir el concepto fuerte

Nota de fuente: el libro (6.1.4 y 6.1.5) da el hilo del proceso: terminada la generación de ideas, se crean categorías que engloben la naturaleza de las ideas; se pasa de nociones individuales a conceptos grupales ("cero brain-storming, 100 % brain-writing": idear de forma individual, poner en común, agrupar, reducir, fortalecer y priorizar por votación los clusters más fuertes); y se unen y combinan las ideas para diseñar el Concepto Fuerte de Solución, que debe tener como mínimo título, problema u oportunidad, solución, y alcance, valor agregado y diferenciación. Los pasos detallados, la mecánica de la votación, la matriz de criterios y los campos adicionales (persona usuaria, evidencia, supuestos críticos, riesgos, qué aprender) son una **adaptación** y no una transcripción del libro. El Anexo del libro (capítulo 10) solo trae índice.

## 1. Agrupar por afinidad (clusters)

**Para qué sirve (libro):** organizar las ideas en categorías que engloben su naturaleza para facilitar el trabajo con ellas.

**Cómo aplicarlo (adaptación, 15 a 20 minutos):**
1. Dejar todas las ideas visibles, una por nota.
2. Agrupar en silencio las que se parecen; no se pone nombre todavía.
3. Revisar los grupos muy grandes (más de 12 ideas): casi siempre hay dos temas distintos.
4. Mover las ideas "huérfanas" a un grupo "Otras" y revisarlo al final: ahí suelen estar las diferentes.
5. Poner nombre a cada grupo como frase completa ("El cliente se entera solo si algo falla", no "Alertas").
6. Asignar `CLU-nn` y anotar las `IDE-nn` de cada uno.

| Señal | Qué hacer |
|---|---|
| Un grupo con más de 12 ideas | Dividir por tema |
| Grupos con 1 idea | Revisar si encaja en otro o dejarlo en "Otras" |
| Nombre que es una etiqueta | Reescribirlo como frase completa |

## 2. Reducir

1. Buscar ideas repetidas o casi iguales dentro de cada grupo.
2. Unirlas en una sola, citando las `IDE-nn` originales.
3. No borrar nada: lo unido queda registrado en la columna de ideas.

## 3. Votación con puntos

**Para qué sirve (libro):** priorizar por votación las soluciones o clusters más fuertes; también sirve como herramienta democrática cuando el equipo tiene problemas para llegar a un consenso a tiempo.

**Cómo aplicarla (adaptación, 5 a 10 minutos):**
1. Dejar visibles los grupos con su nombre.
2. Dar 3 votos por persona (o un voto por cada 4 a 5 grupos, mínimo 3).
3. Votar en silencio y a la vez, para evitar imitación. Se puede poner más de un voto en el mismo grupo.
4. Contar y anotar en `assets/agrupacion-y-votacion.md`.
5. Desempatar con una pregunta: qué grupo responde más directamente al reto.
6. Quien tiene la autoridad confirma qué grupos pasan (`DEC-nn`).

## 4. Matriz de criterios (modo individual o para desempatar)

Calificar cada grupo de 1 (bajo) a 3 (alto) en estos criterios (adaptación; la lista combina las cuatro cualidades de las "ideas con vida" con la conexión con la evidencia):

| Criterio | Pregunta |
|---|---|
| Conecta con la evidencia | ¿Responde a un `HAL-nn`, `NEC-nn` o `TEN-nn` importante? |
| Visible | ¿Se puede imaginar o mostrar con facilidad? |
| Implementable | ¿Se puede dar un primer paso real pronto? |
| Diferente | ¿Se aleja de lo de siempre? |
| Ambiciosa | ¿Mueve de verdad la aguja del reto? |

Sumar y ordenar. La calificación de la IA es una Inferencia de la IA y la corrige la persona. No elimines por puntaje un grupo que la persona defienda: se ajusta la nota y se anota por qué.

## 5. Combinar lo mejor de cada idea

**Para qué sirve (libro):** con las ideas organizadas por categorías se pueden unir y combinar lo mejor de cada una para diseñar un Concepto Fuerte de Solución.

**Cómo aplicarlo (adaptación):**
1. Tomar un grupo elegido y leer sus ideas una por una.
2. Marcar de cada una "lo mejor": la parte que más aporta a la tarea, el dolor o el beneficio del reto.
3. Preguntar qué ideas se complementan (una resuelve el aviso, otra la prueba) y qué ideas se contradicen.
4. Cuando hay contradicción, elegir una y guardar la otra como alternativa.
5. Escribir la solución como un sistema: qué hace cada parte y para quién.

## 6. Redactar el Concepto Fuerte

Orden sugerido (adaptación): título, problema u oportunidad, solución, alcance, valor agregado y diferenciación; después persona usuaria, hallazgos, evidencia, supuestos críticos, riesgos y qué debemos aprender.

- Título: corto y específico; cuenta qué se ofrece o qué cambia.
- Problema u oportunidad: copia o resume el reto y la evidencia; no la solución.
- Solución: qué hace, no con qué tecnología o proveedor.
- Alcance: qué entra y qué no en la primera versión.
- Valor agregado: qué gana la persona que hoy no tiene (alivia un dolor, crea un beneficio).
- Diferenciación: en qué se distingue de lo que ya existe o de lo que hace la competencia.
- Supuestos críticos: lo que debe ser cierto; cada uno recibe `SUP-nn` y queda Pendiente por validar.

```mermaid
flowchart LR
  A[Banco de ideas] --> B[Agrupar]
  B --> C[Nombrar y reducir]
  C --> D[Votar o calificar]
  D --> E[Combinar]
  E --> F[Concepto Fuerte]
  F --> G[Prototipo]
```

| Paso | Qué sale |
|---|---|
| Agrupar | Grupos `CLU-nn` |
| Nombrar y reducir | Nombres en frase completa; ideas unidas |
| Votar o calificar | Prioridad de grupos |
| Combinar | Solución compuesta |
| Concepto Fuerte | `CON-nn` con campos mínimos y extras |
| Prototipo | Etapa siguiente (`disenar-prototipo`) |
