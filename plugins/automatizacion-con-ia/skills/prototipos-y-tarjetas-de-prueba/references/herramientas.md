# Herramientas para tarjetas de prueba

Nota de fuente: la tarjeta de prueba (Creemos que, Para verificarlo haremos, Y mediremos, Acertamos si) y los tipos de prueba provienen de la metodología de Distilled Innovation; la escala de fidelidad, la coincidencia con el concepto, el registro de evidencia y el árbol de decisión son una adaptación de este plugin.

## 1. Cómo escribir un buen "Acertamos si"

| Elemento | Mal | Bien |
|---|---|---|
| Umbral | "Que funcione bien" | "Al menos 24 de 30 mensajes" |
| Tiempo | "Pronto" | "En dos semanas" |
| Qué cuenta | "Que a la gente le guste" | "Que 6 de cada 10 acepten uno de los tres horarios" |
| Quién lo mide | "El equipo" | "La jefa de recepción, con la hoja de conteo" |
| Cuándo se fija | Después de ver resultados | Antes de empezar |

Si el umbral no se puede fijar con un dato, escribe "Pendiente por validar: definir el umbral con ___" y no pruebes todavía.

## 2. Nivel crítico y costo

| Nivel crítico | Criticidad del supuesto (impacto × incertidumbre) | Qué implica |
|---|---|---|
| Crítico | 16 a 25 | Se prueba antes de construir |
| Alto | 10 a 15 | Se prueba antes del piloto, con una versión barata |
| Medio | Menos de 10 | Se observa durante el piloto o se acepta |

| Costo | Referencia | Ejemplo |
|---|---|---|
| Bajo | Unas horas de una o dos personas, sin preparar nada nuevo | Revisar una muestra en papel |
| Medio | Unos días de trabajo, algo de preparación | Una lista hecha a mano para un día de uso |
| Alto | Semanas, varias personas o preparación de datos | Un piloto operativo |

Son anclas para conversar, no estimaciones. El costo es del esfuerzo de la prueba, no del flujo completo.

## 3. Confiabilidad de los datos

| Nivel | Cuándo | Cómo se declara |
|---|---|---|
| Alta | Muestra amplia y representativa, datos reales, dos revisores que coinciden | "Alta: 200 casos, dos revisores coinciden" |
| Media | Muestra pequeña pero real, o un solo grupo | "Media: 30 casos de dos semanas; sin llamadas" |
| Baja | Datos ficticios, opiniones o muestras de menos de 10 | "Baja: 5 opiniones; sirve para orientar, no para decidir" |

Una decisión de escalar con confiabilidad Baja se justifica por escrito o se repite la prueba.

## 4. Coincidencia con el concepto

Una prueba es válida si el prototipo representa lo que se quiere aprender. Revisa cuatro cosas: (1) qué parte del concepto simula, (2) qué parte deja fuera (y de eso no se concluye nada), (3) si una persona hace de sistema y la gente probando lo sabe, (4) si el resultado podría deberse al prototipo y no al concepto. Ejemplo: revisar mensajes a mano prueba que **los datos están**, no que **una IA los lea bien**; eso es otra tarjeta.

## 5. Decisiones y qué pasa después

| Decisión | Cuándo | Qué sigue |
|---|---|---|
| Iterar | El supuesto se cumple en parte o la prueba reveló algo que se puede ajustar | Ajustar diseño o alcance; repetir una prueba más acotada |
| Escalar | Se cumplió el umbral con evidencia confiable | Una prueba de mayor fidelidad o el piloto |
| Pausar | No se puede probar bien ahora (falta un criterio, un dato o una persona) | Anotar qué lo desbloquea y quién |
| Descartar | Falso y sin variante útil | Quitar o simplificar esa parte; mantenerla humana |
| Redefinir el reto | El problema o la meta eran otros | `definir-reto-de-automatizacion` |

La decisión la toma quien tiene la autoridad (`DEC-nn`); el facilitador la recomienda.

## 6. Errores frecuentes

| Error | Cómo se evita |
|---|---|
| Probar con quien ya está de acuerdo | Incluir a quien hace el trabajo y a quien podría rechazarlo |
| Cambiar el umbral al ver los datos | Fijarlo antes y registrar cualquier cambio |
| Construir antes de preguntar | Subir de fidelidad solo si la anterior no alcanza |
| Dar por validada una maqueta | Exigir evidencia de uso o de datos reales |
| Descartar una prueba falsa sin mirar por qué | Revisar variantes y subgrupos (`prueba-falsa-y-variantes.md`) |
| Usar datos reales sin anonimizar | Autorización y anonimización antes de empezar |
