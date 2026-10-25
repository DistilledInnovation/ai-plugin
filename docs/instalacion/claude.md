# Instalar en Claude

Verificado: 2026-10-25

Hay tres caminos. Si tu empresa tiene Claude Team o Enterprise, usa el primero: los participantes no hacen nada.

## Opción 1. El admin lo carga para toda la organización (nivel 1, recomendado)

Para administradores:

1. Descarga desde **Releases** el archivo `.plugin` de la metodología (por ejemplo `innovacion-destilada-v0.1.0.plugin`).
2. Entra a **Organization settings > Plugins & skills**.
3. Pulsa **Add > Upload a skill or plugin** y sube el archivo (`.zip` o `.plugin`, hasta 200 MB, solo archivos de texto).
4. Elige a quién se lo provisionas: a todos o, en Enterprise, a grupos.
5. Prueba con una frase de ejemplo: "Quiero priorizar qué procesos automatizar".

Para participantes: el plugin aparece ya instalado. Pueden activarlo o desactivarlo, pero no borrarlo.

## Opción 2. Agregar el catálogo con un clic (nivel 1b)

Para Claude Cowork:

1. Abre **Customize > Browse plugins > Personal**.
2. Pulsa **"+"** y elige **Add marketplace from GitHub**.
3. Escribe `DistilledInnovation/ai-plugin`.
4. Instala las metodologías que necesites.

Para Claude Code (equipos técnicos):

```bash
claude plugin marketplace add DistilledInnovation/ai-plugin
claude plugin install innovacion-destilada@distilled-innovation
```

## Opción 3. Subir un zip de una skill (nivel 2)

1. Descarga desde **Releases** el zip de la skill (por ejemplo `priorizar-flujos-v0.1.0.zip`). Dentro del zip, la carpeta de la skill debe quedar en la raíz.
2. En Claude.ai abre **Settings > Skills**.
3. Sube el zip.
4. Activa la skill y pruébala con una frase de ejemplo.

## Si algo falla

- El zip se rechaza: confirma que lo descargaste de Releases sin descomprimirlo ni volver a comprimirlo.
- La skill no se activa: escribe una frase más parecida a las del ejemplo, o menciona el nombre de la skill.
