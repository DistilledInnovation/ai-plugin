# Ejemplo: Descubrir procesos en una distribuidora ficticia

Empresa inventada: **Distribuidora Rioclaro** (insumos de oficina y limpieza para empresas pequeñas; 85 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo del facilitador: Daniela, gerente de operaciones, no sabe qué automatizar y tiene un dato (`HAL-01`: unos 120 pedidos al día se copian a mano, unos 6 minutos cada uno).

## Turno 1

**Usuaria:** Quiero entender dónde está el tiempo perdido de verdad. Tengo cuatro áreas: Atención al Cliente, Cuentas por Cobrar, Bodega y Ventas.

**Facilitador:** Perfecto, vamos por áreas. Para empezar con el contexto: ¿qué resultado del negocio te preocupa más este trimestre?

## Turno 2

**Usuaria:** Que los clientes reciban su pedido correcto y a tiempo. Hoy se nos quejan de errores y de que no saben dónde está su pedido.

**Facilitador:** Anoto eso como el resultado que importa (Dicho por participante). Ahora el trabajo real: ¿me cuentas cómo fue el último pedido por correo que llegó, desde que entró hasta que salió de bodega?

## Turno 3

**Usuaria:** Llegó un correo con una lista de productos escrita en párrafos. Alguien de Atención lo leyó, buscó los códigos de cada producto, los tecleó en el sistema de pedidos y respondió confirmando. Después Bodega lo recibió impreso. Esta semana a Bodega le llegaron dos pedidos con el código equivocado.

**Facilitador:** Gracias. Para la evidencia: ¿cuántos de esos errores de código ves por semana y cómo lo sabes?

## Turno 4

**Usuaria:** Bodega dice que unos 4 de cada 100, pero no lo han contado.

**Facilitador:** Lo anoto como Dicho por participante (`SUP-01`: error de unos 4 de cada 100 pedidos, pendiente por validar; se puede contar una semana de devoluciones).

Para descomponer: de los pasos del pedido, ¿cuáles siguen reglas claras y cuáles requieren que alguien interprete?

**Usuaria:** Buscar el código y teclearlo es siempre igual. Interpretar es cuando el cliente escribe "las hojas grandes". Y si no hay stock, decide la jefa de Atención.

## Turno 5

Daniela pide a un representante de cada área que llene una ficha de señal. Llegan cinco más. Resumen de las siete fichas (ficticias):

| ID | Área | Situación (hecho) | Magnitud |
|---|---|---|---|
| `SEN-01` | Atención | Copian pedidos por correo y chat al sistema | Relevancia 5, urgencia 4; unos 120/día, unos 6 min cada uno (medido en 20 pedidos) |
| `SEN-02` | Atención | Clientes preguntan "¿dónde está mi pedido?" y hay que revisar en tres lugares | Relevancia 3, urgencia 3; unas 40 consultas al día, unos 4 min cada una (Dicho por participante) |
| `SEN-03` | Cuentas por Cobrar | Concilian pagos con facturas y hay diferencias | Relevancia 4, urgencia 3; unas 25 diferencias por semana, unos 30 min cada una (Dicho por participante) |
| `SEN-04` | Bodega | Reciben pedidos con código de producto equivocado | Relevancia 4, urgencia 4; unos 4 de cada 100 (No sé: no se ha contado) |
| `SEN-05` | Ventas | Preparan cotizaciones a medida para clientes grandes | Relevancia 3, urgencia 2; unas 6 por semana, unas 2 h cada una |
| `SEN-06` | Ventas | Clientes llaman a su vendedor para preguntar por el estado de su pedido | Relevancia 3, urgencia 3; No sé la frecuencia |
| `SEN-07` | Finanzas | Aprobar crédito a clientes nuevos toma dos días porque la información está en tres lados | Relevancia 2, urgencia 2; unas 8 por semana, unas 1,5 h cada una |

## Turno 6

**Facilitador:** Al leerlas, veo dos pares que podrían ser el mismo problema: `SEN-01` con `SEN-04` (los códigos equivocados nacen al teclear los pedidos) y `SEN-02` con `SEN-06` (dos áreas respondiendo lo mismo: dónde está el pedido). ¿Son el mismo problema visto desde lados distintos?

**Usuaria:** Sí, ambos pares.

## Entregable: inventario de oportunidades

| ID | Oportunidad | Señales | Quién la vive | Frecuencia | Tiempo por vez | Relev. / Urg. | Evidencia | Primera lectura (provisional) |
|---|---|---|---|---|---|---|---|---|
| `OPO-01` | Registrar pedidos sin teclear a mano y sin errores de código | `SEN-01`, `SEN-04` | Atención, Bodega | ~120 al día | ~6 min | 5 / 4 | **Hecho** (medido en 20 pedidos); el error del 4 % es **Supuesto** (`SUP-01`) | Asistir o automatizar |
| `OPO-02` | Responder dónde está el pedido | `SEN-02`, `SEN-06` | Atención, Ventas | ~40 al día | ~4 min | 3 / 3 | Dicho por participante; la frecuencia de Ventas, No sé | Simplificar (primero saber dónde vive el estado) |
| `OPO-03` | Conciliar pagos con facturas | `SEN-03` | Cuentas por Cobrar | ~25 por semana | ~30 min | 4 / 3 | Dicho por participante | Aún no se sabe |
| `OPO-04` | Cotizaciones a medida | `SEN-05` | Ventas | ~6 por semana | ~2 h | 3 / 2 | Dicho por participante | Asistir |
| `OPO-05` | Aprobación de crédito a clientes nuevos | `SEN-07` | Finanzas | ~8 por semana | ~1,5 h | 2 / 2 | Dicho por participante | Mantener humano |

Descomposición de `OPO-01`: reglas claras (buscar el código, teclearlo); interpretación (frases como "las hojas grandes"); juicio (qué hacer si no hay stock, decide la jefa de Atención).

Pendientes por validar: contar una semana de pedidos con error (`SUP-01`); frecuencia real de consultas desde Ventas; qué pasa con las diferencias de pago (si son pocos tipos o muchos).

Sin elegir tecnología. **Siguiente paso sugerido:** `definir-reto-de-automatizacion` para `OPO-01`, la de mayor magnitud y con evidencia, y después encuadrar las demás de forma breve para poder priorizar.

## Lo que se ve en este ejemplo

- No se abrió con "¿qué quieres automatizar?": se empezó por el resultado de negocio.
- Se pidió el último caso real y luego la evidencia, y lo no medido quedó como Supuesto.
- Dos pares de señales de áreas distintas se agruparon con confirmación de la persona.
- La primera lectura es provisional y no incluye tecnología.
