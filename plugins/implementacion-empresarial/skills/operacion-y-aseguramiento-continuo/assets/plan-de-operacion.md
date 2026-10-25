# Plan de operación y aseguramiento continuo

Flujo: ___ (`FLU-__`)  Release vigente: ___ (`REL-__`)  En producción desde: ___  Período de esta revisión: ___
Dueño del flujo (rol): ___  Soporte técnico (rol o tercero, acuerdo `DEC-__`): ___  Aprueba (rol): ___

> Cada cifra lleva procedencia, muestra y fecha. Las cifras de prototipo o piloto se rotulan como tales y nunca se presentan como resultados de producción. Sin secretos ni datos personales.

## 1. Etapa y límites

| Etapa | Criterios verificables | ¿Rige hoy? |
|---|---|---|
| Piloto | Alcance acotado, muestra pequeña, aprobación siempre humana, sin compromiso de servicio | |
| Producción | Release aprobado; dueños y suplentes; rollback ensayado; alertas con dueño; contrato en `production` | |
| Servicio gestionado | Acuerdo escrito con alcance, horario, tiempos de respuesta, informes, mejoras incluidas y recertificación a cargo del tercero | |

Lo que hace el soporte o el servicio gestionado y lo que sigue en el cliente:

| Actividad | Cliente | Soporte o servicio gestionado | Acuerdo |
|---|---|---|---|
| | | | `DEC-__` |

## 2. Observabilidad

| Señal | Qué muestra | Dónde | Cada cuánto se mira | Dueño |
|---|---|---|---|---|
| Casos por estado | | | | |
| Antigüedad en las colas | | | | |
| Errores por clase (transitorio, permanente, incierto) | | | | |
| Llamadas al modelo y fallas | | | | |
| Diferencias de conciliación | | | | |
| Uso del modo manual | | | | |
| Versión de reglas, plantillas e instrucciones por evento | | | | |

## 3. Alertas

| ID | Alerta | Umbral | Llega a | Primera acción (runbook) | Escala a | Probada |
|---|---|---|---|---|---|---|
| `ALE-__` | | | | | | Sí / No |

## 4. KPIs de valor

| ID | Indicador | Línea base (procedencia) | Piloto (muestra) | Meta | Producción (muestra, fecha) | ¿Cumple? |
|---|---|---|---|---|---|---|
| `KPI-__` | | | | | | Sí / No / Muy pronto para saber |

Calidad de IA en producción:

| Indicador | Cómo se mide | Resultado | Umbral del plan de evaluación |
|---|---|---|---|
| | | | `MET-__` |

## 5. Costo por caso

| Componente | Monto del período | Cómo se atribuye al flujo | Procedencia |
|---|---|---|---|
| Consumo de plataforma | | | Evidencia / Supuesto |
| Modelo | | | |
| Mensajería | | | |
| Horas de personas (revisión, aprobación) | | | |
| Soporte | | | |
| **Total / casos del período = costo por caso** | | | |

Qué no se incluye y por qué: ___

## 6. Control de cambios

| Tipo de cambio | Propone | Aprueba | Pruebas que se repiten | Cómo se vuelve atrás |
|---|---|---|---|---|
| Reglas o plantillas | | | | |
| Instrucciones del modelo o modelo | | | | |
| Definición del flujo | | | | |
| Permisos o conexiones | | | | |
| Cambio de diseño (pasos, alcance, autonomía) | Dueño del contrato | | Cadena completa desde `disenar-proceso-futuro` | |

Bitácora: `assets/bitacora-de-cambios.md`.

## 7. Incidentes del período

| ID | Fecha | Qué pasó | Casos afectados | Qué se hizo | Causa | Dueño | Mejora o riesgo aceptado |
|---|---|---|---|---|---|---|---|
| `INC-__` | | | | | | | `MEJ-__` / `DEC-__` |

## 8. Recertificación

| Elemento | Qué se revisa | Responsable | Próxima fecha |
|---|---|---|---|
| Calidad de IA | Repetir las métricas del plan de evaluación con las versiones vigentes | | |
| Permisos y accesos | | | |
| Secretos | Rotación al día | | |
| Retención y auditoría | | | |
| Perfil de plataforma | Volver a verificar con fecha lo que cambió | | |
| Contrato | Describe lo que de verdad ocurre | | |
| Acuerdo de soporte | Vigencia y cumplimiento | | |
| KPIs | Valor frente a la meta | | |

Resultado: Recertificado / Recertificado con condiciones / No recertificado (acción: ___, dueño: ___).

## 9. Backlog de mejoras

| ID | Mejora | Evidencia | Impacto esperado | Va a | Dueño | Estado |
|---|---|---|---|---|---|---|
| `MEJ-__` | | `KPI-__` / `INC-__` / cola | | `disenar-proceso-futuro` (diseño) / control de cambios (configuración) | | |

## 10. Decisiones y pendientes

| ID | Decisión o pendiente | Dueño | Fecha | Aprobación |
|---|---|---|---|---|
| `DEC-__` | | | | |
