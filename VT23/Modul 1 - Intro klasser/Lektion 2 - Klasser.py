import random
from __future__ import annotations


class Pokemon:
    def __init__(self, element, hp, name, attack) -> None:
        self.element = element
        self.hp = hp
        self.name = name
        self.attack = attack
        self.battles = []

    def __str__(self) -> str:
        return f"{self.name} - HP: {self.hp}"

    def battle(self, other_pokemon: Pokemon):
        print(f"{self.name} attacks {other_pokemon.name}.")

        if random.random() > 0.25:
            self.hp -= other_pokemon.attack
        else:
            print(f"{self.name} dodged the attack.")
        if random.random() > 0.25:
            other_pokemon.hp -= self.attack
        else:
            print(f"{other_pokemon.name} dodged the attack.")
        print(
            f"{self.name} now has {self.hp} hp and {other_pokemon.name} now has {other_pokemon.hp} hp."
        )
        self.battles.append(other_pokemon)
        other_pokemon.battles.append(self)


pokemon1 = Pokemon("Fire", 120, "Charmeleon", 40)
pokemon2 = Pokemon("Fire", 125, "Reshiram", 50)

print(pokemon1)
print(pokemon2)

pokemon1.battle(pokemon2)
