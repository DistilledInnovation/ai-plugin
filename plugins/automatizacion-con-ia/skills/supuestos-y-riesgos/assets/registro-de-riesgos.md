# Registro de riesgos

Flujo: ___ (`FLU-__`)  Fecha: ___

Un riesgo es algo que podría pasar y se gestiona con una mitigación y un responsable. La probabilidad es cualitativa y queda marcada como Supuesto mientras no haya datos ("No sé" es una respuesta válida).

## 1. Riesgos del flujo

| ID | Riesgo | Impacto | Probabilidad (Supuesto) | Mitigación | Guardrail | Responsable | Supuesto relacionado |
|---|---|---|---|---|---|---|---|
| RIE-01 | | | Baja, Media, Alta o No sé | | `GRD-__` | | `SUP-__` |

## 2. Riesgos que impiden probar

Lo que podría frenar las pruebas o volverlas poco confiables (datos que no se pueden usar sin anonimizar, personas sin tiempo, un criterio que nadie ha escrito).

| ID | Riesgo | Qué impide | Mitigación | Responsable |
|---|---|---|---|---|
| RIE-__ | | | | |

## 3. Autonomía y riesgo

Cada capacidad con nivel de autoridad mayor que 1 declara qué debe estar validado antes de subirla de nivel (la escalera y los guardrails vienen de `elegir-patron-y-autonomia`).

| Capacidad | Nivel actual | Riesgo si falla | Guardrail | Supuestos que deben estar validados antes de subir | Quién decide subir |
|---|---|---|---|---|---|
| CAP-__ | | `RIE-__` | `GRD-__` | `SUP-__` | |

Se sube con datos y se baja de inmediato si la métrica se degrada.

## 4. Pendientes por validar

- Riesgos sin responsable: ___
- Probabilidades sin base: ___
