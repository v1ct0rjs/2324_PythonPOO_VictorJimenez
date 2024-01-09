import random


class Coordenada:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return f'Longitud = {self.latitud}, Longitud = {self.longitud}'

    @staticmethod
    def geoRamdom():
        latitud = random.randint(0, 60)
        longitud = random.randint(0, 60) * -1
        return Coordenada(latitud, longitud)


class Persona:
    def __init__(self, nombre):
        self.longitud = None
        self.latitud = None
        self.nombre = nombre
        self.localizacion = None

    def __str__(self):
        if self.localizacion:
            return f'Mi nombre es {self.nombre} y estoy en ({Coordenada.geoRamdom()})'
        else:
            return f'Mi nombre es {self.nombre} y no se dónde estoy'

    def obtener_localizacion(self, force=False):
        if self.localizacion and force == False:
            return self.localizacion

        self.localizacion = Coordenada.geoRamdom()
        return self.localizacion


if __name__ == '__main__':
    antonio = Persona('Antonio')
    print(antonio)
    antonio.obtener_localizacion()
    print(antonio)
