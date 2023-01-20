# Creates a class named MyClass
class Student:

    # The __init__ method declares the attribute of the class and gives values to the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # The __str__ method defines what will be printed when an object of the class is printed
    def __str__(self):
        return self.name + " : " + str(self.age)
