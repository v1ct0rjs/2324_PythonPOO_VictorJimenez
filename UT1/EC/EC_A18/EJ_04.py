from enum import Enum, auto, IntFlag


class PermisoFicheroEnum(IntFlag):
    LECTURA = 1
    ESCRITURA = 2
    EJECUCION = 4
    TODOS = 7
    NINGUNO = 0


class PermisoOpcionEnum(Enum):
    USUARIO = auto()
    GRUPO = auto()
    OTROS = auto()


class PermisoFichero:
    def __init__(self, ruta: str, permisos: str):
        self._ruta = ruta
        self._permisos = permisos
        self.__acceso: dict[PermisoOpcionEnum, PermisoFicheroEnum] = {}

    def get_permiso(self, opcion: PermisoOpcionEnum) -> PermisoFicheroEnum:
        return self.__acceso.get(opcion)

    def get_permisoNumerico(self) -> int:
        entero = self.__acceso.PermisoFicheroEnum.value
        return entero

    def set_permiso(self, permisos: dict[PermisoOpcionEnum, PermisoFicheroEnum] | str):
        if isinstance(permisos, dict):
            self.__acceso = permisos
        if isinstance(permisos, str):
            user = permisos[0,3]
            group = permisos[3,5]
            other = permisos[5,9]
            match user:
                case ['r--']:
                    self.__acceso = PermisoFicheroEnum.LECTURA
                case ['-w-']:
                    self.__acceso = PermisoFicheroEnum.ESCRITURA
                case ['--x']:
                    self.__acceso = PermisoFicheroEnum.EJECUCION
                case ['---']:
                    self.__acceso = PermisoFicheroEnum.NINGUNO
                case ['rwx']:
                    self.__acceso = PermisoFicheroEnum.TODOS
                case ['rw-']:
                    self.__acceso = PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.ESCRITURA
                case ['r-x']:
                    self.__acceso = PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.EJECUCION
                case ['-wx']:
                    self.__acceso = PermisoFicheroEnum.ESCRITURA | PermisoFicheroEnum.EJECUCION
            match group:
                case ['r--']:
                    self.__acceso = PermisoFicheroEnum.LECTURA
                case ['-w-']:
                    self.__acceso = PermisoFicheroEnum.ESCRITURA
                case ['--x']:
                    self.__acceso = PermisoFicheroEnum.EJECUCION
                case ['---']:
                    self.__acceso = PermisoFicheroEnum.NINGUNO
                case ['rwx']:
                    self.__acceso = PermisoFicheroEnum.TODOS
                case ['rw-']:
                    self.__acceso = PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.ESCRITURA
                case ['r-x']:
                    self.__acceso = PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.EJECUCION
                case ['-wx']:
                    self.__acceso = PermisoFicheroEnum.ESCRITURA | PermisoFicheroEnum.EJECUCION
            match other:
                case ['r--']:
                    self.__acceso = PermisoFicheroEnum.LECTURA
                case ['-w-']:
                    self.__acceso = PermisoFicheroEnum.ESCRITURA
                case ['--x']:
                    self.__acceso = PermisoFicheroEnum.EJECUCION
                case ['---']:
                    self.__acceso = PermisoFicheroEnum.NINGUNO
                case ['rwx']:
                    self.__acceso = PermisoFicheroEnum.TODOS
                case ['rw-']:
                    self.__acceso = PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.ESCRITURA
                case ['r-x']:
                    self.__acceso = PermisoFicheroEnum.LECTURA | PermisoFicheroEnum.EJECUCION
                case ['-wx']:
                    self.__acceso = PermisoFicheroEnum.ESCRITURA | PermisoFicheroEnum.EJECUCION


if __name__ == '__main__':
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
