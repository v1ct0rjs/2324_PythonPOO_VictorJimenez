# Tarea Evaluable 2.2. Ruleta de la Fortuna. Guardar partida

Siguiendo con el desarrollo de la tarea evaluable 2.1, se pide añadir la funcionalidad de guardar y cargar la partida en un fichero, tanto en formato CSV como JSON.

## Enunciado

El juego debe permitir guardar de una forma automática, cada vez que se finaliza una ronda.
También a la hora de cargar el juego, debe comprobar si existe un fichero de guardado, y preguntar al usuario si desea continuar la partida o empezar una nueva.

- En caso de que el usuario decida continuar la partida, debe cargar la partida guardada.
- En caso de que el usuario decida empezar una nueva partida, debe borrar el fichero de guardado.
- La partida se irá guardando de forma automática, cada vez que se finaliza una ronda. Cuando se finaliza el juego, se borra el fichero de guardado.

## Especificaciones

La partida se puede guardar tanto en formato CSV como JSON. El formato de guardado es libre, pero debe contener la información necesaria para continuar la partida.

- Formato-Fichero: Enumerado que indique el tipo fichero. CSV y JSon.
- En constantes:

  - PARTIDA_SAVE_FILENAME: Nombre del fichero donde se guarda la partida. La extensión del fichero dependerá del formato elegido.
  - PARTIDA_SAVE_FORMAT: Formato de guardado de la partida. (CSV o JSON)

- Clases:
  - Game: Agregar lógica para cargar el estado del juego desde un fichero.
  - Player: Añadir método inicialización stático que cargue la ronda desde diferentes parámetros. `Player.FromSavedPlayer()` -> Como es abstracta, se debe implementar en las clases hijas.
  - RoundGame: Añadir método inicialización stático que cargue la ronda desde diferentes parámetros. `RoundGame.FromSavedRound()` (Aunque no es necesario, pero para practicar el patrón `ConstructorNombrado`)

### Objetivos

- Aplicar los conceptos de manejor de ficheros aprendidos en el curso a un caso práctico.
- Conocer como guardar y cargar información en formato CSV y JSON.
- Aplicar trabajo con ficheros en formato CSV y JSON.

## Tareaa a desarrollar

El juego almacena los datos dentro de una carpeta llamada ".ruleta_fortuna" en el home del usuario. Dentro de esta carpeta se almacena un fichero con la información de la partida guardada.
El nombre del fichero de la partida guardada puede ser cualquiera, pero debe estar

### Formatos

Se debe crear un fichero de documentación en markdown, que explique el formato de guardado de la partida en formato CSV y JSON.

Los puntos que debe tener el fichero son los siguientes:

- Introducción: Explica brevemente el propósito del documento.
- Formato CSV:

  - Indicar el nombre de las columnas (formato lista), explicando de qué tipo es el dato y el contenido que almacena.
  - Ejemplo de un registro (incluyendo el nombre de las columnas)

- Formato JSON:
  - Explicar la estructura del fichero JSON.
  - Ejemplo de un registro.

Datos oligatorios a guardar:

- Nombre del jugador
- Dinero acumulado del jugador, tanto a nivel de la ronda como total.
- Nº de Ronda actual
- Frase actual de la ronda
- Turno del jugador

### Métodos

**Game:**

`__loadGame()`: Método que carga la partida de un fichero.

Si se detecta un fichero en la ruta `FOLDER_DATA\PARTIDA_SAVE_FILENAME`, se debe preguntar al usuario si desea continuar la partida o empezar una nueva.

- Métodod privado: `__loadGameCSV()`: Método específico para el formato CSV.
- Métodod privado: `__loadGameJSON()`: Método específico para el formato JSON.

Este metodo de cargar el estado del juego como si se hubiera iniciado desde el principio, pero con los datos de la partida guardada.

### Formato CSV

Este formato tabular, donde cada fila representa un registro, y cada columna un campo del registro. <br>
El formato es libre (nº de campos y posición), pero la 1ª columna debe contener los nombres de las columnas, y el resto de filas el contenido de las mismas.

### Formato JSON

El formato JSON es un formato estructurado, donde la información no se almacena de forma tabular, sino de una forma jerárquica. <br>
