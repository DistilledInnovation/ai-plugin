# Ejemplo: Plan piloto y especificación en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Continúa el ejemplo de `prototipos-y-tarjetas-de-prueba`: el flujo `FLU-01` (agendar citas, `RET-01`) tiene un canvas en Borrador 1 con un piloto provisional (dos semanas, mensajes y formulario); la prueba `PRU-01` salió falsa y reveló cuatro variantes de solicitud (`DEC-06`: iterar, piloto acotado a la variante A, cita nueva de un paciente con ficha); `PRU-02` salió verdadera en esa variante (19 de 20 fichas, 2,4 minutos por aprobación, 3 propuestas reescritas; confiabilidad Media); `PRU-03` (errores y duplicados) está planeada y `PRU-04` (urgencias) pausada hasta que existan los criterios. Patrón `DEC-05`: híbrido; niveles de autoridad y guardrails `GRD-01` a `GRD-07`; `SUP-06` a `SUP-09` ya registrados.

## Turno 1

**Usuaria (Valeria):** Con lo que probamos, armemos el piloto y dejemos todo por escrito para pasar a implementación.

**Facilitador:** Con la evidencia, el piloto más pequeño que sigue enseñando algo es la variante A: cita nueva de un paciente con ficha, por mensaje o formulario. En la muestra de 30 mensajes fueron 13, el 43 %; sobre las 24 solicitudes diarias por esos dos canales serían unas 10 al día (Supuesto). ¿Lo hacemos como decía el canvas: una recepcionista con el flujo nuevo dos semanas y la otra como hoy, para comparar?

## Turno 2

**Usuaria:** Sí. Y las variantes B, C y D siguen como hoy, o que pasen a revisión, no queremos ensuciar el piloto.

**Facilitador:** Anotado: B, C y D quedan fuera y van a la cola de revisión de recepción. Dos semanas son 10 días hábiles: unas 100 solicitudes (Supuesto), pocas para concluir una tasa de errores; la dejo como indicativa. Para el criterio de éxito: ¿qué tendría que pasar para que el piloto cuente como bueno?

## Turno 3

**Usuaria:** Tres minutos por solicitud, lo que ya dijimos, y que en ninguna revisión se pase una urgencia. Si pasa una, se para la parte con IA.

**Facilitador:** Lo escribo con umbrales: éxito, 3 minutos de promedio en 20 solicitudes cronometradas, no más de 2 propuestas reescritas de cada 10 y ninguna urgencia sin marcar en una revisión de muestra de 40; parada inmediata si una urgencia queda sin marcar o si un paciente recibe datos de otra persona. Como la línea base de 6 minutos es de todas las variantes (`HAL-01`), mediremos 20 solicitudes de la variante A con el método de hoy antes de empezar. ¿Qué haría que construir esto fuera más grande o más pequeño de lo que parece?

## Turno 4

**Usuaria:** Más grande si hubiera que incluir las otras variantes, porque cada una pide datos distintos. El mantenimiento sigue siendo Medio por las reglas de diciembre.

**Facilitador:** Entonces para el piloto, construir es Medio; si se amplía a B, C y D, de Medio a Alto (Supuesto). Operar, Bajo a Medio por la revisión diaria; mantener, Medio (Dicho por participante). El retorno sigue en "No sé". Para los próximos pasos: ¿quién escribe las reglas de agenda y los criterios de urgencia, y para cuándo?

**Usuaria:** La jefa de recepción las reglas, para el 6 de noviembre; la odontóloga los criterios, para el 13.

## Turno 5

**Facilitador:** Con eso armo el plan, la especificación del flujo en `workflow-contract.yaml` y reviso si el flujo está listo para pasar a Implementación Empresarial. Una advertencia que va en el contrato: la definición es portable, pero la ejecución puede ser distinta en cada plataforma. ¿Quién aprueba el plan?

**Usuaria:** Lo apruebo yo después de revisarlo con mi socio. Finalizar.

## Entregable: plan piloto

Flujo `FLU-01` Agendar citas. Versión: borrador 2 (2026-11-03). Aprueba el plan: Valeria (`DEC-07`, pendiente).

### Alcance, usuarios y duración (bloque 10)

| Elemento | Respuesta |
|---|---|
| Qué entra | Variante A (cita nueva de un paciente con ficha) por mensaje y formulario: unas 10 al día (Supuesto: 13 de 30 mensajes de la muestra de `PRU-01`, sobre 24 al día de `SUP-02`) |
| Qué no entra | Llamadas, variantes B, C y D (van a la cola de revisión de recepción), reagendar y cancelar (`FLU-02`) |
| Usuarios | Una recepcionista opera; la otra sigue como hoy y sirve de comparación; la jefa de recepción revisa las excepciones |
| Duración y fechas | Dos semanas (10 días hábiles, unas 100 solicitudes, Supuesto): 2026-11-16 al 2026-11-27 (Propuesta) |
| Autoridad y guardrails | Lo que toca al paciente o a la agenda, nivel 2; urgencias, nivel 1; `GRD-01` a `GRD-07` |
| Modo manual | Como hoy; la jefa de recepción puede apagar la parte con IA sin pedir permiso |

### Línea base → meta (bloque 9)

| Métrica | Línea base (procedencia) | Meta | Prototipo | Piloto | Producción |
|---|---|---|---|---|---|
| Tiempo de trabajo por solicitud | 6 min (`HAL-01`, 20 solicitudes de todas las variantes, Hecho); falta la de la variante A | 3 min | 2,4 min por aprobación en una hoja hecha a mano (`PRU-02`, no incluye lectura ni registro) | Cronometrar 20 solicitudes de la variante A, antes con el método de hoy y durante el piloto | Pendiente: después de la etapa C |
| Citas con error | Unas 4 de cada 100 (`SUP-01`, Dicho por participante, sin contar; `PRU-03`) | 1 de cada 100 | Sin dato | Contar las citas corregidas; indicativo con unas 100 solicitudes | Pendiente |
| Confirmación al paciente | El mismo día (Dicho por participante, en `RET-01`) | No empeora | Sin dato | Tiempo hasta la confirmación | Pendiente |
| Casos que pasan a revisión | No sé | Sin meta todavía | Sin dato | Contarlos (incluye las variantes B, C y D) | Pendiente |

### Criterios de éxito y de parada

| Tipo | Criterio (fijado antes de empezar) | Quién lo revisa |
|---|---|---|
| Éxito | Promedio de 3 minutos o menos en 20 solicitudes cronometradas de la variante A | Jefa de recepción |
| Éxito | No más de 2 propuestas reescritas de cada 10 | Jefa de recepción |
| Éxito | Ninguna urgencia sin marcar en una revisión de muestra de 40 mensajes | Odontóloga coordinadora clínica |
| Parada | Una urgencia sin marcar: se apaga la parte con IA y se vuelve al modo manual | Jefa de recepción |
| Parada | Un paciente recibe datos de otra persona (`RIE-01`): se detienen los envíos | Jefa de recepción |
| Parada | Más de 2 de cada 10 propuestas reescritas durante tres días seguidos | Jefa de recepción y Valeria |

Muestra: unas 100 solicitudes; la tasa de errores es **indicativa, no concluyente**, y no se declarará éxito o fracaso por uno o dos casos de diferencia.

### Qué aprenderemos

| Pregunta o supuesto | Cómo lo sabremos | Decisión que habilita |
|---|---|---|
| `SUP-07` (aceptan uno de tres horarios) | Cuántos pacientes piden otro horario en las primeras 20 propuestas | Ajustar la propuesta |
| `SUP-06` con las dos recepcionistas | Minutos por aprobación y reescrituras con la segunda persona | Ampliar usuarios |
| `SUP-08` con casos reales | Revisión de muestra de urgencias | Mantener el nivel 1 o revisarlo |
| `SUP-09` (en variante B, el profesional y el intervalo del control están en la ficha) | Revisar fichas de pacientes en tratamiento | Decidir si se diseña la variante B |
| Cuántos casos pasan a revisión | Contarlos | Dimensionar la revisión diaria |

### Costo y esfuerzo (bloque 11)

| Dimensión | Piloto (variante A) | Si se amplía a B, C y D | Factores | Procedencia |
|---|---|---|---|---|
| Construir | Medio | Medio a Alto | Reglas de agenda por escribir, dos pasos con IA, aprobaciones, conexión con la agenda y las fichas; cada variante pide datos distintos | Supuesto |
| Operar | Bajo a Medio | Medio | Revisión diaria de casos dudosos | Supuesto |
| Mantener | Medio | Medio | Las reglas de agenda cambian en diciembre y enero (Dicho por participante) | Supuesto |

Retorno esperado: No sé. Capacidad liberada si el piloto cumple la meta solo en la variante A: unas 11 horas por mes (3 min × 10 solicitudes × 22 días), una **meta, no un resultado**; las 44 horas por mes del canvas suponían todas las solicitudes.

### Próximos pasos (bloque 12)

Las fechas que dio Valeria se usan tal cual; las demás son propuestas del facilitador, para que ella las confirme.

| Acción | Responsable | Fecha | Dependencia |
|---|---|---|---|
| Escribir las reglas de agenda | Jefa de recepción | 2026-11-06 (dada por Valeria) | Ninguna |
| Contar una semana de citas con error y revisar los duplicados (`PRU-03`) | Jefa de recepción | 2026-11-09 al 2026-11-13 (Propuesta) | Ninguna |
| Escribir los criterios de urgencia (desbloquea `PRU-04`) | Odontóloga coordinadora clínica | 2026-11-13 (dada por Valeria) | Ninguna |
| Cronometrar 20 solicitudes de la variante A con el método de hoy | Recepción | 2026-11-13 (Propuesta) | Ninguna |
| Aprobar el plan y el contrato | Valeria | 2026-11-13 (Propuesta) | Revisión con su socio |
| Iniciar el piloto | Jefa de recepción | 2026-11-16 (Propuesta) | Reglas, criterios y aprobación |
| Rediseñar las variantes B, C y D con `disenar-proceso-futuro` (no bloquea el piloto) | Facilitador y jefa de recepción | 2026-11-20 (Propuesta) | `PRU-01` |
| Evaluar la puerta de entrada a Implementación Empresarial | Valeria y jefa de recepción | 2026-12-04 (Propuesta) | Cierre del piloto |

### Puerta de entrada a la etapa C

Resultado de hoy: **No pasa todavía**. Se evalúa de nuevo al cerrar el piloto (2026-12-04), con la decisión de Valeria.

| Condición | Cumple | Evidencia o pendiente |
|---|---|---|
| Supuestos críticos con evidencia o decisión sobre el riesgo | Parcial | `SUP-04` parcial (variante A); `SUP-08`, `SUP-01` y `SUP-03` pendientes (`PRU-03`, `PRU-04`) |
| El piloto dio resultados reales frente a la meta | No | Aún no empieza; las cifras actuales son de prototipo |
| Dueño del flujo y quien aprueba el pase | Sí | Jefa de recepción y Valeria |
| Niveles de autoridad y guardrails; modo manual funciona | Parcial | Definidos; falta probar que la jefa puede apagar la parte con IA |
| Datos sensibles y autorización de uso | Parcial | Autorización de la administradora solo para las pruebas (`RIE-06`); falta la del piloto |
| Contrato conforme al esquema y trazable al canvas | Sí | `workflow-contract.yaml` |
| Costo y esfuerzo reevaluados con datos del piloto | No | Después del piloto |
| Criterios de aceptación para producción | No | Pendiente: se definen con el equipo de implementación |

## Entregable: especificación portable

Se entrega `workflow-contract.yaml` (versión `1.0`, madurez `pilot`) siguiendo `assets/workflow-contract.schema.json`. Fragmento:

```yaml
workflow_id: FLU-01
version: "1.0"
metadata:
  name: Agendar citas
  owner: Jefa de recepción
  maturity: pilot
  source_refs: [RET-01, DEC-05, DEC-06, SUP-04, PRU-01, PRU-02]
steps:
  - step_id: FUT-06
    name: Calcular horarios y proponer tres opciones
    kind: deterministic
    actor: ACT-05
    trigger: {type: previous_step, description: "Urgencia descartada por una persona.", after_step: FUT-05}
    inputs:
      - {name: confirmed_patient, description: "Paciente confirmado: por coincidencia exacta en FUT-02 o por recepción en FUT-03.", type: record, required: true, sensitivity: sensitive}
      - {name: appointment_type, description: "Tipo de cita pedido, leído en FUT-01 y revisado por recepción (APR-04).", type: text, required: true, sensitivity: internal}
    outputs:
      - {name: proposal_sent, description: "Mensaje con tres horarios libres.", type: text, required: true, sensitivity: personal}
    authority_level: 2
    guardrails: [GRD-03]
    approval_policy: APR-01
    external_effect: true
    success_state: ST-06
    failure_state: ST-09
    idempotency:
      strategy: idempotency_key
      key_fields: [request_id, proposal_version]
      notes: "Una propuesta por solicitud y versión."
    evidence: [EVD-04]
approval_policies:
  - policy_id: APR-01
    applies_to: [FUT-06]
    approver_role: Recepcionista del piloto
    condition: "Siempre, mientras dure el piloto, antes de enviar la propuesta."
```

(El archivo completo trae los ocho pasos `FUT-01` a `FUT-08`, seis actores, once estados (`ST-11` es la espera de una coincidencia dudosa; un paciente sin ficha o con una solicitud abierta va a la cola de revisión `ST-09`), cuatro políticas de aprobación, seis evidencias, cuatro métricas y seis pruebas de aceptación.)

| Requisito del esquema | Cómo cumple el ejemplo |
|---|---|
| Claves obligatorias de primer nivel | Están `workflow_id`, `version` (`"1.0"`), `actors`, `states`, `steps`, `approval_policies` y `evidence_requirements` |
| Claves obligatorias de cada paso | Los ocho pasos traen `step_id`, `trigger`, `inputs`, `outputs`, `success_state`, `failure_state`, `idempotency` y `evidence` |
| Referencias que existen | Cada actor, estado, política y evidencia citada está definida |
| Efecto externo con aprobación | `FUT-06` y `FUT-08` envían o registran, y tienen `APR-01` y `APR-02` e idempotencia por clave |
| Casos negativos | `AT-02` a `AT-06`: instrucciones ocultas, urgencia, solicitud abierta, variantes fuera del piloto y registro repetido |
| Sin credenciales ni datos personales | Solo capacidades y roles; sin direcciones, productos ni datos de pacientes |

**Advertencia de portabilidad:** esta especificación es portable como definición; la ejecución no tiene por qué ser idéntica en cada plataforma (transacciones, identidad, tiempos de espera, orquestación, costos y comportamiento del modelo). Ni este plan ni el contrato prometen conversión automática entre plataformas.

**Patrones de solución:** este flujo no es de vigilancia de fuentes, así que no se usó el patrón de monitoreo de `references/patrones-de-solucion.md`.

**Siguiente paso sugerido:** ejecutar los pasos previos al piloto y, al cerrarlo, volver a evaluar la puerta de entrada; si pasa o pasa con condiciones, el plugin Implementación Empresarial recibe el `workflow-contract.yaml`.

## Lo que se ve en este ejemplo

- El piloto se acotó con la evidencia de `PRU-01` y `PRU-02`: solo la variante A.
- Las cifras de prototipo (2,4 minutos por aprobación) están rotuladas como tales y no se presentan como resultado del piloto.
- La tasa de errores se declara indicativa por el tamaño de la muestra.
- El costo se clasifica Bajo, Medio o Alto con factores, por alcance; el retorno sigue en "No sé".
- La puerta de entrada a la etapa C dice "No pasa todavía" con lo que falta, en vez de aprobarse por entusiasmo.
- El contrato cumple el esquema y lleva la advertencia de que portable no significa ejecución idéntica.
