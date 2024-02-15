import os # import

def normalizar_ruta():
    ruta = input("Ingrese la ruta de archivo: ")
    ruta_normalizada = os.path.normpath(ruta)
    print("\nRuta Original:", ruta)
    print("Ruta Normalizada:", ruta_normalizada)


if __name__ == '__main__':
    normalizar_ruta()