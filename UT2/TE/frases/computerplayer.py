from .player import Player


class ComputerPlayer(Player):
    def __init__(self, name: str, prizeMoney: float, priceMoneyRound: float):
        super().__init__(name, prizeMoney, priceMoneyRound)
        self.name = 'Computer'
        self.prizeMoney = prizeMoney
        self.priceMoneyRound = priceMoneyRound

    def goMove(self):
        pass