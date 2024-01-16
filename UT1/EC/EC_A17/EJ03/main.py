from ciencia import fisica
from ciencia import matematica




if __name__ == '__main__':
    assert fis.movimiento.distancia_inicial(5, 10, 2) == 150.0
    assert fis.movimiento.velocidad_final(3, 12, 2) == 27

    assert mat.algebra.ecuacion_lineal(1, 5, 1) == -4
    #assert mat.algebra.ecuacion_cuadratica(3, 5, 1) == -0.2324081207560018