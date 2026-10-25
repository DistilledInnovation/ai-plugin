# Herramientas para crear una skill de flujo

Nota de fuente: la entrevista, la separación entre pasos de lectura y pasos que modifican sistemas, la aprobación del diseño antes de construir y la prueba segura provienen del flujo de creación de skills propias de la metodología de Distilled Innovation; la plantilla y la lista de revisión siguen el estándar de este repositorio.

## 1. Qué tareas sí y cuáles no

| Buena candidata | Mala candidata |
|---|---|
| Se repite cada semana o cada día | Ocurre una vez al año |
| Los pasos se pueden escribir | Depende del criterio en cada caso |
| Las entradas son archivos o datos conocidos | Las entradas cambian de forma impredecible |
| El resultado es un borrador, una lista o un resumen | Termina en una acción irreversible |
| Una persona puede verificar el resultado en minutos | Nadie podría notar un error |

Si la tarea toca a personas externas, dinero o decisiones de alto impacto, no es una skill personal: pasa por la metodología.

## 2. Clasificar cada paso

| Clase | Qué es | Aprobación |
|---|---|---|
| Solo lectura | Abre, mira, compara, calcula; no cambia nada | No hace falta |
| Local | Crea o cambia un borrador o un archivo propio | Se muestra el resultado antes de usarlo |
| Modifica algo externo | Envía, publica, compra, elimina, registra o cambia un sistema | **Siempre**: la persona aprueba antes, y la skill lo dice |

Regla: ante la duda, trátalo como "modifica algo externo".

## 3. Contradicciones y riesgos frecuentes

| Se oye | Señal |
|---|---|
| "Que lo mande solo, pero revísalo antes" | Contradicción: ¿se envía solo o con aprobación? Se resuelve con aprobación |
| "Los datos están en varias hojas" | Dependencia sin dueño: ¿cuál es la fuente? |
| "A veces hay filas vacías" | Caso de borde que debe estar en "Si algo falla" |
| "Usa mi clave de..." | Credencial: nunca se guarda; se usa el acceso ya configurado |
| "Y de paso también hace..." | Alcance: son dos skills |

## 4. Credenciales y privacidad

- La skill no contiene contraseñas, claves, tokens ni datos de personas, ni en el texto ni en los ejemplos.
- El acceso a servicios se describe como dependencia ("necesita poder leer la hoja de inventario"), no como conexión.
- Si el asistente de la persona no tiene el acceso, la skill se detiene y lo dice.

## 5. La descripción de la skill

Estructura: qué hace + resultado que entrega + "Úsala cuando" + de 3 a 5 frases reales de la persona (tal como las escribiría). Máximo 1.024 caracteres. Prueba: ¿una persona que no conoce la skill sabría cuándo activarla?

## 6. Errores frecuentes

| Error | Cómo se evita |
|---|---|
| Construir antes de que el diseño esté aprobado | Pedir un sí explícito |
| Una skill que hace tres tareas | Dividir en tres |
| Aprobaciones olvidadas al escribir | Revisar la tabla "Puntos de aprobación" contra el diseño |
| Probar con datos reales | Muestra inventada y paso final detenido en el borrador |
| Dar por bueno un resultado cuando falta una dependencia | Detener la prueba y decirlo |
