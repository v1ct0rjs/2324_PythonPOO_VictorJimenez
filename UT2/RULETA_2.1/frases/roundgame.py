from .humanplayer import HumanPlayer
from .computerplayer import ComputerPlayer
from .duoPlayer import DuoPlayer
from .player import Player
from .frase import Phrase
from .constantes import Constantes
import random
import os
import time


class RoundGame:
    consonantes = 'bcdfghjklmnñpqrstvwxyz'
    vocales = 'aeiou'

    def __init__(self, players: list[Player], phrase: Phrase):
        self.players = players  # Lista de jugadores
        self.phrase = phrase  # Frase a adivinar
        self.rondas = Constantes.TOTAL_ROUNDS  # Número de rondas
        self.letras_introducidas = []  # Letras introducidas
        self.current_player = self.players[0]  # Jugador actual

    def playRound(self):
        """Jugar una ronda"""
        # La ronda continúa hasta que se resuelva la frase
        while not self.__isPhraseSolved():
            # Iterar por cada uno de los jugadores
            for player in self.players:
                if self.playTurn(player):  # Si el turno ha terminado
                    if self.__isPhraseSolved():  # Si la frase ha sido resuelta
                        os.system('clear')
                        print(f'El jugador {player.name} ha ganado la ronda')
                        player.priceMoneyRound = player.prizeMoney
                        player.applyWinRound()  # Aplicar premio por victoria
                        print()
                        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        print()
                        self.__showInfo(self.rondas)
                        print()
                        self.letras_introducidas = []
                        input('Pulsa ENTER para continuar')
                        os.system('clear')
                        return True  # Termina la ronda
                player = self.__calculateNextPlayerTurn(player)  # Calcular el siguiente jugador
        return False

    def playTurn(self, player: Player):
        """Jugar un turno"""
        while True:
            if isinstance(player, HumanPlayer):
                if self.__juegaHumano(player):
                    return True
                return False

            if isinstance(player, DuoPlayer):  # Jugador equipo
                if self.__juegaDuo(player):
                    return True
                return False

            if isinstance(player, ComputerPlayer):  # Jugador computadora
                if self.__juegaComputer(player):
                    return True
                return False

    def __showInfo(self, ronda):
        """Mostrar información de la ronda"""
        i = 1
        print(f'Ronda {i} de {ronda}')
        for player in self.players:
            print(f'{player.name} dinero acumulado: {player.priceMoneyRound} €')
        i += 1

    def __showTurnInfo(self, player):
        """Mostrar información del turno"""
        if isinstance(player, HumanPlayer):
            print(f'''
            Es el turno de {player.name}
            =================================== 
            Dinero ronda {player.name}: {player.prizeMoney} €
            ''')
        elif isinstance(player, DuoPlayer):
            print(f'''
            Es el turno de {player.name}
            =================================== 
            Dinero ronda {player.name}, {player.jugadores}: {player.prizeMoney} €
            ''')
        else:
            print(f'''
            Es el turno de {player.name}
            =================================== 
            Dinero ronda {player.name}: {player.prizeMoney} €
            ''')

    def __solvePanel(self, player: Player, solucion: str):
        """Resolver la frase"""
        if solucion.lower() == self.phrase.frase.lower():  # Comprobar si la solución es correcta
            for letra in set(self.phrase.frase.lower()):
                if letra.isalpha():  # Añadir todas las letras de la frase a las introducidas
                    self.letras_introducidas.append(letra)
            player.addPrizeRound(player.prizeMoney)  # Asumiendo que prizeMoney es el premio acumulado
            return True  # La frase ha sido resuelta correctamente
        else:
            return False  # La frase no ha sido resuelta

    def __guessLetter(self, letra, player: Player):
        """Adivinar una letra de la frase"""
        if letra in self.letras_introducidas:  # Comprobar si la letra ya ha sido introducida
            return False
        else:
            self.letras_introducidas.append(letra)  # Añadir la letra a las introducidas
        if letra in self.phrase.frase:  # Comprobar si la letra está en la frase
            veces = self.phrase.frase.count(letra)
            player.addMoney(Constantes.RECOMPENSA_LETRA * veces)  # Asumiendo que prizeMoney es el premio acumulado
            return True
        else:
            return False

    def __calculateNextPlayerTurn(self, player: Player):
        """Calcular el siguiente jugador después de cada turno"""
        index = self.players.index(player)  # Obtener el índice del jugador actual
        if index == len(self.players) - 1:  # Si el jugador actual es el último de la lista
            return self.players[0]  # Devolver el primer jugador
        else:
            return self.players[index + 1]  # Devolver el siguiente jugador

    def __mostrarPhrase(self, phrase, letras_introducidas: list[str]):
        """Mostrar la frase con las letras introducidas"""
        print("""
        
        ============================================== LA RULETA DE LA FORTUNA =================================
                                                                                                           
        """)
        self.__showInfo(self.rondas)  # Mostrar información de la ronda
        frase = ''
        introdudidas = list(set(letras_introducidas))  # Convertimos a conjunto y luego a lista para eliminar duplicados
        for letra in phrase.frase:
            if letra.lower() in [l.lower() for l in letras_introducidas]:
                frase += letra.upper()
            elif letra == ' ':
                frase += ' '
            else:
                frase += '_ '
        introdudidas = ' '.join(sorted(introdudidas))  # Convertimos la lista a una cadena
        print(f'''
        +---------------------------------------------------------------------------------------------------+
                                                                                                           
           {" " * ((100 - len(frase)) // 2)}{frase}{" " * ((100 - len(frase)) // 2)} 
                                                                                                                                                                                               
                                                                                                           
           Categoria: {phrase.categoria}
           Pista: {phrase.pista}
           Letras introducidas: {introdudidas}
                                                                                                           
        +---------------------------------------------------------------------------------------------------+
        ''')  # Mostrar la frase con las letras introducidas

    def __isPhraseSolved(self):
        """Verificar si todas las letras de la frase están en las letras introducidas"""
        normalized_phrase = [letter.lower() for letter in self.phrase.frase if letter.isalpha()]
        normalized_introducidas = [letter.lower() for letter in self.letras_introducidas]
        return set(normalized_phrase).issubset(
            set(normalized_introducidas))  # Comprobar si todas las letras de la frase están en las introducidas

    def __isPanelSolved(self):
        """Verificar si todas las letras de la frase están en las letras introducidas"""
        normalized_phrase = set(letter.lower() for letter in self.phrase.frase if
                                letter.isalpha())  # Convertir a conjunto para eliminar duplicados
        normalized_introducidas = set(letter.lower() for letter in self.letras_introducidas)
        return normalized_phrase.issubset(
            normalized_introducidas)  # Comprobar si todas las letras de la frase están en las introducidas

    def __juegaHumano(self, player):
        while True:
            os.system('clear')
            self.__mostrarPhrase(self.phrase, self.letras_introducidas)
            self.__showTurnInfo(player)
            tirada = player.goMove()
            if tirada == "Pierde turno":
                print("Pierde Turno")
                input('Pulsa ENTER para continuar')
                return False
            elif tirada == "Quiebra":
                print("Quiebra")
                input('Pulsa ENTER para continuar')
                player.applyBankrupt()
                return False
            else:
                accion = input('¿Que hacer ENTER - Adivinar, 1 - Solucionar, 2 - Pasar, 3 - Vocal: ')
                match accion:
                    case '':
                        letra = input('Introduce una letra consonante: ')
                        if letra in self.consonantes:
                            if self.__guessLetter(letra, player):
                                if self.__isPanelSolved():
                                    print()
                                    print(f'¡Felicidades! {player.name} ha completado el panel.')
                                    input('Pulsa ENTER para continuar')
                                    return True  # Termina el turno indicando que el panel ha sido resuelto
                                continue
                            else:
                                if player.prizeMoney == 0:
                                    player.prizeMoney = 0
                                    return False
                                elif (player.prizeMoney - tirada) < 0:
                                    player.prizeMoney = 0
                                    return False
                                else:
                                    player.addMoney(-tirada)
                                    return False
                        else:
                            print('La letra introducida no es una consonante')
                            input('Pulsa ENTER para continuar')
                            continue
                    case '1':
                        solucion = input('Introduce la solución: ')
                        if self.__solvePanel(player, solucion):
                            print()
                            print(f'¡Correcto! {player.name} ha resuelto el panel.')
                            input('Pulsa ENTER para continuar')
                            return True  # Finaliza el turno indicando que el panel ha sido resuelto
                        else:
                            print()
                            print('Incorrecto. No se resuelve el panel.')
                            input('Pulsa ENTER para continuar')
                            return False  # El panel no se resuelve, el turno continúa
                    case '2':
                        if player.prizeMoney == 0:
                            player.prizeMoney = 0
                            return False
                        elif (player.prizeMoney - tirada) < 0:
                            player.prizeMoney = 0
                            return False
                        else:
                            player.addMoney(-tirada)
                            return False
                    case '3':
                        vocal = input('Introduce una vocal: ')
                        if vocal in self.vocales:
                            if vocal in self.phrase.frase:
                                if player.prizeMoney >= 250:
                                    player.addMoney(-250)
                                    self.letras_introducidas.append(vocal)
                                    if self.__isPanelSolved():
                                        print()
                                        print(f'¡Felicidades! {player.name} ha completado el panel.')
                                        input('Pulsa ENTER para continuar')
                                        return True  # Termina el turno indicando que el panel ha sido resuelto
                                    continue
                                else:
                                    print('No tienes suficiente dinero para comprar una vocal')
                                    input('Pulsa ENTER para continuar')
                                    continue
                            else:
                                if player.prizeMoney == 0:
                                    player.prizeMoney = 0
                                    return False
                                elif (player.prizeMoney - tirada) < 0:
                                    player.prizeMoney = 0
                                    return False
                                else:
                                    player.addMoney(-tirada)
                                    return False
                        else:
                            print('La letra introducida no es una vocal')
                            input('Pulsa ENTER para continuar')
                            continue

    def __juegaDuo(self, player):
        while True:
            os.system('clear')
            self.__mostrarPhrase(self.phrase, self.letras_introducidas)
            self.__showTurnInfo(player)
            tirada = player.goMove()
            if tirada == "Pierde turno":
                print("Pierde Turno")
                input('Pulsa ENTER para continuar')
                return False
            elif tirada == "Quiebra":
                print("Quiebra")
                input('Pulsa ENTER para continuar')
                player.applyBankrupt()
                return False
            else:
                accion = input('¿Que hacer ENTER - Adivinar, 1 - Solucionar, 2 - Pasar, 3 - Vocal: ')
                match accion:
                    case '':
                        letra = input('Introduce una letra consonante: ')
                        if letra in self.consonantes:
                            if self.__guessLetter(letra, player):
                                if self.__isPanelSolved():
                                    print()
                                    print(f'¡Felicidades! {player.name} ha completado el panel.')
                                    input('Pulsa ENTER para continuar')
                                    return True  # Termina el turno indicando que el panel ha sido resuelto
                                continue
                            else:
                                if player.prizeMoney == 0:
                                    player.prizeMoney = 0
                                    return False
                                elif (player.prizeMoney - tirada) < 0:
                                    player.prizeMoney = 0
                                    return False
                                else:
                                    player.addMoney(-tirada)
                                    return False
                        else:
                            print('La letra introducida no es una consonante')
                            input('Pulsa ENTER para continuar')
                            continue
                    case '1':
                        solucion = input('Introduce la solución: ')
                        if self.__solvePanel(player, solucion):
                            print()
                            print(f'¡Correcto! {player.name} ha resuelto el panel.')
                            input('Pulsa ENTER para continuar')
                            return True  # Finaliza el turno indicando que el panel ha sido resuelto
                        else:
                            print()
                            print('Incorrecto. No se resuelve el panel.')
                            input('Pulsa ENTER para continuar')
                            return False  # El panel no se resuelve, el turno continúa
                    case '2':
                        if player.prizeMoney == 0:
                            player.prizeMoney = 0
                            return False
                        elif (player.prizeMoney - tirada) < 0:
                            player.prizeMoney = 0
                            return False
                        else:
                            player.addMoney(-tirada)
                            return False
                    case '3':
                        vocal = input('Introduce una vocal: ')
                        if vocal in self.vocales:
                            if vocal in self.phrase.frase:
                                if player.prizeMoney >= 250:
                                    player.addMoney(-250)
                                    self.letras_introducidas.append(vocal)
                                    if self.__isPanelSolved():
                                        print()
                                        print(f'¡Felicidades! {player.name} ha completado el panel.')
                                        input('Pulsa ENTER para continuar')
                                        return True  # Termina el turno indicando que el panel ha sido resuelto
                                    continue
                                else:
                                    print('No tienes suficiente dinero para comprar una vocal')
                                    input('Pulsa ENTER para continuar')
                                    continue
                            else:
                                if player.prizeMoney == 0:
                                    player.prizeMoney = 0
                                    return False
                                elif (player.prizeMoney - tirada) < 0:
                                    player.prizeMoney = 0
                                    return False
                                else:
                                    player.addMoney(-tirada)
                                    return False
                        else:
                            print('La letra introducida no es una vocal')
                            input('Pulsa ENTER para continuar')
                            continue

    def __juegaComputer(self, player):
        while True:  # Jugador computadora
            os.system('clear')
            self.__mostrarPhrase(self.phrase, self.letras_introducidas)
            self.__showTurnInfo(player)
            tirada = player.goMove()
            if tirada == "Pierde turno":
                print("Pierde Turno")
                time.sleep(1)
                return False
            elif tirada == "Quiebra":
                print("Quiebra")
                time.sleep(1)
                player.applyBankrupt()
                return False
            else:
                print('¿Que hacer ENTER - Adivinar, 1 - Solucionar, 2 - Pasar, 3 - Vocal: ')
                time.sleep(2)
                accion = random.choice(['', '2', '3'])
                if player.prizeMoney > 250 and accion == '3':
                    accion = '3'
                elif player.prizeMoney < 250 and accion == '3':
                    accion = random.choice(['', '2'])
                match accion:
                    case '':
                        letra = ComputerPlayer.consonanteAleatoria()
                        time.sleep(1)
                        print(f'Introduce una letra: {letra}')
                        time.sleep(2)
                        if self.__guessLetter(letra, player):
                            if self.__isPanelSolved():
                                print(f'¡Felicidades! {player.name} ha completado el panel.')
                                input('Pulsa ENTER para continuar')
                                return True  # Termina el turno indicando que el panel ha sido resuelto
                            continue
                        else:
                            if player.prizeMoney == 0:
                                player.prizeMoney = 0
                                return False
                            elif (player.prizeMoney - tirada) < 0:
                                player.prizeMoney = 0
                                return False
                            else:
                                player.addMoney(-tirada)
                                return False
                    case '2':
                        print("Pasa Turno")
                        time.sleep(1)
                        if player.prizeMoney == 0:
                            player.prizeMoney = 0
                            return False
                        elif (player.prizeMoney - tirada) < 0:
                            player.prizeMoney = 0
                            return False
                        else:
                            player.addMoney(-tirada)
                            return False
                    case '3':
                        vocal = ComputerPlayer.compraVocal()
                        time.sleep(1)
                        print(f'Introduce una vocal: {vocal}')
                        time.sleep(2)
                        if vocal in self.letras_introducidas:
                            vocal = ComputerPlayer.compraVocal()
                        else:
                            self.letras_introducidas.append(vocal)
                        if vocal in self.phrase.frase:
                            player.addMoney(-250)
                            self.letras_introducidas.append(vocal)
                            if self.__isPanelSolved():
                                print(f'¡Felicidades! {player.name} ha completado el panel.')
                                input('Pulsa ENTER para continuar')
                                return True  # Termina el turno indicando que el panel ha sido resuelto
                            continue
                        else:
                            if player.prizeMoney == 0:
                                player.prizeMoney = 0
                                return False
                            elif (player.prizeMoney - tirada) < 0:
                                player.prizeMoney = 0
                                return False
                            else:
                                player.addMoney(-tirada)
                                return False
