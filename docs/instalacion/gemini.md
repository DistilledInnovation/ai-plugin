# Instalar en Gemini

Verificado: 2026-10-25

## Opción 1. Gem con copiar y pegar (nivel 3, para novatos)

Los Gems aceptan instrucciones y unos 10 archivos de conocimiento. El proceso exacto de la interfaz puede cambiar (verificar).

1. Descarga desde **Releases** el paquete `<metodologia>-copiar-pegar-vX.Y.Z.zip` y descomprímelo.
2. En Gemini crea un **Gem** nuevo.
3. Pega el contenido de `INSTRUCCIONES.md` en las instrucciones del Gem.
4. Sube como conocimiento los archivos `01-*.md`, `02-*.md`, etc. (el paquete respeta el tope de 10 archivos).
5. Guarda el Gem y pruébalo con una frase de ejemplo.

Este camino se actualiza a mano: con cada versión nueva, repite los pasos 1 a 4.

## Opción 2. Gemini CLI (desarrolladores)

Gemini CLI lee `SKILL.md` de forma nativa.

1. Descarga y descomprime el zip de la skill.
2. Copia la carpeta a `.gemini/skills/` (proyecto) o a la carpeta de skills de tu usuario.
3. Inicia Gemini CLI y escribe tu frase de ejemplo.

## Gemini Enterprise

El registro de servidores MCP lo hace el administrador y queda fuera del alcance de esta versión.
