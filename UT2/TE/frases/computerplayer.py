from .player import Player
from .ruleta import Ruleta
import random


class ComputerPlayer(Player):
    def __init__(self, name: str, prizeMoney: float, priceMoneyRound: float):
        super().__init__(name, prizeMoney, priceMoneyRound)
        self.name = 'Computer'
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

    @staticmethod
    def consonanteAleatoria():
        consonantes = random.choice("bcdfghjklmnñpqrstvwxyz")
        return random.choice(consonantes)

    @staticmethod
    def compraVocal():
        vocal = random.choice("aeiou")
        return vocal
