from typing import Set


class UserBO():

    @staticmethod
    def register_user(name: str, age: int, email: str) -> set[str | int] | None:
        diccionario = {name, age, email}
        try:
            if not isinstance(name, str):
                raise TypeError('Error: Se esperaba una cadena de texto')
            if not isinstance(age, int):
                raise TypeError('Error: Se esperaba un número entero')
            if '@' not in email or '.' not in email:
                raise ValueError('Error: El correo electronico no es valido')
            return diccionario
        except TypeError:
            return None
        except ValueError:
            return None
        except Exception as err:
            print('Error: Se ha producido un error inesperado ', err)
            return None


def main():
    user_1 = UserBO.register_user("Juan", 25, "email@yahoo.com")
    user_2 = UserBO.register_user("Juan", "25", "email")
    user_3 = UserBO.register_user(45, 25, "email")

    print(user_1)
    print(user_2)
    print(user_3)


if __name__ == '__main__':
    main()
