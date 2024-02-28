from frases import Game

# def buildPlayers():
#     player1 = HumanPlayer("John", "Smith")
#     player2 = HumanPlayer("Pedro", "Smith")
#
#     return [player1, player2]


# def testRound(num: int, players: list[Player], frase: Phrase):
#     categoriaName = Phrase.requestCategory()
#     frase = Phrase.getPhrase(category=categoriaName)
#     round = RoundGame(players, frase)
#     playerWinner = round.playRound()
#     playerWinner.addPrizeRound(playerWinner.priceMoneyRound)


def initGame():
    juego = Game(0, '', None)
    juego.start()



if __name__ == '__main__':
    initGame()


