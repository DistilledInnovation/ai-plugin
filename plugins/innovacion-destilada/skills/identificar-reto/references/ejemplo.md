# Ejemplo: Identificar reto en una empresa de transporte ficticia

Empresa inventada: **Transportes Marea Azul** (carga refrigerada regional, 65 empleados, 22 camiones, ventas de unos USD 3,1 millones al año). Todo es ficticio.

## Turno 1

**Facilitador:** Ya tengo el estado del proyecto: etapa preparar, sin reto. Primera pregunta: ¿qué ha pasado en tu negocio o tu entorno que te hace pensar que hay algo que innovar?

**Usuaria (Paula, gerente comercial):** Perdimos dos clientes grandes de pescado fresco este año. Dijeron que no podían saber dónde iba su carga. Y los camiones vuelven vacíos casi la mitad de los viajes.

**Facilitador:** Registro: `HAL-01` (dicho por participante): se perdieron 2 clientes por falta de visibilidad de la carga. `HAL-02` (dicho por participante): casi 50 % de los retornos vacíos, **Pendiente por validar** con datos de despacho. Los clasifico así: HAL-01 es un *problema*, HAL-02 un *activo desaprovechado* (capacidad ociosa). ¿Esta lectura te cuadra?

## Turno 2

**Usuaria:** Sí.

**Facilitador:** Ahora el modelo de negocio, por partes. Primero: ¿a quién le vendes?

**Usuaria:** A productores y distribuidores de alimentos frescos.

(En turnos siguientes, de a una pregunta, cuenta qué ofrece (transporte con frío garantizado) y cómo cobra (por viaje y por kilo); se completan los 9 bloques; se marcan con tensión: propuesta de valor, relación con clientes, recursos. Se repasan las fuerzas del entorno: un competidor ofrece rastreo en línea y aumentan las exigencias de trazabilidad de los compradores. Se bosqueja el Perfil del Cliente como supuesto.)

## Turno 3: alternativas y priorización

**Facilitador:** Con lo que me contaste, estas preguntas del libro resuenan. Reescritas para tu caso:
- ¿Cómo podemos desarrollar una propuesta de valor que los competidores no puedan copiar? (pregunta 3)
- ¿A partir de qué activos con los que contamos podemos apoyarnos? (pregunta 7, capacidad ociosa)
- ¿Cómo podemos generar una nueva propuesta de valor aprovechando las relaciones y canales existentes? (pregunta 9)

¿Cuáles te generan más interés?

**Usuaria:** Me importa más lo de la confianza de los clientes. Lo de los retornos puede esperar.

## Entregable final

# Ficha de reto: Visibilidad de la carga

Proyecto: Marea Azul, 2026-10-25, borrador 1

**Reto priorizado `RET-01` (hipótesis):** ¿Cómo podemos lograr que los productores de alimentos frescos confíen en que su carga llega a tiempo y en buen estado, y lo puedan comprobar durante todo el viaje?

| ID | Reto | Tipo | Interés | Urgencia | Potencial | Evidencia | Decisión |
|---|---|---|---|---|---|---|---|
| RET-01 | Confianza y visibilidad de la carga | Problema | Alto | Alta | Alto | Media (2 clientes perdidos, dicho por participante) | Prioritario |
| RET-02 | Aprovechar la capacidad de retorno vacío | Activo desaprovechado | Medio | Media | Alto | Baja | Otro horizonte (`DEC-01`) |

**Actores**

| Actor | Rol | Procedencia |
|---|---|---|
| Productores y distribuidores de alimentos frescos | Afectado | Dicho por participante |
| Conductores | Ejecuta | Observación del facilitador (Inferencia de la IA: serían quienes reportan estado) |
| Paula y gerencia | Decide | Dicho por participante |

Perfil ideal de solucionadores: personas con experiencia en cadena de frío, sensores o comunicación con clientes.

**Evidencias (Hecho)**: `HAL-01` pérdida de 2 clientes grandes este año (dicho por participante; falta confirmar con registros de ventas).

**Supuestos**

| ID | Supuesto | Prueba |
|---|---|---|
| SUP-01 | Los clientes se fueron por falta de visibilidad, no por precio | Pendiente por validar |
| SUP-02 | Casi el 50 % de los retornos van vacíos | Pendiente por validar con datos de despacho |
| SUP-03 | Un cliente que ve su carga confía más | Pendiente por validar |

**Preguntas de investigación:** ¿Qué hizo el cliente perdido para decidir irse y qué alternativa eligió? ¿Qué información quiere ver y cuándo? Se averigua con entrevistas a los dos clientes perdidos y a tres actuales.

**Alcance preliminar:** dentro, la experiencia de seguimiento de carga; fuera, la renovación de flota. Horizonte: 3 meses para investigar.

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RIE-01 | La causa real es el precio y no la visibilidad | El reto sería incorrecto | Entrevistar antes de diseñar solución |

Siguiente paso sugerido: `investigar-y-empatizar`, para validar con los clientes si el reto es el correcto. No se eligió tecnología de rastreo: sería una decisión de etapas posteriores.
