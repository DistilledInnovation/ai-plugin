# Ejemplo: Facilitador con una distribuidora ficticia

Empresa inventada: **Distribuidora Rioclaro** (insumos de oficina y limpieza para empresas pequeñas; 85 empleados; ventas anuales de unos USD 6 millones). Todo lo siguiente es ficticio. Esta empresa es la misma de los ejemplos de `descubrir-procesos`, `definir-reto-de-automatizacion` y `priorizar-flujos`.

## Turno 1

**Usuaria:** Hola, soy Daniela, gerente de operaciones de Distribuidora Rioclaro. Mi gerente general quiere que usemos IA en operaciones y yo no sé por dónde empezar. Todo el mundo dice que se pierde mucho tiempo, pero nadie sabe en qué exactamente.

**Facilitador:** Gracias, Daniela. Antes de hablar de IA quiero entender el trabajo. ¿Cuál fue la última vez que viste a alguien de tu equipo quedarse tarde o quejarse de lo mucho que le tomaba una tarea?

## Turno 2

**Usuaria:** Esta semana. En Atención al Cliente copian a mano los pedidos que llegan por correo y por chat al sistema de pedidos; son unos 120 al día y calculan que cada uno les toma unos 6 minutos. Eso lo medimos con 20 pedidos la semana pasada. Todo lo demás son impresiones.

**Facilitador:** Con eso ya puedo ubicarte.

**Resumen de apertura**
1. Distribuidora Rioclaro quiere usar IA en operaciones por mandato de la gerencia general. (Dicho por participante)
2. Se percibe que "se pierde mucho tiempo", sin saber dónde. (Dicho por participante)
3. Una tarea tiene datos: copiar pedidos a mano, unos 120 al día a unos 6 minutos cada uno, medido con 20 pedidos. `HAL-01`, **Hecho** (Evidencia)
4. No hay inventario de procesos ni se sabe cuántos otros dolores existen. **Pendiente por validar**
5. No hay ninguna solución elegida, y está bien: todavía no se sabe si la respuesta es IA.

**Qué está claro:** una tarea candidata con cifras. **Incertidumbre principal:** no sabemos si esa es la tarea con más valor ni cuáles otras hay.

**Punto de entrada:** 1, no sabe qué automatizar (etapa A). El dolor existe y hay un ejemplo concreto, así que no hace falta pasar por `identificar-reto`.

```yaml
organizacion: Distribuidora Rioclaro
actualizado: 2026-10-25
punto_de_entrada: descubrir
etapa: A
reto: pendiente
procesos:
  - id: FLU-01
    nombre: Captura de pedidos que llegan por correo y chat
    dueno: Jefa de Atención al Cliente
    procedencia: Dicho por participante
evidencia:
  - id: HAL-01
    dato: "Unos 120 pedidos al día se copian a mano; unos 6 minutos cada uno (muestra de 20 pedidos)"
    procedencia: Evidencia
supuestos:
  - id: SUP-01
    afirmacion: "La captura de pedidos es el proceso con más valor para automatizar"
    prueba: pendiente por validar
decisiones: []
pendientes_por_validar:
  - "Otros procesos con dolor en Atención, Cuentas por Cobrar, Bodega y Ventas"
siguiente_skill: descubrir-procesos
```

**Recomendación:** seguir con `descubrir-procesos` para recoger señales de las áreas y armar un inventario de oportunidades antes de elegir. Es posible que la mejor respuesta para algún proceso sea simplificarlo o no tocarlo.

**Facilitador:** ¿Quieres que sigamos ahora con `descubrir-procesos`, empezando por las áreas que mencionaste?

## Turno 3

**Usuaria:** Sí, vamos.

**Facilitador:** Listo, guardo el estado y lo actualizo al terminar esa etapa.

## Lo que se ve en este ejemplo

- No se abrió con "¿qué quieres automatizar?", sino con una pregunta sobre el trabajo real.
- El dato medido (`HAL-01`) se separa de la creencia de que la captura es lo más valioso (`SUP-01`).
- No se eligió tecnología ni se prometió IA.
- El resumen tiene cinco puntos, nombra lo claro y la incertidumbre principal, y termina con una pregunta.
