# Ejemplo: Segmentación e ICP de una firma contable ficticia

Empresa inventada: **Brújula Contadores** (6 personas; 62 clientes activos; ticket mensual promedio de unos USD 210). Todo lo siguiente es ficticio. Continúa el ejemplo de `diagnostico-comercial`: problema `PRO-01` (propuestas a quien no es el perfil), `BAC-01` y la decisión `DEC-01`.

## Turno 1

**Facilitador:** Empecemos por `BAC-01`. ¿Cuáles son tus tres o cuatro mejores clientes, los que más valor dejan y menos esfuerzo piden, y qué tienen en común?

## Turno 2

**Usuaria (socia fundadora):** Una agencia de contenidos de nueve personas, un estudio de diseño de doce, un centro de fisioterapia y un consultorio de nutrición. Pagan a tiempo, entregan los documentos completos y nos recomiendan. Los cuatro tienen entre 4 y 15 personas y dueños que no quieren ocuparse de la contabilidad.

**Facilitador:** Revisé tu lista de los 9 clientes ganados en seis meses y las 7 propuestas perdidas por "no era el perfil" (negocios muy pequeños o sin facturación formal, `HAL-04`).

| Grupo | Ganados | Perdidos por no ser el perfil |
|---|---|---|
| Agencias y estudios creativos o digitales | 4 | 0 |
| Consultorios y centros de salud independientes | 3 | 1 |
| Comercios minoristas | 1 | 5 |
| Emprendimientos de comercio electrónico | 1 | 1 |

Esto es un **Hecho** (registro de la socia) para estos 9 y 7 casos; con tan pocos datos, los patrones son frágiles. ¿Qué otros grupos de clientes te han comprado o te han preguntado?

**Usuaria:** Esos cuatro grupos son los que aparecen, más o menos.

## Turno 3: matriz

| ID | Segmento | Potencial | Acceso | Rentabilidad | Competencia | Conversión | Total | Nota |
|---|---|---|---|---|---|---|---|---|
| `SEG-03` | Agencias y estudios creativos o digitales de 4 a 20 personas | 4 | 4 | 4 | 3 | 4 | 19 | 4 de 9 ganados, ninguno perdido por perfil (`HAL-04`) |
| `SEG-02` | Consultorios y centros de salud independientes de 3 a 12 personas | 4 | 3 | 4 | 3 | 4 | 18 | 3 de 9 ganados; acceso por recomendaciones de colegas |
| `SEG-04` | Emprendimientos de comercio electrónico en crecimiento | 4 | 2 | 3 | 2 | 3 | 14 | 1 ganado y 1 perdido; no hay camino de acceso claro |
| `SEG-01` | Comercios minoristas de 3 a 15 personas | 3 | 4 | 2 | 2 | 2 | 13 | 5 de 7 perdidos por perfil; poco margen, mucha rotación (nota por el 2 en rentabilidad: atender cuesta más de lo que dejan) |

Puntajes propuestos (**Inferencia de la IA**). La socia ajusta: sube acceso de `SEG-02` a 4 porque dos médicos le recomiendan a colegas. Totales finales: `SEG-03` 19 y `SEG-02` 19.

## Turno 4: foco

**Facilitador:** ¿Con cuáles dos segmentos empezamos y cuáles dejamos fuera por ahora?

**Usuaria:** `SEG-03` y `SEG-02`. Comercios, descartado por ahora; comercio electrónico, explorar después.

Decisión `DEC-02`: foco en `SEG-03` y `SEG-02`; `SEG-01` descartado por ahora (margen bajo y rotación alta, `HAL-04`); `SEG-04` en "explorar después". Lo cambiaría: si aparecen cinco consultas de comercio electrónico con facturación formal.

## Turno 5: ficha ICP

**Facilitador:** ¿Qué suele pasar en una de estas empresas justo antes de que busque contador?

**Usuaria:** Cambia de contador porque no les responde, les llega una multa, van a contratar a su quinta persona, o piden un préstamo y les piden estados financieros ordenados.

**ICP-01** (segmento `SEG-03`)

| Rasgo | Descripción | Procedencia |
|---|---|---|
| Actividad | Agencia o estudio creativo o digital (contenidos, diseño, desarrollo, medios) | Evidencia |
| Tamaño | De 4 a 20 personas; facturación entre USD 15.000 y 80.000 al mes | Supuesto (rango de la socia; se verifica con las próximas propuestas) |
| Cómo compra hoy | Contador independiente o una persona interna sin cierre mensual puntual | Dicho por participante |
| Problema | El dueño no tiene tiempo para ocuparse de la contabilidad y se entera tarde de sus números | Evidencia (4 clientes ganados) |
| Disparadores | Cambio de contador por falta de respuesta, multa tributaria, quinta contratación, solicitud de financiamiento (`HAL-06`) | Dicho por participante |
| Señales de encaje | Facturación formal, 1 a 3 socios, entregan documentos con regularidad | Evidencia |
| Exclusiones | Negocios sin facturación formal; facturación menor a USD 8.000 al mes; busca solo el precio más bajo; pide "firmar" sin llevar la contabilidad | Evidencia (`HAL-04`) |

**ICP-02** (segmento `SEG-02`): consultorios y centros de salud independientes de 3 a 12 personas, con honorarios profesionales y retenciones por manejar; disparadores: apertura de un segundo consultorio, nueva obligación tributaria, cambio de contador; exclusiones iguales a las de `ICP-01`.

## Mapa de actores de compra (`ICP-01`)

| ID | Rol | Cargo típico | Qué le importa | Qué teme | Cómo se le habla |
|---|---|---|---|---|---|
| `ACT-01` | Decisor y pagador | Socio gerente o dueño | Tranquilidad y números a tiempo para decidir | Una multa o una sorpresa de impuestos | Resultado y fecha de entrega, sin jerga contable |
| `ACT-02` | Usuario | Coordinadora administrativa | Que entregar documentos sea simple | Más trabajo | Qué hay que entregar, cuándo y cómo |
| `ACT-03` | Bloqueador potencial | Contador actual | Conservar al cliente | Perder ingresos | No se le critica: se hace un traspaso ordenado |
| `ACT-04` | Influenciador | Socio de finanzas o asesor legal | Orden para financiarse | Errores en estados financieros | Calidad del cierre y calendario tributario |
| `ACT-05` | Referidor | Cliente actual, asesor legal o gestor bancario | Quedar bien con su contacto | Que el servicio falle | Pedir recomendación con un caso concreto |

## Lista de cuentas (extracto, descripciones sin nombres)

| ID | Cuenta | Segmento | Nivel | Cómo se llega | Hipótesis (**Supuesto**) | Disparador | Entrada |
|---|---|---|---|---|---|---|---|
| `CUE-01` | Agencia de branding (10 personas) | `SEG-03` | A | Recomendada por un cliente actual | Cierre mensual tardío con su contador actual | Quejas por demoras | `ACT-01` |
| `CUE-02` | Productora audiovisual (14 personas) | `SEG-03` | A | Recomendada por un asesor legal | Quiere ordenar números para un préstamo | Solicitud de financiamiento | `ACT-04` |
| `CUE-03` | Agencia de desarrollo web (11 personas) | `SEG-03` | A | Contacto directo de un socio | Sin cierre mensual ordenado | Contratación de la quinta persona | `ACT-01` |
| `CUE-04` | Clínica de psicología (8 personas) | `SEG-02` | A | Recomendado por un colega | Manejo de honorarios y retenciones sin apoyo | Apertura de un segundo local | `ACT-01` |
| `CUE-05` | Consultorio odontológico (6 personas) | `SEG-02` | B | Sin camino directo | Cambio de contador cercano | Obligación tributaria nueva | `ACT-01` |

Hay cinco cuentas más en niveles B y C (`CUE-06` a `CUE-10`). Ninguna es cliente ni oportunidad abierta: todas están sin contactar (los clientes actuales y las oportunidades abiertas no van en esta lista); ningún mensaje sale sin que una persona lo revise y lo envíe.

**Mensajes clave (`ICP-01`, para `ACT-01`):** problema: "enterarte tarde de tus números y vivir con el temor de una multa"; resultado: "tu cierre mensual listo a tiempo y tus impuestos al día"; prueba hoy: cuatro clientes del segmento que renovaron, sin cifras de resultado todavía (**Pendiente por validar** la promesa de fecha de entrega, que se trabaja en `oferta-y-propuesta-de-valor`).

**Facilitador:** Siguiente paso (**Recomendación**): `oferta-y-propuesta-de-valor`, para convertir esos mensajes en una oferta y una razón de compra verificables. ¿Seguimos?

## Qué quedó claro del ejemplo

- El foco incluye lo que se descarta, con motivo y condición de cambio.
- La ficha trae exclusiones concretas y disparadores observables.
- La lista de cuentas no contiene nombres: son descripciones con hipótesis marcadas como Supuesto.
- Los mensajes no inventan prueba; lo que falta queda como Pendiente por validar.
