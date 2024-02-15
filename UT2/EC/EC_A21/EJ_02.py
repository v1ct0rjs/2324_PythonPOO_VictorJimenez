import os
#import sys

class TreeOptions:
    def __init__(self, level_maximo=0, processHidden=True, processOutput=True):
        self.level_maximo = level_maximo
        self.processHidden = processHidden
        self.processOutput = processOutput


def tree_with_options(path: str, nivel_profundidad=0, options: TreeOptions = TreeOptions()):
    for elemento in os.scandir(path):
        alcanzadoNivelProfundidadMaximo = options.level_maximo > 0 and nivel_profundidad >= options.level_maximo

        processDirectory = True
        if alcanzadoNivelProfundidadMaximo:
            processDirectory = False

        if processDirectory and elemento.name.startswith(".") and options.processHidden == True:
            # Si es oculto y no se procesan los ocultos
            processDirectory = False
        if options.processOutput == True:
            print(elemento.name,'|', elemento.path,'|', elemento)
        else:
            if elemento.is_dir() and processDirectory:
                print(f"{'|__' * nivel_profundidad} {elemento.name}")
                tree(elemento.path, nivel_profundidad + 1, options.level_maximo)
            else:
                if not elemento.name.startswith("."):
                    print(f"{' ' * nivel_profundidad} -- {elemento.name}")

def tree(path: str, nivel_profundidad=0, level_maximo=0, processHidden=False):
    for elemento in os.scandir(path):
        alcanzadoNivelProfundidadMaximo = level_maximo > 0 and nivel_profundidad >= level_maximo
        if elemento.is_dir() and not elemento.name.startswith(".") and not alcanzadoNivelProfundidadMaximo:
            print(f"{'|__' * nivel_profundidad} {elemento.name}")
            tree(elemento.path, nivel_profundidad + 1, level_maximo)
        else:
            if not elemento.name.startswith("."):
                print(f"{' ' * nivel_profundidad} -- {elemento.name}")

def convertir_bytes(bytes):
    # Función para convertir bytes a KB o MB
    KB = 1024
    MB = 1024 * KB

    if bytes >= MB:
        return f"{bytes/MB:.2f} MB"
    elif bytes >= KB:
        return f"{bytes/KB:.2f} KB"
    else:
        return f"{bytes} bytes"



if __name__ == '__main__':
    options = TreeOptions(2, processHidden=False, processOutput=False)
    tree_with_options('/home/v1ct0r/', options=options)