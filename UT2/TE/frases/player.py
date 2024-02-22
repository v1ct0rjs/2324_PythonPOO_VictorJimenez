import abc


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
