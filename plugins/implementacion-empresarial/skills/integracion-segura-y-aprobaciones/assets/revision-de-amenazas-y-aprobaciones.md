# Revisión de amenazas y aprobaciones

Flujo: ___ (`FLU-__`)  Contrato (fecha): ___  Plan de implementación (versión): ___  Mapa de capacidades: ___
Fecha: ___  Revisa (rol): ___  Aprueba (rol): ___  Estado: Borrador / Aprobada

> Sin secretos, credenciales, direcciones reales ni datos personales en este documento. Los secretos se nombran por su función y por dónde se referencian, nunca por su valor.

## 1. Activos y límites de confianza

| Activo (dato o capacidad) | Sensibilidad | Dónde vive | Quién responde | Cruza los límites |
|---|---|---|---|---|
| | public / internal / personal / sensitive | `CMP-__` | | `CMP-__` → `CMP-__` |

## 2. Modelo de amenazas

| ID | Límite o flujo | Categoría | Cómo ocurre | Impacto | Probabilidad | Control | Riesgo residual | Dueño |
|---|---|---|---|---|---|---|---|---|
| `AME-__` | | Suplantación / Alteración / Repudio / Fuga / Denegación / Privilegios / Instrucciones ocultas / Exceso de autonomía / Salida no validada / Fuga al modelo | | | Alta / Media / Baja / No sé | `CTL-__` | | |

## 3. Mínimo privilegio

| Rol o componente | Lee | Escribe | Aprueba | Administra | No puede | Revisa los permisos (rol, cada cuánto) |
|---|---|---|---|---|---|---|
| | | | | | | |

## 4. Secretos

| Secreto (función) | Lo usa | Dónde vive | Quién puede leerlo | Rotación | Dónde está prohibido |
|---|---|---|---|---|---|
| | `CMP-__` | Almacén de secretos (decisión `DEC-__`) | | | Contrato, plan, mapa, código, definiciones, exportaciones, registros, chat |

## 5. Datos hacia el modelo

| Paso con IA | Datos que necesita | Se omiten | Se enmascaran o anonimizan (cómo) | Quedan sin anonimizar (decisión) | Modelo permitido y dónde se procesa |
|---|---|---|---|---|---|
| `FUT-__` | | | | `DEC-__` | `DEC-__` |

## 6. Matriz de aprobación humana

| Acción de impacto | Quién la propone | Quién aprueba | Cuándo | Si nadie responde | Si rechaza | Evidencia | Política del contrato |
|---|---|---|---|---|---|---|---|
| | | | | | | `EVD-__` | `APR-__` o Nueva |

Acciones que siempre se revisan: enviar a terceros, registrar o modificar en sistemas, borrar, cambiar reglas o criterios, cambiar el modelo o sus instrucciones, conceder accesos, encender la parte con IA tras un apagado.

## 7. Auditoría

| Evento | Qué se registra | Qué no se registra | Dónde | Retención (decisión) | Quién puede leerlo |
|---|---|---|---|---|---|
| | Quién, qué, cuándo, versión de reglas e instrucciones, decisión | Copias completas de datos sensibles | | `DEC-__` | |

## 8. Controles y cómo se prueban

| ID | Control | Amenazas que cubre | Prueba (positiva y negativa) | Estado |
|---|---|---|---|---|
| `CTL-__` | | `AME-__` | | Diseñado / Probado / Pendiente por validar |

## 9. Decisiones y riesgos residuales

| ID | Decisión o riesgo aceptado | Alternativas | Dueño | Fecha | Aprobación |
|---|---|---|---|---|---|
| `DEC-__` | | | | | Pendiente |

## 10. Pendientes

| Pendiente | Quién decide | Para cuándo | Bloquea |
|---|---|---|---|
| | | | |
