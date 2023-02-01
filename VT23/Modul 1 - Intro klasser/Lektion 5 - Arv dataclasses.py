from dataclasses import dataclass
import random


@dataclass
class Enemy:

    attack: int
    hp: int
    maxhp: int
    name: str
    type: str
    crit: int

    def heal(self, amount):
        if self.hp + amount > self.maxhp:
            self.hp = self.maxhp
        else:
            self.hp += amount

    def attack(self, other: "Enemy"):
        if random.random < 0.05:
            other.hp -= self.crit * self.attack
        else:
            other.hp -= self.attack


@dataclass
class Goblin(Enemy):
    gold: int = 20
    type: str = "Goblin"

    def steal(self, amount):
        self.gold += amount


@dataclass
class Dragon(Enemy):

    attack = random.randrange(100, 200)
    type: str = "Dragon"
    wingspan: int = 20


enemies = []
enemies.append(Goblin(50, 100, 100, "Fares"))

enemies.append(Goblin(attack=20, hp=100, maxhp=100, name="Adam", gold=100))

enemies[1].steal(1000)
print(enemies[1])
