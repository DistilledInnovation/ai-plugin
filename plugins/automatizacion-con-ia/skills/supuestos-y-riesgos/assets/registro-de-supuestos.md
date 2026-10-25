# Registro de supuestos

Flujo: ___ (`FLU-__`)  Canvas: versión ___  Fecha: ___  Quién conoce los datos: ___

Un supuesto es algo que damos por cierto y que se puede desmentir. Cada fila trae una señal que se puede observar y un umbral que lo haría falso. **Criticidad = impacto × incertidumbre.** El puntaje ordena la conversación; no es una verdad objetiva.

## 1. Supuestos

Fórmula: "Creemos que [quién o qué] [resultado] bajo [condición]. Lo sabremos porque [señal]. Es falso si [umbral]."

| ID | Afirmación falsable | Tipo | Evidencia actual (procedencia) | Impacto (1-5) | Incertidumbre (1-5) | Criticidad | Evidencia mínima para aceptar o rechazar | Responsable |
|---|---|---|---|---|---|---|---|---|
| SUP-01 | Creemos que ___. Lo sabremos porque ___. Es falso si ___. | | | | | | | |

Tipos: deseabilidad, valor, factibilidad técnica, datos, viabilidad económica, seguridad y cumplimiento, adopción.

Justificación de las notas (una línea por supuesto): ___

## 2. Cobertura por tipo

| Tipo | Supuestos | Si no hay ninguno |
|---|---|---|
| Deseabilidad | | ¿Quién tendría que querer usar esto y lo hemos confirmado? |
| Valor | | |
| Factibilidad técnica | | |
| Datos | | |
| Viabilidad económica | | |
| Seguridad y cumplimiento | | |
| Adopción | | |

Un tipo sin supuestos puede ser un punto ciego: anótalo como "Pendiente por validar" con su motivo.

## 3. Los 3 a 5 más arriesgados

| Orden | ID | Por qué va primero (criticidad, dependencia o bloqueo) | Siguiente paso |
|---|---|---|---|
| 1 | | | Tarjeta de prueba `PRU-__` |

Ajuste con juicio humano: lo que bloquea a otros supuestos va antes; un riesgo legal o de seguridad no espera por ser caro de probar.

## 4. Pendientes por validar

- Umbrales por definir con el negocio: ___
- Datos que nadie ha contado: ___
