# Instalar en Claude

<!-- estado:en-construccion -->
> **Estado: en construcción.** La primera Release (v1.0.0) aún no está publicada; las skills descritas son el catálogo objetivo. Los nombres de archivos y frases de ejemplo de esta página muestran cómo será la instalación cuando la Release exista.
<!-- /estado:en-construccion -->

Verificado: 2026-10-25

Hay tres caminos. Si tu empresa tiene Claude Team o Enterprise, usa el primero: los participantes no hacen nada.

## Opción 1. El admin lo carga para toda la organización (nivel 1, recomendado)

Para administradores:

1. Descarga desde **Releases** el archivo `.plugin` de la metodología (por ejemplo `innovacion-destilada-v0.1.0.plugin`).
2. Entra a la configuración de la organización y busca la sección de plugins y skills (según la investigación: **Organization settings > Plugins & skills**) (verificar).
3. Busca la opción para agregar y subir una skill o plugin (reportado como **Add > Upload a skill or plugin**) y sube el archivo (`.zip` o `.plugin`, hasta 200 MB, solo archivos de texto) (verificar).
4. Elige a quién se lo provisionas: a todos o, en Enterprise, a grupos.
5. Prueba con una frase de ejemplo: "Quiero priorizar qué procesos automatizar".

Para participantes: el plugin aparece ya instalado. Según lo reportado, pueden activarlo o desactivarlo, pero no borrarlo (verificar).

## Opción 2. Agregar el catálogo con un clic (nivel 1b)

Para Claude Cowork:

1. Abre la personalización y busca la exploración de plugins, en la sección personal (reportado como **Customize > Browse plugins > Personal**) (verificar).
2. Pulsa el botón "+" y elige agregar un marketplace desde GitHub (verificar).
3. Escribe `DistilledInnovation/ai-plugin`.
4. Instala las metodologías que necesites.

Para Claude Code (equipos técnicos):

```bash
claude plugin marketplace add DistilledInnovation/ai-plugin
claude plugin install innovacion-destilada@distilled-innovation
```

## Opción 3. Subir un zip de una skill (nivel 2)

1. Descarga desde **Releases** el zip de la skill (por ejemplo `priorizar-flujos-v0.1.0.zip`). Dentro del zip, la carpeta de la skill debe quedar en la raíz.
2. En Claude.ai busca la opción de Skills en la configuración (reportado como **Settings > Skills**) (verificar).
3. Sube el zip.
4. Activa la skill y pruébala con una frase de ejemplo.

## Si algo falla

- El zip se rechaza: confirma que lo descargaste de Releases sin descomprimirlo ni volver a comprimirlo.
- La skill no se activa: escribe una frase más parecida a las del ejemplo, o menciona el nombre de la skill.
