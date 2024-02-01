def calculadora_division(a: float, b: float) -> float | None:
    try:
        if b != 0:
            return a / b
        if b == 0:
            raise ZeroDivisionError
        if not isinstance(b, float):
            raise TypeError
    except ZeroDivisionError:
        print(f'No se puede dividir entre 0')
        return None
    except TypeError as err:
        print(f'Se debe introducir un número >>> {err}')
        return None


def main():
    resultado_1 = calculadora_division(10, 2)
    print(f"Resultado 1: {resultado_1}")

    resultado_2 = calculadora_division(5, 0)
    print(f"Resultado 2: {resultado_2}")

    resultado_3 = calculadora_division("abc", 2)
    print(f"Resultado 3: {resultado_3}")


if __name__ == "__main__":
    main()

#ejercicio 2