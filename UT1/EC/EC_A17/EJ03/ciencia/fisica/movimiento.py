
def distancia_inicial(velocidad: float, tiempo: float, aceleracion: float) -> float:
    return ((velocidad * tiempo) + (aceleracion * (tiempo ** 2))) / 2


def velocidad_final(velocidad_inicial: float, aceleracion: float, tiempo: float) -> float:
    return velocidad_inicial + (aceleracion * tiempo)
