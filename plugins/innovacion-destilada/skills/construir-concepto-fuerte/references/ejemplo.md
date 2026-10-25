# Ejemplo: construir el concepto fuerte en una empresa de transporte ficticia

Empresa inventada: **Transportes Marea Azul** (carga refrigerada regional, 65 empleados, 22 camiones). Continúa el ejemplo de `facilitar-ideacion`. Todo es ficticio, incluidas las cifras.

Entrada: `RET-03` "¿Cómo podemos mitigar la incertidumbre sobre si se cortó el frío durante el traslado de la carga?"; banco con 114 ideas (`IDE-01` a `IDE-114`) en cinco grupos de la sesión; evidencia `HAL-06`, `NEC-01`, `TEN-01`, `TEN-02`.

## Turno 1: reunir

**Facilitador:** Tengo el banco de la sesión con 114 ideas y 5 grupos preliminares. Primera pregunta: ¿quieres usar los grupos y votos que hicieron en la sesión?

**Usuaria (Paula, gerente comercial):** Sí, usemos los de la sesión, pero revisemos los nombres.

## Turno 2: agrupar y nombrar

**Facilitador:** Con los grupos de la sesión, estos son los nombres como frase completa:

| ID | Nombre | Ideas |
|---|---|---|
| CLU-01 | El cliente se entera solo si algo falla | 36 |
| CLU-02 | El cliente puede mirar el frío cuando quiera | 28 |
| CLU-03 | El conductor tiene una rutina de aviso | 17 |
| CLU-04 | El cliente recibe prueba del frío al llegar | 21 |
| CLU-05 | Garantía con compensación | 12 |

¿Cambiarías el nombre de alguno?

**Usuaria:** No, están bien.

## Turno 3: reducir

**Facilitador:** Veo ideas casi iguales dentro de `CLU-01`: `IDE-01` (mensaje al cliente si la temperatura sale del rango) e `IDE-90` (combinar el aviso de frío con el de llegada) comparten el aviso. ¿Unimos estas ideas repetidas?

**Usuaria:** Sí, únelas.

**Facilitador:** Hecho: queda `IDE-01+IDE-90` como una sola, con los dos números citados. En total 7 uniones en `CLU-01` y `CLU-02`; nada se borró.

## Turno 4: priorizar

**Facilitador:** Los votos de la sesión (3 por persona, 6 personas) fueron `CLU-01` con 7, `CLU-02` con 5, `CLU-04` con 3, `CLU-03` con 2 y `CLU-05` con 1. Esa votación prioriza, pero la decisión es tuya. ¿Con cuáles de estos grupos seguimos?

**Usuaria:** Con `CLU-01` y `CLU-02`. Van juntos: que avise si falla y que pueda mirar si quiere.

**Facilitador:** Registrado como `DEC-03`: se fortalecen `CLU-01` y `CLU-02`; `CLU-03`, `CLU-04` y `CLU-05` quedan guardados.

## Turno 5: combinar

**Facilitador:** De las ideas de `CLU-01`, ¿cuáles no pueden faltar en la solución?

**Usuaria:** Que el aviso llegue solo cuando se corte el frío, y que diga qué hacer.

**Facilitador:** Ahora, de las ideas de `CLU-02`, ¿cuáles no pueden faltar en la solución?

**Usuaria:** Que el cliente pueda ver la temperatura de su carga sin llamar a nadie.

**Facilitador:** Se complementan: el aviso resuelve el momento crítico y la vista resuelve la tranquilidad de fondo. Las dos juntas forman un solo concepto. Veo un punto que choca: dentro de `CLU-01` hay ideas de aviso constante e ideas de aviso solo cuando algo falla. ¿Qué tipo de aviso quieres que lleve el concepto?

**Usuaria:** Solo cuando falla; si avisamos todo el tiempo, el cliente deja de leer.

**Facilitador:** Registrado como `DEC-05`: el concepto lleva aviso solo cuando falla, decidido por Paula; las ideas de aviso constante quedan guardadas como alternativa.

## Turno 6: redactar (un campo por turno, resumen)

**Facilitador:** Borrador del título: "Aviso de frío para el cliente". ¿Este título cuenta la solución en pocas palabras?

**Usuaria:** Agrégale "y vista de la carga".

(En turnos siguientes, de a un campo: problema, solución, alcance, valor agregado y diferenciación. En el alcance la persona decide que la primera versión cubre solo a los dos clientes perdidos y a tres clientes actuales, y deja fuera la facturación y el rastreo de ubicación. En la diferenciación señala que un competidor ofrece solo ubicación y no el estado del frío.)

## Turno 7: supuestos

**Facilitador:** ¿Qué estamos dando por cierto en este concepto que, si fuera falso, lo tumbaría?

**Usuaria:** Que a los clientes les basta un aviso. Y que de verdad vamos a poder medir el frío durante todo el viaje.

**Facilitador:** Anoto `SUP-05` y `SUP-06`, ambos Pendientes por validar.

## Entregable final

# Concepto Fuerte de Solución: Aviso de frío y vista de la carga

Proyecto: Marea Azul, 2026-10-25, borrador 1. ID `CON-01`. Reto `RET-03`. Ideas combinadas: `IDE-01+IDE-90`, `IDE-03`, `IDE-85`. Grupos de origen: `CLU-01`, `CLU-02`.

**Título:** Aviso de frío y vista de la carga.

**Problema u oportunidad:** los clientes no saben si se cortó el frío durante el traslado hasta que la carga llega tibia (`TEN-01`, `HAL-06`); dos clientes se fueron por eso (Hecho, dicho por participante).

**Solución:** el cliente recibe un aviso solo cuando el frío de su carga sale de un rango acordado, con la instrucción de qué hacer, y puede consultar el estado del frío cuando quiera sin llamar a nadie. (No se elige tecnología: cómo se mide es una decisión de etapas posteriores.)

| | Descripción | Procedencia |
|---|---|---|
| Alcance | Dentro: dos clientes que se fueron y tres actuales, avisos de frío y una vista de consulta. Fuera: ubicación del camión, facturación, flota completa | Decisión (`DEC-04`) |
| Valor agregado | Alivia el dolor de enterarse tarde y crea la certeza de que el frío se mantuvo (`NEC-01`) | Evidencia (`HAL-06`) |
| Diferenciación | Un competidor ofrece ubicación, no el estado del frío | Dicho por participante, Pendiente por validar |

| Campo | Contenido | Procedencia |
|---|---|---|
| Persona usuaria | Jefe de logística de un productor de alimentos frescos | Evidencia |
| Qué debemos aprender | Qué rango de frío importa a cada cliente y qué hace cuando recibe un aviso | Pendiente por validar |

| ID | Supuesto | Estado | Cómo se prueba |
|---|---|---|---|
| SUP-05 | A los clientes les basta un aviso temprano | Pendiente por validar | Simular el aviso a mano con tres clientes |
| SUP-06 | Se puede medir el frío durante todo el viaje | Pendiente por validar | Prueba de medición en una ruta |

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RIE-02 | Demasiados avisos y el cliente los ignora | El aviso pierde valor | Probar el umbral con tres clientes |

Decisiones `DEC-03` (grupos que se fortalecen), `DEC-04` (alcance) y `DEC-05` (aviso solo cuando falla): tomadas por Paula. Alternativas guardadas: `CLU-03`, `CLU-04` y `CLU-05`.

Siguiente paso sugerido: `disenar-prototipo`, para contrastar el concepto con el Perfil del Cliente y simular el aviso con una maqueta barata.

## Lo que se ve en este ejemplo

- Una pregunta por turno, también al combinar y al redactar.
- Lo que se une o se descarta queda registrado, no se borra.
- La votación prioriza; la decisión la toma la persona (`DEC-nn`).
- El concepto cita ideas, evidencia y supuestos, y no elige tecnología.
