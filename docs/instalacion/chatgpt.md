# Instalar en ChatGPT

Verificado: 2026-10-25

No usamos GPTs personalizados: según fuentes secundarias están en retiro (verificar). Usa Skills; si no están disponibles en tu plan, usa un Proyecto.

## Opción 1. Skills del espacio de trabajo (nivel 1 y 2)

Disponibles en planes Business, Enterprise y Edu. En planes personales las fuentes se contradicen (verificar).

Para participantes o admins que suben la skill:

1. Descarga desde **Releases** el zip de la skill (por ejemplo `priorizar-flujos-v0.1.0.zip`). La carpeta de la skill debe estar en la raíz del zip.
2. En ChatGPT abre **Skills > Create > Upload from computer** y elige la carpeta o el zip.
3. Espera el resultado del análisis. Las cargas se escanean y pueden quedar **"Needs Review"** (pendiente de revisión) o **"Blocked"** (bloqueada); en ese caso avisa a tu admin.
4. Prueba con una frase de ejemplo.

Para administradores: el admin controla las Skills del espacio de trabajo. Carga las skills una vez, aprueba las que queden en revisión y confirma que quedan disponibles para el equipo.

## Opción 2. Proyecto con copiar y pegar (nivel 3, respaldo)

1. Descarga desde **Releases** el paquete `<metodologia>-copiar-pegar-vX.Y.Z.zip` y descomprímelo.
2. Crea un **Proyecto** en ChatGPT.
3. En las instrucciones del proyecto, pega el contenido de `INSTRUCCIONES.md`.
4. Sube como archivos del proyecto los archivos `01-*.md`, `02-*.md`, etc.
5. Abre un chat dentro del proyecto y escribe tu frase de ejemplo.

Este camino tiene menor calidad y se actualiza a mano: cuando salga una versión nueva, repite los pasos 1 a 4.
