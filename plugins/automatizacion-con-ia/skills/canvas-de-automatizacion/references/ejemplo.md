# Ejemplo: Canvas de automatización en una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados). Todo lo siguiente es ficticio. Este ejemplo reúne los entregables de las skills anteriores del flujo `FLU-01` (agendar citas, `RET-01`), caso piloto elegido en `priorizar-flujos` (`DEC-01`): el mapa del proceso actual (`PAS-01` a `PAS-08`, `EXC-01` a `EXC-04`, RACI), el proceso futuro (`FUT-01` a `FUT-08`, `CAP-01` a `CAP-07`, `DEC-03`, `DEC-04`), y la decisión de patrón y autonomía (`DEC-05`, `GRD-01` a `GRD-07`, `RIE-01` a `RIE-03`). Lo que no existe todavía: plan piloto, costo y próximos pasos.

## Turno 1

**Usuaria (Valeria):** Ya tenemos el proceso actual, el futuro y el patrón. Armemos el canvas de agendar citas.

**Facilitador:** Con lo que ya hay puedo llenar los bloques 1 a 6, 8 y 9 casi completos; el 4 y el 5 salen de la decisión de patrón, y los datos del 7 quedan en términos funcionales, con las herramientas pendientes hasta el MVP. Faltan el plan piloto (10), el costo y esfuerzo (11) y los próximos pasos (12). Empecemos por el piloto, que condiciona lo demás: ¿prefieres probarlo con una recepcionista usando el flujo nuevo mientras la otra sigue como hoy, o con todas las solicitudes digitales a la vez durante unos días?

## Turno 2

**Usuaria:** Con una sola recepcionista, dos semanas, y solo con los mensajes y el formulario. Las llamadas no, que ahí hay más imprevistos.

**Facilitador:** Anoto el piloto como borrador: alcance, solicitudes por mensaje y formulario (unas 24 de las 40 al día, `SUP-02`); usuaria, una recepcionista con la otra como comparación; duración, dos semanas. El éxito lo tomo de las metas del reto (3 minutos por solicitud y 1 cita con error por cada 100) más que no se pierda ninguna urgencia en una revisión de muestra. Queda Provisional hasta que lo confirmes. Para el bloque 11, propongo esta clasificación como Supuesto: construcción Medio (reglas de agenda por escribir, dos pasos con IA, aprobaciones y conexión con la agenda y las fichas), costo operativo Bajo a Medio (revisión diaria de los casos dudosos) y mantenimiento Medio. ¿Ves algo que lo haga más grande o más pequeño?

## Turno 3

**Usuaria:** El mantenimiento sí es Medio: las reglas de agenda cambian en diciembre y en enero por las vacaciones.

**Facilitador:** Anotado como factor (Dicho por participante). Del retorno no hay datos: lo dejo en "No sé", y solo muestro la cuenta de la meta: de 88 a 44 horas por mes si se cumple (3 minutos por 40 solicitudes al día por 22 días), marcada como meta, no como resultado. Los bloques 1 a 9 los armé con los entregables anteriores: ¿algo de ellos no refleja lo que acordaron?

## Turno 4

**Usuaria:** No, está bien. ¿Qué falta?

**Facilitador:** Esto falta:

| Pendiente | Qué se necesita | Quién |
|---|---|---|
| Bloque 10 (Provisional) | Confirmar el piloto con la jefa de recepción | Jefa de recepción |
| Bloque 11 (Supuesto) | Afinar la clasificación después del piloto | Facilitador y administradora |
| Bloque 7 | Herramientas y conexiones: Pendiente hasta el MVP | Etapa del MVP |
| Supuestos | `SUP-01` (contar errores), `SUP-03` (causa de duplicados), `SUP-04` (mensajes con datos suficientes), `SUP-05` (búsqueda de la ficha) | Jefa de recepción y recepción |
| Pie | Quién aprueba el canvas | Valeria |

**Usuaria:** Aprobarlo lo hago yo cuando lo revise con mi socio. Finalizar canvas.

## Entregable: canvas completo

# CANVAS DE AUTOMATIZACIÓN CON IA

| Flujo / Proceso | Equipo | Fecha | Versión |
|---|---|---|---|
| Agendar citas (`FLU-01`) | Recepción, jefa de recepción, administradora, odontóloga coordinadora clínica | 2026-10-25 | Borrador 1 |

## 1. Disparador y contexto
¿Qué inicia este flujo? ¿Quién o qué lo activa? ¿Cuál es el objetivo de negocio y el contexto?

- Estado: Completo.
- Llega una solicitud de cita de un paciente por llamada, mensaje o formulario (unas 40 al día: 16, 18 y 6; `SUP-02`). La activa el paciente.
- Objetivo (`RET-01`): de 6 a 3 minutos por solicitud y de 4 a 1 cita con error por cada 100 antes del cierre del trimestre, sin empeorar la confirmación el mismo día.
- Contexto: clínica de 3 consultorios y 14 empleados; recepción de 2 personas; dueña del proceso, la jefa de recepción; decide Valeria. Caso piloto elegido en `DEC-01`.

## 2. Flujo actual (As-Is)
¿Cómo funciona hoy? Pasos, responsables, sistemas, puntos de dolor y resultado actual.

- Estado: Completo (validado por la jefa de recepción).
- Ocho pasos: recibir, identificar al paciente, decidir si parece urgencia, revisar disponibilidad, proponer horarios, esperar respuesta, registrar y confirmar (`PAS-01` a `PAS-08`); 6 minutos de trabajo (`HAL-01`). Responsables: recepcionista ejecuta, jefa de recepción responde.
- Sistemas: la agenda de la clínica y las fichas de pacientes.
- Dolores: se teclea lo mismo dos veces; citas duplicadas (`EXC-04`, unas 4 de cada 100 según recepción, `SUP-01`, causa supuesta `SUP-03`); esperas largas por mensaje.
- Resultado actual: cita registrada y confirmada; nadie revisa el registro de otra persona.

## 3. Flujo futuro (To-Be)
¿Cómo debería funcionar con IA? ¿Qué se automatiza, qué cambia y cuál es el resultado?

- Estado: Completo (`DEC-04`).
- Todas las solicitudes entran a una lista única y se leen sus datos (`FUT-01`); se identifica al paciente y se detecta si ya hay una solicitud abierta (`FUT-02`); las coincidencias dudosas las revisa recepción (`FUT-03`); se marca si parece urgencia y decide una persona (`FUT-04`, `FUT-05`); se calculan horarios y se prepara una propuesta con tres opciones que recepción aprueba (`FUT-06`); se espera la respuesta con un aviso interno si no hay (`FUT-07`); se registra y se confirma tras la aprobación (`FUT-08`).
- Se eliminan el tecleo repetido y la revisión manual de duplicados. Resultado: cita registrada y confirmada, con una persona que aprueba.

## 4. Capacidades y herramientas de IA
¿Qué debe saber hacer la IA? ¿Qué skills, tools, apps, APIs o MCPs necesita (ej. clasificar, extraer, resumir, recuperar, generar, recomendar, predecir, planear, etc.)?

- Estado: Completo en capacidades; herramientas pendientes.
- Con IA (flujo con IA): extraer datos del mensaje (`CAP-01`, nivel 2) y clasificar el motivo y marcar posible urgencia (`CAP-03`, nivel 1).
- Con reglas: validar la ficha y las solicitudes repetidas (`CAP-02`, nivel 3); recomendar horarios (`CAP-04`), redactar la propuesta con una plantilla fija (`CAP-05`), registrar (`CAP-06`) y notificar (`CAP-07`), en nivel 2 durante el piloto.
- Herramientas: **Pendiente hasta el MVP**.

## 5. Patrón de automatización
¿Cuál es el mejor patrón para este flujo?

- [x] Automatización determinística (reglas / lógica)
- [x] Flujo con IA (proceso fijo + LLM)
- [ ] Copiloto / Asistente (humano en el loop)
- [ ] Agente Autónomo (dinámico / autónomo)
- [x] Híbrido (combinación)

Explicación / Justificación: el orden de los pasos es fijo y solo dos capacidades entienden texto libre, así que alcanza un flujo híbrido de reglas y dos llamadas acotadas a la IA; un agente no aporta, porque no hay caminos que decidir en cada caso (Recomendación, `DEC-05`).

- Estado: Completo.

## 6. Responsables humanos y controles
¿Quién hace qué? ¿Qué decisiones requieren humano? ¿Cómo se aprueba, supervisa y manejan las excepciones?

- Estado: Completo.
- Recepción aprueba la propuesta y el registro, y decide si es urgencia (criterios y responsabilidad: odontóloga coordinadora clínica, `DEC-03`). La jefa de recepción responde por el proceso, revisa las excepciones y puede apagar la parte con IA y volver al modo manual. Valeria decide los cambios.
- Autoridad: el piloto queda en el nivel 2; urgencias en el nivel 1. Guardrails `GRD-01` a `GRD-07`.

## 7. Sistemas, datos y herramientas
¿Qué sistemas se usan? ¿Qué datos se necesitan? ¿Qué integraciones, APIs o conectores (MCPs)?

- Estado: Provisional (lo técnico, Pendiente).
- Hoy se usan la agenda de la clínica y las fichas de pacientes. Datos necesarios, en palabras funcionales: datos de contacto y documento del paciente, agenda de cada consultorio y profesional, reglas de qué tipo de cita ocupa qué hueco (por escribir) y criterios de urgencia (por escribir).
- Herramientas, integraciones y conectores: **Pendiente hasta el MVP**.

## 8. Riesgos y mitigaciones
¿Cuáles son los principales riesgos? ¿Cómo los mitigaremos (seguridad, privacidad, precisión, cumplimiento, etc.)?

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| `RIE-01` | Un registro o un mensaje equivocado llega al paciente o a la agenda | Citas duplicadas o a la hora equivocada | `GRD-02`, `GRD-03`, `GRD-04`, `GRD-07` |
| `RIE-02` | Una urgencia no se detecta | Paciente con dolor fuerte espera sin atención | `GRD-05`: ante la duda se marca; decide una persona |
| `RIE-03` | Datos de pacientes expuestos a un componente no aprobado | Falta de confidencialidad de datos de salud | `GRD-01`, `GRD-06` |

- Estado: Completo.

## 9. Métricas y evaluación
¿Cómo mediremos el éxito? ¿Qué KPIs importan? ¿Cuál es la línea base y la meta?

| Métrica | Línea base (procedencia) | Meta | Cómo se mide |
|---|---|---|---|
| Tiempo de trabajo por solicitud | 6 min (`HAL-01`, medido en 20 solicitudes) | 3 min | Medir 20 solicitudes del piloto |
| Citas con error | Unas 4 de cada 100 (`SUP-01`, Dicho por participante, sin contar) | 1 de cada 100 | Contar las citas corregidas una semana antes y durante el piloto |
| Confirmación al paciente | El mismo día | No empeora | Revisar el tiempo hasta la confirmación |
| Casos que pasan a revisión | No sé | Sin meta todavía | Contarlos en el piloto |

- Estado: Completo (la línea base de errores sigue Pendiente por validar).

## 10. Plan piloto
¿Qué vamos a probar primero? Alcance, usuarios, duración, criterios de éxito y qué aprenderemos.

- Estado: Provisional.
- Alcance: solicitudes por mensaje y formulario (unas 24 de 40 al día, `SUP-02`); las llamadas quedan fuera. Usuarios: una recepcionista con el flujo nuevo; la otra sigue como hoy y sirve de comparación. Duración: dos semanas.
- Criterios de éxito: 3 minutos por solicitud y 1 cita con error por cada 100, y ninguna urgencia sin marcar en una revisión de muestra. Qué aprenderemos: `SUP-04` y `SUP-05`, y cuántos casos pasan a revisión.

## 11. Costo y esfuerzo estimado
¿Qué esfuerzo de implementación y operación se requiere? ¿Cuál es el costo estimado y el ROI esperado?

| Dimensión | Clasificación inicial | Factores principales |
|---|---|---|
| Esfuerzo de construcción | Medio | Reglas de agenda por escribir, dos pasos con IA, aprobaciones, conexión con la agenda y las fichas |
| Costo operativo | Bajo a Medio | Revisión diaria de los casos dudosos; uso moderado |
| Mantenimiento | Medio | Las reglas de agenda cambian en diciembre y enero (Dicho por participante) |

ROI esperado: No sé. Capacidad liberada si se cumple la meta: de 88 a 44 horas por mes (3 min × 40 al día × 22 días); es una meta, no un resultado. Estado: Supuesto.

## 12. Próximos pasos
¿Qué acciones siguen? ¿Quién es responsable? ¿Cuándo?

| Acción | Responsable | Fecha | Dependencia |
|---|---|---|---|
| Contar una semana de citas con error (`SUP-01`) y revisar la causa de los duplicados (`SUP-03`) | Jefa de recepción | Antes del piloto | Ninguna |
| Escribir las reglas de agenda | Jefa de recepción | Antes del piloto | Ninguna |
| Definir los criterios de urgencia | Odontóloga coordinadora clínica | Antes del piloto | Ninguna |
| Revisar 30 mensajes reales para `SUP-04` y probar la búsqueda de ficha (`SUP-05`) | Recepción | Antes del piloto | Reglas de agenda |
| Convertir los supuestos en pruebas con `supuestos-y-riesgos` (Próximamente) | Facilitador y jefa de recepción | Próxima sesión | Canvas aprobado |
| Elegir herramientas y conexiones | Etapa del MVP | Pendiente hasta el MVP | Plan piloto confirmado |

| Aprobado por | Fecha | Notas |
|---|---|---|
| Pendiente (lo aprueba Valeria tras revisarlo con su socio) | Pendiente | Borrador 1; bloques 7 y 10 Provisionales; herramientas pendientes hasta el MVP |

## Entregable: vista A3

**Flujo / Proceso:** Agendar citas (`FLU-01`)  **Equipo:** Recepción y administración  **Fecha:** 2026-10-25  **Versión:** Borrador 1

| 1. Disparador y contexto | 2. Flujo actual (As-Is) | 3. Flujo futuro (To-Be) | 4. Capacidades y herramientas de IA |
|---|---|---|---|
| Solicitud de cita por llamada, mensaje o formulario (~40 al día). Meta `RET-01`: 6 a 3 min, errores de 4 a 1 por 100. | Ocho pasos (`PAS-01` a `PAS-08`), 6 min. Dolores: doble tecleo, duplicados, esperas. | Lista única, ficha y duplicados automáticos, urgencia marcada y decidida por persona, tres horarios, aprobación (`FUT-01` a `FUT-08`). | Extraer y clasificar con IA; validar, recomendar, redactar, registrar y notificar con reglas. Herramientas: Pendiente hasta el MVP. |
| **5. Patrón de automatización** | **6. Responsables humanos y controles** | **7. Sistemas, datos y herramientas** | **8. Riesgos y mitigaciones** |
| [x] Determinística <br> [x] Flujo con IA <br> [ ] Copiloto / Asistente <br> [ ] Agente Autónomo <br> [x] Híbrido <br> Orden fijo; IA solo en dos capacidades. | Recepción aprueba y decide urgencia; jefa de recepción revisa y puede apagar; nivel 2 en el piloto, urgencias nivel 1. | Agenda y fichas; reglas de agenda y criterios de urgencia por escribir. Herramientas: Pendiente hasta el MVP. | `RIE-01` registro equivocado, `RIE-02` urgencia no detectada, `RIE-03` datos expuestos; `GRD-01` a `GRD-07`. |
| **9. Métricas y evaluación** | **10. Plan piloto** | **11. Costo y esfuerzo estimado** | **12. Próximos pasos** |
| 6 a 3 min; 4 a 1 error por 100; confirmación el mismo día sin empeorar. | Dos semanas, una recepcionista, mensajes y formulario (Provisional). | Construcción Medio; operación Bajo a Medio; mantenimiento Medio (Supuesto). | Contar errores, escribir reglas y criterios, revisar mensajes, `supuestos-y-riesgos`. |

**Aprobado por:** Pendiente  **Fecha:** Pendiente  **Notas:** Borrador 1

## Entregable: YAML (abreviado)

```yaml
encabezado:
  flujo: "Agendar citas (FLU-01)"
  equipo: "Recepción y administración"
  fecha: "2026-10-25"
  version: "borrador 1"
bloques:
  4_capacidades_y_herramientas_de_ia:
    estado: completo
    capacidades:
      - {id: CAP-01, verbo: Extraer, nivel_de_autoridad: 2}
      - {id: CAP-03, verbo: Clasificar, nivel_de_autoridad: 1}
    herramientas: pendiente_hasta_el_mvp
  5_patron_de_automatizacion:
    estado: completo
    determinista: true
    flujo_con_ia: true
    copiloto_asistente: false
    agente_autonomo: false
    hibrido: true
    justificacion: "Orden fijo; IA solo en dos capacidades que entienden texto libre."
    decision: DEC-05
  7_sistemas_datos_y_herramientas:
    estado: provisional
    herramientas_e_integraciones: pendiente_hasta_el_mvp
  10_plan_piloto:
    estado: provisional
    duracion: "2 semanas"
  11_costo_y_esfuerzo_estimado:
    esfuerzo_de_construccion: Medio
    costo_operativo: "Bajo a Medio"
    mantenimiento: Medio
    roi_esperado: "No sé"
    procedencia: supuesto
pie:
  aprobado_por: ""
  fecha: ""
  notas: "Borrador 1"
vacios_y_pendientes: [SUP-01, SUP-03, SUP-04, SUP-05]
```

(El YAML real incluye los 12 bloques completos, siguiendo `assets/canvas-de-automatizacion.yaml`.)

**Siguiente paso sugerido:** `supuestos-y-riesgos` (Próximamente), para convertir `SUP-01`, `SUP-03`, `SUP-04` y `SUP-05` en pruebas. Mientras tanto, el facilitador puede acompañar esa conversación.

## Lo que se ve en este ejemplo

- El canvas se armó con los entregables anteriores; solo se preguntó por el piloto, el costo y los próximos pasos.
- Los bloques 4, 5 y 7 apuntan a la decisión de patrón y dejan las herramientas pendientes hasta el MVP.
- El pie quedó "Pendiente" porque la aprobación es de Valeria, no del facilitador.
- El retorno quedó "No sé", y la cuenta de 88 a 44 horas se presentó como meta, no como resultado.
- La vista A3 resume cada bloque con IDs, y el Markdown sigue siendo la fuente de verdad.
