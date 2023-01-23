from dataclasses import dataclass


@dataclass
class Enemy:

    attack: int
    hp: int
    maxhp: int
    charisma: int
    name: str

    def __str__(self) -> str:
        return f"{self.name} - HP : {self.hp}."

    def heal(self, amount):
        if self.hp + amount > self.maxhp:
            self.hp = self.maxhp
        else:
            self.hp += amount


# Vi skapar ett objekt / en instans av klassen Enemy
enemy1 = Enemy(20, 120, 120, 30, "Oskar Åberg")
enemy2 = Enemy(hp=90, maxhp=120, charisma=50, name="Alex Jonsson", attack=20)

print(f"{enemy1.name} attacks {enemy2.name}.")
enemy2.hp -= enemy1.attack
print(f"{enemy2.name} now has {enemy2.hp} hp left. Fs in the chat.")

print(enemy1)


class ClassName:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass
