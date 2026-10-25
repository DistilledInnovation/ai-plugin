# Instalar en Claude

Verificado: 2026-10-25

## La forma más corta

Claude Code o Cowork, en el chat:

```
/plugin marketplace add DistilledInnovation/ai-plugin
/plugin install innovacion-destilada@distilled-innovation
```

Repite el segundo comando con `automatizacion-con-ia`, `implementacion-empresarial` y `aceleracion-comercial` si los necesitas. En Cowork también puedes usar la exploración de plugins personales y agregar `DistilledInnovation/ai-plugin` como marketplace de GitHub (verificar la ruta exacta del menú).

Claude.ai (sin terminal): Descarga desde **Releases** el archivo `<metodologia>-todo-en-uno-v*.zip` (uno por metodología; son 4 en total). Trae la metodología completa en una sola skill: el asistente lee la guía de cada etapa cuando la necesita.

1. En Claude.ai busca **Settings > Skills** (reportado) (verificar) y sube el zip.
2. Actívala y escribe: "Quiero priorizar qué procesos automatizar".

## El admin lo sube una vez para todos

1. Entra a **Organization settings > Plugins & skills** (reportado) (verificar).
2. Elige **Add > Upload a skill or plugin** (reportado) (verificar) y sube el zip todo en uno (`.zip` o `.plugin`, hasta 200 MB, solo texto).
3. Elige a quién se lo provisionas: a todos o, en Enterprise, a grupos.

Los participantes lo ven ya instalado; según lo reportado pueden activarlo o desactivarlo, pero no borrarlo (verificar).

## Respaldo

- Un zip por skill (para administradores): `<skill>-v*.zip` en Releases, con la carpeta de la skill en la raíz.
- Si el zip se rechaza, descárgalo de nuevo sin descomprimirlo ni volver a comprimirlo.
