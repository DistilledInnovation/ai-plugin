# Instalar en Microsoft 365 Copilot

<!-- estado:en-construccion -->
> **Estado:** las instalaciones por línea de comandos funcionan hoy. Los archivos descargables aparecerán en **Releases** cuando se publique la primera Release (v1.0.0).
<!-- /estado:en-construccion -->

Verificado: 2026-10-25

## La forma más corta

En Microsoft 365 Copilot las skills viven dentro de un **agente declarativo** con un máximo de **8 skills** y menos de 20.000 caracteres por instrucciones. No está claro si ya es disponibilidad general o sigue en vista previa (verificar). Por eso el archivo todo en uno es ideal: una sola skill por metodología.

Descarga desde **Releases** el archivo `<metodologia>-todo-en-uno-v*.zip` (uno por metodología; son 4 en total). Trae la metodología completa en una sola skill: el asistente lee la guía de cada etapa cuando la necesita.

1. Abre Agent Builder (o Teams Toolkit si tu equipo es técnico) y crea un agente declarativo (verificar los nombres exactos del menú).
2. Agrega el zip como habilidad personalizada (verificar el paso exacto).
3. Prueba con: "Quiero priorizar qué procesos automatizar".

## El admin lo publica una vez para todos

1. Revisa el agente en el centro de administración de Microsoft 365 (verificar la ruta exacta).
2. Despliégalo a las personas o grupos del taller (verificar).
3. Confirma que aparece en Copilot para un usuario de prueba.

## Respaldo

Si tu plataforma no acepta el zip, pega `INSTRUCCIONES.md` del paquete `<metodologia>-copiar-pegar-v*.zip` en las instrucciones del agente (menor calidad, se actualiza a mano).
