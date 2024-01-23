from enum import Enum, auto, IntFlag


class PermisoFicheroEnum(IntFlag):
    LECTURA = 1
    ESCRITURA = 2
    EJECUCION = 4
    TODOS = 7
    NINGUNO = 0

    @staticmethod
    def letter_to(letter: str) -> PermisoFicheroEnum:
        if letter == 'r':
            return PermisoFicheroEnum.LECTURA
        if letter == 'w':
            return PermisoFicheroEnum.ESCRITURA
        if letter == 'x':
            return PermisoFicheroEnum.EJECUCION
        return PermisoFicheroEnum.NINGUNO


class PermisoOpcionEnum(Enum):
    USUARIO = auto()
    GRUPO = auto()
    OTROS = auto()


class PermisoFichero:
    def __init__(self, fichero: str, permisos: str):
        self.ruta = fichero
        self.__permisos: dict[PermisoOpcionEnum, PermisoFicheroEnum] = {}
        self.__permisos = self.conv_per_str(permisos)

    def conv_per_str(self, permisos: str) -> dict:
        # 1.dividir la cadena en 3 partes
        # 2.cada parte dividirla en 3 y obtener de cada letra el permiso
        # > parte usuario
        permisos_calculados: dict = {}
        parte = permisos[1:4]
        permiso_ususario = PermisoFicheroEnum.NINGUNO
        for letra in parte:
            permiso_ususario += PermisoFicheroEnum.letter_to(letra)
        permisos_calculados[PermisoOpcionEnum.USUARIO] = permiso_ususario
        # > parte grupo
        parte = permisos[4:7]
        permiso_ususario = PermisoFicheroEnum.NINGUNO
        for letra in parte:
            permiso_ususario += PermisoFicheroEnum.letter_to(letra)
        permisos_calculados[PermisoOpcionEnum.GRUPO] = permiso_ususario
        # > parte otros
        parte = permisos[7:10]
        permiso_ususario = PermisoFicheroEnum.NINGUNO
        for letra in parte:
            permiso_ususario += PermisoFicheroEnum.letter_to(letra)
        permisos_calculados[PermisoOpcionEnum.OTROS] = permiso_ususario

        return permisos_calculados

    def __conv_partletter_enum(self, letters: str) -> PermisoFicheroEnum:
        permiso = PermisoFicheroEnum.NINGUNO


    def get_permiso(self, opcion: PermisoOpcionEnum) -> PermisoFicheroEnum:
        return self.__permisos.get[opcion]

    def get_permisoNumerico(self) -> str:
        return self.__permisos.PermisoFicheroEnum.value

    def set_permiso(self, permisos: dict[PermisoOpcionEnum, PermisoFicheroEnum] | str) -> None:
        if isinstance(permisos, dict):
            self.__permisos = permisos
        if isinstance(permisos, str):
            user = permisos[0, 3]
            group = permisos[3, 5]
            other = permisos[5, 9]


def main():
    # Comprobaciones de funcionamiento
    ficheroPermisos = PermisoFichero("fichero.txt", "-rwxrwx--x")
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.USUARIO) is PermisoFicheroEnum.ESCRITURA
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.GRUPO) is PermisoFicheroEnum.LECTURA
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.OTROS) is PermisoFicheroEnum.EJECUCION
    assert ficheroPermisos.get_permisoNumerico() == 774

    ficheroPermisos.set_permiso("-rwx---rwx")
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.USUARIO) is PermisoFicheroEnum.TODOS
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.GRUPO) in PermisoFicheroEnum.NINGUNO
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.OTROS) in PermisoFicheroEnum.TODOS
    # assert file.get_permiso_numerico() == 707

    # ficheroPermisos.set_permiso([(PermisoOpcionEnum.USUARIO, PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.EJECUCION), (PermisoOpcionEnum.GRUPO, PermisoFicheroEnum.EJECUCION), (PermisoOpcionEnum.OTROS, PermisoFicheroEnum.NINGUNO)])
    assert ficheroPermisos.get_permiso(
        PermisoOpcionEnum.USUARIO) in PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.EJECUCION
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.GRUPO) in PermisoFicheroEnum.EJECUCION
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.OTROS) in PermisoFicheroEnum.NINGUNO


if __name__ == '__main__':
    main()
