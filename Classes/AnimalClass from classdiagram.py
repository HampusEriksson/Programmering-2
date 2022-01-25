#Creates a class named MyClass
class Animal:

    # The __init__ method declares the attribute of the class and gives values to the attributes
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        self.hunger = 0

    # The __str__ method defines what will be printed when an object of the class is printed
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nHunger: {self.hunger}"

    def make_noise(self):
        for _ in range(3):
            print(self.sound.upper())

    def eat(self):
        self.hunger -= 2
        self.hunger = max(self.hunger, 0)

my_animal = Animal("Noppen", 18, "Mjauw")
my_other_animal = Animal("Fido", 12, "Voff")
print(my_animal)

my_animal.make_noise()
