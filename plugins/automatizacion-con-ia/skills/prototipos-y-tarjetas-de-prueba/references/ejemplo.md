# Ejemplo: Prototipos y tarjetas de prueba en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `supuestos-y-riesgos`: el flujo `FLU-01` (agendar citas, `RET-01`) tiene ocho supuestos `SUP-01` a `SUP-08`; los más arriesgados son `SUP-04` (los mensajes traen datos suficientes, criticidad 20), `SUP-08` (la marca de urgencia, 20), `SUP-01` (citas con error, 16), `SUP-03` (causa de los duplicados, 12) y `SUP-05` (búsqueda de la ficha, 12); `SUP-06` (recepción aprueba sin reescribir, 12) se prueba junto con `SUP-05`. Riesgo que impide probar: `RIE-06` (no hay mensajes reales sin anonimizar; autoriza la administradora). Hasta aquí, nadie ha probado nada.

## Turno 1

**Usuaria (Valeria):** Armemos las pruebas de lo más arriesgado. No quiero gastar en nada antes de saber.

**Facilitador:** De los supuestos prioritarios, el que más condiciona al resto es `SUP-04`: si los mensajes no traen los datos, la lectura automática no tiene de qué partir. Para armar la tarjeta: ¿podrían revisar esta semana 30 mensajes reales de las últimas dos semanas, ya sin nombres, documentos ni teléfonos?

## Turno 2

**Usuaria:** Sí, la administradora los prepara y los revisan la jefa de recepción y una recepcionista, cada una por su lado.

**Facilitador:** Entonces es una prueba de papel, la fidelidad más baja posible, y no hace falta construir nada. Armo la tarjeta `PRU-01` y las otras tres, y tú me confirmas los umbrales. Una pregunta de coincidencia con el concepto: esta revisión a mano prueba que los datos **están** en el mensaje, no que una IA los lea bien; ¿aceptas que eso quede para otra tarjeta?

**Usuaria:** Sí, primero saber si están.

## Turno 3 (cuatro días después)

**Usuaria:** Ya revisamos. De 30 mensajes, solo 17 traían todo lo necesario. Las dos coincidieron en 28 de los 30.

**Facilitador:** El umbral era 24 de 30; con 17, `PRU-01` salió **falsa**. Antes de descartar `SUP-04`, miremos dónde sí se cumplió: ¿en qué mensajes faltaban datos y qué tenían en común?

## Turno 4

**Usuaria:** Los que faltaban eran de gente que pide el control de un tratamiento ("mi control de ortodoncia"), de padres o hijos que piden para otra persona, y de pacientes nuevos. Los de una cita nueva de un paciente que ya viene casi siempre traían todo.

**Facilitador:** Eso cambia la lectura: el supuesto se cumple en una parte del proceso y falla en otras tres, porque lo que llamamos "una solicitud" son cuatro variantes. Lo cuento por variante con tus datos y propongo la decisión: **iterar**, no descartar. ¿Quién decide, tú?

**Usuaria:** Yo. Hagámoslo así.

## Turno 5 (una semana después, 2026-11-03)

**Usuaria:** Hicimos lo de la hoja con 20 solicitudes de la variante A. Una recepcionista las revisó con cronómetro: encontró 19 fichas, tardó 2,4 minutos en promedio por aprobación y corrigió 3 propuestas.

**Facilitador:** Contra el umbral de `PRU-02` (18 fichas, menos de 3 minutos, no más de 4 reescritas), salió **verdadera** para `SUP-05` y `SUP-06`. La confiabilidad es Media: una sola recepcionista, 20 solicitudes y una sola variante. Propongo **escalar** al piloto, limitado a la variante A. ¿Lo decides tú?

**Usuaria:** Sí, escalamos a la A y las demás siguen como hoy.

## Entregable: tarjetas de prueba

### `PRU-01` (hecha)

| Frase | Respuesta |
|---|---|
| **Creemos que** (`SUP-04`) | En al menos 24 de 30 mensajes reales se pueden leer los datos necesarios (nombre, documento o teléfono, y motivo) sin volver a preguntar |
| **Para verificarlo, haremos** | Revisar 30 mensajes de las últimas dos semanas, anonimizados por la administradora, contra la lista de datos necesarios; dos personas revisan por separado |
| **Y mediremos** | Cuántos mensajes traen todos los datos y, en los demás, qué falta |
| **Acertamos si** | Al menos 24 de 30 (80 %, umbral confirmado por Valeria) |

| Campo | Respuesta |
|---|---|
| Nivel crítico | Crítico (criticidad 20) |
| Costo | Bajo: unas 3 horas entre dos personas, más la preparación de la administradora |
| Tipo de prueba | Experimento de proceso |
| Fidelidad | 1 (papel y una lista) |
| Evidencia | Hechos: mensajes reales anonimizados, sin opiniones |
| Confiabilidad esperada | Media: 30 mensajes de dos semanas, sin llamadas |
| Límites de seguridad | Mensajes anonimizados; no se envía ni se registra nada (`RIE-06`) |
| Dependencias | Autorización de la administradora |
| Fecha y duración | 2026-10-26 al 2026-10-29 |

Coincidencia con el concepto: representa **que los datos están en el mensaje**; no representa que una IA los lea bien (otra tarjeta); el resultado no depende de un prototipo porque no hay ninguno.

| Resultado | |
|---|---|
| Lo observado | 17 de 30 mensajes con todos los datos; los dos revisores coincidieron en 28 de 30 |
| ¿Acertamos? | **Falso** (17 de 30 es 57 %, por debajo del 80 %) |
| Confiabilidad real | Media: muestra pequeña; buena coincidencia entre revisores (28 de 30) |
| Qué nos sorprendió | Las fallas no se reparten al azar: se concentran en tres tipos de solicitud |
| Decisión | **Iterar** (`DEC-06`, decide Valeria) |

| Variante | Mensajes | Con datos suficientes | Cumplimiento |
|---|---|---|---|
| A. Cita nueva de un paciente con ficha | 13 | 12 | 92 % |
| B. Control de un tratamiento en curso | 8 | 3 | 38 % |
| C. Pide para otra persona (hijo, madre o padre) | 5 | 0 | 0 % |
| D. Paciente nuevo sin ficha (`EXC-01`) | 4 | 2 | 50 % |
| Total | 30 | 17 | 57 % |

### `PRU-02` (hecha, solo con la variante A)

| Frase | Respuesta |
|---|---|
| **Creemos que** (`SUP-05` y `SUP-06`) | Buscar por documento y teléfono encuentra la ficha correcta, y recepción aprueba cada propuesta en menos de 3 minutos y sin reescribir más de 2 de cada 10 |
| **Para verificarlo, haremos** | Preparar a mano una lista de 20 solicitudes de la variante A, ya con la ficha encontrada y tres horarios propuestos según las reglas escritas; una recepcionista las aprueba o corrige con el cronómetro |
| **Y mediremos** | Fichas encontradas, minutos por aprobación y propuestas reescritas |
| **Acertamos si** | Al menos 18 de 20 fichas, menos de 3 minutos de promedio y no más de 4 propuestas reescritas |

| Campo | Respuesta |
|---|---|
| Nivel crítico | Alto (criticidad 12) |
| Costo | Bajo a Medio: unas 6 horas de preparación a mano y una mañana de la recepcionista |
| Tipo de prueba | Conserje (el facilitador y la jefa preparan a mano lo que haría el flujo) |
| Fidelidad | 2 (hoja preparada a mano) |
| Evidencia | Hechos: cronómetro y conteo, no opiniones |
| Confiabilidad esperada | Media: una sola recepcionista, 20 solicitudes de una variante |
| Límites de seguridad | Datos anonimizados; ninguna propuesta se envía a un paciente |

Coincidencia con el concepto: representa la **experiencia de aprobar**; la hoja la prepara una persona, no el sistema, y la recepcionista lo sabe; no representa la lectura automática, ni las variantes B a D.

| Resultado | |
|---|---|
| Lo observado | 19 de 20 fichas encontradas; 2,4 minutos de promedio por aprobación; 3 propuestas reescritas |
| ¿Acertamos? | **Verdadero** para ambos supuestos |
| Confiabilidad real | Media |
| Decisión | **Escalar** al piloto, limitado a la variante A (`DEC-06`) |

### `PRU-03` (planeada)

| Frase | Respuesta |
|---|---|
| **Creemos que** (`SUP-01` y `SUP-03`) | Hoy hay unas 4 citas con error por cada 100, y los duplicados nacen de que el mismo paciente usa dos canales |
| **Para verificarlo, haremos** | Contar una semana las citas corregidas y revisar cada duplicado: ¿llegó por dos canales? |
| **Y mediremos** | Citas con error por cada 100 y la parte de duplicados entre canales distintos |
| **Acertamos si** | Entre 2 y 8 errores por cada 100, y más de la mitad de los duplicados entre canales distintos |

Nivel crítico: Crítico (16). Costo: Bajo. Tipo: experimento de proceso. Fidelidad: 1. Confiabilidad esperada: Media (una semana). Responsable: jefa de recepción. Fecha: 2026-11-09 al 2026-11-13.

### `PRU-04` (pausada)

| Frase | Respuesta |
|---|---|
| **Creemos que** (`SUP-08`) | La marca de posible urgencia detecta todos los mensajes que la odontóloga coordinadora clínica considera urgentes |
| **Para verificarlo, haremos** | Una demo funcional del paso de marca con 40 mensajes anonimizados que la odontóloga revisa por su cuenta |
| **Y mediremos** | Mensajes urgentes sin marcar |
| **Acertamos si** | Ninguno sin marcar en los 40 |

Nivel crítico: Crítico (20). Costo: Medio. Tipo: demo funcional (fidelidad 4). Confiabilidad esperada: Media. **Pausada**: depende de que la odontóloga escriba los criterios de urgencia (fecha 2026-11-13); sin ellos no hay contra qué comparar.

## Entregable: registro de evidencia

| Prueba | Supuesto | Estado | Fecha | Lo observado | ¿Acertamos? | Confiabilidad | Decisión |
|---|---|---|---|---|---|---|---|
| `PRU-01` | `SUP-04` | Hecha | 2026-10-29 | 17 de 30 mensajes con datos suficientes; 92 % en la variante A | Falso (parcial: se cumple en A) | Media | Iterar (`DEC-06`) |
| `PRU-02` | `SUP-05`, `SUP-06` | Hecha | 2026-11-02 al 2026-11-03 | 19 de 20 fichas; 2,4 min; 3 reescritas | Verdadero | Media | Escalar a piloto, variante A (`DEC-06`) |
| `PRU-03` | `SUP-01`, `SUP-03` | Planeada | 2026-11-09 | Pendiente | Pendiente | Pendiente | Pendiente |
| `PRU-04` | `SUP-08` | Pausada | Pendiente | Espera los criterios de urgencia | Pendiente | Pendiente | Pendiente |

| Supuesto | Antes (procedencia) | Ahora | Qué falta |
|---|---|---|---|
| `SUP-04` | Supuesto del diseño | Parcial: validado solo en la variante A (`PRU-01`) | Las variantes B, C y D |
| `SUP-05` | Dicho por participante | Validado en la variante A (`PRU-02`, confiabilidad Media) | Confirmar en el piloto con más solicitudes |
| `SUP-06` | Dicho por participante | Validado en la variante A (`PRU-02`, confiabilidad Media) | Confirmar con las dos recepcionistas |
| `SUP-01`, `SUP-03` | Dicho por participante | Pendiente por validar | `PRU-03` |
| `SUP-08` | Sin evidencia | Pendiente por validar | Criterios de urgencia y `PRU-04` |

**Hallazgo que cambia el diseño (`DEC-06`):** "una solicitud de cita" son al menos cuatro variantes (A cita nueva de un paciente con ficha, B control de un tratamiento, C pide para otra persona, D paciente nuevo); `FUT-01` a `FUT-03` suponían una sola. Qué se reabre en `disenar-proceso-futuro`: qué datos pide el flujo en B, C y D. Mientras tanto, el piloto se acota a la variante A, y B, C y D van a revisión de recepción.

**Supuesto nuevo:** `SUP-09`: "Creemos que en la variante B el profesional y el intervalo del control están en la ficha; es falso si faltan en más de 2 de cada 10 fichas de pacientes en tratamiento". Pendiente por validar: tarjeta por escribir.

**Siguiente paso sugerido:** `plan-piloto-y-especificacion`, con el piloto acotado a la variante A, la línea base de `PRU-03` y las condiciones de entrada del plugin Implementación Empresarial.

## Lo que se ve en este ejemplo

- Cada tarjeta fija el umbral antes de probar; ninguno se cambió después.
- Las pruebas son de fidelidad baja (papel y una hoja hecha a mano): no se construyó nada.
- `PRU-01` salió falsa y por eso se encontró que el proceso tiene variantes; la decisión fue iterar, no descartar.
- `PRU-02` salió verdadera, pero su confiabilidad es Media (una recepcionista y una sola variante) y se declaró así.
- Una prueba quedó pausada por una dependencia, y otra planeada: ninguna se dio por validada sin evidencia.
