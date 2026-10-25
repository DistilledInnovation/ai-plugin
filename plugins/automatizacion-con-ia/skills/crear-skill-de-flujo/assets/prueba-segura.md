# Prueba segura de una skill de flujo

Skill: ___  Fecha: ___  Quién prueba: ___

Una prueba segura comprueba que la skill sigue sus pasos **sin consecuencias**: no envía, no publica, no compra, no elimina y no expone información privada.

## 1. Antes de probar

| Revisión | Respuesta |
|---|---|
| ¿Los datos de prueba son de ejemplo (ficticios o sin información de personas)? | |
| ¿Algún paso de la skill modifica algo externo? ¿Cuál? | |
| ¿Cómo se evita que ese paso ocurra de verdad? (se detiene antes de la aprobación, se usa un borrador o un destino de prueba) | |
| ¿Están disponibles las dependencias declaradas? | Sí, o se detiene la prueba y se dice cuál falta |
| ¿La prueba necesita alguna clave? | No. Si la necesitara, se detiene: las claves no se comparten |

## 2. Cómo armar el ejemplo

- Usa un archivo o texto de muestra con datos inventados y pocas filas, que incluya al menos un caso normal y un caso de borde (por ejemplo, un dato faltante).
- Si el flujo termina en un envío o registro, la prueba llega hasta el borrador y se detiene en el punto de aprobación.
- Si un paso depende de otra persona, simúlala con una respuesta de ejemplo escrita de antemano.

## 3. Informe de la prueba

| Campo | Resultado |
|---|---|
| Nombre de la skill | |
| Archivos usados (de la skill y de la muestra) | |
| Dependencias | |
| Pasos ejecutados y su clase (solo lectura, local, modifica algo externo) | |
| Pasos que se detuvieron en una aprobación | |
| Resultado observado | |
| ¿Se envió, publicó, compró, eliminó o expuso algo? | No (si la respuesta fuera sí, la prueba falló) |
| Qué falló o qué se ajusta | |

## 4. Si falta una dependencia

Detén la prueba, di qué falta y quién puede resolverlo. No simules el resultado ni lo des por bueno.

## 5. Después de la prueba

- Ajusta el `SKILL.md` solo con lo que la prueba mostró.
- Repite la prueba si cambió un paso que modifica algo externo.
- Las primeras veces de uso real, una persona verifica el resultado.
