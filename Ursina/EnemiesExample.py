from Ursina.UrsinaClasses import *

class MyGame:

    def __init__(self, player):
        self.player = player
        self.level = 1

class Enemy(Entity):

    def __init__(self, position, scale, texture, damage, health, game):
        super(Enemy, self).__init__(position=position, scale=scale, texture=texture, model="cube")
        self.damage = damage
        self.health = health
        self.game = game

    def update(self):
        pass


class Dragon(Enemy):

    def __init__(self, position, wingspan, game):
        super(Dragon, self).__init__(position, 3, "Images/dragon.png", random.randrange(100, 200),
                                     random.randrange(1000, 2000), game)
        self.wingspan = wingspan

    def update(self):
        self.look_at(target=self.game.player)
        self.position += self.forward * time.dt

class Dwarf(Enemy):

    def __init__(self, position, game):
        super(Dwarf, self).__init__(position, 0.5, "Images/dwarf.jpg", random.randrange(10, 20),
                                    random.randrange(100, 200), game)

    def gearup(self):
        self.damage *= 5

    def update(self):
        self.look_at(target=self.game.player)
        self.position += self.forward * time.dt

app = Ursina()


def createworld():
    Ground(scale=(30, 1, 30))

def update():
    pass

createworld()
sky = Sky()
player = FirstPersonController(position=(0, 0, 0))
mygame = MyGame(player)
enemies = []
enemies.append(Dragon((0, 10, 0), 30, mygame))
enemies.append(Dwarf((3, 1, 3), mygame))

app.run()
