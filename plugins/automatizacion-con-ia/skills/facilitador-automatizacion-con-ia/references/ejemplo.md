# Ejemplo: Facilitador con una clínica dental ficticia

Empresa inventada: **Clínica Dental Sonrisa Norte** (clínica privada pequeña: 3 consultorios, 14 empleados, ingresos anuales de unos USD 600.000). Todo lo siguiente es ficticio. Esta empresa es la misma de los ejemplos de `descubrir-procesos`, `definir-reto-de-automatizacion` y `priorizar-flujos`.

## Turno 1

**Usuaria:** Hola, soy Valeria, odontóloga y directora de Sonrisa Norte. Mi socio quiere que usemos IA en la clínica y yo no sé por dónde empezar. Todos dicen que se pierde mucho tiempo en recepción, pero nadie sabe en qué exactamente.

**Facilitador:** Gracias, Valeria. Antes de hablar de IA quiero entender el trabajo. ¿Cuál fue la última vez que viste a alguien de tu equipo quedarse tarde o quejarse de lo mucho que le tomaba una tarea?

## Turno 2

**Usuaria:** Esta semana. Recepción registra a mano en la agenda las solicitudes de cita que llegan por llamada, por mensaje y por el formulario de la página; son unas 40 al día y calculan que cada una les toma unos 6 minutos. Eso lo medimos con 20 solicitudes la semana pasada. Todo lo demás son impresiones.

**Facilitador:** Con eso ya puedo ubicarte.

**Resumen de apertura**
1. Sonrisa Norte quiere usar IA por iniciativa de uno de los socios. (Dicho por participante)
2. Se percibe que "se pierde mucho tiempo" en recepción, sin saber dónde. (Dicho por participante)
3. Una tarea tiene datos: registrar solicitudes de cita a mano, unas 40 al día a unos 6 minutos cada una, medido con 20 solicitudes. `HAL-01`, **Hecho** (Evidencia)
4. No hay inventario de procesos ni se sabe cuántos otros dolores existen. **Pendiente por validar**
5. No hay ninguna solución elegida, y está bien: todavía no se sabe si la respuesta es IA.

**Qué está claro:** una tarea candidata con cifras. **Incertidumbre principal:** no sabemos si esa es la tarea con más valor ni cuáles otras hay.

**Punto de entrada:** 1, no sabe qué automatizar (etapa A). El dolor existe y hay un ejemplo concreto, así que no hace falta pasar por `identificar-reto`.

```yaml
organizacion: Clínica Dental Sonrisa Norte
actualizado: 2026-10-25
punto_de_entrada: descubrir
etapa: A
reto: pendiente
procesos:
  - id: FLU-01
    nombre: Agendamiento de citas (solicitudes por llamada, mensaje y formulario)
    dueno: Jefa de recepción
    procedencia: Dicho por participante
evidencia:
  - id: HAL-01
    dato: "Unas 40 solicitudes de cita al día se registran a mano; unos 6 minutos cada una (muestra de 20 solicitudes)"
    procedencia: Evidencia
supuestos:
  - id: SUP-01
    afirmacion: "El agendamiento es el proceso con más valor para automatizar"
    prueba: pendiente por validar
decisiones: []
pendientes_por_validar:
  - "Otros procesos con dolor en recepción, administración, esterilización y consultorios"
siguiente_skill: descubrir-procesos
```

**Recomendación:** seguir con `descubrir-procesos` para recoger señales de las áreas y armar un inventario de oportunidades antes de elegir. Es posible que la mejor respuesta para algún proceso sea simplificarlo o no tocarlo.

**Facilitador:** ¿Quieres que sigamos ahora con `descubrir-procesos`, empezando por las áreas que mencionaste?

## Turno 3

**Usuaria:** Sí, vamos.

**Facilitador:** Listo, guardo el estado y lo actualizo al terminar esa etapa.

## Lo que se ve en este ejemplo

- No se abrió con "¿qué quieres automatizar?", sino con una pregunta sobre el trabajo real.
- El dato medido (`HAL-01`) se separa de la creencia de que el agendamiento es lo más valioso (`SUP-01`).
- No se eligió tecnología ni se prometió IA.
- El resumen tiene cinco puntos, nombra lo claro y la incertidumbre principal, y termina con una pregunta.
