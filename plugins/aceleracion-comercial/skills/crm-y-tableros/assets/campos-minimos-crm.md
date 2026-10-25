# Campos mínimos del registro

Organización: ___  Fecha: ___  Versión: borrador 1

Regla: cada campo responde a una decisión, una regla o un KPI. Si nadie lo usa, no entra. Una fila por oportunidad.

## 1. Campos (`CAM-nn`)

| ID | Campo | Grupo | Qué decisión, regla o KPI alimenta | Obligatorio desde la etapa |
|---|---|---|---|---|
| CAM-01 | Identificador (`OPO-nn`) | Núcleo | Referencia estable en reuniones y tableros | ETA-01 |
| CAM-02 | Cuenta (nombre o descripción) | Núcleo | Evitar duplicados | ETA-01 |
| CAM-03 | Segmento o ICP (`SEG-nn`, `ICP-nn` o "Fuera de perfil") | Núcleo | `KPI-02`, exclusiones | ETA-01 |
| CAM-04 | Origen (canal) | Núcleo | `KPI-01`, atribución | ETA-01 |
| CAM-05 | Responsable | Núcleo | Quién lleva la oportunidad; `KPI-08` | ETA-01 |
| CAM-06 | Etapa (`ETA-nn`) | Núcleo | Pipeline, forecast | ETA-01 |
| CAM-07 | Contacto y actor (`ACT-nn`) | Núcleo | Con quién se habla y su rol | ETA-02 |
| CAM-08 | Último contacto (fecha) | Núcleo | `KPI-07` (estancadas) | ETA-02 |
| CAM-09 | Siguiente paso | Núcleo | Qué hará quién; `KPI-12` | Siempre (oportunidad abierta) |
| CAM-10 | Fecha del siguiente paso | Núcleo | Alerta de vencido; `KPI-12` | Siempre (oportunidad abierta) |
| CAM-11 | Importe mensual | Núcleo | `KPI-09`, forecast | ETA-05 |
| CAM-12 | Fecha estimada de decisión | Núcleo | Forecast | ETA-06 |
| CAM-13 | Resultado (abierta, ganada, perdida, nutrir, descartada) | Núcleo | `KPI-05` | ETA-07 |
| CAM-14 | Fecha de creación | Medición | `KPI-04` (cohorte) | ETA-01 |
| CAM-15 | Fecha de reunión realizada | Medición | `KPI-04`, `KPI-05`, `KPI-06` con la definición de oportunidad de la línea base | ETA-04 |
| CAM-16 | Fecha de cierre | Medición | `KPI-06` | ETA-07 |
| CAM-17 | Motivo de pérdida (frase del cliente) | Medición | Aprendizaje de mercado (7 a 1) | ETA-07 si se pierde |
| CAM-18 | Necesidad (Sí, Parcial, No) | Calificación | `REG-nn` | ETA-03 |
| CAM-19 | Puntaje BANT (0 a 8) | Calificación | `REG-nn` | ETA-03 |
| CAM-20 | Dolor (frase del cliente) | Calificación | Mensajes y argumentario | ETA-03 |
| CAM-21 | Paquete (`OFE-nn`) | Opcional | Análisis por oferta | ETA-05 |
| CAM-22 | Referidor (`ACT-nn`) | Opcional | Agradecimiento y atribución | ETA-01 si hay |
| CAM-23 | Notas (descuento aprobado y quién lo aprobó; notas MEDDICC) | Opcional | Regla de descuentos del kit; solo ventas complejas para MEDDICC | Opcional |

Si el negocio usa una definición de "oportunidad" distinta de la etapa de la línea base, `CAM-15` guarda la fecha que permite comparar. Anota la decisión aquí: ___ (`DEC-nn`).

## 2. Qué se queda fuera (y por qué)

| Dato candidato | Por qué no entra por ahora |
|---|---|
| ___ | ___ |

## 3. Datos que no se guardan

Documentos fiscales, claves, datos bancarios y cualquier dato sensible del cliente: ___ (no se guardan en el registro).

## 4. Pendientes por validar

- ___
