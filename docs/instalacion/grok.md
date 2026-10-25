# Instalar en Grok

Verificado: 2026-10-25

## La forma más corta

Copiar y pegar, que funciona en cualquier chat:

1. Descarga y descomprime `<metodologia>-copiar-pegar-v*.zip` de **Releases**.
2. Pega `INSTRUCCIONES.md` al inicio de la conversación o en las instrucciones personalizadas (verificar).
3. Adjunta los archivos `01-*.md`, `02-*.md`, etc., hasta donde la herramienta lo permita (verificar).

## Importar skills en el chatbot

La importación de skills (`.zip`, `.skill` o `.md`) aparece solo en fuentes secundarias (verificar). Si ves la opción en la configuración, sube el `<metodologia>-todo-en-uno-v*.zip`.

## Grok Build (desarrolladores)

Grok Build lee `SKILL.md` de forma nativa. Prueba `npx skills add DistilledInnovation/ai-plugin` y, si no lo lista, copia la carpeta de la skill a `.grok/skills/` (verificar la ruta).
