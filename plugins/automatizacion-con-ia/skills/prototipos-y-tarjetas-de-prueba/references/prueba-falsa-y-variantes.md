# Patrón: una prueba "falsa" que revela variantes del proceso

Nota: patrón genérico construido a partir de la experiencia de talleres de automatización, sin datos de ninguna organización.

## La idea

Una tarjeta de prueba puede salir **falsa** y, aun así, ser la más valiosa. Cuando una prueba falla de forma desigual (muy bien en una parte de los casos y muy mal en otra), el hallazgo no es "el supuesto es malo", sino **"el proceso no es uno solo"**: hay variantes que el mapa del proceso trataba como si fueran iguales.

## Cómo se reconoce

| Señal | Qué sugiere |
|---|---|
| El promedio no alcanza el umbral, pero algunos casos cumplen de sobra | Hay una variante donde el supuesto es cierto |
| Las fallas se concentran en un tipo de caso | Ese tipo necesita otro tratamiento o quedar fuera del piloto |
| Dos revisores explican las fallas de distinta forma | El proceso se ejecuta de formas distintas según quién lo haga |
| Las fallas tienen la misma causa (un dato que falta, un permiso, un criterio) | Es una condición previa, no una variante |

## Qué hacer, paso a paso

1. **No descartar todavía.** Pregunta: "¿en qué casos sí se cumplió?".
2. **Agrupar los casos que fallaron** por lo que tienen en común (quién pide, qué pide, qué información trae).
3. **Contar por variante** y calcular el cumplimiento de cada una; anota el tamaño de cada grupo.
4. **Comparar con el mapa** (`PAS-nn`, `FUT-nn`): ¿el diseño supone una sola variante?
5. **Decidir** casi siempre **iterar**: acotar el piloto a la variante donde el supuesto se cumple, y diseñar aparte (o dejar humanas) las demás.
6. **Registrar** el hallazgo, los supuestos nuevos que nacen de cada variante y qué se reabre en `disenar-proceso-futuro`.

## Por qué importa

Un piloto que mezcla variantes mide un promedio que no se parece a ninguna. Acotarlo a la variante validada da una lectura limpia, y las demás variantes se convierten en las siguientes tarjetas de prueba. Un ejemplo completo, en una clínica ficticia, está en `ejemplo.md` (`PRU-01`).
