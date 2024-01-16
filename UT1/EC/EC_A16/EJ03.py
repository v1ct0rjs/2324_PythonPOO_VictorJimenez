from abc import ABC, abstractmethod


class GeneroSexo:
    def __init__(self, genero: int):
        self.genero = genero

    def __str__(self):
        return f'Genero >> {self.genero}'

    def esMasculino(self) -> bool:
        if self.genero == 1:
            return True
        else:
            return False

    def esFemenino(self) -> bool:
        if self.genero == 2:
            return True
        else:
            return False

    def esOtro(self) -> bool:
        if self.genero == 3:
            return True
        else:
            return False


class Direccion:
    def __init__(self, calle: str, ciudad: str, codigo_postal: str):
        self._calle = calle
        self._ciudad = ciudad
        self._codigo_postal = codigo_postal

    def __str__(self):
        return f'Calle: {self._calle}, Ciudad: {self._ciudad}, CP: {self._codigo_postal}'

    @property
    def cCalle(self):
        return self._calle

    @property
    def cCiudad(self):
        return self._ciudad

    @property
    def cCp(self):
        return self._codigo_postal


class Persona(ABC):
    def __init__(self, nombre: str, edad: str, genero: GeneroSexo, direccion: Direccion):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self._direccion = direccion

    @property
    def cNombre(self):
        return self._nombre

    @property
    def cEdad(self):
        return self._edad

    @property
    def cGenero(self):
        return self._genero

    @property
    def cDireccion(self):
        return self._direccion


class Empleado(Persona):
    def __init__(self, nombre: str, edad: str, genero: GeneroSexo, direccion: Direccion, id_empleado: int,
                 salario: float):
        super().__init__(nombre, edad, genero, direccion)
        self._id_empleado = id_empleado
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @property
    def id_empleado(self):
        return self._id_empleado


class Cliente(Persona):
    def __init__(self, nombre: str, edad: str, genero: GeneroSexo, direccion: Direccion, id_cliente: int, IdenFiscal: str):
        super().__init__(nombre, edad, genero, direccion)
        self._id_cliente = id_cliente
        self._IdenFiscal = IdenFiscal

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def id_fiscal(self):
        return self._IdenFiscal


class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._empleados = []
        self._clientes = []

    @property
    def Empleados(self) -> list:
        self._empleados = []
        return self._empleados

    @property
    def Clientes(self) -> list:
        self._clientes = []
        return self._clientes

    @agregarEmpleado.setter
    def agregarEmpleado(self, empleado: object):
        self._empleados.append(empleado)

    @agregarCliente.setter
    def agregarCliente(self, cliente: object):
        self._clientes.append(cliente)

    def obtenerSalario_total(self) -> float:
        total = 0
        for empleado in self._empleados:
            if isinstance(empleado, Empleado):
                total += empleado.salario
        return total


if __name__ == '__main__':
    hombre = GeneroSexo(1)
    mujer = GeneroSexo(2)
    otro = GeneroSexo(3)

    direccion1 = Direccion("Calle 1", "Ciudad 1", "12345")
    direccion2 = Direccion("Calle 2", "Ciudad 2", "54321")

    empleado1 = Empleado("Juan", 30, hombre, direccion1, 1, 1000)
    empleado2 = Empleado("Manuela", 40, mujer, direccion2, 2, 2000)

    cliente1 = Cliente("Ana", 20, mujer, direccion1, 1, "12345678A")

    empresa = Empresa("Empresa 1")
    empresa.agregarEmpleado(empleado1)
    empresa.agregarEmpleado(empleado2)

    empresa.agregarCliente(cliente1)

    assert empresa.obtenerSalario_total() == 3000
    assert empresa.empleados[0].nombre == "Juan"
    assert empresa.empleados[1].nombre == "Manuela"
    assert empresa.clientes[0].nombre == "Ana"

    assert len(empresa.empleados) == 2
    assert len(empresa.clientes) == 1