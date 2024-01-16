import math


def area_cuadrado(lado: float) -> float | None:
    if lado >= 0:
        return lado * lado
    else:
        return None


def area_circulo(radio: float) -> float | None:
    if radio >= 0:
        return math.pi * (radio ** 2)
    else:
        return None


def area_triangulo(base: float, altura: float) -> float | None:
    if base >= 0 and altura >=  0:
        return (base / 2) * altura
    else:
        return None


def area_rectangulo(base: float, altura: float) -> float | None:
    if base >= 0 and altura >= 0:
        return base * altura
    else:
        return None
