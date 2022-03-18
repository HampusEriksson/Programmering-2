class Person:

    def __init__(self, name, year, month):
        self.name = name
        self.year = year
        self.month = month


p1 = Person("Mary", 2004, 4)
p2 = Person("Ida", 2004, 9)
p3 = Person("Fabian", 2004, 6)

print(p1 * p3)