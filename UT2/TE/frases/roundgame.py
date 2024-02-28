
from .humanplayer import HumanPlayer
from .computerplayer import ComputerPlayer
from .player import Player
from .frase import Phrase

from .constantes import Constantes
import random
import os


class RoundGame:


    def __init__(self, players: list[Player], phrase: Phrase):
        self.players = players
        self.phrase = phrase
        self.rondas = Constantes.TOTAL_ROUNDS
        self.letras_introducidas = []

    def playRound(self):
        i = 0
        while True:
            player = self.players[i]
            while self.playTurn(player):
                player = self.__calculateNextPlayerTurn(player)
            print(f'El jugador {player.name} ha ganado la ronda')
            i = (i + 1) % len(self.players)  # Vuelve al primer jugador cuando se llega al final de la lista
            self.rondas -= 1
            self.showInfo(self.rondas)
            if self.rondas == 0:
                return max(self.players, key=lambda player: player.prizeMoney)
            else:
                self.phrase = Phrase.getPhrase()
                self.letras_introducidas = []

    def playTurn(self, player: Player):
        while True:
            if isinstance(player, HumanPlayer):
                while True:
                    os.system('clear')
                    self.__mostrarPhrase(self.phrase, self.letras_introducidas)
                    self.showTurnInfo(player)
                    print(f'Resultado de la tirada {player.goMove()}')
                    accion = input('¿Que hacer ENTER - Adivinar, 1 - Solucionar, 2 - Pasar, 3 - Vocal: ')
                    match accion:
                        case '':
                            letra = input('Introduce una letra: ')
                            if self.guessLetter(letra, player):
                                if self.solvePanel(player):
                                    return True
                                continue
                            else:
                                return False
                        case '1':
                            solucion = input('Introduce la solucion: ')
                            if solucion == self.phrase.frase:
                                player.addPrizeRound(player.priceMoneyRound)
                                return True
                            else:
                                return False
                        case '2':
                            return True
                        case '3':
                            vocal = input('Introduce una vocal: ')
                            if vocal in self.phrase.frase:
                                player.addMoney(-250)
                                self.letras_introducidas.append(vocal)
                                if self.solvePanel(player):
                                    return True
                                continue
                            else:
                                return False
            else:
                while True:
                    os.system('clear')
                    self.__mostrarPhrase(self.phrase, self.letras_introducidas)
                    self.showTurnInfo(player)
                    tirada = player.goMove()
                    print(f'Resultado de la tirada {tirada}')
                    if tirada == "Pierde turno":
                        return True  # Cambia al siguiente jugador
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
                            if self.guessLetter(letra, player):
                                continue
                            else:
                                return False
                        case '2':
                            return True  # Cambia al siguiente jugador
                        case '3':
                            vocal = ComputerPlayer.compraVocal()
                            if vocal in self.letras_introducidas:
                                vocal = ComputerPlayer.compraVocal()
                            else:
                                self.letras_introducidas.append(vocal)

                            if vocal in self.phrase.frase:
                                player.addMoney(-250)
                                continue
                            else:
                                return False

    def showInfo(self, ronda):
        print(f'Ronda {ronda}')
        for player in self.players:
            print(f'{player.name} dinero ronda: {player.prizeMoney} €')

    def showTurnInfo(self, player):
        print(f'Es el turno de {player.name} dinero ronda: {player.prizeMoney} €')

    def solvePanel(self, player: Player):
        if self.playTurn(player):
            if set(self.phrase.frase.lower()) <= set(self.letras_introducidas):
                return True
        return False

    def guessLetter(self, letra, player: Player):
        if letra in self.letras_introducidas:
            return False
        else:
            self.letras_introducidas.append(letra)
        if letra in self.phrase.frase:
            #veces = count(self.phrase)
            player.addMoney(Constantes.RECOMPESA_LETRA)
            return True
        else:
            return False

    def __calculateNextPlayerTurn(self, player: Player):
        index = self.players.index(player)
        if index == len(self.players) - 1:
            return self.players[0]
        else:
            return self.players[index + 1]

    def __mostrarPhrase(self, phrase, letras_introducidas: list[str]):
        frase = ''
        introdudidas = list(set(letras_introducidas))  # Convertimos a conjunto y luego a lista para eliminar duplicados
        for letra in phrase.frase:
            if letra.lower() in letras_introducidas:
                frase += letra.upper()
            else:
                frase += '_ '
        introdudidas = ' '.join(sorted(introdudidas))  # Convertimos la lista a una cadena
        print(f'{frase}  categoria: {phrase.categoria}  pista: {phrase.pista}  letras introducidas: {introdudidas}')
