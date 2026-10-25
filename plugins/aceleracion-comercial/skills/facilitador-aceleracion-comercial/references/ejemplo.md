# Ejemplo: Facilitador con una firma contable ficticia

Empresa inventada: **Brújula Contadores**, firma pequeña de contabilidad y cumplimiento tributario (6 personas: 2 socios, 2 contadoras, 1 analista de impuestos y 1 asistente administrativa) que vende servicios mensuales a pequeñas empresas. Todo lo siguiente es ficticio. Es la misma empresa que continúa en los ejemplos de `diagnostico-comercial`, `segmentacion-e-icp`, `oferta-y-propuesta-de-valor` y `proceso-de-ventas-y-pipeline`.

## Turno 1

**Usuaria:** Hola, soy la socia fundadora de Brújula Contadores. Queremos crecer, pero siento que vendemos por suerte. Casi todo viene de recomendaciones y casi todo lo cierro yo.

**Facilitador:** Gracias. Antes de pensar en cómo crecer quiero entender cómo venden hoy. ¿Cómo llegó tu último cliente nuevo y qué pasó desde el primer contacto hasta que firmó?

## Turno 2

**Usuaria:** Fue una agencia de contenidos de nueve personas. Su dueño me la recomendó un cliente, hablamos por videollamada, le mandé una propuesta por correo a los dos días y a la semana me dijo que sí. En los últimos seis meses cerramos 9 clientes nuevos y perdimos 5; tenemos 62 activos. Contamos los contactos en una hoja: unos 84 en el periodo, 54 por recomendación. Yo cerré 7 de los 9.

**Facilitador:** Con eso ya puedo ubicarte.

**Resumen de apertura**
1. Brújula vende servicios contables mensuales a pequeñas empresas; 62 clientes activos. (Dicho por participante)
2. En seis meses: 84 contactos, 9 clientes ganados y 5 perdidos. `HAL-01`, **Hecho** (Evidencia: la hoja de contactos)
3. El 64 % de los contactos (54 de 84) viene de recomendaciones. `HAL-02`, **Hecho** (Evidencia)
4. La socia fundadora cierra 7 de 9 ventas; hoy la venta depende de ella. `HAL-03`, **Hecho** (Dicho por participante, sin registro)
5. No se sabe en qué paso se pierden las oportunidades ni por qué. **Pendiente por validar**

**Qué está claro:** hay ventas, un volumen medido de contactos y una dependencia fuerte de una persona y de un canal. **Incertidumbre principal:** no hay números por etapa (reuniones, propuestas) ni motivos de pérdida, así que no sabemos si el problema es a quién se le vende, qué se ofrece o cómo se da seguimiento.

**Modalidad y etapa:** A, estructurar las ventas de un negocio existente (ya hay clientes que pagan). Etapa 0: no hay línea base acordada ni problemas prioritarios; sin eso, las etapas siguientes serían opinión. Lo que ya existe (la hoja de contactos) se aprovecha, no se rehace.

```yaml
organizacion: Brújula Contadores
actualizado: 2026-10-25
modalidad: A
etapa: 0
oferta_principal: "Contabilidad mensual y cumplimiento tributario para pequeñas empresas"
meta_comercial: pendiente
segmentos: []
icp: []
evidencia:
  - id: HAL-01
    dato: "84 contactos, 9 clientes ganados y 5 perdidos en seis meses; 62 clientes activos"
    procedencia: Evidencia
  - id: HAL-02
    dato: "54 de 84 contactos (64 %) vienen por recomendación"
    procedencia: Evidencia
  - id: HAL-03
    dato: "La socia fundadora cerró 7 de las 9 ventas"
    procedencia: Dicho por participante
supuestos:
  - id: SUP-01
    afirmacion: "El problema principal es que faltan más recomendaciones"
    prueba: pendiente por validar
decisiones: []
etapas_cerradas: []
pendientes_por_validar:
  - "Reuniones y propuestas por periodo; motivos de pérdida"
siguiente_skill: diagnostico-comercial
```

**Facilitador:** Mi recomendación (**Recomendación**) es empezar por `diagnostico-comercial`. Una nota: `SUP-01` es un supuesto, y el diagnóstico puede mostrar que el problema no es el número de contactos. ¿Quieres que empecemos ahora y reconstruyamos juntos cuántas reuniones y propuestas hubo en esos seis meses?

## Qué quedó claro del ejemplo

- El primer mensaje nunca sugiere canales ni herramientas y cierra con una pregunta.
- La modalidad se decide por evidencia de ventas pagadas.
- La etapa es la primera cuyo criterio de salida no se cumple.
- Los supuestos se separan de los hechos desde el primer resumen; `SUP-01` abre una verificación en la etapa 0.
- Las etapas 4 a 7 están Próximamente: si la persona las necesita antes de tiempo, se avanza con borradores marcados.
