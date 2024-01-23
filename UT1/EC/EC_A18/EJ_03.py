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
        self.__acceso.module = nivel_acceso

    def unassing_module_access(self, module: ModuloEnum):
        self.__acceso.module = NivelAccesoEnum.SIN_ACCESO

    def reset_module_access(self):
        self.__acceso = {}

    def is_module_access(self, module: ModuloEnum) -> bool:
        return module in self.__acceso

    def has_module_access(self, module: ModuloEnum, nivel_acceso: NivelAccesoEnum) -> bool:
        return self.__acceso.get(module) == nivel_acceso

if __name__ == '__main__':

    user1 = UserAuth("Juan", "juanin")
    user1.assing_all_module_access([(ModuloEnum.VENTAS, NivelAccesoEnum.NORMAL), (ModuloEnum.COMPRAS, NivelAccesoEnum.RESTRINGIDO)])
    assert user1.is_module_access(ModuloEnum.VENTAS) == True
    assert user1.is_module_access(ModuloEnum.COMPRAS) == True
    assert user1.is_module_access(ModuloEnum.ALMACEN) == False

    user1.unassing_module_access(ModuloEnum.VENTAS)
    assert user1.is_module_access(ModuloEnum.VENTAS) == False

    user1.reset_module_access()
    assert user1.is_module_access(ModuloEnum.VENTAS) == False
    assert user1.is_module_access(ModuloEnum.COMPRAS) == False

    user1.assign_module_access(ModuloEnum.COMPRAS, NivelAccesoEnum.TOTAL)
    user1.assign_module_access(ModuloEnum.VENTAS, NivelAccesoEnum.NORMAL)
    assert user1.has_module_access(ModuloEnum.VENTAS, NivelAccesoEnum.NORMAL) == True
    assert user1.has_module_access(ModuloEnum.VENTAS, NivelAccesoEnum.RESTRINGIDO) == False
    assert user1.has_module_access(ModuloEnum.COMPRAS, NivelAccesoEnum.NORMAL) == False
