# Ejemplo: Facilitador de Implementación Empresarial en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `plan-piloto-y-especificacion` (plugin Automatización con IA): el flujo `FLU-01` (agendar citas, `RET-01`) tiene un `workflow-contract.yaml` con madurez `pilot`, ocho pasos `FUT-01` a `FUT-08`, once estados, cuatro políticas de aprobación (`APR-01` a `APR-04`), seis evidencias (`EVD-01` a `EVD-06`) y seis pruebas de aceptación (`AT-01` a `AT-06`). Patrón híbrido (`DEC-05`), guardrails `GRD-01` a `GRD-07`, riesgos `RIE-01` a `RIE-06`. Las decisiones de diseño llegaron hasta `DEC-07`.

El piloto corrió del 2026-11-16 al 2026-11-27. La clínica no tiene equipo de TI propio: la implementación la hace su **proveedor de TI externo** con acompañamiento de una consultora de Distilled. Quien habla es el líder técnico del proveedor; Valeria (directora) aprueba.

## Turno 1

**Líder técnico:** Nos pidieron llevar a producción el flujo de citas que diseñaron con la consultora. ¿Por dónde empezamos?

**Facilitador:** Antes de hablar de construcción necesito la especificación del flujo. ¿Tienen el `workflow-contract.yaml` que salió del plan piloto, o pueden resumirme en un párrafo qué pasos tiene y cuáles envían o registran algo fuera del flujo?

## Turno 2

**Líder técnico:** Sí, aquí está el archivo (lo adjunta). También el informe de cierre del piloto.

**Facilitador:** Lo revisé con la lista de `references/rutas-de-implementacion.md`.

| Comprobación | Resultado |
|---|---|
| Claves obligatorias y pasos completos | Pasa: los ocho pasos traen disparador, entradas, salidas, estados, idempotencia y evidencia |
| Referencias | Pasa: actores, estados, políticas y evidencias existen; las ramas de `FUT-02` y `FUT-05` están declaradas |
| Efectos externos | Pasa: `FUT-06` (propuesta al paciente) y `FUT-08` (registro y confirmación) tienen `APR-01` y `APR-02` y clave de idempotencia |
| Valores "por definir" | Tres: plazo de espera de `FUT-07`, retención de `EVD-01` a `EVD-06`, y el rol aprobador "Recepcionista del piloto", que en producción no existe |
| Datos | Pasa: solo roles y capacidades |
| Madurez | `pilot` |

Resultados del cierre del piloto (Hecho, piloto; muestra pequeña, indicativos): 3,4 minutos por solicitud en 20 solicitudes cronometradas de la variante A (meta: 3); ninguna urgencia sin marcar en una revisión de 40 mensajes; 15 de cada 100 propuestas reescritas; 1 cita con error en 94. ¿Quién decidió que el flujo pasa a implementación, y con qué condiciones?

## Turno 3

**Líder técnico:** Valeria lo decidió el 4 de diciembre. Dijo que pasa, pero que la administradora todavía tiene que autorizar el uso de datos reales en producción y que las reglas de agenda de enero tienen que estar escritas antes de salir.

**Facilitador:** Entonces la puerta **pasa con condiciones** (`DEC-08`). Lo registro con lo que no se cumplió: el criterio de éxito era 3 minutos o menos y el piloto dio 3,4 (Hecho, piloto, muestra pequeña); Valeria lo aceptó y la meta de 3 minutos se vuelve a medir en producción. Las condiciones quedan en el registro con dueño y fecha; la autorización de datos bloquea cualquier conexión con datos reales hasta que exista. ¿La plataforma ya la decidió la clínica, o es una de las decisiones que tenemos que tomar?

## Turno 4

**Líder técnico:** No está decidida. La clínica usa correo y documentos en la nube de un proveedor grande, pero nadie dijo que tenga que ser ahí.

**Facilitador:** Entonces la ruta es la **completa**: primero una arquitectura lógica, sin productos; la plataforma la elige la clínica en el mapeo de capacidades, como decisión registrada. Que ya usen un proveedor es un dato para esa decisión, no una elección. Hay un valor del contrato que no puede quedar implícito: el plazo de espera de la respuesta del paciente en `FUT-07`. ¿Quién lo fija y para cuándo?

## Turno 5

**Líder técnico:** La jefa de recepción, la semana que viene. Y la retención de evidencias la decide la administradora. Valeria también dijo que en producción aprueban las dos recepcionistas, no solo la del piloto. Finalizar.

**Facilitador:** Con eso cierro el diagnóstico.

## Entregable: resumen de cinco puntos

1. Hay un contrato válido de `FLU-01` con madurez `pilot`; pasa la revisión con tres valores por definir. (Evidencia)
2. La puerta de entrada pasa con condiciones: autorización de datos para producción y reglas de agenda de enero; el tiempo por solicitud (3,4 minutos) no alcanzó el umbral de 3 minutos y Valeria lo aceptó (`DEC-08`, Decisión de Valeria).
3. Ruta completa; la plataforma se decide en el mapeo de capacidades (`DEC-09`). Que la clínica use un proveedor de nube para correo es Dicho por participante, no una decisión.
4. Hay un cambio al contrato: el aprobador de `APR-01` a `APR-04` pasa de "Recepcionista del piloto" a "Recepcionista de turno" (`DEC-13`, pendiente de la jefa de recepción como dueña del contrato).
5. Incertidumbre principal: los valores del cliente (plazo de espera, retención) y la autorización de datos; ninguno bloquea la arquitectura lógica, todos bloquean la salida a producción.

## Entregable: registro de decisiones (extracto)

Flujo: Agendar citas (`FLU-01`). Contrato: `workflow-contract.yaml` (madurez `pilot`, 2026-11-03). Aprueba las decisiones de implementación: Valeria (directora). Última actualización: 2026-12-07.

| ID | Decisión | Alternativas consideradas | Dueño | Fecha | Aprobación | Procedencia | Toca |
|---|---|---|---|---|---|---|---|
| `DEC-08` | La puerta de entrada a la etapa C pasa con condiciones: autorización de datos para producción (`RIE-06`) y reglas de agenda de enero escritas antes de salir (`RIE-05`). Criterio no cumplido y aceptado: 3,4 minutos por solicitud frente al umbral de 3 o menos (piloto, 20 solicitudes); la meta se mide de nuevo en producción | Pasar sin condiciones; repetir el piloto | Valeria | 2026-12-04 | Aprobada por Valeria | Decisión | `RET-01`, `RIE-05`, `RIE-06` |
| `DEC-09` | Ruta completa; la plataforma se decide en el mapeo de capacidades | Elegir ya el proveedor que usan para correo | Valeria | 2026-12-07 | Aprobada por Valeria | Decisión | Todo el contrato |
| `DEC-10` | Alcance inicial de producción: variante A, por mensaje y formulario; variantes B, C y D siguen en la cola de revisión | Ampliar a todas las variantes | Valeria | 2026-12-07 | Aprobada por Valeria | Decisión | `FUT-01`, `extensions.pilot_scope` |
| `DEC-11` | Plazo de espera de la respuesta del paciente en `FUT-07` | 24 horas; 48 horas; hasta el día anterior a la cita | Jefa de recepción | Para 2026-12-11 | Pendiente | Pendiente por validar | `FUT-07` |
| `DEC-12` | Retención de las evidencias `EVD-01` a `EVD-06` | Por definir con la administradora | Administradora | Para 2026-12-18 | Pendiente | Pendiente por validar | `EVD-01` a `EVD-06` |
| `DEC-13` | Cambio al contrato: aprobador de `APR-01` a `APR-04` = "Recepcionista de turno" | Mantener una sola recepcionista aprobadora | Jefa de recepción (dueña del contrato) | Para 2026-12-11 | Pendiente | Dicho por participante (Valeria) | `APR-01` a `APR-04` |

**Valores de configuración del cliente**

| Valor | Dónde aparece | Valor decidido | Decisión | Dueño | Para cuándo |
|---|---|---|---|---|---|
| Plazo de espera de respuesta | `FUT-07` | Pendiente | `DEC-11` | Jefa de recepción | 2026-12-11 |
| Retención de evidencias | `EVD-01` a `EVD-06` | Pendiente | `DEC-12` | Administradora | 2026-12-18 |
| Rol aprobador | `APR-01` a `APR-04` | Recepcionista de turno (propuesto) | `DEC-13` | Jefa de recepción | 2026-12-11 |
| Hora del aviso "al final del día" | `on_timeout` de `APR-01` y `APR-02` | Pendiente | Por registrar en `arquitectura-de-implementacion` | Jefa de recepción | Por definir con la jefa de recepción |
| Plataforma | Todo el flujo | Por decidir | `DEC-09` (se decide en el mapeo) | Valeria | Al cerrar el mapeo |

## Entregable: estado de la implementación

```yaml
organizacion: Clínica Dental Sonrisa Norte
actualizado: 2026-12-07
flujo: FLU-01 Agendar citas
contrato:
  existe: true
  madurez: pilot
  revision: pasa con observaciones
  observaciones:
    - "FUT-07: plazo de espera por definir (DEC-11)"
    - "EVD-01 a EVD-06: retención por definir (DEC-12)"
    - "APR-01 a APR-04: aprobador del piloto no existe en producción (DEC-13)"
puerta_de_entrada:
  resultado: pasa con condiciones
  decidio: Valeria (directora)
  decision: DEC-08
  condiciones:
    - "Autorización de datos reales para producción (administradora, RIE-06)"
    - "Reglas de agenda de enero escritas antes de salir (jefa de recepción, RIE-05)"
    - "Criterio de 3 minutos no alcanzado en el piloto (3,4); aceptado por Valeria y se vuelve a medir en producción"
ruta: completa
plataforma:
  estado: por decidir
  decision: DEC-09
decisiones_abiertas:
  - {id: DEC-11, tema: plazo de espera, dueno: Jefa de recepción, para: 2026-12-11}
  - {id: DEC-12, tema: retención de evidencias, dueno: Administradora, para: 2026-12-18}
  - {id: DEC-13, tema: rol aprobador en producción, dueno: Jefa de recepción, para: 2026-12-11}
skills:
  arquitectura-de-implementacion: pendiente
  mapeo-de-capacidades-de-plataforma: pendiente
  integracion-segura-y-aprobaciones: pendiente
  idempotencia-y-confiabilidad: proximamente
  pruebas-y-evaluacion: proximamente
  release-y-transferencia: proximamente
  operacion-y-aseguramiento-continuo: proximamente
siguiente_skill: arquitectura-de-implementacion
```

**Siguiente paso sugerido:** `arquitectura-de-implementacion`, porque convierte los ocho pasos del contrato en componentes lógicos con límites claros antes de mirar ninguna plataforma; los valores pendientes no la bloquean. `pruebas-y-evaluacion` está Próximamente: los criterios de aceptación de producción se dejan como pendiente con dueño.

## Lo que se ve en este ejemplo

- El facilitador pidió el contrato antes de hablar de construcción y lo revisó con una lista, sin completarlo inventando pasos.
- La puerta "pasa con condiciones" se registró como decisión de Valeria, no del equipo técnico.
- Que la clínica ya use un proveedor de nube quedó como dato, no como elección de plataforma.
- Cada valor "por definir" del contrato se convirtió en una decisión con dueño y fecha, aunque siga Pendiente.
- El cambio de aprobador no se hizo en silencio: es un cambio al contrato que aprueba su dueña.
- Las cifras del piloto se rotularon como piloto e indicativas.
