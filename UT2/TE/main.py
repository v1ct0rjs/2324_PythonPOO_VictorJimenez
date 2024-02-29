from frases import Game


def initGame():
    """ Método que inicia el juego"""
    juego = Game(0, '', None)
    juego.start()


if __name__ == '__main__':
    initGame()
