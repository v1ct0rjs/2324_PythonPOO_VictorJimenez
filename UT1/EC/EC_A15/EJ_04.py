class MathOperationsMixin:
    @staticmethod
    def sum_numbers(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract_numbers(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply_numbers(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide_numbers(a: float, b: float) -> float | str:
        if b != 0:
            return a / b
        else:
            return f'No puedes dividir entre 0'


class Calculator(MathOperationsMixin):
    def __init__(self, name: str):
        self.name = name

    def add(self, a: float, b: float):
        return self.sum_numbers(a, b)

    def subtract(self, a:float, b:float):
        return self.subtract_numbers(a, b)
