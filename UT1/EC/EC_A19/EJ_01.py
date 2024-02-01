def text_to_number(text: str, default: int) -> int:
    try:
        try:
            valor_convertido = int(text)
            return valor_convertido
        except Exception:
            if default is None:
                raise TypeError(f'El parametro pasado no es texto')

            return default

    except Exception as err:
        raise ArithmeticError(f"La conversión no ha sido posible {err}")


def main():
    text_to_number('abc', 0)
    text_to_number('abc', 24)


if __name__ == '__main__':
    main()

#ejercicio 1
