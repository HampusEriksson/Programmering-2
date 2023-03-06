class SchoolPerson:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        pass


class Student(SchoolPerson):
    def __init__(self, name, age, major) -> None:
        super(Student, self).__init__(name, age)
        self.major = major
        self.grades = []


class SchoolPersonal(SchoolPerson):
    def __init__(self, name, age, credentials, salary) -> None:
        super(SchoolPersonal, self).__init__(name, age)
        self.credentials = credentials
        self.salary = salary


class Teacher(SchoolPersonal):
    def __init__(self, name, age, credentials, salary, subject) -> None:
        super(Teacher, self).__init__(name, age, credentials, salary)
        self.subject = subject
        self.classes = []


class Principal(SchoolPersonal):
    def __init__(self, name, age, credentials, salary, power, responsibility) -> None:
        super(Principal, self).__init__(name, age, credentials, salary)
        self.power = power
        self.responsibility = responsibility


print(Principal())
