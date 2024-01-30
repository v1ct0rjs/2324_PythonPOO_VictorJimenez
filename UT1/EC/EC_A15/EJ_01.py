class LoggerMinix:
    @staticmethod
    def log(message: str):
        print(message)


class Person(LoggerMinix):
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


juan = Person("Juan", "Perez")
juan.log("Hola soy juan")

if __name__ == '__main__':
    pass

