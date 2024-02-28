from .constantes import Constantes
from .player import Player
from .humanplayer import HumanPlayer
from .computerplayer import ComputerPlayer
# from .roundgame import RoundGame
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
        from .roundgame import RoundGame
        # 1. Inicializar el juego (contruir jugadores,...)
        self.__initGame()

        # 2. Logica principal (Llamar a la ronda, ....)

        # Iterar por cada una de rondas
        os.system('clear')
        categoriaName = Phrase.requestCategory()
        frase = Phrase.getPhrase(category=categoriaName)
        round = RoundGame(self.players, frase)
        while self.rondas > 0:
            round.playRound()
            self.rondas -= 1
        # 3. Finaliza las rondas --> Mostrar Ganador
        self.showWinner()


    def __initGame(self):
        print("""

                ====================================
                BIENVENIDO A LA RULETA DE LA FORTUNA
                ====================================

                """)
        input('Pulsa ENTER para comenzar el juego')
        os.system('clear')
        self.jugadores = int(input('Indica el número de jugadores (2-4): '))
        for i in range(self.jugadores):
            nombre = input(f'Nombre del jugador {i + 1}: ')
            tipo = input(f'¿Es un jugador humano? (s/n): ')
            if tipo == 's':
                self.players.append(HumanPlayer(nombre, 0, 0))
            else:
                self.players.append(ComputerPlayer(nombre, 0, 0))

    def showWinner(self):
        winner = None
        maxPrize = 0
        for player in self.players:
            if player.prizeMoney > maxPrize:
                winner = player
                maxPrize = player.prizeMoney
        print(f'El ganador es {winner.name} con {winner.prizeMoney} €')


