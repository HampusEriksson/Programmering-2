class Person:

    def __init__(self, name, year, month):
        self.name = name
        self.year = year
        self.month = month

    def __lt__(self, other):
        if isinstance(other, Person):
            if self.year < other.year:
                return True
            elif self.month<other.month:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, Person):
            if self.year > other.year:
                return True
            elif self.month>other.month:
                return True
            else:
                return False

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.year == other.year and self.month == other.month

vlad = Person("vlad", 2004, 9)
hampus = Person("hampus", 1994,1)
print(vlad>hampus)