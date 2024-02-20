from enum import Enum
import random
import abc
import json
import os
from frases import frases


class Constantes(Enum):
    TOTAL_ROUNDS = 3
    VOCAL_PRECIO = 250
    RECOMPENSA_PANEL = 500


class Game:
    def __init__(self, jugadores: int, nombre: str, tipo: bool, rondas: Constantes):
        self.jugadores = jugadores
        self.nombre = nombre
        self.tipo = tipo
        self.rondas = rondas.TOTAL_ROUNDS
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
            nombre = input(f'Nombre del jugador {i+1}: ')
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


class Player:
    def __init__(self, name: str, prizeMoney: float, priceMoneyRound: float):
        self.name = name
        self.prizeMoney = prizeMoney
        self.priceMoneyRound = priceMoneyRound


    def addMoney(self, amt: float):
        self.prizeMoney += amt


    def applyBankrupt(self):
        self.priceMoneyRound = 0


    def addPrizeRound(self, prize: float):
        self.prizeMoney += prize


    def applyWinRound(self):
        self.priceMoneyRound += self.prizeMoney

    @abc.abstractmethod
    def goMove(self):
        pass

    def __str__(self):
        return f'{self.name}: {self.prizeMoney}'


class HumanPlayer(Player):
    def __init__(self, name: str, prizeMoney: float, priceMoneyRound: float):
        super().__init__(name, prizeMoney, priceMoneyRound)
        self.name = name
        self.prizeMoney = prizeMoney
        self.priceMoneyRound = priceMoneyRound

    def goMove(self):
        tirada = Ruleta.girar()
        if tirada == -1:
            self.applyBankrupt()
            return "Quiebra"
        elif tirada == 0:
            return "Pierde turno"
        else:
            self.addMoney(tirada)
            return f'Ha ganado {tirada} €'

class ComputerPlayer(Player):
    def __init__(self, name: str, prizeMoney: float, priceMoneyRound: float):
        super().__init__(name, prizeMoney, priceMoneyRound)
        self.name = 'Computer'
        self.prizeMoney = prizeMoney
        self.priceMoneyRound = priceMoneyRound

    def goMove(self):
        pass

class Ruleta():

    valores = [100, 50, 100, 150, 50, 200, 250, 50, 100, 150, 300, -1, 400, 0, 500, 200, 100, 50, 250, 150, 100, 50, 200]
    @staticmethod
    def girar() -> int:
        tirada = random.choice(Ruleta.valores)
        return tirada

class RoundGame():

    def __init__(self):

        pass


