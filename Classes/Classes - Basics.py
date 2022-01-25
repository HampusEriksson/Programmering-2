# Genomgång 19/1

class Pokemon:

    # Funktion i en class kallas metod
    def __init__(self, name, hp, level = 1):
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


all_pokemon = [Pokemon("Meowth", 100), Pokemon("Mewtwo", 550, 100)]

for _ in range(200):
    all_pokemon[0].levelup()