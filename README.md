# Proyecto_Buscaminas_PlataformasAbiertas
## Universidad de Costa Rica
### IE 0117 - Programación Bajo Plataformas Abiertas
Proyecto final de Lenguaje Python
- Manfred Soza Garcia, B97755
- Alexa López Marcos, B94353
- Frank Wang Wu, B57946
  
## Contenido

- [Objetivos](#Objetivos)
- [Introducción](#Introdución)
- [Marco Teórico](#Marco-Teórico)
- [Resultados](#Resultados)
- [Análisis y conclusiones](#Análisis-y-conclusiones)

## Objetivos

### Objetivo general
Aplicar los conocimientos adquiridos a lo largo del curso mediante la creación de un juego usando el lenguaje de programación Python.

### Objetivos específicos
1.Investigar sobre el manejo de las librerías previstas, su aplicación, funcionamiento, y los diferentes códigos a usar.

2.Aplicar las técnicas de programación para el desarrollo de los casos con el fin de determinar si el usuario ganó o no el minijuego.

3.Desarrollar un ambiente amigable con el usuario con el fin de entretener al usuario.


## Introducción
El proyecto consiste en la creación de un juego mediante el lenguaje de programación Python. En dicho proyecto además de repasar los conceptos fundamentales del lenguaje, se aplican principios de programación orientada a objetos y manipulación de interfaces gráficas.
Algunas de las bibliotecas empleadas son **pygame, sys, time, random**. Pygame brinda una experiencia interactiva y atractiva visualmente.

## Marco Teórico

La lógica detrás de la asignación aleatoria de minas, el conteo de minas adyacentes y la expansión recursiva al destapar áreas vacías son elementos esenciales del Buscaminas. Además, la interfaz gráfica proporcionada por Pygame facilita la interacción del usuario con el juego.

En la implementación, se utiliza la orientación a objetos para organizar el código de manera clara y modular. Se han definido clases como Boton, Menu, y Juego para gestionar diferentes aspectos del juego. Además, el código hace uso de conceptos como eventos de mouse, manejo de tiempo, y manipulación de imágenes para crear una experiencia de juego completa.
El juego cuenta con 4 niveles de dificultad, en el que con respecto a la dificultad aumenta el número de la cuadrícula y la cantidad de minas en esta.

Fácil: Será una cuadrícula de 5x5 con 5 minas.

Intermedio: Será una cuadrícula de 10x10 con 20 minas.

Difícil: Será una cuadrícula de 15x15 con 45 minas.

Muy Difícil: Será una cuadrícula de 20x20 con 80 minas.

El script ejecucion.py, cuenta con las siguientes características generales:

-Clase Boton y Clase Menu:
La clase Boton se encarga de representar los botones en la interfaz gráfica del menú. Cada botón tiene propiedades como posición, tamaño, color y texto asociado.
La clase Menu gestiona una lista de botones y proporciona métodos para agregar botones y dibujar el menú en la pantalla.

-Función Modo(texto_boton):
La función Modo recibe el texto de un botón del menú y devuelve el modo de juego correspondiente. Los modos van desde "Fácil" hasta "Muy Difícil".

Función main():
La función principal main inicia el entorno Pygame y presenta el menú principal con opciones de dificultad.
Cuando el usuario selecciona un nivel, se inicializa una instancia del juego (Df.Juego) con el modo elegido.
El juego se ejecuta en un bucle donde se manejan los eventos del mouse para interactuar con la cuadrícula del Buscaminas.
Se gestionan eventos como descubrir celdas, colocar/quitar banderas y mostrar mensajes de victoria o derrota.

En cuanto al script de definicion.py, se puede mencionar lo siguiente:

-Clase Juego:
Inicializa el juego con parámetros como el ancho, alto y modo de juego.
Establece atributos relacionados con la interfaz gráfica de Pygame, como la ventana, fuentes y sonidos.
Gestiona la cuadrícula del juego, incluyendo la colocación de minas y la cuenta de minas adyacentes.
Proporciona métodos para descubrir celdas, colocar/quitar banderas y ejecutar la lógica principal del juego.
HacerCuadricula y MostrarCuadricula:

-HacerCuadricula: 
Crea la cuadrícula del juego y establece las coordenadas de los cuadros.
MostrarCuadricula dibuja la cuadrícula en la ventana Pygame.

-ColocarMinas y safe:
ColocarMinas coloca minas aleatorias en la cuadrícula del juego.
safe garantiza que el primer clic del jugador no sea una mina, reubicando las minas si es necesario.

-ContarCuadros:
Cuenta el número de minas adyacentes a cada cuadro y actualiza un diccionario con esta información.

-Uncover y ejecucion:
Uncover revela el contenido de una celda, mostrando números o minas.
ejecucion ejecuta la lógica principal del juego, revelando celdas y expandiéndose según las reglas del Buscaminas.

-Poner o QuitarBandera:
Coloca o quita banderas en la cuadrícula, actualizando el estado del juego.

-ImpTiempo y MostrarRespuesta:
ImpTiempo muestra el tiempo transcurrido durante el juego.
MostrarRespuesta revela la ubicación de minas y muestra una "X" sobre banderas mal colocadas cuando el jugador pierde

## Resultados

<img src="https://github.com/Alexalopezm/Proyecto_Buscaminas_PlataformasAbiertas/blob/Imagenes/Menu.png" alt="Menu">
<img src="https://github.com/Alexalopezm/Proyecto_Buscaminas_PlataformasAbiertas/blob/Imagenes/Instrucciones.png" alt="Instrucciones de juego">
<img src="https://github.com/Alexalopezm/Proyecto_Buscaminas_PlataformasAbiertas/blob/Imagenes/Celdas.png" alt="Interfaz al iniciar">
<img src="https://github.com/Alexalopezm/Proyecto_Buscaminas_PlataformasAbiertas/blob/Imagenes/CeldasDesbloqueadas.png" alt="Juego en ejecución">


## Análisis y conclusiones
-La implementación del juego Buscaminas en Python con Pygame demuestra la versatilidad de este lenguaje de programación y su capacidad para crear aplicaciones interactivas. 

-El uso de la biblioteca Pygame simplifica la gestión de la interfaz gráfica, permitiendo una representación visual atractiva de la cuadrícula del Buscaminas. 

-El diseño orientado a objetos favorece la reutilización del código y la fácil incorporación de nuevas características en el futuro.
