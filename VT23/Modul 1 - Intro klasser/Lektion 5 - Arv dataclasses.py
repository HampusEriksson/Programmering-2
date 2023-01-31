from dataclasses import dataclass


@dataclass
class Enemy:

    attack: int
    hp: int
    maxhp: int
    name: str
    type: str

    def heal(self, amount):
        if self.hp + amount > self.maxhp:
            self.hp = self.maxhp
        else:
            self.hp += amount
