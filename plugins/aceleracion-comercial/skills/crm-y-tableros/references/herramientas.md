# Herramientas de CRM y tableros

## 1. Cómo decidir qué campos entran

1. Lista las decisiones que se toman cada semana sobre una oportunidad (a quién llamar, qué propuesta seguir, qué cerrar).
2. Lista los KPIs de la línea base y la fórmula de cada uno.
3. Para cada campo candidato, escribe la decisión o el KPI que alimenta. Sin respuesta, no entra.
4. Marca desde qué etapa es obligatorio: pedir todo desde el primer contacto genera datos falsos.
5. Revisa cada trimestre qué campos nadie usa y quítalos (ciclo 7 a 4).

## 2. Cómo escribir un diccionario de datos

- Un nombre corto y estable por campo, con identificador (`CAM-nn`).
- Tipo: texto, número, fecha o lista cerrada. Cuando hay pocas opciones, lista cerrada.
- Valores permitidos escritos, con el significado de cada uno.
- Quién lo llena y cuándo; una sola persona responsable por campo.
- Regla de validación que se pueda comprobar con un filtro.

## 3. Cómo elegir qué automatizar

| Pregunta | Si la respuesta es sí |
|---|---|
| ¿La tarea es repetitiva y se olvida? | Candidata |
| ¿Se equivoca mucho una persona al hacerla? | Candidata |
| ¿El error es reversible y no llega al cliente? | Se puede automatizar |
| ¿Habla con un cliente, mueve dinero o cambia datos de contrato? | No se automatiza sin aprobación humana |

Orden: eliminar el paso, simplificar, regla o validación determinística, y solo al final IA. Cada automatización lleva dueño y una revisión periódica.

## 4. Cómo diseñar un tablero

1. Parte de la pregunta que responde y de la reunión donde se lee.
2. Muestra pocos indicadores, con numerador y denominador.
3. Define colores con umbrales escritos antes de ver el dato.
4. Si nadie lo mira dos veces seguidas, se elimina o se rediseña.

## 5. Higiene de datos

- Auditoría semanal con filtros: filas abiertas con campos vacíos, cuentas repetidas, cerradas sin motivo y estancadas.
- Muestra mensual contra la realidad: se pregunta a quien lleva la oportunidad si lo anotado es cierto.
- El indicador es `KPI-12`; la meta es una hipótesis con plazo.
- Se corrige el proceso antes que a la persona: si un campo se deja vacío siempre, es difícil de llenar o innecesario.

## 6. Cómo conducir la adopción

| Obstáculo común | Qué hacer |
|---|---|
| "No tengo tiempo" | Reducir campos y fijar la rutina de cinco minutos |
| "No veo para qué sirve" | Usar el tablero en la reunión semanal, de modo que lo anotado se vea |
| "Me da miedo que me vigilen" | Explicar que el registro mide el proceso, no castiga a la persona |
| "Lo anoto después" | Regla: si no está en el registro, no existe en la reunión |

## 7. Versión mínima viable y migración futura

La hoja de cálculo descrita en `assets/crm-en-hoja-de-calculo.md` alcanza para equipos pequeños. Si más adelante se adopta una herramienta, se lleva el diccionario de datos, las listas y las reglas `AUT-nn`; se migran primero las abiertas, luego las cerradas con los campos mínimos y se audita la calidad una semana después. No se afirma que ninguna herramienta cumpla estas funciones sin verificarlo con el proveedor, y no se envía ningún dato de clientes a una herramienta sin permisos y política de datos.

## 8. Integraciones con formularios, correo y mensajería

Conectar un formulario, el correo o la mensajería solo se hace con consentimiento del cliente y bajo la política de datos de la organización. El mínimo es que cada lead nuevo tenga origen, fecha y responsable; el resto se puede ingresar a mano al principio.
