# Ejemplo: diseñar un prototipo en una empresa de transporte ficticia

Empresa inventada: **Transportes Marea Azul** (carga refrigerada regional, 65 empleados, 22 camiones). Continúa el ejemplo de `construir-concepto-fuerte`. Todo es ficticio, incluidas las cifras.

Entrada: `CON-01` "Aviso de frío y vista de la carga"; Perfil del Cliente del jefe de logística de un productor: 1ra tarea, asegurar que su carga llegue con el frío intacto (`HAL-01`, `HAL-02`); 1er dolor, no saber si se cortó el frío durante el traslado (`TEN-01`); 2do dolor, llamadas repetidas al conductor (`TEN-02`, pendiente por validar); 1er beneficio, enterarse a tiempo si algo sale mal (`NEC-01`). Supuestos `SUP-05` (basta un aviso) y `SUP-06` (se puede medir el frío durante todo el viaje).

## Turno 1: concepto

**Facilitador:** Tengo el concepto `CON-01` y el Perfil del Cliente de la síntesis. Primera pregunta: ¿qué productos o servicios concretos incluye tu concepto?

**Usuaria (Paula, gerente comercial):** Un aviso al cliente cuando el frío se sale del rango y una página donde puede ver la temperatura de su carga.

**Facilitador:** Registro `PRS-01` aviso de frío (ayuda a la 1ra tarea) y `PRS-02` vista de la temperatura (ayuda a la 1ra tarea y al 2do dolor).

## Turnos 2 y 3: aliviadores y creadores (un dato por turno)

**Facilitador:** ¿Cómo alivia tu solución el 1er dolor del cliente?

**Usuaria:** El aviso le llega en el momento en que el frío falla, no al llegar la carga.

**Facilitador:** Anotado `ALI-01` (alivia `TEN-01`). Siguiente pregunta: ¿cómo alivia tu solución el 2do dolor?

**Usuaria:** Con la vista no tiene que llamar al conductor.

**Facilitador:** Anotado `ALI-02` (alivia `TEN-02`, pendiente por validar). Siguiente pregunta: ¿qué beneficio de los que espera el cliente crea tu solución?

**Usuaria:** Enterarse a tiempo para decidir qué hacer con la carga.

**Facilitador:** Anotado `CRB-01` (crea el 1er beneficio, `NEC-01`).

## Turno 4: encaje en el papel

**Facilitador:** Contrasté el Mapa de Valor con el Perfil del Cliente:

| Orden | Perfil del Cliente | Mapa de Valor | Estado |
|---|---|---|---|
| 1ra tarea | Asegurar que la carga llegue con frío intacto | `PRS-01`, `PRS-02` | Parcial: avisa si falla, pero no evita que falle |
| 1er dolor | No saber si se cortó el frío | `ALI-01` | Cubierto |
| 2do dolor | Llamadas repetidas al conductor | `ALI-02` | Cubierto (pendiente por validar) |
| 1er beneficio | Enterarse a tiempo | `CRB-01` | Cubierto |

Lectura inversa: todos los elementos responden a algo del perfil. Encaje en el papel: **medio-alto**. El hueco es la 1ra tarea, porque el concepto avisa pero no evita el corte. ¿Qué hacemos con lo que la solución todavía no cubre?

**Usuaria:** Lo dejamos fuera de alcance por ahora: primero queremos saber si el aviso les sirve.

**Facilitador:** Registrado `DEC-06`: la brecha de la 1ra tarea queda fuera de alcance. Recuerda que esto es un encaje en el papel (hipótesis); el encaje con el mercado se prueba después.

## Turnos 5 y 6: qué aprender

**Facilitador:** ¿Cuál es el supuesto más arriesgado de este concepto?

**Usuaria:** Que con un aviso les basta, `SUP-05`.

**Facilitador:** Siguiente pregunta: ¿a quién se lo mostrarías primero?

**Usuaria:** A Julián, jefe de logística de un cliente actual, y a otros dos.

## Turno 7: prototipo rápido

**Facilitador:** Para aprender si un aviso basta no hace falta medir nada: hace falta que la persona reaccione a un aviso. Opciones de baja fidelidad: una historieta, un mensaje de texto escrito a mano por una persona o una simulación manual. ¿Qué es lo más barato que podemos armar en pocos días para que esa persona reaccione?

**Usuaria:** Una simulación manual: Julio, de despacho, les manda un mensaje de texto cuando un camión de prueba "falla", con una hoja que simula la vista.

**Facilitador:** Perfecto: fidelidad baja, costo casi cero. Lo que no tiene, a propósito: medición real del frío (eso es `SUP-06`, otro experimento).

## Turno 8: guion de prueba (resumen)

Qué aprender: si un aviso temprano basta para que el cliente decida qué hacer con la carga (`SUP-05`). Persona: tres jefes de logística de clientes actuales. Escenario: un camión de prueba con carga se avisa como "frío cortado". Tarea: decir qué haría al recibir el aviso. Evidencia: qué decide y cuánto tarda. Criterio de éxito (decidido antes): 2 de 3 deciden una acción sin pedir más información.

**Facilitador:** ¿Qué tendría que hacer o decir esa persona para que consideres que la prueba salió bien?

**Usuaria:** Que diga qué va a hacer con la carga sin llamar al conductor.

## Turnos 9 a 13: pitch A.I.D.A. (uno por turno, resumen)

**Facilitador:** ¿Ante quién vas a presentar el pitch?

**Usuaria:** Ante el dueño de un productor de alimentos frescos.

**Facilitador:** Siguiente pregunta: ¿qué quieres que haga esa persona al terminar?

**Usuaria:** Que acepte probar el aviso con una de sus cargas.

(Luego, una letra por turno: Atraer, Interesar, Deseo y Acción, cada una con su pregunta guía.)

## Entregable final

# Prototipo y pitch: Aviso de frío y vista de la carga

Marea Azul, 2026-10-25, borrador 1. `CON-01`.

| ID | Mapa de Valor | Responde a |
|---|---|---|
| PRS-01 | Aviso de frío al cliente | 1ra tarea |
| PRS-02 | Vista de la temperatura de la carga | 1ra tarea y 2do dolor |
| ALI-01 | Aviso en el momento en que falla el frío | 1er dolor (`TEN-01`) |
| ALI-02 | Vista sin llamar al conductor | 2do dolor (`TEN-02`, pendiente por validar) |
| CRB-01 | Enterarse a tiempo para decidir | 1er beneficio (`NEC-01`) |

**Encaje Problema-Solución en el papel:** medio-alto; brecha: la solución no evita el corte (`DEC-06`: fuera de alcance). Es una hipótesis.

**Prototipo:** simulación manual (mensaje de texto escrito por una persona y una hoja que simula la vista). Fidelidad baja. Prueba de `SUP-05` con tres clientes; éxito si 2 de 3 deciden una acción sin pedir más información.

**Pitch A.I.D.A. (versión corta):**

| Letra | Texto | Procedencia |
|---|---|---|
| Atraer | "Si el frío de tu carga se corta a mitad de camino, ¿te enteras antes de que llegue?" | Supuesto de apertura, a probar con el público |
| Interesar | "Dos clientes se fueron porque se enteraron tarde. Llevamos años moviendo carga fría" | Hecho (`HAL-06`) y Dicho por participante |
| Deseo | "Te avisamos en el momento en que falla y puedes ver la temperatura cuando quieras. Ya lo estamos probando a mano; aún no tenemos resultados" | Hecho (se prueba) y Pendiente por validar (resultados) |
| Acción | "Probemos el aviso con una de tus cargas la próxima semana" | Recomendación |

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RIE-03 | Que la simulación manual no se parezca al aviso real | Resultados poco representativos | Repetir con un aviso real en una segunda prueba |

Pendientes por validar: `SUP-05`, `SUP-06`; si la vista resuelve de verdad el 2do dolor (`TEN-02`).

Siguiente paso sugerido: `validar-supuestos-y-mvp`, para diseñar el experimento y el MVP.

## Lo que se ve en este ejemplo

- Una pregunta por turno, también en el Mapa de Valor y el pitch.
- Aliviadores y creadores citan el dolor o beneficio que atienden.
- El encaje se declara con su brecha y se aclara que es una hipótesis en el papel.
- El prototipo es de baja fidelidad porque lo que se quiere aprender es si basta un aviso, no si se puede medir el frío.
- El pitch no inventa evidencia: lo que no se probó se reconoce.
