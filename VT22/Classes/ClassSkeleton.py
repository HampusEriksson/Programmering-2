#Creates a class named MyClass
class MyClass:

    # The __init__ method declares the attribute of the class and gives values to the attributes
    def __init__(self, attr1, attr2, attr3 = 1337):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = "Hello world"

    # The __str__ method defines what will be printed when an object of the class is printed
    def __str__(self):
        return self.attr1 + " " + self.attr4
