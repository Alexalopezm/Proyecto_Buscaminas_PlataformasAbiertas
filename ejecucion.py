'''
Este módulo de código contiene la sección de ejecución,
la cual se encarga de generar el menú y ejecutar el juego
en el modo seleccionado por el usuario
'''
import pygame
import sys
import time
import definicion as Df

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (150, 150, 150)


class Boton:
    def __init__(self, x, y, ancho, alto, color, texto=''):
        """
        Inicializa un objeto Botón con su posición, dimensiones, color y texto (opcional).

        Args:
        - x: Coordenada x del botón.
        - y: Coordenada y del botón.
        - ancho: Ancho del botón.
        - alto: Alto del botón.
        - color: Color del botón en formato RGB o RGBA.
        - texto: Texto que se muestra en el botón (opcional).
        """
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color
        self.texto = texto

    def dibujar(self, pantalla, outline=None):
        """
        Dibuja un botón en la pantalla con un posible borde.

        Args:
        - pantalla: La ventana de Pygame donde se dibujará el botón.
        - outline: El color del borde del botón (opcional). Si se proporciona,
                se dibuja un borde con este color alrededor del botón.
        """
        if outline:
            pygame.draw.rect(pantalla, outline, self.rect, 0)

        pygame.draw.rect(pantalla, self.color, self.rect)

        if self.texto != '':
            fuente = pygame.font.Font(None, 36)
            texto = fuente.render(self.texto, True, NEGRO)
            texto_rect = texto.get_rect(center=self.rect.center)
            pantalla.blit(texto, texto_rect)


class Menu:
    def __init__(self):
        self.botones = []

    def agregar_boton(self, boton):
        self.botones.append(boton)

    def mostrar_instrucciones(pantalla):
        """
        Muestra las instrucciones del juego en la pantalla.

        Args:
        - pantalla: La ventana de Pygame donde se mostrarán las instrucciones.
        """
        instrucciones = True
        tiempo_inicio = pygame.time.get_ticks()
    
        # Texto de las instrucciones
        texto_instrucciones = [
            "Instrucciones del Buscaminas:",
            "",
            "1. El objetivo del juego es despejar el campo de juego",
            "   sin detonar ninguna mina.",
            "2. Haz clic izquierdo para revelar una celda.",
            "3. Haz clic derecho para colocar o quitar una bandera ",
            "   en una celda sospechosa.",
            "4. Cada número en una celda indica la cantidad de minas",
            "   adyacentes a esa celda.",
            "5. Si revelas una mina, pierdes el juego.",
            "",
            "¡Buena suerte!  ^ ^"
        ]
    
        # Definir la fuente y el tamaño del texto
        fuente_instrucciones = pygame.font.Font(None, 30)
    
        while instrucciones:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            tiempo_actual = pygame.time.get_ticks()
            pantalla.fill(NEGRO)  # Limpiar la pantalla
    
            # Mostrar el texto de las instrucciones en la ventana
            y_pos = 100
            for linea in texto_instrucciones:
                texto = fuente_instrucciones.render(linea, True, BLANCO)
                pantalla.blit(texto, (50, y_pos))
                y_pos += 30  # Espacio entre líneas
    
            if tiempo_actual - tiempo_inicio >= 30000:  # 30 segundos = 30000 milisegundos
                # Si han pasado 30 segundos, salir del bucle y volver al menú principal
                instrucciones = False
    
            pygame.display.update()
 
 
    def dibujar(self, pantalla):
        """
        Dibuja la interfaz del menú en la pantalla.

        Args:
        - pantalla: La ventana de Pygame donde se dibujará el menú.
        """
        ANCHO, ALTO = 700, 600
        pantalla.fill(NEGRO)
        fuente_titulo = pygame.font.Font(None, 60)
        texto_titulo = fuente_titulo.render('Buscaminas', True, BLANCO)
        texto_titulo_rect = texto_titulo.get_rect(center=(ANCHO/2, 50))
        pantalla.blit(texto_titulo, texto_titulo_rect)

        fuente_subtitulo = pygame.font.Font(None, 36)
        texto_subtitulo = fuente_subtitulo.render('Niveles', True, BLANCO)
        texto_subtitulo_rect = texto_subtitulo.get_rect(center=(ANCHO/2, 220))
        pantalla.blit(texto_subtitulo, texto_subtitulo_rect)

        espacios_entre_botones = [10, 70, 20, 20, 20, 60]  # Lista de espacios entre botones
        y_inicial = 120

        for i, espacio in enumerate(espacios_entre_botones):
            if i == 0:
                y_inicial += espacio
            else:
                y_inicial += self.botones[i - 1].rect.height + espacio

            self.botones[i].rect.centerx = ANCHO // 2
            self.botones[i].rect.y = y_inicial
            self.botones[i].dibujar(pantalla, NEGRO)

def Modo(texto_boton):
    """
    Determina el modo de juego seleccionado según el texto del botón.

    Args:
    - texto_boton: El texto asociado al botón presionado.

    Returns:
    - modo: El nivel de dificultad seleccionado para el juego.
    """
    if texto_boton == "Salir":
        pygame.quit()
        sys.exit()
    elif texto_boton == "Fácil":
        modo = 5
    elif texto_boton == "Intermedio":
        modo = 10
    elif texto_boton == "Difícil":
        modo = 15
    elif texto_boton == "Muy Difícil":
        modo = 20
    return modo


def main():
    """
    Función principal que ejecuta el juego Buscaminas.

    Esta función inicializa Pygame, crea la ventana del juego, configura el menú, y controla la lógica del juego
    a través de interacciones del usuario con los botones del menú y las acciones en la pantalla de juego.
    """
    pygame.init()
    m = 0
    pantalla = pygame.display.set_mode((700, 600))
    pygame.display.set_caption('Buscaminas')

    menu = Menu()
    menu.agregar_boton(Boton(0, 0, 200, 40, GRIS, 'Instrucciones'))
    menu.agregar_boton(Boton(0, 0, 200, 40, GRIS, 'Fácil'))
    menu.agregar_boton(Boton(0, 0, 200, 40, GRIS, 'Intermedio'))
    menu.agregar_boton(Boton(0, 0, 200, 40, GRIS, 'Difícil'))
    menu.agregar_boton(Boton(0, 0, 200, 40, GRIS, 'Muy Difícil'))
    menu.agregar_boton(Boton(0, 0, 200, 40, GRIS, 'Salir'))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = pygame.mouse.get_pos()
                for boton in menu.botones:
                    if boton.rect.collidepoint(pos):
                        if boton.texto == 'Instrucciones':
                            pantalla.fill(NEGRO)
                            Menu.mostrar_instrucciones(pantalla)
                        else:
                            nivel_elegido = Modo(boton.texto)
                            if nivel_elegido != "Salir": 
                                juego = Df.Juego(700, 600, nivel_elegido)
                                t1 = time.perf_counter()
                                juega = True
                                # Posición de los mensajes arriba de la cuadrícula
                                pos_arriba = (juego.centro[0] - 75, juego.centro[1] - (juego.width + 5) * (juego.size/2) - 40)
                                pos_abajo = (juego.centro[0], juego.centro[1] + (juego.width + 5) * (juego.size/2) + 15)
                                run = True
                                while run:
                                    juego.MostrarCuadricula()
                                    # Lee los eventos
                                    event = pygame.event.poll()
                                    if event.type == pygame.QUIT:
                                        # Termina el ciclo
                                        run = False
                                    if event.type == pygame.MOUSEBUTTONDOWN and juega:
                                        # Lee la posición del mouse
                                        pos = event.dict['pos']
                                        if event.button == 1:
                                            if m == 0:
                                                # Ejecuta el método safe, si se ejecuta adecuadamente retorna 1 y no se vuelve a hacer
                                                m = juego.safe(pos)
                                            juego.ejecucion(pos)
                                        if event.button == 3:
                                            juego.PonerOQuitarBandera(pos)

                                    # Mensaje de las banderas restantes
                                    msg_banderas = juego.temp.render("Banderas: {0}".format(juego.banderas_restantes), 1, (255, 255, 0))
                                    # Fondo del mensaje
                                    pygame.draw.rect(juego.ventana, (0, 0, 0), (pos_abajo[0] + 100, pos_abajo[1], juego.width * 20, 30))
                                    # Imprime el mensaje
                                    juego.ventana.blit(msg_banderas, (pos_abajo[0] + 100, pos_abajo[1]))
                                    # Si todas las banderas estan bien colodadas
                                    if juego.cont_band == juego.banderas_max:
                                        # Mensaje de victoria
                                        msg = juego.msg.render("Victoria", 1, (255, 255, 0))
                                        # Imprime el fondo del mensaje
                                        pygame.draw.rect(juego.ventana, (0, 0, 0), (pos_arriba[0], pos_arriba[1], juego.width * 10, 30))
                                        # Imprime el mensaje
                                        juego.ventana.blit(msg, pos_arriba)
                                        # Actualiza por última vez
                                        pygame.display.update()
                                        juega = False
                                        time.sleep(5)
                                        if juega is False:
                                            # Hace que deje de leer clicks en la cuadrícula
                                            return main()

                                    # Si clickeo una mina
                                    elif not juego.est:
                                        # Mensaje de derrota
                                        msg = juego.msg.render("Perdiste", 1, (255, 255, 0))
                                        # Imprime el fondo del mensaje
                                        pygame.draw.rect(juego.ventana, (0, 0, 0), (pos_arriba[0], pos_arriba[1], juego.width * 10, 30))
                                        # Imprime el mensaje
                                        juego.ventana.blit(msg, pos_arriba)
                                        juego.MostrarRespuesta()
                                        # Actualiza por última vez
                                        pygame.display.update()
                                        juega = False
                                        time.sleep(5)
                                        if juega is False:
                                            # Hace que deje de leer clicks en la cuadrícula
                                            return main()

                                    else:
                                        juego.ImpTiempo(t1)
                                        pygame.display.update()
                                pygame.quit()

        menu.dibujar(pantalla)
        pygame.display.flip()


if __name__ == "__main__":
    main()
