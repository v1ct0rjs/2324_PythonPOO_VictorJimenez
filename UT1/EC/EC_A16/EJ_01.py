class Vehiculo:
    def __init__(self, matricula: str, marca: str, modelo: str, tarifa: float, disponible: bool):
        self._disponible = disponible
        self._tarifa = tarifa
        self._modelo = modelo
        self._marca = marca
        self._matricula = matricula

    @property
    def tarifa(self):
        return self._tarifa

    @property
    def modelo(self):
        return self._modelo

    @property
    def matricula(self):
        return self._matricula

    @property
    def marca(self):
        return self._marca

    @property
    def disponible(self):
        return self._disponible


class Cliente:
    def __init__(self, dni: str, nombre: str, apellidos: str, telefono: str):
        self._telefono = telefono
        self._apellidos = apellidos
        self._nombre = nombre
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellidos(self):
        return self._apellidos

    @property
    def teledono(self):
        return self._telefono


class VehiculoAlquilado:
    def __init__(self, vehiculo: Vehiculo):
        self._cliente = None
        self._vehiculo = vehiculo

    def alquilar(self, cliente: Cliente):
        self._cliente = cliente

    def finalizar_alquiler(self):
        self._cliente = None

    def estaDisponible(self):
        return self._cliente is None


if __name__ == '__main__':
    veh = Vehiculo('8117FLC', 'Peugeot', '5008', 20.3, True)
    miguel = Cliente('785748682Q', 'Miguel', 'Rodriguez', '924253658')

    vehAlquilado = VehiculoAlquilado(veh)
    vehAlquilado.alquilar(miguel)
    vehAlquilado.finalizar_alquiler()
