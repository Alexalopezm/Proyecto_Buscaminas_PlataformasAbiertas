import random
import time
import pygame


class Juego:
    '''La clase juego contiene todas las funciones necesarias
    para poder realizar la acción de juego, como:
    - Recibir el modo de juego.
    - Colocar las banderas.
    - Colocar los números.
    - Colocar las bombas.
    '''
# Inicializador de la clase. Crea la cuadricula, las minas y los valores de cada cuadro
    def __init__(self, ancho, alto, modo):
        """
        Inicializa una nueva instancia de la clase con los parámetros dados.

        Args:
        - ancho (int): Ancho de la instancia a crear.
        - alto (int): Alto de la instancia a crear.
        - modo (str): Modo de inicialización de la instancia.

        Returns:
        - None: Esta función no retorna un valor específico.
        """
    # Modo de juego
        self.size = modo
        # Ancho de la cuadricula
        self.width = 400//self.size
    # Atributos propios de pygame
        self.p_ancho = ancho
        self.p_alto = alto
        # Numeros
        self.fuente = pygame.font.SysFont('newsorkitalicttf', self.width, True)
        # Tiempo
        self.temp = pygame.font.SysFont('newyorkitalicttf', 20, True)
        # Mensaje de victoria y derrota
        self.msg = pygame.font.SysFont('newyorkitalicttf', 30, True)
        # Ventana y dimensiones
        self.ventana = pygame.display.set_mode((self.p_ancho, self.p_alto))
        pygame.display.set_caption("Buscaminas")
        # Centro de la ventana
        self.centro = self.ventana.get_rect().center
        mina = pygame.image.load("Mina.png")
        # Imagen de la mina
        self.mina = pygame.transform.scale(mina, (self.width, self.width))
        bandera = pygame.image.load("Bandera.png")
        # Imagen de la bandera
        self.bandera = pygame.transform.scale(bandera, (self.width, self.width))
        pygame.mixer.init()
        # Sonido de la explosion
        pygame.mixer.music.load('explosion.mp3')
        # Volumen de sonido
        pygame.mixer.music.set_volume(0.1)

    # Atributos propios del buscaminas
        # Diccionario con coordenadas y color del cuadro
        self.cord = {}
        # Contador de banderas bien colocadas
        self.cont_band = 0
        # Banderas que tiene el jugador
        self.banderas_restantes = 0
        # Banderas maximas que puede tener el jugador
        self.banderas_max = 0
        '''Diccionario con coordenadas y valores
        booleanos que indican la presencia de banderas'''
        self.estado = {}
        # Indica con un booleano si se esta en juego o no
        self.est = True
        # Lista de coordenadas del tablero
        self.cuadricula = []
        self.HacerCuadricula()
        # Diccionario que indica si hay minas o no en una coorenada
        self.minas_d = {}
        self.ColocarMinas()
        # Diccionario con el valor del nimero de minas aledañas a un cuadro
        self.minasA_dt = {}
        self.ContarCuadros()

# Metodo que llena la cuadricula y el diccionario de coordenadas
    def HacerCuadricula(self):
        """
        Método que llena la cuadrícula y el diccionario de coordenadas.

        Este método inicializa la cuadrícula del juego, creando cuadros con sus respectivos colores
        y llenando el diccionario de coordenadas para su posterior utilización.
        """
        # Obitiene la coordenada x para iniciar la cuadricula
        x = self.centro[0] - (self.size * (self.width + 5) / 2)
        # Obtiene la coordenada y para iniciar la cuadricula
        y = self.centro[1] - (self.size * (self.width + 5) / 2)
        for i in range(self.size):
            for j in range(self.size):
                # Crea los cuadros con  su respectivo color
                self.cord[(x, y)] = self.cord.get((x, y), (192, 192, 192))
                # Inicializa los cuadros sin banderas
                self.estado[(x, y)] = False
                self.cuadricula.append((x, y))
                x += self.width + 5
            x -= (self.width + 5) * self.size
            y += self.width + 5

# Metodo que imprime el mapa en pantalla
    def MostrarCuadricula(self):
        """
        Método que imprime el mapa en pantalla.

        Este método dibuja la cuadrícula en la ventana de juego con los colores correspondientes a cada cuadro.
        """
        for i in self.cuadricula:
            color = self.cord.get(i)
            x = i[0]
            y = i[1]
            # Borde superior e izquierdo de cada cuadro
            pygame.draw.polygon(self.ventana, (224, 224, 224),
                                [(x + self.width, y),
                                 (x + self.width + 2.5, y - 2.5),
                                 (x - 2.5, y - 2.5),
                                 (x - 2.5, y + self.width + 2.5),
                                 (x, y + self.width), (x, y)])
            # Borde inferior y derecho de cada cuadro
            pygame.draw.polygon(self.ventana, (96, 96, 96),
                                [(x, y + self.width),
                                 (x - 2.5, y + self.width + 2.5),
                                 (x + self.width + 2.5, y + self.width + 2.5),
                                 (x + self.width + 2.5, y - 2.5),
                                 (x + self.width, y),
                                 (x + self.width, y + self.width)])
            # Cuadros
            pygame.draw.rect(self.ventana, (color),
                             (x, y, self.width, self.width))

# Metodo que asigna minas a una parte de las coordenadas de la cuadricula
    def ColocarMinas(self):
        """
        Método que asigna minas a una parte de las coordenadas de la cuadrícula.

        Este método vacía el diccionario para reasignar en la primera jugada,
        reinicia el número de banderas restantes y máximas, y asigna minas aleatoriamente a las coordenadas de la cuadrícula.

        """
        # Vacia el diccionario para reasignar en la primera jugada
        self.minas_d = {}
        # Reinicia el numero de banderas restantes
        self.banderas_restantes = 0
        # Reinicia el numero de banderas maximas
        self.banderas_max = 0
        for i in self.cuadricula:
            # False indica que no hay mina
            self.minas_d[i] = self.minas_d.get(i, False)
        rng = random.Random()
        while self.banderas_restantes < len(self.minas_d) // 5:
            M = rng.randrange(0, len(self.cuadricula))
            if self.minas_d.get(self.cuadricula[M]) is False:
                # True indica que hay una mina en la posicion M
                self.minas_d[self.cuadricula[M]] = True
                '''Cada que asigna una mina aumenta en 1
                el numero de banderas restantes'''
                self.banderas_restantes += 1
                '''Cada que asigna una mina aumenta en 1
                el numero de banderas maximas'''
                self.banderas_max += 1

# Metodo que mezcla las minas para que el jugador no pierda en el primer turno
    def safe(self, pos):
        """
        Función que verifica si la posición en la que se dio click es un cuadro de la cuadrícula.

        Itera sobre los cuadros de la cuadrícula para identificar si la posición dada está dentro de un cuadro.
        En caso afirmativo, reasigna las minas y cuenta los cuadros hasta que el cuadro donde se presionó no tenga minas alrededor.

        :param pos: Posición del click.
        :return: 1 si se presionó en un cuadro, 0 si no se presionó en un cuadro.
        """
        for i in self.cord:
            '''Revisa si la posicion en la que se dio click
            es un cuadro de la cuadricula o no'''
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                '''Vuelve a asignar las minas y a contar los cuadros hasta que
                el cuadro en que se presiono no tenga minas alrededor'''
                while self.minasA_dt[i] != 0:
                    self.ColocarMinas()
                    self.ContarCuadros()
                return 1  # Si se presiono en un cuadro
        return 0  # Si no se presiono un cuadro

    def ContarCuadros(self):
        """
        Método que cuenta las minas que están alrededor de algún cuadro.

        Este método reinicia el diccionario para reasignar en la primera jugada y
        recorre la cuadrícula para contar las minas adyacentes a cada cuadro.
        """
        # Reinicia el diccionario para reasignar en la primera jugada
        self.minasA_dt = {}
        # Contador que avanza por la cuadrícula
        counter = 0

        for cord, has_mine in self.minas_d.items():
            # Contador de minas adyacentes
            minasC = 0

            if has_mine:
                self.minasA_dt[cord] = True

            else:
                for dx in [-self.width - 5, 0, self.width + 5]:
                    for dy in [-self.width - 5, 0, self.width + 5]:
                        c1 = cord[0]
                        c2 = cord[1]
                        v = (c1 + dx, c2 + dy)
                        if v != cord and v in self.minas_d and self.minas_d[v]:
                            minasC += 1

                self.minasA_dt[cord] = minasC

            # Avanza al siguiente cuadro
            counter += 1

# Metodo que destapa una casilla del mapa
    def uncover(self, i):
        """
        Función que destapa un cuadro y muestra su valor en la cuadrícula.

        :param i: Posición del cuadro a destapar.
        """
        val = self.minasA_dt.get(i)
        pos = [i[0] + (self.width // 5), i[1]]
        self.cord[i] = (96, 96, 96)
        self.MostrarCuadricula()

        # Mapeo de valores a colores
        colors = {
            1: (0, 128, 255),
            2: (0, 204, 0),
            3: (255, 0, 0),
            4: (0, 0, 204),
            5: (102, 51, 0),
            6: (0, 255, 255),
            7: (51, 0, 0),
            8: (64, 64, 64),
            9: (0, 0, 0)
        }

        if str(val) in map(str, colors.keys()):
            val = self.fuente.render(str(val), 1, colors[int(val)])
            self.ventana.blit(val, pos)

        if i in self.cuadricula:
            self.cuadricula.remove(i)

    def PonerOQuitarBandera(self, pos):
        """
        Método que coloca o quita banderas en el mapa

        :param pos: Posición del cuadro seleccionado.
        """
        for i in self.cord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                # Obtiene la posicion sobre la que se pondra la bandera
                pos = [i[0], i[1]]
                # Si el cuadro no tiene bandera
                if self.estado[i] is False:
                    # No hace nada si no quedan banderas
                    if self.banderas_restantes != 0:
                        # Si no se ha descubierto el cuadro se ejecuta
                        if i in self.cuadricula:
                            # Elimina la posicion de la cuadricula
                            # para que no se pueda destapar
                            self.cuadricula.remove(i)
                            # Muestra la bandera
                            self.ventana.blit(self.bandera, pos)
                            # Resta 1 a las banderas del usuario
                            self.banderas_restantes -= 1
                            # Actualiza el estado a tener una bandera
                            self.estado[i] = True
                        if self.minasA_dt[i] is True:
                            '''Si habia una mina en el lugar
                            le suma 1 al contador final'''
                            self.cont_band += 1
                        break
                # Si el cuadro tiene bandera
                else:
                    # Vuelve a incluir el cuadro en la lista de cuadricula
                    self.cuadricula.append(i)
                    # Le suma 1 a las banderas restantes
                    self.banderas_restantes += 1
                    # Actualiza el estado a no tener bandera
                    self.estado[i] = False
                    '''Compara con el valor de la mina
                    se debe convertir a str para que
                    no cuente los 1 como true'''
                    if str(self.minasA_dt[i]) == "True":
                        self.cont_band -= 1
                    break

    def ejecucion(self, pos):
        """
        Método que lleva a cabo la acción principal.

        :param pos: Posición del cuadro seleccionado.
        """
        for i in self.cord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                # Solo abre si en el cuadro no hay bandera
                if self.estado[i] is not True:
                    # Si se oprimio una mina
                    if self.minas_d[i] is True:
                        # Obtiene la posicion para poner la mina
                        pos = [i[0], i[1]]
                        # Pone la mina en la ventana
                        self.ventana.blit(self.mina, pos)
                        pygame.mixer.music.play()
                        # Hace que el juego se deje de ejecutar
                        self.est = False
                    else:
                        # Destapa el cuadro
                        self.uncover(i)
                        # Si no hay minas aledañas
                        if self.minasA_dt[i] == 0:
                            # Convierte el 0 a str para que no lo vuelva a leer como 0
                            self.minasA_dt[i] = "0"
                            '''Revisa los valores alrededor en el mismo orden que la funcion
                            contar cuadros los destapa y revisa su valor para
                            expandir como el buscaminas clasico'''

                            if (i[0] + self.width + 5, i[1]) in self.minasA_dt:
                                a = self.minasA_dt[(i[0] + self.width + 5, i[1])]
                                self.uncover((i[0] + self.width + 5, i[1]))
                                if a == 0:
                                    self.ejecucion((i[0] + self.width + 5, i[1]))
                            if (i[0] + self.width + 5, i[1] + self.width + 5) in self.minas_d:
                                a = self.minasA_dt[(i[0] + self.width + 5, i[1] + self.width + 5)]
                                self.uncover((i[0] + self.width + 5, i[1] + self.width + 5))
                                if a == 0:
                                    self.ejecucion((i[0] + self.width + 5, i[1] + self.width + 5))
                            if (i[0], i[1] + self.width + 5) in self.minasA_dt:
                                a = self.minasA_dt[(i[0], i[1] + self.width + 5)]
                                self.uncover((i[0], i[1] + self.width + 5))
                                if a == 0:
                                    self.ejecucion((i[0], i[1] + self.width + 5))
                            if (i[0] - self.width - 5, i[1] + self.width + 5) in self.minas_d:
                                a = self.minasA_dt[(i[0] - self.width - 5, i[1] + self.width + 5)]
                                self.uncover((i[0] - self.width - 5, i[1] + self.width + 5))
                                if a == 0:
                                    self.ejecucion((i[0] - self.width - 5, i[1] + self.width + 5))
                            if (i[0] - self.width - 5, i[1]) in self.minasA_dt:
                                a = self.minasA_dt[(i[0] - self.width - 5, i[1])]
                                self.uncover((i[0] - self.width - 5, i[1]))
                                if a == 0:
                                    self.ejecucion((i[0] - self.width - 5, i[1]))
                            if (i[0] - self.width - 5, i[1] - self.width - 5) in self.minas_d:
                                a = self.minasA_dt[(i[0] - self.width - 5, i[1] - self.width - 5)]
                                self.uncover((i[0] - self.width - 5, i[1] - self.width - 5))
                                if a == 0:
                                    self.ejecucion((i[0] - self.width - 5, i[1] - self.width - 5))
                            if (i[0], i[1] - self.width - 5) in self.minasA_dt:
                                a = self.minasA_dt[(i[0], i[1] - self.width - 5)]
                                self.uncover((i[0], i[1] - self.width - 5))
                                if a == 0:
                                    self.ejecucion((i[0], i[1] - self.width - 5))
                            if (i[0] + self.width + 5, i[1] - self.width - 5) in self.minas_d:
                                a = self.minasA_dt[(i[0] + self.width + 5, i[1] - self.width - 5)]
                                self.uncover((i[0] + self.width + 5, i[1] - self.width - 5))
                                if a == 0:
                                    self.ejecucion((i[0] + self.width + 5, i[1] - self.width - 5))
                break


    def ImpTiempo(self, t1):
        """
        Método que muestra el tiempo que lleva el usuario.

        :param t1: Tiempo inicial.
        """
        # Posicion del tiempo: Abajo en el centro
        pos = (self.centro[0] - 200, self.centro[1] +
               (self.width + 5) * (self.size/2) + 15)
        t2 = time.perf_counter()
        t = str(int(t2-t1))
        # Crea el mensaje que muestra el tiempo
        t = self.temp.render("Tiempo : {0} sec".format(t), 1, (255, 255, 0))
        # Dibuja un fondo negro para que no se sobreponga
        pygame.draw.rect(self.ventana, (0, 0, 0),
                         (pos[0], pos[1], 200, self.width))
        # Dibuja el mensaje
        self.ventana.blit(t, (pos))


# Metodo que muestra la solucion si el jugador pierde
    def MostrarRespuesta(self):
        '''
        Método que muestra la solución si el jugador pierde
        '''
        for i in self.minas_d:
            '''Dibuja una mina si el cuadro tiene
            y si no hay bandera en el cuadro'''
            if self.minas_d[i] is True and self.estado[i] is False:
                pos = [i[0], i[1]]
                self.ventana.blit(self.mina, pos)
            if self.estado[i] is True and self.minas_d[i] is False:
                # Dibuja una x sobre una bandera mal puesta
                pygame.draw.line(self.ventana, (0, 0, 0), (i[0], i[1]),
                                 (i[0] + self.width, i[1] + self.width), (5))
                pygame.draw.line(self.ventana, (0, 0, 0),
                                 (i[0] + self.width, i[1]),
                                 (i[0], i[1] + self.width), (5))
