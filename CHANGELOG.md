# Cambios

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y versionado semántico.

## [Sin publicar]

### Agregado
- Estructura del repositorio: marketplace de Claude con cuatro plugins (Innovación Destilada, Automatización con IA, Implementación Empresarial y Aceleración Comercial).
- Scripts de sincronización de bloques compartidos, validación y empaquetado (zips por skill, `.plugin` por plugin y paquetes copiar-pegar).
- Flujos de GitHub Actions para validar en cada cambio y publicar en cada tag `v*`.
- README, `AGENTS.md`, guías de instalación por plataforma y guía de taller.

### Seguridad
- La publicación falla si el secreto `TERMINOS_PROHIBIDOS` está vacío o si la versión del tag no coincide con los manifiestos.
