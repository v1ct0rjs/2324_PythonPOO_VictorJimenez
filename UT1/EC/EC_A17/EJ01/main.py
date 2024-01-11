import matematica.operaciones as mat

if __name__ == '__main__':
    a = int(input('Introduzca el operador A >>> '))
    b = int(input('Introduzca el operados B >>> '))

    print(f'Suma >>> {mat.suma(a, b)}')
    print(f'Resta >>> {mat.resta(a, b)}')
    print(f'Multiplicación >>> {mat.multiplacacion(a, b)}')
    print(f'División >>> {mat.division(a, b)}')