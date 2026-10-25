# Runbook de operación y transferencia

Flujo: ___ (`FLU-__`)  Release: ___ (`REL-__`)  Vigente desde: ___  Dueño del runbook (rol): ___  Próxima revisión: ___

> Para quien opera el flujo después de la salida. Sin secretos, direcciones reales ni datos personales: los secretos se nombran por su función y por dónde viven; las personas, por su rol.

## 1. Resumen del servicio

| Pregunta | Respuesta |
|---|---|
| Qué hace el flujo, en una oración | |
| Horario de operación | |
| Qué está fuera de alcance (va a revisión) | |
| Dónde se ve el estado de los casos | |

## 2. Contactos por rol

| Rol | Para qué se le busca | Horario | Suplente |
|---|---|---|---|
| Dueño del proceso | | | |
| Responsable de datos | | | |
| Soporte técnico | | Según acuerdo `DEC-__` | |
| Quien aprueba la salida y los cambios mayores | | | |

## 3. Operación diaria

| Tarea | Quién | Cuándo | Cómo se sabe que está hecha |
|---|---|---|---|
| Atender la cola de revisión | | | |
| Revisar la cola de errores | | | |
| Revisar la conciliación | | | |

## 4. Alertas: qué hacer

| Alerta | Umbral | Llega a | Primera acción | Si no se resuelve en | Escalar a |
|---|---|---|---|---|---|
| | | | | | |

## 5. Incidentes

| Severidad | Ejemplo | Quién decide | Primera acción | Comunicación |
|---|---|---|---|---|
| Alta (efecto equivocado hacia afuera, datos de una persona a otra) | | | El nivel de rollback que el plan fija para ese disparador (normalmente el 3: un efecto equivocado llegó hacia afuera), de inmediato | |
| Media (flujo detenido o lento) | | | | |
| Baja (error aislado sin efecto) | | | | |

Todo incidente queda registrado con: qué pasó, cuándo, casos afectados, qué se hizo, causa y mejora (`INC-__`).

## 6. Rollback paso a paso

**Nivel 1: apagar la parte con IA (modo manual).**
1. ___
2. ___
Volver a encender: solo ___ (rol), con la causa resuelta y registrada.

**Nivel 2: volver a la versión anterior de reglas, plantillas o instrucciones.**
1. ___
2. ___

**Nivel 3: desactivar el flujo y volver al proceso anterior.**
1. ___
2. Casos en curso: ___
3. Cómo se vuelve a activar: ___

## 7. Tareas periódicas

| Tarea | Frecuencia | Dueño | Registro |
|---|---|---|---|
| | | | |

## 8. Dónde está cada cosa

| Artefacto | Dónde (sin direcciones reales) | Quién lo mantiene |
|---|---|---|
| Contrato del flujo | | |
| Registro de decisiones | | |
| Plan de evaluación y evidencia | | |
| Registro de idempotencia | | |
| Secretos | Almacén de secretos (sin valores en ningún documento) | |
| Bitácora de cambios | | |
