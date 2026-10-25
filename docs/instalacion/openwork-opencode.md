# Instalar en OpenWork y opencode

<!-- estado:en-construccion -->
> **Estado:** las instalaciones por línea de comandos funcionan hoy. Los archivos descargables aparecerán en **Releases** cuando se publique la primera Release (v1.0.0).
<!-- /estado:en-construccion -->

Verificado: 2026-10-25

## La forma más corta

Necesitas [Node.js](https://nodejs.org). En la terminal:

```
npx skills add DistilledInnovation/ai-plugin
```

Elige opencode en la lista y las skills que quieras. Para una sola: `--skill priorizar-flujos`; con `-g` queda en tu usuario y no solo en el proyecto. Reinicia la sesión y escribe: "Quiero priorizar qué procesos automatizar".

## Copiar las carpetas a mano

OpenWork y opencode leen `SKILL.md` desde `.opencode/skills/` (proyecto), `~/.config/opencode/skills/` (tu usuario), `.claude/skills` y `.agents/skills`.

1. Descarga de **Releases** el zip de la skill y descomprímelo.
2. Copia la carpeta de la skill a una de esas rutas.

## Catálogo en formato de plugins de Claude

Si tu instalación usa ese formato, agregar `DistilledInnovation/ai-plugin` como marketplace depende de la versión (verificar). Si no lo encuentras, usa `npx skills` o copia las carpetas.

Quien mantiene el repo: [`AGENTS.md`](../../AGENTS.md).
