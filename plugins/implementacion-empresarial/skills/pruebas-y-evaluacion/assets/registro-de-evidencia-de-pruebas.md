# Registro de evidencia de pruebas

Flujo: ___ (`FLU-__`)  Plan de evaluación: ___ (`EVP-__`)  Etapa que habilita: prototipo / piloto / producción
Entorno: ___ (separado de producción: Sí / No)  Datos: ficticios / anonimizados / reales con autorización (`DEC-__`)
Responsable del registro (rol): ___  Aprueba la puerta (rol): ___

> Sin credenciales, direcciones reales ni datos personales. La evidencia se referencia por su ubicación y su ID, nunca copiando datos de casos reales.

## 1. Versiones probadas

Toda corrida declara con qué versiones se hizo. Si una versión cambia, las pruebas que la cubren se repiten.

| Elemento | Versión | Aprobada por | Fecha |
|---|---|---|---|
| Definición del flujo | | | |
| Reglas | | | |
| Plantillas | | | |
| Instrucciones del modelo | | | |
| Modelo | | | |

## 2. Corridas

| ID | Fecha | Casos (`TC-__`) | Categoría | Versiones | Resultado | Evidencia (dónde) | Ejecutó (rol) | Observación | Defecto |
|---|---|---|---|---|---|---|---|---|---|
| `EVI-__` | | | functional / security / resilience / ai_quality | | Pasó / Falló / Bloqueada | | | | `DEF-__` |

## 3. Métricas de calidad de IA

| Métrica (`MET-__`) | Tipo | Conjunto (`DS-__`) | Umbral | Resultado | Cumple | Corrida |
|---|---|---|---|---|---|---|
| | exactitud / relevancia / fundamentación / consistencia estructural / selección de herramientas / tasa de escalamiento / sesgo / errores de extracción | | | | Sí / No / No aplica (razón) | `EVI-__` |

## 4. Defectos

| ID | Encontrado en | Descripción | Gravedad | Dueño | Corrección | ¿Requiere aprobación? (cambio de reglas, instrucciones o modelo) | Nueva corrida | Estado |
|---|---|---|---|---|---|---|---|---|
| `DEF-__` | `EVI-__` | | Alta / Media / Baja | | | Sí (`DEC-__`) / No | `EVI-__` | Abierto / Cerrado |

## 5. Trazabilidad requisito → prueba

| Elemento (`AT-__`, `CTL-__`, `RES-__`, `REQ-__`, `MET-__`) | Casos | Último resultado | Brecha |
|---|---|---|---|
| | `TC-__` | | Sin caso / No se puede probar antes de producción (pasa a operación con dueño) |

## 6. Criterios de aceptación

| Criterio (`CA-__`) | Etapa | Umbral | Resultado | Estado | Aprueba | Decisión |
|---|---|---|---|---|---|---|
| | | | | Cumplido / No cumplido / Dispensado / Pendiente | | `DEC-__` |

## 7. Puerta de pruebas

| Pregunta | Respuesta |
|---|---|
| ¿Las cuatro categorías tienen casos y corridas? | |
| ¿Todos los criterios de la puerta están cumplidos o dispensados con decisión? | |
| ¿Hay defectos abiertos? ¿Cuáles bloquean? | |
| ¿Qué pasa a operación por no poder probarse antes? | |
| **Aprobación** (rol, fecha, `DEC-__`) | |
