from abc import ABC, abstractmethod


class GeneroSexo:
    def __init__(self, genero: int):
        self.genero = genero

    def esMasculino(self) -> bool:
        pass

    def esFemenino(self) -> bool:
        pass

    def esOtro(self) -> bool:
        pass


class Direccion:
    def __init__(self, calle: str, ciudad: str, codigo_postal: str):
        self._calle = calle
        self._ciudad = ciudad
        self.codigo_postal = codigo_postal


class Persona(ABC):
    def __init__(self, nombre: str, edad: str, genero: GeneroSexo, direccion: Direccion):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self._direccion = direccion


class Empleado(Persona):
    def __init__(self, nombre: str, edad: str, genero: GeneroSexo, direccion: Direccion, id_empleado: int,
                 salario: float):
        super().__init__(nombre, edad, genero, direccion)
        self._id_empleado = id_empleado
        self._salario = salario

    @property
    def salario(self):
        return self._salario


class Cliente(Persona):
    def __init__(self, nombre: str, edad: str, genero: GeneroSexo, direccion: Direccion, id_cliente: int,
                 IdenFiscal: str):
        super().__init__(nombre, edad, genero, direccion)
        self._id_cliente = id_cliente
        self._IdenFiscal = IdenFiscal


class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._empleados = []
        self._clientes = []

    def get_Empleados(self) -> list:
        self._empleados = []
        return self._empleados

    def get_Clientes(self) -> list:
        self._clientes = []
        return self._clientes

    def set_agregarEmpleado(self, empleado: object):
        self._empleados.append(empleado)

    def set_agregarCliente(self, cliente: object):
        self._clientes.append(cliente)

    def obtenerSalario_total(self) -> float:
        total = 0
        for empleado in self._empleados:
            if isinstance(empleado, Empleado):
                total += empleado.salario
        return total
