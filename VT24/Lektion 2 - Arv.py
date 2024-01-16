class Person:
    def __init__(self, name, age, height) -> None:
        self.name = name
        self.age = age
        self.height = height

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."

    def sleep(self, hours):
        print(f"{self.name} sleeps {hours} hours a night.")


class Student(Person):
    def __init__(self, name, age, height) -> None:
        super().__init__(name, age, height)
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def sleep(self, hours):
        print(
            f"{self.name} sleeps {hours} hours a night and {hours/2} during Hampus's lessons."
        )


class Teacher(Person):
    def __init__(self, name, age, height, salary=0) -> None:
        super().__init__(name, age, height)
        self.salary = salary

    def yell_at_students(self, student):
        print(f"{self.name} yells at {student.name}.")

    def raise_salary(self):
        self.salary *= 1.04


student1 = Student("Tom", 17, 170)
student2 = Student("Erik", 17, 185)
student3 = Student("Markus", 17, 175)

student1.add_grade("Math", "A")
student1.add_grade("English", "C")
student2.add_grade("Math", "B")
student2.add_grade("English", "A")
student3.add_grade("Math", "A")
student3.add_grade("English", "A")

teacher1 = Teacher("Lars", 45, 180, 30000)
teacher2 = Teacher("Anna", 35, 170, 25000)
teacher3 = Teacher("Sara", 40, 175)


student1.sleep(8)
teacher1.sleep(8)

teacher3.yell_at_students(student2)

teacher3.raise_salary()
