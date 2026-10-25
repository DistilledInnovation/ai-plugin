# Tipos de prueba y fidelidad

## 1. Los ocho tipos

| Tipo | Qué es | Sirve para aprender | Costo típico | Cuidado |
|---|---|---|---|---|
| Entrevista | Conversación estructurada con quien vive el proceso | Deseabilidad, contexto, criterios | Bajo | Lo que dicen no siempre es lo que hacen |
| Smoke test | Ofrecer algo falso o incompleto para ver si alguien lo pide o lo usa | Interés real, antes de construir | Bajo | Mide interés, no calidad |
| Conserje | El equipo hace a mano, con la persona delante, lo que haría el flujo | Experiencia y valor del servicio | Bajo a Medio | No escala; mide el servicio, no el sistema |
| Mago de Oz | Parece automático, pero una persona opera detrás | Reacción y uso de un flujo "automático" | Medio | Hay que decirlo al equipo; no prueba la viabilidad técnica |
| Prototipo clicable | Maqueta navegable de las pantallas o mensajes | Usabilidad y comprensión | Medio | Una maqueta bonita no valida que los datos existan |
| Demo funcional | Una parte funciona de verdad con datos ficticios o anonimizados | Factibilidad y calidad de un paso | Medio a Alto | No pruebas integración ni operación real |
| Piloto operativo | El flujo opera con usuarios reales, alcance acotado y controles | Valor, adopción y operación | Alto | Es una decisión mayor: se planea en `plan-piloto-y-especificacion` |
| Experimento de proceso | Medir o revisar el proceso real (contar, cronometrar, revisar muestras) | Línea base, datos, causas y variantes | Bajo | Una muestra pequeña es indicativa, no concluyente |

## 2. Cómo elegir

| Lo que necesitas saber | Empieza por |
|---|---|
| ¿Esto le importa a alguien? | Entrevista o smoke test |
| ¿Los datos y el proceso son como creemos? | Experimento de proceso |
| ¿Funciona la experiencia para quien lo usa? | Conserje, mago de Oz o prototipo clicable |
| ¿Puede un paso hacer el trabajo con la calidad necesaria? | Demo funcional con datos anonimizados |
| ¿Funciona en la operación real, con riesgo controlado? | Piloto operativo |

## 3. Escala de fidelidad (usa la más baja que sirva)

| Nivel | Qué es | Ejemplo genérico |
|---|---|---|
| 1 | Papel, guion o lista | Revisar 30 mensajes contra una lista de datos |
| 2 | Hoja de cálculo o documento hecho a mano | Una lista de solicitudes preparada a mano y aprobada por una persona |
| 3 | Maqueta navegable | Las pantallas o mensajes del flujo, sin lógica real |
| 4 | Demo funcional con datos ficticios o anonimizados | Un paso que de verdad lee un texto de ejemplo |
| 5 | Piloto con datos reales, alcance acotado | Una persona opera con el flujo durante unas semanas |

Sube de nivel solo cuando el anterior ya no da la evidencia que se necesita. El prototipo puede ser más elaborado si eso mejora la validez de la prueba, pero nunca debe aparentar capacidades que no se probaron.
