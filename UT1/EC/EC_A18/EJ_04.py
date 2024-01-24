from enum import Enum, auto, IntFlag


class PermisoFicheroEnum(IntFlag):
    LECTURA = 1
    ESCRITURA = 2
    EJECUCION = 4
    TODOS = 7
    NINGUNO = 0

    @staticmethod
    def letter_to(letter: str):
        if letter == 'r':
            return PermisoFicheroEnum.LECTURA
        if letter == 'w':
            return PermisoFicheroEnum.ESCRITURA
        if letter == 'x':
            return PermisoFicheroEnum.EJECUCION
        return PermisoFicheroEnum.NINGUNO

    def __contains__(item1, item2):
        if (item2 & item1) == item1:
            return True
        return False


class PermisoOpcionEnum(Enum):
    USUARIO = auto()
    GRUPO = auto()
    OTROS = auto()


class PermisoFichero:
    def __init__(self, fichero: str, permisos: str):
        self.ruta = fichero
        self.__permisos: dict[PermisoOpcionEnum, PermisoFicheroEnum] = {}
        self.__permisos = self.__conv_per_str(permisos)

    def __conv_per_str(self, permisos: str) -> dict:
        # 1.dividir la cadena en 3 partes

        permisos_calculados: dict = {}
        permisos_calculados[PermisoOpcionEnum.USUARIO] = self.__conv_partletter_enum(permisos[1:4])
        permisos_calculados[PermisoOpcionEnum.GRUPO] = self.__conv_partletter_enum(permisos[4:7])
        permisos_calculados[PermisoOpcionEnum.OTROS] = self.__conv_partletter_enum(permisos[7:10])
        return permisos_calculados

    def __perm_entero(self, permisos: str) -> dict:
        if len(permisos) <= 3:
            permisos_calculados: dict = {}
            permisos_calculados[PermisoOpcionEnum.USUARIO] = permisos[0]
            permisos_calculados[PermisoOpcionEnum.GRUPO] = permisos[1]
            permisos_calculados[PermisoOpcionEnum.OTROS] = permisos[2]
            return permisos_calculados
        return None



    @staticmethod
    def __conv_partletter_enum(letters: str) -> PermisoFicheroEnum:
        permiso = PermisoFicheroEnum.NINGUNO
        for letra in letters:
            permiso += PermisoFicheroEnum.letter_to(letra)

        return permiso

    def get_permiso(self, opcion: PermisoOpcionEnum) -> PermisoFicheroEnum:
        return self.__permisos[opcion]


    def get_permisoNumerico(self) -> str:
        return f'{self.__permisos.PermisoFicheroEnum.value}'

    def set_permiso(self, permisos: dict[PermisoOpcionEnum, PermisoFicheroEnum] | str) -> None:
        if isinstance(permisos, dict):
            self.__permisos = permisos
            return

        if isinstance(permisos, str):
            if len(permisos) == 10:
                self.__permisos = self.__conv_per_str(permisos)
                return
            if len(permisos) == 3:
                self.__permisos = self.__perm_entero(permisos)
                return
            return
def main():
    # Comprobaciones de funcionamiento
    ficheroPermisos = PermisoFichero("fichero.txt", "-rwxrwx--x")
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.USUARIO) in PermisoFicheroEnum.ESCRITURA
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.GRUPO) is PermisoFicheroEnum.LECTURA
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.OTROS) is PermisoFicheroEnum.EJECUCION
    assert ficheroPermisos.get_permisoNumerico == 774

    ficheroPermisos.set_permiso("-rwx---rwx")
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.USUARIO) is PermisoFicheroEnum.TODOS
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.GRUPO) in PermisoFicheroEnum.NINGUNO
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.OTROS) in PermisoFicheroEnum.TODOS
    assert file.get_permisoNumerico() == 707

    ficheroPermisos.set_permiso([(PermisoOpcionEnum.USUARIO, PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.EJECUCION), (PermisoOpcionEnum.GRUPO, PermisoFicheroEnum.EJECUCION), (PermisoOpcionEnum.OTROS, PermisoFicheroEnum.NINGUNO)])
    assert ficheroPermisos.get_permiso(
        PermisoOpcionEnum.USUARIO) in PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.EJECUCION
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.GRUPO) in PermisoFicheroEnum.EJECUCION
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.OTROS) in PermisoFicheroEnum.NINGUNO


if __name__ == '__main__':
    main()
