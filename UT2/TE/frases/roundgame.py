from .player import Player
from .frase import Phrase


class RoundGame():

    def __init__(self, players: list, phrases: int):
        self.players = players
        self.phrases = phrases
        self.currentPhrase = None
        self.currentPlayer = None

    def playRound(self):
        for player in self.players:
            self.currentPlayer = player
            self.currentPhrase = Phrase.getPhrase()
            self.currentPhrase.showPhrase()
            self.currentPlayer.guessPhrase(self.currentPhrase)
