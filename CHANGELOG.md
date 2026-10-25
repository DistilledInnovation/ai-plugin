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

### Seguridad
- La publicación falla si el secreto `TERMINOS_PROHIBIDOS` está vacío o si la versión del tag no coincide con los manifiestos.
