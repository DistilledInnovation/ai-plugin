# Instalar en Microsoft 365 Copilot

Verificado: 2026-10-25

En Microsoft 365 Copilot las skills viven dentro de un **agente declarativo**. Hay límites que conviene conocer:

- Máximo **8 skills por agente**.
- Las instrucciones de cada skill deben tener menos de 20.000 caracteres (por eso cada `SKILL.md` se mantiene por debajo de ese tope).
- No está claro si esta capacidad ya es de disponibilidad general o sigue en vista previa; las fuentes se contradicen (verificar).

## Para quien arma el agente

1. Elige hasta 8 skills de una metodología según el taller (por ejemplo el facilitador y 7 skills de etapas).
2. Descarga desde **Releases** el zip de cada skill.
3. Abre **Agent Builder** (o Teams Toolkit si tu equipo es técnico) y crea un agente declarativo.
4. Agrega cada skill como habilidad personalizada con su carpeta `SKILL.md`.
5. Prueba el agente con una frase de ejemplo: "Quiero priorizar qué procesos automatizar".

## Para el administrador

1. Revisa el agente en el **Centro de administración de Microsoft 365**.
2. Despliégalo a las personas o grupos que participarán en el taller.
3. Confirma que aparece disponible en Copilot para un usuario de prueba.

## Si tu metodología tiene más de 8 skills

Crea más de un agente (por ejemplo uno por etapa) o usa el paquete copiar-pegar en las instrucciones de un agente (nivel 3, menor calidad).
