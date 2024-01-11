def suma(a: int, b: int):
    return a + b


def resta(a: int, b: int):
    return a - b


def multiplacacion(a: int, b: int):
    return a * b


def division(a: int, b: int):
    if b == 0:
        return 'La operación no está definida, división por 0'
    else:
        return a / b