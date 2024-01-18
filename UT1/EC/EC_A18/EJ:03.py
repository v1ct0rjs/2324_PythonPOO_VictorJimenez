from enum import IntEnum, IntFlag


class NivelAccesoEnum(IntEnum):
    SIN_ACCESO = 0
    RESTRINGIDO = 2
    NORMAL = 3
    TOTAL = 3


def verificar_acceso(nivel_acceso_usuario: NivelAccesoEnum, nivel_acceso_check: NivelAccesoEnum) -> bool:
    return nivel_acceso_usuario >= nivel_acceso_check


class ModuloEnum(IntFlag):
    VENTAS = 1
    COMPRAS = 2
    ALMACEN = 4
    CONTABILIDAD = 8
    RRHH = 16
    ADMINISTRACION = 32
    DIRECCION = 64


class UserAuth:
    def __init__(self, nombre: str, login: str):
        self.nombre = nombre
        self.login = login
        self.__acceso: dict[ModuloEnum, NivelAccesoEnum] = {}

    def get_module_access_level(self, module: ModuloEnum) -> NivelAccesoEnum:
        if self.__acceso.module >= ModuloEnum:
            return module.get(self.__acceso)
        return NivelAccesoEnum.SIN_ACCESO

    def assing_all_module_access(self, modules: dict[ModuloEnum, NivelAccesoEnum]):
        self.__acceso.modules = NivelAccesoEnum.TOTAL

    def assign_module_access(self, module: ModuloEnum, nivel_acceso: NivelAccesoEnum):
        self.__acceso.module = NivelAccesoEnum.nivel_acceso
        pass

    def unassing_module_access(self, module: ModuloEnum):
        # Completa este método
        pass

    def reset_module_access(self):
        # Completa este método
        pass

    def is_module_access(self, module: ModuloEnum) -> bool:
        # Completa este método
        pass

    def has_module_access(self, module: ModuloEnum, nivel_acceso: NivelAccesoEnum) -> bool:
        # Completa este método. True si el usuario tiene acceso al módulo con el nivel de acceso indicado, False en caso contrario
        pass
