# Cambios

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y versionado semántico.

## [Sin publicar]

### Agregado
- Estructura del repositorio: marketplace de Claude con cuatro plugins (Innovación Destilada, Automatización con IA, Implementación Empresarial y Aceleración Comercial).
- Scripts de sincronización de bloques compartidos, validación y empaquetado (zips por skill, `.plugin` por plugin y paquetes copiar-pegar).
- Flujos de GitHub Actions para validar en cada cambio y publicar en cada tag `v*`.
- README, `AGENTS.md`, guías de instalación por plataforma y guía de taller.

- Innovación Destilada 0.3.0: skills `facilitador-innovacion-destilada`, `alinear-equipo` e `identificar-reto` con plantillas, ejemplos ficticios, evals y README del plugin.
- Innovación Destilada 0.5.0: skills `investigar-y-empatizar` (escalera de profundidad, plan, guía de entrevista, perfil de usuario y diario) y `sintetizar-y-redefinir-reto` (hallazgos, necesidades y tensiones, Mapa de Empatía, Perfil del Cliente y reto redefinido), con ejemplos ficticios y evals. Los IDs de evidencia del facilitador pasan de `HEC` a `HAL`, notas de fuente más explícitas y `validar.py` ignora `evals/results/`.
- Innovación Destilada 0.7.0: skills `facilitar-ideacion` (agenda de sesión, Principios de Participación, calentamiento, técnicas paso a paso, modos taller en vivo e individual), `construir-concepto-fuerte` (agrupación, votación y Concepto Fuerte de Solución) y `disenar-prototipo` (Mapa de Valor, Encaje Problema-Solución, prototipos rápidos, guion de prueba y Pitch A.I.D.A.), con ejemplos ficticios y evals. La regla de un solo signo de interrogación por mensaje pasa a `compartido/reglas-facilitacion.md`.
- Innovación Destilada 0.9.0: skills `validar-supuestos-y-mvp` (siete categorías de supuestos, calificación, tarjeta de prueba, MVP de Kniberg con la tabla "No de esta forma / Sino de esta"), `probar-y-aprender` (Tablero de Validación, seis métricas de evaluación, cuatro salidas de decisión y bitácora), `modelo-de-negocio-y-escalamiento` (los 9 bloques con preguntas guía, de Product/Market Fit a Business Model Fit, piloto y ruta de escalamiento) e `innovacion-abierta-y-ecosistema` (7 patrones, 7 prácticas, mapa de ecosistema y reglas de colaboración), con ejemplos ficticios y evals. Con esto las 12 skills del plugin quedan disponibles. Correcciones en los ejemplos: IDs `SUP-nn` y `DEC-nn` estables entre ejemplos encadenados, agenda con la sexta columna del libro, instrucciones del taller en un solo paso por mensaje y preguntas de una sola petición.

### Cambiado
- La regla de facilitación de preguntas se relaja: una pregunta principal por turno, con hasta dos seguimientos breves del mismo punto o una disyuntiva; nunca una lista de preguntas sin relación. Se ajustan los graders de primer turno, el eval `disenar-prototipo-entregable` (ahora el mensaje trae escenario, tarea y criterio de éxito) y se quitan las frases "si esa skill aún no está disponible" porque las 12 skills existen.

### Seguridad
- La publicación falla si el secreto `TERMINOS_PROHIBIDOS` está vacío o si la versión del tag no coincide con los manifiestos.
