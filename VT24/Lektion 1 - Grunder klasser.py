# Tidigare datatyper
# Listor, dictionaries, funktioner
import random


# Skapar en klass som heter Pokemon
class Pokemon:
    # init definierar klassens attribut / egenskaper
    def __init__(self, type, move, hp, name, damage) -> None:
        self.type = type
        self.move = move
        self.hp = hp
        self.name = name
        self.damage = damage

    # str-metoden visar vad som ska printas om objektet printas ut
    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nHp: {self.hp}\n"

    def battle(self, other_pokemon):
        print(f"{self.name} is attacking {other_pokemon.name}")
        self.hp -= random.randint(other_pokemon.damage - 10, other_pokemon.damage + 10)
        other_pokemon.hp -= random.randint(self.damage - 10, self.damage + 10)

    def heal(self):
        self.hp = 100


pokemon1 = Pokemon("electric", "thunder bolt", 40, "Pikachu", 40)
pokemon2 = Pokemon("fire", "flamethrower", 38, "Charmander", 30)
pokemon3 = Pokemon("normal", "sleep", 70, "Snorlax", 0)


print(pokemon3.hp)
pokemon1.battle(pokemon3)
print(pokemon3.hp)
