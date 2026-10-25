# Plantilla de SKILL.md para una skill de flujo

Rellena lo que está entre corchetes. Reglas del estándar: el frontmatter lleva **solo** `name` y `description`; `name` en minúsculas con guiones y **igual al nombre de la carpeta**; `description` de 1.024 caracteres o menos, con la frase "Úsala cuando" y de 3 a 5 frases reales de la persona; el archivo, de 20.000 caracteres o menos y sin rutas con dos puntos seguidos. Sin credenciales ni datos de personas.

````markdown
---
name: [nombre-en-kebab-case]
description: [Qué hace la skill en una o dos frases, con el resultado que entrega.] Úsala cuando [la persona] diga "[frase real 1]", "[frase real 2]", "[frase real 3]" o "[frase real 4]".
---
# [Nombre legible de la skill]

[Una o dos frases: qué tarea resuelve, para quién y qué entrega.]

## Cuándo usarla / cuándo no

**Úsala** cuando [situación y desencadenante].

**No la uses** cuando [lo que queda fuera: otra tarea, datos que no corresponden, un paso que requiere otra persona].

## Antes de empezar

- Entradas necesarias: [archivos, datos o mensajes, descritos en palabras].
- Dependencias: [accesos, archivos o personas que deben estar disponibles]. Si falta alguna, detente y dilo; no finjas éxito.
- Credenciales: la skill usa el acceso que la persona ya tiene configurado en su asistente. Nunca pidas ni guardes contraseñas, claves ni tokens.

## Proceso

1. **[Paso 1]** (solo lectura). [Qué hace.]
2. **[Paso 2]** (local). [Qué hace; produce un borrador o archivo propio.]
3. **[Paso 3]** (modifica algo externo). [Qué hace.] **Antes de este paso, pide la aprobación de la persona** y espera un sí claro.

## Puntos de aprobación

| Paso | Qué modifica | Quién aprueba | Qué pasa si no aprueba |
|---|---|---|---|
| [3] | [Envía, publica, compra, elimina o registra...] | [Persona] | [Queda el borrador; no se envía nada] |

## Qué decide sola y qué no

- Decide sola: [acciones de solo lectura o reversibles].
- Nunca sin aprobación: [lista de acciones que modifican algo externo].

## Si algo falla

| Falla habitual | Qué hacer |
|---|---|
| [Falla 1] | [Acción] |

## Entregables

- [Qué entrega, en qué formato y dónde queda].

## Criterio de salida

[Cómo se sabe que salió bien: la comprobación simple que la persona hace.]
````

## Lista de revisión antes de entregar

| Revisión | Cumple |
|---|---|
| El frontmatter tiene solo `name` y `description` | |
| `name` es igual a la carpeta y está en kebab-case | |
| La descripción tiene "Úsala cuando" y de 3 a 5 frases reales | |
| Cada paso está clasificado y los que modifican algo externo piden aprobación | |
| No hay contraseñas, claves, tokens ni datos de personas | |
| Las dependencias están declaradas y la skill se detiene si falta una | |
| El alcance es una sola tarea | |
