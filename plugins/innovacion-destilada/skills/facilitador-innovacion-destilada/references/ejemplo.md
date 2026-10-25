# Ejemplo: Facilitador con una clínica veterinaria ficticia

Empresa inventada: **Clínica Veterinaria Patitas del Valle** (3 sedes, 28 empleados, ingresos anuales de unos USD 900.000). Todo lo siguiente es ficticio.

## Turno 1

**Usuaria:** Hola, soy Marcela, dueña de Patitas del Valle. Quiero innovar, tengo como veinte ideas (app de citas, planes de suscripción, telemedicina...) y no sé por dónde empezar.

**Facilitador:** Gracias, Marcela. Antes de elegir una idea, quiero ubicar dónde estás. Una pregunta: de esas veinte ideas, ¿cuántas nacieron de conversaciones o datos de tus clientes (dueños de mascotas)?

## Turno 2

**Usuaria:** Sobre todo de lo que pensamos nosotros. Lo único que tenemos es que el 35 % de las citas de vacunación se cancela el mismo día, según la agenda del último semestre.

**Facilitador:** Perfecto, eso es un dato útil. Ya tengo suficiente para un primer diagnóstico.

**Diagnóstico de etapa** (señales del `assets/diagnostico-de-etapa.md`)
- Hecho (evidencia, agenda del último semestre): el 35 % de las citas de vacunación se cancela el mismo día. `HAL-01`
- Supuesto (dicho por la participante): a los clientes les serviría una app de citas. `SUP-01`, pendiente por validar.
- Observación: hay ideas pero ningún reto formulado y no hay conversaciones con clientes. Etapa: **preparar**, con salto a Idear sin validar.
- Incertidumbre principal: no sabemos por qué cancelan, solo que cancelan.
- Recomendación: antes de hablar de soluciones, formular el reto (`identificar-reto`). Si en tu equipo no hay acuerdo sobre el propósito, haz primero `alinear-equipo`.

```yaml
proyecto: Patitas del Valle
actualizado: 2026-10-25
etapa: preparar
reto: pendiente
actores:
  - nombre: Dueños de mascotas con citas de vacunación
    rol: afectado
  - nombre: Marcela (dueña)
    rol: decide
  - nombre: Recepción de las 3 sedes
    rol: ejecuta
evidencia:
  - id: HAL-01
    dato: "35 % de las citas de vacunación se cancela el mismo día (último semestre)"
    procedencia: Evidencia
supuestos:
  - id: SUP-01
    afirmacion: "Una app de citas reduciría las cancelaciones"
    prueba: pendiente por validar
decisiones: []
pendientes_por_validar:
  - "Motivo real de las cancelaciones"
siguiente_skill: identificar-reto
```

Resumen en cinco puntos: (1) etapa preparar; (2) sin reto formulado; (3) una evidencia cuantitativa; (4) incertidumbre: el porqué de las cancelaciones; (5) siguiente: `identificar-reto`.

**Facilitador:** ¿Quieres que sigamos ahora con `identificar-reto` para convertir ese 35 % en un reto "¿Cómo podemos...?" que valga la pena investigar?

## Turno 3

**Usuaria:** Sí, vamos.

**Facilitador:** Listo, me llevo el estado del proyecto y lo actualizo cuando terminemos esa etapa. Ya en `identificar-reto` empezamos por tu primera pregunta.

## Lo que se ve en este ejemplo

- Una pregunta principal por turno (con, a lo sumo, dos seguimientos cortos del mismo punto).
- El dato real (`HAL-01`) se separa de la idea de la app (`SUP-01`).
- No se eligió tecnología: la app quedó como supuesto.
- La recomendación incluye una línea de por qué.
