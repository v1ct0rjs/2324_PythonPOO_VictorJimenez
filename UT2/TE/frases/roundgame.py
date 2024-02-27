from .humanplayer import HumanPlayer
from .computerplayer import ComputerPlayer
from .player import Player
from .frase import Phrase
from .game import Game
from .constantes import Constantes
import random


class RoundGame:

    def __init__(self, players: list[Player], phrase: Phrase):
        self.players = players
        self.phrase = phrase
        self.rondas = Constantes.TOTAL_ROUNDS
        self.letras_introducidas = []

    def playRound(self):
        for player in self.players:
            if self.playTurn(player):
                return f'{player.name} ha ganado la ronda'
            else:
                self.__calculateNextPlayerTurn(player)
        self.rondas -= 1
        self.showInfo(self.rondas)
        if self.rondas == 0:
            return Game.showWinner()

    def playTurn(self, player: Player):
        while True:
            if isinstance(player, HumanPlayer):
                while True:
                    self.__mostrarPhrase(self.phrase)
                    self.showTurnInfo(player)
                    print(f'Resultado de la tirada {HumanPlayer.goMove()}')
                    accion = input('¿Que hacer ENTER - Adivinar, 1 - Solucionar, 2 - Pasar, 3 - Vocal: ')
                    match accion:
                        case '':
                            letra = input('Introduce una letra: ')
                            self.letras_introducidas.append(letra)
                            if letra in self.phrase:
                                player.addMoney(50)
                                continue
                            else:
                                return False
                        case '1':
                            solucion = input('Introduce la solucion: ')
                            if solucion == self.phrase:
                                player.addPrizeRound(player.priceMoneyRound)
                                return True
                            else:
                                return False
                        case '2':
                            return False
                        case '3':
                            vocal = input('Introduce una vocal: ')
                            if vocal in self.phrase:
                                player.addMoney(-250)
                                continue
                            else:
                                return False
            else:
                while True:
                    self.__mostrarPhrase(self.phrase)
                    self.showTurnInfo(player)
                    print(f'Resultado de la tirada {ComputerPlayer.goMove()}')
                    print('¿Que hacer ENTER - Adivinar, 1 - Solucionar, 2 - Pasar, 3 - Vocal: ')
                    accion = random.choice(['', '2', '3'])
                    if player.prizeMoney > 250 and accion == '3':
                        accion = '3'
                    elif player.prizeMoney < 250 and accion != '3':
                        accion = random.choice(['', '2'])
                    match accion:
                        case '':
                            print('Introduce una letra: ')
                            letra = ComputerPlayer.consonanteAleatoria()
                            if letra in self.letras_introducidas:
                                letra = ComputerPlayer.consonanteAleatoria()
                            else:
                                self.letras_introducidas.append(letra)
                            if letra in self.phrase:
                                player.addMoney(50)
                                continue
                            else:
                                return False
                        case '2':
                            return False
                        case '3':
                            vocal = ComputerPlayer.compraVocal()
                            if vocal in self.letras_introducidas:
                                vocal = ComputerPlayer.compraVocal()
                            else:
                                self.letras_introducidas.append(vocal)

                            if vocal in self.phrase:
                                player.addMoney(50)
                                continue
                            else:
                                return False

    def showInfo(self, ronda):
        print(f'Ronda {ronda}')
        for player in self.players:
            print(f'{player.name} dinero ronda: {player.prizeMoney} €')

    def showTurnInfo(self, player):
        return f'Es el turno de {player.name} dinero ronda: {player.prizeMoney} €'

    def solvePanel(self, player: Player):
        if self.playTurn(player):
            return True

    def guessLetter(self):
        pass

    def __calculateNextPlayerTurn(self, player: Player):
        index = self.players.index(player)
        if index == len(self.players) - 1:
            return self.players[0]
        else:
            return self.players[index + 1]

    def __mostrarPhrase(self, phrase, letras_introducidas: list[str]):
        frase = ''
        introdudidas = ''
        for letra in phrase:
            if letra.lower() in letras_introducidas:
                frase += letra.upper()
            else:
                frase += '_ '
            introdudidas += letra + ' '
        for i in introdudidas:
            introdudidas += i + ' '

        print(f'{frase}  categoria: {phrase.categoria}  pista: {phrase.pista}  letras introducidas: {introdudidas}')
