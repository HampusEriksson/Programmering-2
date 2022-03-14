class Person:

    def __init__(self, name, year, month):
        self.name = name
        self.year = year
        self.month = month

    def __lt__(self, other):
        if isinstance(other, int):
            return self.year < other

        elif isinstance(other, str):
            return self.name < other

        elif isinstance(other, Person):
            if self.year < other.year:
                return True
            elif self.year > other.year:
                return False
            elif self.year == other.year:
                return self.month < other.month

    def __gt__(self, other):
        if isinstance(other, int):
            return self.year > other

        elif isinstance(other, str):
            return self.name > other

        elif isinstance(other, Person):
            if self.year > other.year:
                return True
            elif self.year < other.year:
                return False
            elif self.year == other.year:
                return self.month > other.month

    def __eq__(self, other):
        if isinstance(other, int):
            return self.year == other

        elif isinstance(other, str):
            return self.name == other

        elif isinstance(other, Person):
            return self.year == other.year and self.month == other.month
    def __le__(self, other):
        return self<other or self==other

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self,other):
        return not self == other
p1 = Person("Mary", 2004, 4)
p2 = Person("Ida", 2004, 9)
p3 = Person("Fabian", 2004, 6)

print(p1 <= p3)