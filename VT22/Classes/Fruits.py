class Fruit:

    def __init__(self,
                 name=input("What is the name of the fruit?"),
                 color=input("What color is the fruit?"),
                 ripe = input("Is the fruit ripe?") == "yes"
                 ):
        self.name = name
        self.color = color
        self.ripe = ripe

    def __str__(self):
        return f"{self.color} {self.name} that is {'ripe' if self.ripe else 'not ripe'}."



class FruitBowl:

    def __init__(self):
        self.fruits = []

    def print_content(self):
        print( *self.fruits)

    def add_fruit(self):
        """Add fruit to the fruitbowl"""

        new_fruit = Fruit()
        self.fruits.append(new_fruit)
        print("Fruit added")

my_fruitbowl = FruitBowl()
my_fruitbowl.add_fruit()
my_fruitbowl.print_content()