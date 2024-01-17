from enum import Enum, auto
from math import sqrt
from typing import Any


class OpAritmeticaEnum(Enum):
    SUMA = auto()
    RESTA = auto()
    MULTIPLICACION = auto()
    DIVISION = auto()
    POTENCIA = auto()
    RAIZ_CUADRADA = auto()


class Calculadora:

    @staticmethod
    def calcular(a: float, b: float, operacion: OpAritmeticaEnum) -> float | None | Any:
        if operacion == OpAritmeticaEnum.SUMA:
            return a + b
        if operacion == OpAritmeticaEnum.RESTA:
            return a - b
        if operacion == OpAritmeticaEnum.MULTIPLICACION:
            return a * b
        if operacion == OpAritmeticaEnum.DIVISION.DIVISION:
            return a / b
        if operacion == OpAritmeticaEnum.POTENCIA:
            return a ** b
        if operacion == OpAritmeticaEnum.RAIZ_CUADRADA:
            return sqrt(a)

        return None


if __name__ == '__main__':
    assert Calculadora.calcular(2, 3, OpAritmeticaEnum.SUMA) == 5
    assert Calculadora.calcular(2, 3, OpAritmeticaEnum.RESTA) == -1
    assert Calculadora.calcular(2, 3, OpAritmeticaEnum.MULTIPLICACION) == 6
    assert Calculadora.calcular(3, 3, OpAritmeticaEnum.DIVISION) == 1
    assert Calculadora.calcular(2, 3, OpAritmeticaEnum.POTENCIA) == 8
    assert Calculadora.calcular(2, 3, OpAritmeticaEnum.RAIZ_CUADRADA) == 1.4142135623730951
