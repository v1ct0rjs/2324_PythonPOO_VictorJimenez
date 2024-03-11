def abrifichero(filename: str):
    fichero = None
    try:
        fichero = open(filename, mode='r')
        print(fichero)
    except Exception as e:
        print(e)
    finally:
        if fichero:
            fichero.close()


def abrirFicheroConWith(filename: str):
    try:
        with open(filename, mode='r') as fichero:
            #Devuelve todo el contenido como una cadena de texto
            print("------Leer todo, método read()---------- \n")
            contenido_completo = fichero.read()
            print(contenido_completo)

        with open(filename, mode='r') as fichero:
            # Para leer el contenido por lieneas, utiliza el mñetodo readlines()
            print('------ Leer por lineas, método readlines() ------ \n')
            for linea in fichero.readlines():
                print(linea)

    except Exception as e:
        print(e)



if __name__ == '__main__':
    # abrifichero("temp.dat")
    abrirFicheroConWith("temp.dat")

