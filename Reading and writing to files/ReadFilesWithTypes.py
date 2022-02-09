# Creates a class named MyClass
class Student:

    # The __init__ method declares the attribute of the class and gives values to the attributes
    def __init__(self, name, perssonnr, fav_food, fav_subject, fav_hobby):
        self.name = name
        self.perssonnr = perssonnr
        self.fav_food = fav_food
        self.fav_subject = fav_subject
        self.fav_hobby = fav_hobby

    # The __str__ method defines what will be printed when an object of the class is printed
    def __str__(self):
        return f"Namn: {self.name} Personnummer: {self.perssonnr}"


students = []
with open("Students.csv", "r", encoding="utf8") as file:
    #print(type(file))
    for row in file:
        row = row.strip("\n")
        #print(type(row), row)
        row_list = row.split(",")
        #print(type(row_list), row_list)
        students.append(Student(
            row_list[0], row_list[1], row_list[2], row_list[3], row_list[4]
        ))


for student in students:
    if "spel" in student.fav_hobby.lower():
        print(student.name, student.fav_hobby)
