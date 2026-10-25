# Instalar en Grok

Verificado: 2026-10-25

## Opción 1. Chatbot de Grok

La importación de skills en el chatbot (archivos `.zip`, `.skill` o `.md`) aparece solo en fuentes secundarias (verificar). Si no ves esa opción, usa el respaldo de copiar y pegar.

1. Descarga desde **Releases** el zip de la skill.
2. Busca en la configuración de Grok la opción para importar skills y sube el archivo (verificar).
3. Pruébala con una frase de ejemplo.

Respaldo (nivel 3):

1. Descarga el paquete `<metodologia>-copiar-pegar-vX.Y.Z.zip` y descomprímelo.
2. Pega el contenido de `INSTRUCCIONES.md` al inicio de la conversación (o en las instrucciones personalizadas) (verificar).
3. Adjunta los archivos `01-*.md`, `02-*.md`, etc., hasta donde la herramienta lo permita (verificar).

## Opción 2. Grok Build (desarrolladores)

Grok Build lee `SKILL.md` de forma nativa.

1. Descarga y descomprime el zip de la skill.
2. Copia la carpeta a `.grok/skills/`.
3. Inicia Grok Build y escribe tu frase de ejemplo.
