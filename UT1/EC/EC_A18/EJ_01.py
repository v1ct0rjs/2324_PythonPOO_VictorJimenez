from enum import Enum


class WeekDays(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

    @staticmethod
    def is_laborable(dia):
        if isinstance(dia, int):
            return dia <= 5
        return dia.value <= 5

    @staticmethod
    def get_weekend_days():
        return [WeekDays.SABADO, WeekDays.DOMINGO]

    @staticmethod
    def get_week_days():
        return [WeekDays.LUNES, WeekDays.MARTES, WeekDays.MIERCOLES, WeekDays.JUEVES, WeekDays.VIERNES]


def main():
    diaTexto = int(input('Introduzca un dia de la semana.'))
    if not isinstance(diaTexto, int):
        print('Valor introducido no es un número.')
        return

    if diaTexto <= 0 | diaTexto >= 8:
        print('Número fuera de rango. Debe ser entre 1 y 7')
        return

    diaEnum = WeekDays(diaTexto)
    if WeekDays.is_laborable(diaEnum):
        print(f'El dia {diaEnum.name} es laborable, y es el dia {diaEnum.value} de la seman')
        return

    print(f'El dia {diaEnum.name} no es laborable')

if __name__ == '__main__':

