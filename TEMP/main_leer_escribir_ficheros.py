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

def copyFile(sourceFile:str, targetFile: str):
    contenido = ""
    with open(sourceFile, mode='r') as sfile:
        # Leo contenido
        contenido = sfile.read()

    with open(targetFile, mode='a') as tfile:
        tfile.write(f'{contenido}\n')

    print("Fichero copiado correctamente")

def copyFileLineaLinea(sourceFile:str, targetFile: str):
    contenido = ""
    with open(sourceFile, mode='r') as sfile:
        with open(targetFile, mode='w') as tfile:
            for linea in sfile:
                tfile.write(f'{linea}\n')



    print("Fichero copiado correctamente")

if __name__ == '__main__':
    # abrifichero("temp.dat")
    # abrirFicheroConWith("temp.dat")
    copyFile('temp.dat', 'temp_bk.dat')
    copyFileLineaLinea('temp.dat', 'temp_bk_2.dat')