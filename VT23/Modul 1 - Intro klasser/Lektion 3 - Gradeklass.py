course_points = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "F": 0}


class Grade:
    # points = 100 är ett default värde
    # Om inget annat värde skickas in, så blir points 100
    def __init__(self, grade, course, points=100) -> None:
        self.grade = grade
        self.course = course
        self.points = points
        self.passed = False if grade == "F" else True
        self.value = course_points[grade]

    def __str__(self) -> str:
        return f"{self.course} - {self.grade}"

    def meritvalue(self):
        # Metoden ska printa meritvärde
        pass

    def prövning(self):
        if self.grade == "F":
            new_grade = input("What is the new grade?")
            self.grade = new_grade
        else:
            print("You can only do prövning when you have F.")


my_grades = []
while True:
    choice = input("1. Add grade\n2. Look at grades\n3. Print meritvalue\n4. Quit\n")

    if choice == "1":
        course = input("What course do you want to register?")
        grade = input("What grade did you get?").capitalize()
        point = int(input("How many points was the course?"))
        my_grades.append(Grade(grade, course, point))
    elif choice == "2":
        for grade in my_grades:
            print(grade)

    elif choice == "3":
        pass

    elif choice == "4":
        print("Good bye")
        break
