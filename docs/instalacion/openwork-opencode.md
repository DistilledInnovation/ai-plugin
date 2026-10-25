# Instalar en OpenWork y opencode

<!-- estado:en-construccion -->
> **Estado: en construcción.** La primera Release (v1.0.0) aún no está publicada; las skills descritas son el catálogo objetivo. Los nombres de archivos y frases de ejemplo de esta página muestran cómo será la instalación cuando la Release exista.
<!-- /estado:en-construccion -->

Verificado: 2026-10-25

OpenWork y opencode leen skills (`SKILL.md`) desde estas carpetas: `.opencode/skills/` (proyecto), `~/.config/opencode/skills/` (tu usuario), `.claude/skills` y `.agents/skills`. También leen `AGENTS.md`.

## Opción 1. Copiar las carpetas

1. Descarga desde **Releases** el zip de la skill (o el `.plugin` y descomprímelo).
2. Copia la carpeta de la skill a `.opencode/skills/` del proyecto, o a `~/.config/opencode/skills/` para tenerla en todos tus proyectos.
3. Reinicia la sesión y escribe tu frase de ejemplo: "Quiero priorizar qué procesos automatizar".

## Opción 2. Agregar el catálogo (formato de plugins de Claude)

Si tu instalación usa el formato de plugins de Claude, el mecanismo de agregar el catálogo desde GitHub (`DistilledInnovation/ai-plugin`) depende de la versión (verificar). Si no encuentras la opción, usa la Opción 1: copiar las carpetas.

## Para equipos que mantienen el repo

El archivo [`AGENTS.md`](../../AGENTS.md) de este repositorio describe cómo se mantiene el contenido.
