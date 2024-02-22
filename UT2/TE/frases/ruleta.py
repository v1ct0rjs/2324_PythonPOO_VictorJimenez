import random
class Ruleta():

    valores = [100, 50, 100, 150, 50, 200, 250, 50, 100, 150, 300, -1, 400, 0, 500, 200, 100, 50, 250, 150, 100, 50, 200]
    @staticmethod
    def girar() -> int:
        tirada = random.choice(Ruleta.valores)
        return tirada