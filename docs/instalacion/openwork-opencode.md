# Instalar en OpenWork y opencode

Verificado: 2026-10-25

OpenWork y opencode leen skills (`SKILL.md`) desde estas carpetas: `.opencode/skills/` (proyecto), `~/.config/opencode/skills/` (tu usuario), `.claude/skills` y `.agents/skills`. También leen `AGENTS.md`.

## Opción 1. Copiar las carpetas

1. Descarga desde **Releases** el zip de la skill (o el `.plugin` y descomprímelo).
2. Copia la carpeta de la skill a `.opencode/skills/` del proyecto, o a `~/.config/opencode/skills/` para tenerla en todos tus proyectos.
3. Reinicia la sesión y escribe tu frase de ejemplo: "Quiero priorizar qué procesos automatizar".

## Opción 2. Agregar el catálogo (formato de plugins de Claude)

Si tu instalación usa el formato de plugins de Claude, agrega el catálogo desde GitHub:

1. Agrega el marketplace `DistilledInnovation/ai-plugin`.
2. Instala la metodología que necesites.

## Para equipos que mantienen el repo

El archivo [`AGENTS.md`](../../AGENTS.md) de este repositorio describe cómo se mantiene el contenido.
