from geometria import planas
from geometria import solidas

if __name__ == '__main__':
    assert planas.area_cuadrado(5) == 25
    assert planas.area_rectangulo(5, 10) == 50
    assert planas.area_triangulo(5, 10) == 25
    assert planas.area_circulo(5) == 78.53981633974483
    assert solidas.volumen_cubo(5) == 125
    assert solidas.volumen_esfera(5) == 523.5987755982989
    assert solidas.volumen_cilindro(5, 10) == 785.3981633974483

    print(planas.area_rectangulo(22, 3))
    print(planas.area_triangulo(12, -3))
    print(solidas.volumen_cubo(-10))