# Herramientas del proceso de ventas y pipeline

## 1. Cómo diseñar las etapas

1. Parte del mapa as-is: los pasos que ya existen en la práctica.
2. Para cada paso, pregunta: "¿qué hecho observable demuestra que se completó?". Ese hecho es la regla de entrada de la etapa siguiente.
3. Revisa que cada etapa **discrimine**: que cambie lo que se hace, lo que se mide o quién actúa. Si no, se fusiona con otra.
4. Define el dato obligatorio: el mínimo que debe estar anotado para entrar a la etapa. Pocos campos; los demás son opcionales.
5. Fija un tiempo máximo por etapa a partir de lo medido en la etapa 0, no de un deseo.
6. Prueba con tres oportunidades reales: ganada, perdida y abierta. Cada una debe caer en una sola etapa.

## 2. Reglas de entrada que se pueden verificar

| Evita (sensación) | Usa (hecho) |
|---|---|
| "Parece interesado" | El cliente respondió y acordó una fecha de reunión |
| "Va bien" | El decisor vio la propuesta y se fijó la siguiente acción con fecha |
| "Casi lo cerramos" | Se conocen condiciones, decisores y fecha esperada de decisión |

## 3. Siguiente paso y estancamiento

- Toda oportunidad abierta tiene siguiente acción con fecha; el siguiente paso describe algo que **hará alguien** (no "esperar").
- Estancada: sin avance durante el umbral acordado (por ejemplo, 14 días) o sin siguiente paso fechado.
- Qué hacer con una estancada: contactar con un motivo nuevo, proponer cerrar el ciclo ("¿cierro esta conversación?") o marcarla perdida con motivo "sin respuesta". Nunca se deja abierta por inercia.

## 4. Motivos de pérdida

Lista corta y cerrada (para poder contar): precio, no era el perfil, eligió a otro proveedor, momento no adecuado, sin respuesta, otro (con texto). Se registra la frase del cliente. Cada mes se revisa la distribución: es la entrada del ciclo 7 a 1 (aprendizaje de mercado) y 7 a 3 (fricción de proceso).

## 5. Calificación: cómo usar BANT y MEDDICC

- **BANT simplificado** (y MEDDICC después) son marcos de calificación de ventas muy usados y de uso general, no una invención de esta metodología. Se puntúa con lo que el cliente dijo, no con lo que se supone. Cada criterio en Sí (2), Parcial (1) o No (0). La regla de decisión escrita evita discutir caso por caso.
- **Cuándo sumar MEDDICC**: ventas con varios decisores, ciclo mayor a unos dos meses o ticket alto. Se agregan como notas de la oportunidad: métricas, comprador económico, criterios de decisión, proceso de decisión, identificación del dolor, campeón y competencia (incluida la opción de no hacer nada).
- **Revisión**: cada mes compara la tasa de cierre de calificadas contra no calificadas. Si no hay diferencia, la regla no discrimina.

## 6. Adaptar a otros tipos de venta

| Tipo | Ajuste |
|---|---|
| B2B consultiva (ciclo largo, varios actores) | Más etapas, mapa de actores y preguntas MEDDICC |
| B2B de ciclo corto | Fundir descubrimiento y calificación, y propuesta y negociación |
| B2C de ciclo corto | Tres o cuatro etapas (interés, oferta, decisión, resultado); la calificación se reduce a necesidad y tiempo |
| Colectivo (modalidad C) | Un pipeline modelo de cuatro a cinco etapas que cada miembro lleve en una hoja |

## 7. Mínimo viable en una hoja de cálculo

Mientras no exista un registro más completo (etapa 4, `crm-y-tableros`), el proceso puede empezar en una hoja con una fila por oportunidad. No es una herramienta recomendada: es un formato.

| Columna | Qué guarda | Obligatoria desde la etapa |
|---|---|---|
| ID de oportunidad (`OPO-nn`) | Identificador estable | ETA-01 |
| Cuenta | Nombre o descripción | ETA-01 |
| Segmento / ICP | `SEG-nn` / `ICP-nn` | ETA-01 |
| Origen | Canal o persona que refirió | ETA-01 |
| Responsable | Quién lleva la oportunidad | ETA-01 |
| Etapa (`ETA-nn`) | Etapa actual | ETA-01 |
| Contacto y actor (`ACT-nn`) | Con quién se habla y su rol | ETA-02 |
| Dolor | Problema declarado | ETA-03 |
| Puntaje BANT | Total de 8 | ETA-03 |
| Importe | Valor mensual o del contrato | ETA-05 |
| Fecha estimada de decisión | | ETA-06 |
| Último contacto | Fecha | ETA-02 |
| Siguiente paso y fecha | Qué hará quién y cuándo | Siempre |
| Resultado y motivo de pérdida | Ganada o perdida y por qué | ETA-07 |

Con estas columnas se pueden calcular a mano los KPIs de conversión, ciclo, estancadas e higiene de la línea base. Una vista de "siguiente paso vencido" (filtro por fecha) cumple la función de alerta.

## 8. Prueba de la persona nueva

1. Elige a alguien que no participó en el diseño.
2. Entrégale el manual corto, sin explicación.
3. Pídele que explique con sus palabras cómo se vende y qué cuenta como avance, y que ubique tres oportunidades reales en las etapas.
4. Lo que confunda indica una definición floja: se corrige la definición, no a la persona.
