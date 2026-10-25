# Ejemplo: armar el modelo de negocio y el piloto en una empresa de transporte ficticia

Empresa inventada: **Transportes Marea Azul** (carga refrigerada regional, 65 empleados, 22 camiones). Continúa el ejemplo de `probar-y-aprender`. Todo es ficticio, incluidas las cifras.

Entrada: `CON-01` "Aviso de frío y vista de la carga"; resultado de `PRU-04` (mensaje con temperatura e instrucción): 2 de 3 clientes decidieron sin pedir más datos (Hecho, hoja de despacho); `DEC-09`: perseverar, decidido por Paula; dos clientes aceptaron por correo pagar un recargo de prueba de 60 dólares por viaje durante dos meses (Evidencia: correos). Mapa de Valor `PRS-01`, `ALI-01`, `CRB-01`. Perfil del Cliente: jefe de logística de un productor de alimentos frescos.

## Turno 1: evidencia

**Facilitador:** Tengo el Mapa de Valor, los resultados de `PRU-04` y los dos correos de aceptación del recargo. Primera pregunta: ¿qué evidencia tienes hoy de que tu solución crea valor para el cliente?

**Usuaria (Paula, gerente comercial):** Dos de tres decidieron con el aviso y dos aceptaron pagar el recargo. No tengo más: son tres clientes.

**Facilitador:** Lo registro como Hecho con esa muestra de tres, y no se generaliza.

## Turnos 2 y 3: segmento y propuesta

**Facilitador:** El segmento viene del Perfil del Cliente y la propuesta del Mapa de Valor; la uso tal cual (`PRS-01`, `ALI-01`, `CRB-01`). Siguiente pregunta: ¿quién es el cliente para el que vas a crear valor primero?

**Usuaria:** Productores medianos de alimentos frescos de la región que despachan entre 3 y 10 cargas por semana.

## Turno 4: los otros siete bloques (un bloque por turno, resumen de tres)

**Facilitador:** Siguiente pregunta: ¿cómo se entera el cliente de que existes y cómo recibe tu solución?

**Usuaria:** Por mis vendedores, que ya los visitan. El aviso llega por mensaje de texto.

**Facilitador:** Anotado en canales (Supuesto: solo se probó con clientes actuales). Siguiente pregunta: ¿por qué valor estaría dispuesto a pagar ese cliente y cómo lo pagaría?

**Usuaria:** Por saber a tiempo y no perder la carga; como un recargo fijo por viaje.

**Facilitador:** Anotado en fuentes de ingresos: recargo por viaje, 60 dólares en la prueba (Hecho, dos clientes; Supuesto para otros). Siguiente pregunta: ¿cuáles son los costos más importantes de operar tu modelo?

**Usuaria:** El tiempo de Julio, el de despacho, y los termómetros registradores. Los termómetros todavía no los hemos cotizado.

**Facilitador:** Anotado en estructura de costos: tiempo de despacho (Hecho) y termómetros (Pendiente por validar).

*(Se completan, uno por turno, relación con clientes, actividades clave, recursos clave y socios clave.)*

## Turno 5: hipótesis

**Facilitador:** Con el lienzo completo, así quedó cada bloque:

| Bloque | Estado |
|---|---|
| Segmento | Hecho en 3 clientes actuales, Supuesto para otros |
| Propuesta de valor | Hecho parcial (`PRU-04`: 2 de 3) |
| Canales | Supuesto |
| Relación con clientes | Supuesto |
| Ingresos | Hecho en 2 clientes, Supuesto para otros |
| Actividades | Supuesto |
| Recursos | Supuesto |
| Socios | Pendiente por validar |
| Costos | Hecho parcial |

¿Cuál de estos bloques te genera más dudas?

**Usuaria:** Costos y recursos: no sé si podemos medir el frío en los 22 camiones y cuánto cuesta.

## Turno 6: Business Model Fit (un criterio por turno)

**Facilitador:** Primera pregunta: ¿qué evidencia tienes de que podrías repetir esta venta con otros clientes sin empezar de cero?

**Usuaria:** Con los tres usamos el mismo proceso, pero con clientes que ya conocíamos.

**Facilitador:** Siguiente pregunta: ¿cuánto ingresa por cada cliente?

**Usuaria:** 60 dólares por viaje, y hacen unos 6 viajes al mes con nosotros.

**Facilitador:** Siguiente pregunta: ¿cuánto cuesta atender a un cliente?

**Usuaria:** En la prueba Julio dedica unas 2 horas por viaje; la hora de despacho nos cuesta unos 8 dólares.

**Facilitador:** Con tus números: ingreso de 60 dólares por viaje menos 16 de tiempo de despacho deja 44 dólares por viaje, o 264 dólares al mes por cliente, sin contar termómetros ni costo de conseguir al cliente. El ingreso es Hecho en dos clientes; el costo es Supuesto porque es una estimación tuya de horas. Siguiente pregunta: ¿qué tendría que crecer en tu operación para atender a diez veces más clientes?

**Usuaria:** Habría que automatizar la medición; a mano no se puede con 22 camiones.

## Turno 7: priorizar

**Facilitador:** Las hipótesis pendientes son: `SUP-06` (se puede medir el frío durante todo el viaje), `SUP-08` (el recargo se mantiene con más clientes) y una nueva, `SUP-09`: se puede atender a más clientes sin que el tiempo de despacho crezca igual. ¿Cuál de estas hipótesis, si no fuera como crees, haría inviable tu modelo?

**Usuaria:** `SUP-06`: si no puedo medir el frío en todos los camiones, no hay servicio.

**Facilitador:** Registrado como `DEC-10`: se valida `SUP-06` primero, decidido por Paula.

## Turno 8: piloto (un dato por turno)

**Facilitador:** ¿A cuántos clientes les ofrecerías el piloto?

**Usuaria:** A seis, incluidos los tres de la prueba, y tres nuevos del segmento.

**Facilitador:** Siguiente pregunta: ¿cuánto tiempo duraría el piloto?

**Usuaria:** Ocho semanas.

**Facilitador:** Siguiente pregunta: ¿qué recursos necesitarías para sostenerlo?

**Usuaria:** Seis termómetros registradores en seis camiones y las horas de dos despachadores.

**Facilitador:** Siguiente pregunta: ¿qué resultado tendría que dar el piloto para que sigas adelante con el modelo?

**Usuaria:** Que el frío quede registrado en todo el viaje en 5 de los 6 camiones y que al menos 4 de los 6 clientes renueven el recargo.

**Facilitador:** Siguiente pregunta: si no llega a ese resultado, ¿qué harías?

**Usuaria:** Con 2 o 3 renovaciones ajusto el precio y repito; con menos, replanteo el modelo.

## Turno 9: ruta de escalamiento

**Facilitador:** Con el piloto definido, armé cuatro etapas (piloto, pocos clientes, más clientes, crecimiento). ¿Qué tendría que ser cierto para pasar del piloto a la siguiente etapa?

**Usuaria:** Que se cumpla lo del piloto y que el margen por viaje siga siendo positivo con costos reales.

**Facilitador:** Registrado como `DEC-11`: la primera puerta es el resultado del piloto más margen positivo con costos reales, definida por Paula.

## Turno 10: riesgos y cierre

**Facilitador:** Anoto `RIE-06`: que los termómetros fallen y se pierda la evidencia del frío. ¿Qué quieres hacer primero?

**Usuaria:** Cotizar los termómetros esta semana.

## Entregable final

# Modelo de negocio y plan de piloto: `CON-01`

Marea Azul, 2026-10-25, borrador 1.

| Bloque | Contenido | Estado |
|---|---|---|
| Segmento | Productores medianos de alimentos frescos de la región (3 a 10 cargas por semana) | Hecho en 3 clientes, Supuesto para otros |
| Propuesta de valor | Aviso de frío y vista de la carga (`PRS-01`, `ALI-01`, `CRB-01`) | Hecho parcial (`PRU-04`) |
| Canales | Vendedores actuales; aviso por mensaje de texto | Supuesto |
| Relación con clientes | Seguimiento por el vendedor asignado | Supuesto |
| Ingresos | Recargo fijo por viaje, 60 dólares en la prueba | Hecho en 2 clientes |
| Actividades clave | Registrar el frío, enviar el aviso, atender el reclamo | Supuesto |
| Recursos clave | Termómetros registradores, despachadores | Pendiente por validar |
| Socios clave | Proveedor de termómetros | Pendiente por validar |
| Costos | Tiempo de despacho (8 dólares por hora), termómetros sin cotizar | Hecho parcial |

**Business Model Fit:** repetible, evidencia parcial (3 clientes conocidos); rentable, 44 dólares por viaje antes de termómetros y costo de adquisición (Supuesto en costos); escalable, pendiente por validar (depende de `SUP-06`). No se declara el Business Model Fit.

**Piloto (`DEC-10`):** valida `SUP-06`. 6 clientes, 8 semanas, 6 termómetros y 2 despachadores. Éxito (decidido por Paula antes de ejecutar): frío registrado en todo el viaje en 5 de 6 camiones y al menos 4 de 6 clientes renuevan el recargo. Regla: 2 o 3 renovaciones, ajustar precio y repetir; menos, replantear.

| Etapa | Condición para pasar (`DEC-11`) |
|---|---|
| Piloto | Métrica de éxito alcanzada |
| Pocos clientes | Proceso repetible sin empezar de cero |
| Más clientes | Margen por viaje positivo con costos reales |
| Crecimiento | Capacidad operativa probada |

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RIE-06 | Que los termómetros fallen y se pierda la evidencia del frío | El piloto no valida `SUP-06` | Cotizar los termómetros esta semana (propuesto por Paula) |

Pendientes por validar: `SUP-06`, `SUP-08`, `SUP-09`; costo de los termómetros; costo de conseguir clientes.

Siguiente paso sugerido: ejecutar el piloto y registrar los resultados en `probar-y-aprender`. Si hiciera falta un proveedor de medición, `innovacion-abierta-y-ecosistema`.

## Lo que se ve en este ejemplo

- Una pregunta por turno, también al calcular la economía y al diseñar el piloto.
- Cada bloque queda marcado Hecho, Supuesto o Pendiente por validar; la muestra de tres no se generaliza.
- La IA hace la cuenta con los números de Paula y señala qué parte es estimación.
- Paula decide qué hipótesis va primero, el umbral del piloto y las puertas de la ruta.
- El Business Model Fit no se declara sin evidencia.
