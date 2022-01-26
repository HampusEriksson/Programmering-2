class Animal:

    def __init__(self, length,weight, age, gender, species):
        self.length = length
        self.weight = weight
        self.age = age
        self.gender = gender
        self.species = species

class Fish(Animal):

    def __init__(self, length,weight, age, gender, fin_count, watertype):
        super(Fish, self).__init__(length,weight, age, gender, "Fish")
        self.fin_count = fin_count
        self.watertype = watertype

class Monkey(Animal):

    def __init__(self, length,weight, age, gender, tail_length):
        super(Monkey, self).__init__(length,weight, age, gender, "Monkey")
        self.tail_length = tail_length

class Elephant(Animal):

    def __init__(self, length,weight, age, gender, trunk_length):
        super(Elephant, self).__init__(length,weight, age, gender, "Elephant")
        self.trunk_length = trunk_length

nemo = Fish(50, 20, 5, 2, "male", "salt")
print(nemo.length)