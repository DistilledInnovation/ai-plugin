# Automatizaciones básicas

Organización: ___  Fecha: ___  Versión: borrador 1

Solo tareas de bajo riesgo y reversibles. Ninguna contacta a un cliente, mueve una oportunidad de etapa o cambia un importe sin que lo apruebe una persona. En una hoja de cálculo se logran con validaciones, marcas por fecha y vistas filtradas; en una herramienta más completa, con reglas equivalentes.

## 1. Reglas (`AUT-nn`)

| ID | Qué hace | Disparador | Acción (solo hacia el equipo) | Dueño | Lo que no hace | Riesgo |
|---|---|---|---|---|---|---|
| AUT-01 | Recordatorio de siguiente paso vencido | Fecha del siguiente paso anterior a hoy | Marca la fila y la lista en la vista "Vencidos" | ___ | No escribe al cliente | Bajo |
| AUT-02 | Alerta de estancamiento | Último contacto con más de ___ días (el umbral de la etapa 3) | Marca la fila como estancada | ___ | No cierra la oportunidad | Bajo |
| AUT-03 | Regla de cambio de etapa | Intento de pasar a una etapa sin el dato obligatorio | Rechaza el cambio y muestra qué falta | ___ | No mueve etapas por su cuenta | Bajo |
| AUT-04 | Revisión de duplicados | Cuenta o contacto repetido | Marca el par para que una persona lo una o lo descarte | ___ | No borra ni une filas | Bajo |
| AUT-05 | Asignación de responsable | Lead nuevo | Propone responsable según la regla ___ | ___ | No reasigna oportunidades abiertas | Bajo |

## 2. Qué no se automatiza todavía

| Candidato | Por qué espera | Condición para reconsiderarlo |
|---|---|---|
| Envío automático de mensajes al cliente | Requiere permisos, revisión humana y política de datos | Plan aprobado y con consentimiento |
| ___ | ___ | ___ |

## 3. Revisión

Cada ___ se revisa si las alertas se atienden o se ignoran. Una alerta que nadie atiende se ajusta o se elimina (backlog `BAC-nn`).
