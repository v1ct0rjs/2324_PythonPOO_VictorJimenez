import math


def volumen_cubo(lado: float) -> float | None:
    if lado >= 0:
        return lado ** 3
    else:
        return None


def volumen_esfera(radio: float) -> float | None:
    if radio >= 0:
        return (4 / 3) * math.pi * (radio ** 3)
    else:
        return None


def volumen_cilindro(radio: float, altura: float) -> float | None:
    if radio >= 0 and altura >= 0:
        return math.pi * (radio ** 2) * altura
    else:
        return None
