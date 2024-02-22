from .constantes import Constantes
from .humanplayer import HumanPlayer
from .computerplayer import ComputerPlayer


class Game:
    def __init__(self, jugadores: int, nombre: str, tipo: bool):
        self.jugadores = jugadores
        self.nombre = nombre
        self.tipo = tipo
        self.rondas = Constantes.TOTAL_ROUNDS
        self.players = []

    def start(self):
        print("""

        ====================================
        BIENVENIDO A LA RULETA DE LA FORTUNA
        ====================================

        """)
        input('Pulsa ENTER para comenzar el juego')
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
        print(f'El ganador es {winner.name} con {winner.prizeMoney} puntos')

    # def loadGame(self):
    #     with open(os.path.expanduser('~/.ruleta_fortuna/savegame.json'), 'r') as file:
    #         data = json.load(file)
    #         self.jugadores = data['jugadores']
    #         self.nombre = data['nombre']
    #         self.tipo = data['tipo']
    #         self.rondas = data['rondas']
    #         self.players = data[HumanPlayer(**player) if player['tipo'] == 's' else ComputerPlayer(**player) for player in data['players']]
    #
    # def saveGame(self):
    #     data = {
    #         'jugadores': self.jugadores,
    #         'nombre': self.nombre,
    #         'tipo': self.tipo,
    #         'rondas': self.rondas,
    #         'players': [player.__dict__ for player in self.players]
    #     }
    #     with open(os.path.expanduser('~/.ruleta_fortuna/savegame.json'), 'w') as file:
    #         json.dump(data, file)