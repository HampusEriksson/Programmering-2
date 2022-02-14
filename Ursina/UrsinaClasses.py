from ursina import *

class Ground(Entity):

    def __init__(self, scale = (1,1,1), position=(0, 0, 0)):
        super(Ground, self).__init__(
            parent=scene,
            position=position,
            model="cube",
            color = rgb(128, 128, 0) ,
            collider='box',
            scale = scale
        )

class Target(Entity):

    def __init__(self, game):
        test = random.random()
        if test < 0.25:
            position = (20, random.randrange(3,7) , random.randrange(0,20))

        elif test< 0.5:
            position = (0, random.randrange(3,7) , random.randrange(0,20))

        elif test < 0.75:
            position = (random.randrange(0,20), random.randrange(3,7) , 20)

        else:
            position = (random.randrange(0,20), random.randrange(3,7) , 0)

        self.speed = 1
        self.game = game
        super(Target, self).__init__(
            parent=scene,
            model="cube",
            texture="Images/barbar.jpg",
            position=position,
            collider = 'cube')

    def input(self, key):
        if self.hovered and key == 'left mouse down':
            destroy(self)
            self.game.targets.remove(self)

    def update(self):
        self.lookAt(self.game.player.position + (0,3,0))
        self.position += self.forward * time.dt * self.game.level
        self.scale = 1/self.game.level


class Sun(Entity):

    def __init__(self, position=(10, 10, 10)):
        self.speed = 1
        super(Sun, self).__init__(
            parent=scene,
            position=position,
            model="sphere",
            color=color.yellow,
        )