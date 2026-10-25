# Preparación de release

Flujo: ___ (`FLU-__`)  Release: ___ (`REL-__`)  Plan de evaluación: ___ (`EVP-__`)  Fecha prevista de salida: ___
Prepara (rol): ___  Aprueba la salida (rol del cliente): ___  Estado: No listo / Listo para aprobación / Aprobado

> Regla: este release **no se declara listo** mientras falte un dueño, la **aprobación** de quien tiene autoridad del cliente o un **rollback** ensayado. Sin secretos, direcciones reales ni datos personales.

## 1. Qué se libera

| Elemento | Versión que se libera | Versión probada | ¿Coinciden? | Si no: aprobación y regresión |
|---|---|---|---|---|
| Definición del flujo | | | Sí / No | `DEC-__`, `EVI-__` |
| Reglas | | | | |
| Plantillas | | | | |
| Instrucciones del modelo | | | | |
| Modelo | | | | |
| Configuración (reintentos, alertas, interruptor) | | | | |

## 2. Entradas

| Entrada | Estado | Referencia |
|---|---|---|
| Puerta de pruebas aprobada | Sí / No | `DEC-__` |
| Criterios cumplidos o dispensados con decisión | | `CA-__` |
| Decisiones bloqueantes abiertas (datos, cumplimiento, retención, modelo permitido, condiciones de la puerta de entrada) | Ninguna / Lista | `DEC-__` |
| Riesgos residuales aceptados por su dueño | | `RIE-__` |
| Pendientes de pruebas que pasan a operación, con dueño | | `TC-__` |

## 3. Dueños

| Qué | Dueño (rol) | Suplente (rol) | Del cliente o de un tercero (acuerdo) |
|---|---|---|---|
| Proceso y reglas | | | |
| Datos, retención y auditoría | | | |
| Aprobaciones del día a día | | | |
| Cola de revisión | | | |
| Cola de errores y alertas técnicas | | | |
| Interruptor de modo manual | | | |
| Soporte técnico | | | Acuerdo `DEC-__` |

## 4. Rollback

| Nivel | Qué hace | Disparadores verificables | Decide (sin pedir permiso) | Pasos (runbook) | Casos en curso | Tiempo objetivo | Ensayo (fecha, tiempo, quién) |
|---|---|---|---|---|---|---|---|
| 1 | Apagar la parte con IA (modo manual) | | | | | | |
| 2 | Volver a la versión anterior de reglas, plantillas o instrucciones | | | | | | |
| 3 | Desactivar el flujo y volver al proceso anterior | | | | | | |

Cómo se avisa un rollback (a quién, por qué medio): ___

## 5. Plan de salida

| Elemento | Respuesta |
|---|---|
| Ventana (fecha, hora, quién está presente) | |
| Salida gradual (qué primero, criterio para ampliar) | |
| Comunicación a las personas afectadas | |
| Acompañamiento reforzado (duración, quién, criterio de cierre) | |

## 6. Checklist de salida

| # | Comprobación | Sí / No | Evidencia |
|---|---|---|---|
| 1 | Puerta de pruebas aprobada y ninguna decisión bloqueante abierta | | |
| 2 | Lo que se libera coincide con lo probado | | |
| 3 | Cada componente, cola, alerta y tarea periódica con dueño y suplente | | |
| 4 | **Rollback** por niveles con disparadores y quién decide | | |
| 5 | **Rollback** ensayado en el entorno de prueba | | |
| 6 | Runbook entregado y revisado por quien opera | | |
| 7 | Personas capacitadas (aprobadores, dueños de colas, interruptor) | | |
| 8 | Secretos en el almacén, con rotación definida; ningún valor en artefactos | | |
| 9 | Alertas probadas: llegan a su dueño | | |
| 10 | Contrato actualizado con su dueño (madurez `production`) | | |
| 11 | **Aprobación** de salida del cliente registrada | | `DEC-__` |

## 7. Aprobación

| Decisión | Quién aprueba | Fecha | Condiciones | Registro |
|---|---|---|---|---|
| Salida a producción | | | | `DEC-__` |
