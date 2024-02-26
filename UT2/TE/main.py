
from frases import Ruleta, Phrase, Player, Constantes, Game, RoundGame, HumanPlayer, ComputerPlayer


def buildPlayers():

    player1 = HumanPlayer("John", "Smith")
    player2 = HumanPlayer("Pedro", "Smith")

    return [player1, player2]


def testRound(num: int, players: list[Player], frase: Phrase):
    categoriaName = Phrase.requestCategory()
    frase = Phrase.getPhrase(category=categoriaName)
    round = RoundGame(players, frase)
    playerWinner = round.playRound()
    playerNext = __calculateNextPlayerTurn(playerWinner)



def initGame():
    juego = Game(0, '', None)
    juego.start()

if __name__ == '__main__':
    testRound(1, buildPlayers())


    RoundGame.playRound(Game.players, Phrase.getPhrase(category=))

# subir a git
