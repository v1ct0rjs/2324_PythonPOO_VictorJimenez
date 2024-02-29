import random
class Ruleta(): # Clase que representa la ruleta de la fortuna

    valores = [100, 50, 100, 150, 50, 200, 250, 50, 100, 150, 300, -1, 400, 0, 500, 200, 100, 50, 250, 150, 100, 50, 200, -1, 0, -1, 0] # Valores de la ruleta se añadene los valores -1 y 0 para mayor dificultad
    @staticmethod
    def girar() -> int:
        """ Método que simula el giro de la ruleta de la fortuna """
        tirada = random.choice(Ruleta.valores)
        return tirada