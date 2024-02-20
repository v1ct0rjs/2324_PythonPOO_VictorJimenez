from enum import Enum
import random
import abc
#import frases
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

    def start(self):
        print("""
        
        ====================================
        BIENVENIDO A LA RULETA DE LA FORTUNA
        ====================================
        
        """)
        input('Pulsa ENTER para comenzar el juego')
        self.jugadores = int(input('Indica el número de jugadores (2-4): '))
        pass

    def showWinner(self):
        pass

    def loadGame(self):
        pass

    def saveGame(self):
        pass


class Player:
    def __init__(self, name: str, prizeMoney: float, priceMoneyRound: float):
        self.name = name
        self.prizeMoney = prizeMoney
        self.priceMoneyRound = priceMoneyRound

    @abc.abstractmethod
    def addMoney(self, amt: float):
        pass

    @abc.abstractmethod
    def applyBankrupt(self):
        pass

    @abc.abstractmethod
    def addPrizeRouund(self, prize: float):
        pass

    @abc.abstractmethod
    def applyWinRound(self):
        pass

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
        pass

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
        frases.Phrase.getPhrase()
        pass


