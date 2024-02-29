from .player import Player
from .ruleta import Ruleta


class HumanPlayer(Player): # Clase que representa al jugador humano
    def __init__(self, name: str, prizeMoney: float, priceMoneyRound: float):
        super().__init__(name, prizeMoney, priceMoneyRound)
        self.name = name
        self.prizeMoney = prizeMoney
        self.priceMoneyRound = priceMoneyRound

    def goMove(self):
        """ Método que simula el movimiento del jugador humano en la ruleta de la fortuna """
        tirada = Ruleta.girar()
        if tirada == -1:
            self.applyBankrupt()
            return "Quiebra"
        elif tirada == 0:
            return "Pierde turno"
        else:
            self.addMoney(tirada)
            return f'Ha ganado {tirada} €'