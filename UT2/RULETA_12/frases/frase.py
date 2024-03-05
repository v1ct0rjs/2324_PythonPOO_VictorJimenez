import random


class Phrase:
    # Lista frases ruleta de la fortuan
    __phrases = [
        {
            "categoria": "Peliculas",
            "nombre": "Lo que el viento se llevo",
            "pista": ""
        },
        {
            "categoria": "Peliculas",
            "nombre": "El feo, el gordo y el flaco",
            "pista": "Complexión corporal"
        },
        {
            "categoria": "refranes",
            "nombre": "Al que madruga, Dios le ayuda",
            "pista": "Horario"
        },
        {
            "categoria": "refranes",
            "nombre": "Nunca es tarde si la dicha es buena",
            "pista": "Horario"
        },
        {
            "categoria": "refranes",
            "nombre": "Quien siembra vientos, recoge tempestades",
            "pista": "Cultivo"
        },
        {
            "categoria": "refranes",
            "nombre": "Quien mucho abarca, poco aprieta",
            "pista": "ansia"
        },
        {
            "categoria": "refranes",
            "nombre": "A quien madruga, Dios le ayuda",
            "pista": "Horario"
        },
        {
            "categoria": "refranes",
            "nombre": "A caballo regalado, no le mires el dentado",
            "pista": "Regalo"
        },
        {
            "categoria": "refranes",
            "nombre": "A cada cerdo le llega su San Martin",
            "pista": "Destino"
        },
        {
            "categoria": "refranes",
            "nombre": "A Dios rogando y con el mazo dando",
            "pista": "Oración"
        },
        {
            "categoria": "refranes",
            "nombre": "A falta de pan, buenas son tortas",
            "pista": "Alimento"
        },
        {
            "categoria": "peliculas",
            "nombre": "El Padrino",
            "pista": "Mafia"
        },
        {
            "categoria": "peliculas",
            "nombre": "La lista de Schindler",
            "pista": "Nazismo"
        },
        {
            "categoria": "peliculas",
            "nombre": "El señor de los anillos",
            "pista": "Fantasía"
        },
        {
            "categoria": "peliculas",
            "nombre": "El club de la lucha",
            "pista": "Desdoblamiento"
        },
        {
            "categoria": "peliculas",
            "nombre": "El silencio de los corderos",
            "pista": "Asesino"
        },
        {
            "categoria": "peliculas",
            "nombre": "El bueno, el feo y el malo",
            "pista": "Oeste"
        },
        {
            "categoria": "peliculas",
            "nombre": "El resplandor",
            "pista": "Hotel"
        },
        {
            "categoria": "peliculas",
            "nombre": "El club de la lucha",
            "pista": "Desdoblamiento"
        },
        {
            "categoria": "peliculas",
            "nombre": "El silencio de los corderos",
            "pista": "Asesino"
        },
        {
            "categoria": "peliculas",
            "nombre": "El bueno, el feo y el malo",
            "pista": "Oeste"
        },
        {
            "categoria": "frases celebres",
            "nombre": "Darme un punto de apoyo y movere el mundo",
            "pista": "Física"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La ignorancia es la noche de la mente",
            "pista": "Conocimiento"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida es sueño",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida es sueño",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida es sueño",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida es sueño",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida es sueño",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida es sueño",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida es sueño",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida es sueño",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "El corazon tiene razones que la razon ignora",
            "pista": "Amor"
        },
        {
            "categoria": "frases celebres",
            "nombre": "Solo sé que no se nada",
            "pista": "Filosofía"
        },
        {
            "categoria": "frases celebres",
            "nombre": "No hay peor sordo que el que no quiere oir",
            "pista": "Sentidos"
        },
        {
            "categoria": "frases celebres",
            "nombre": "La vida no deberia medirse en cantidad sino en calidad",
            "pista": "Vida"
        },
        {
            "categoria": "frases celebres",
            "nombre": "El hombre que mueve montañas comienza apartando piedrecitas",
            "pista": "Paciencia"
        },
        {
            "categoria": "frases celebres",
            "nombre": "Haz el amor y no la guerra",
            "pista": "Amor"
        },
        {
            "categoria": "frases celebres",
            "nombre": "Cada dia sabemos mas y entendemos menos",
            "pista": "Conocimiento"
        },
        {
            "categoria": "frases celebres",
            "nombre": "Si das pescado a un hombre hambriento, le nutres una jornada. Si le enseñas a pescar, le nutrirás toda su vida",
            "pista": "Enseñanza"
        }
    ]

    def __init__(self, categoria: str, nombre: str, pista: str):
        self.categoria = categoria
        self.frase = nombre
        self.pista = pista

    @staticmethod
    def getPhrase(category: str = None) -> 'Phrase':
        """
        Obtiene una frase aleatoria
        :return: Phrase
        """
        solo_categoria = []
        for item in Phrase.__phrases:
            if category is None or "categoria" not in item.keys():
                solo_categoria.append(item)
            elif item["categoria"] == category:
                solo_categoria.append(item)

        entry = random.choice(solo_categoria)

        return Phrase(entry["categoria"], entry["nombre"], entry["pista"])

    @staticmethod
    def requestCategory() -> str:
        category = ""
        while True:
            value = input(" >> Introduce la categoría de la frase (1-pelicula, 2-frases, 3-refranes): ")
            match value:
                case "1":
                    return "peliculas"
                case "2":
                    return "frases celebres"
                case "3":
                    return "refranes"
                case _:
                    print(" ❌ La categoría no es válida. Introduce un número entre (1-3)")
                    continue