from .constantes import Constantes
from .player import Player
from .humanplayer import HumanPlayer
from .computerplayer import ComputerPlayer
from .duoPlayer import DuoPlayer
from .frase import Phrase
import os



class Game:

    def __init__(self, jugadores: int, nombre: str, tipo: bool):
        self.jugadores = jugadores
        self.nombre = nombre
        self.tipo = tipo
        self.rondas = Constantes.TOTAL_ROUNDS
        self.players: list[Player] = []

    def start(self):
        """ Método que inicia el juego """
        from .roundgame import RoundGame
        # 1. Inicializar el juego (construir jugadores,...)
        self.__initGame()

        # 2. Lógica principal (Llamar a la ronda, ....)

        # Iterar por cada una de las rondas
        os.system('clear')
        while self.rondas > 0:  # Mientras queden rondas
            categoriaName = Phrase.requestCategory()
            frase = Phrase.getPhrase(category=categoriaName) # Obtener frase
            round = RoundGame(self.players, frase)
            roundResult = round.playRound() # Llamar a la ronda
            if roundResult:  # Si playRound retorna True, se decrementan las rondas
                self.rondas -= 1
        # 3. Finalizan las rondas --> Mostrar Ganador
        self.showWinner()

    def __initGame(self):
        """ Método que inicializa el juego """
        os.system('clear')

        print("""
        =====================================================================================================
                                        BIENVENIDO A LA RULETA DE LA FORTUNA
                                        Creado por: Víctor Manuel Jiménez Sánchez
                                        CE_Python IES Suarez de Figueroa
        =====================================================================================================  
        """)
        input('Pulsa ENTER para comenzar el juego...')

        os.system('clear')
        try:
            num = 1
            self.jugadores = int(input('Indica el número de jugadores (2-4): '))
            if self.jugadores < 2 or self.jugadores > 4:
                print('El número de jugadores debe estar entre 2 y 4')
                self.__initGame()
            for i in range(self.jugadores): # Iterar por cada jugador
                tipo = input(f'¿Es un jugador HUMANO - COMPUTADORA - EQUIPO? (h/c/e): ') # Preguntar si es humano o computadora
                tipo = tipo.lower()
                if tipo == 'h': # Si es humano
                    nombre = input(f'Nombre del jugador {i + 1}: ')
                    self.players.append(HumanPlayer(nombre, 0, 0))
                elif tipo == 'e': # Si es equipo
                    jugadores = []
                    nombreEquipo = input(f'Nombre del equipo: ')
                    while len(jugadores) < 2:
                        nombreJugador = input(f'Nombre del jugador {len(jugadores) + 1}: ')
                        jugadores.append(nombreJugador)
                    self.players.append(DuoPlayer(nombreEquipo, jugadores, 0, 0))
                else: # Si es computadora
                    computadora = 'Computer ' + str(num)
                    self.players.append(ComputerPlayer(computadora, 0, 0))
                    num += 1
        except ValueError:
            print('El número de jugadores debe ser un número entero')
            self.__initGame()

    def showWinner(self):
        """ Método que muestra el ganador del juego """
        winner = None
        maxPrize = 0
        for player in self.players:
            if player.priceMoneyRound > maxPrize:
                winner = player
                maxPrize = player.priceMoneyRound
        os.system('clear')
        print(f'El ganador es {winner.name} con {winner.priceMoneyRound} €')
        print('''
        Gracias por jugar a la Ruleta de la Fortuna
        ''')
        print('Pulse ENTER para salir')
        input()


    def __loadGame(self):
        """ Método que comprueba si existe una partida guardada """
        while True:
            try:
                valor = input('¿Desea cargar una partida existente o craar una nueva? (s/n): ').lower()
                if valor == 's':
                    pass
                elif valor == 'n':
                    return False
                    pass
                else:
                    raise TypeError
            except TypeError:
                print('No se reconoce el caracter')


    def __loadGameCSV(self):
        """ Método que carga una partida guardada en formato CSV """
        try:
            if os.path.exists('~/.ruleta_fortuna/savegame.json'):
                pass
            else:
                raise FileNotFoundError
        except FileNotFoundError as e:
            print('No se ha encontrado ninguna partida guardada', e)


    def __loadGameJSON(self):
        """ Método que carga una partida guardada en formato JSON """
        try:
            if os.path.exists('~/.ruleta_fortuna/savegame.cvs'):
                pass
            else:
                raise FileNotFoundError
        except FileNotFoundError as e:
            print('No se ha encontrado ninguna partida guardada', e)


