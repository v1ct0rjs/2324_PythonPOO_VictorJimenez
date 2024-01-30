class LoggerMinix:
    @staticmethod
    def log(message: str):
        print(message)


class Person(LoggerMinix):
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, name: str, surname: str, student_id: int):
        super().__init__(name, surname)
        self.student_id = student_id


juan = Person("Juan", "Perez")
juan.log("Hola soy juan")

jose = Student("José", "García", 1234)
jose.log(f"Hola soy José y tengo el id {jose.student_id}")


if __name__ == '__main__':
    pass
