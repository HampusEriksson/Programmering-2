class Person:

    def __init__(self, name, year, month):
        self.name = name
        self.year = year
        self.month = month

    def __str__(self):
        return f"Name: {self.name} Year: {self.year}"
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

    def __add__(self, other):
        if isinstance(other, Person):
            return Person(self.name[:int(len(self.name)/2)]+other.name[int(len(self.name)/2):], int((self.year+other.year)/2),int((self.month+other.month)/2) )

        elif isinstance(other, int):
            return Person(self.name, self.year+other, self.month)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

# /
    def __truediv__(self, other):
        pass

# //
    def __floordiv__(self, other):
        pass
p1 = Person("Mary", 2004, 4)
p2 = Person("Ida", 2004, 9)
p3 = Person("Fabian", 2004, 4)

print(p1 < p3)