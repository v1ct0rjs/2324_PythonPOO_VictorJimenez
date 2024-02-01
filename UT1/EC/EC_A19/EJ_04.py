def es_palindromo(texto: str) -> str | None:
    try:
        if not isinstance(texto, str):
            raise TypeError('Error: Se esperaba una cadena de texto')
        if len(texto) == 0:
            raise ValueError('Error: La cadena no puede estar vacía')
        texto = texto.lower()
        texto = texto.replace(' ', '')
        palindrimo = texto == texto[::-1]

    except TypeError:
        return None
    except ValueError:
        return None
    except Exception as err:
        print(f'Error: Se ha producido un error inesperado {err}')
        return None
    else:
        if palindrimo:
            return f'{texto} es palindromo'
        if not palindrimo:
            return f'{texto} no es palindromo'


def main():
    es_palindromo("ana")  # El ana es un palíndromo
    es_palindromo("dabale arroz a la zorra el abad")  # El dabale arroz a la zorra el abad es un palíndromo
    es_palindromo("hola")  # El hola no es un palíndromo
    es_palindromo(123)  # Error: Se esperaba una cadena de texto
    es_palindromo("")  # Error: La cadena no puede estar vacía


if __name__ == '__main__':
    main()

