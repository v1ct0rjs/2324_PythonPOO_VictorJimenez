import abc
from .constantes import Constantes

class Player: # Clase abstracta
    def __init__(self, name: str, prizeMoney: float, priceMoneyRound: float):
        self.name = name
        self.prizeMoney = prizeMoney
        self.priceMoneyRound = priceMoneyRound

    def addMoney(self, amt: float): # Añadir dinero
        self.prizeMoney += amt

    def applyBankrupt(self): # Aplicar quiebra
        self.prizeMoney = 0

    def addPrizeRound(self, prize: float): # Añadir premio de ronda
        self.priceMoneyRound += prize

    def applyWinRound(self): # Aplicar premio por victoria
        self.priceMoneyRound += Constantes.RECOMPENSA_PANEL

    @abc.abstractmethod
    def goMove(self): # Método abstracto para simular el movimiento del jugador
        pass

    def __str__(self): # Método para imprimir el objeto
        return f'{self.name}: {self.prizeMoney}'

    @abc.abstractmethod
    def FromSavedPlayer(self):
        pass
