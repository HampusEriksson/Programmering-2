class Animal:
    def __init__(self, length, weight, age, gender, species):

        self.length = length

        self.weight = weight

        self.age = age

        self.gender = gender

        self.species = species

    def age_up(self):

        self.age += 1


class Fish(Animal):
    def __init__(self, length, weight, age, gender, fin_count, watertype):

        super(Fish, self).__init__(length, weight, age, gender, "Fish")

        self.fin_count = fin_count

        self.watertype = watertype


class Monkey(Animal):
    def __init__(self, length, weight, age, gender, tail_length):

        super(Monkey, self).__init__(length, weight, age, gender, "Monkey")

        self.tail_length = tail_length


class Elephant(Animal):
    def __init__(self, length, weight, age, gender, trunk_length):

        super(Elephant, self).__init__(length, weight, age, gender, "Elephant")

        self.trunk_length = trunk_length


class Pokemon:
    def __init__(self, name, hp, level=1):

        self.name = name

        self.hp = hp

        self.level = level

        self.happiness = -2

    def __str__(self):

        return f"Name: {self.name} \nHP: {self.hp} \nLevel: {self.level}"

    def levelup(self):

        self.level += 1

        self.hp = round(self.hp * 1.05)

        self.happiness -= 1

        print(f"{self.name} has leveled up to level {self.level}.")


class Elev:
    def __init__(self, name, grade, personnr):

        self.name = name

        self.grade = grade

        self.personnr = personnr

    def raise_grade(self):

        self.grade += 1

        print(f"Grade raised to {self.grade}")
