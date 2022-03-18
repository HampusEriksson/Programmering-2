from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Obstacle(Entity):

    def __init__(self, x):
        super(Obstacle, self).__init__(model='cube',
                color=color.red,
                collider='box',
                position = (x + 10, random.choice([0.5,3]), 0))


class Ground(Entity):

    def __init__(self, scale = (1,1,1), position=(0, 0, 0)):
        super(Ground, self).__init__(
            parent=scene,
            position=position,
            model="cube",
            texture="white_cube",
            color=color.blue,
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

class ReactionButton(Button):
    def __init__(self, position, game):
        super().__init__()
        self.position = position
        self.scale = 0.1
        self.disabled = False
        self.color = color.red
        self.highlight_color = self.color.tint(0.2)
        self.pressed_color = self.color.tint(-0.2)
        self.game = game


    def on_click(self):
        if self.color == color.green:
            self.color = color.red
            self.highlight_color = self.color.tint(0.2)
            self.pressed_color = self.color.tint(-0.2)
            self.game.score += 1

        else:
            self.game.score -= 1

    def activate(self):
        self.color = color.green
        self.highlight_color = self.color.tint(0.2)
        self.pressed_color = self.color.tint(-0.2)

class MenuButton(Button):
    def __init__(self, position, scene, target):
        super().__init__()
        self.position = position
        self.scale = 0.1
        self.disabled = False
        self.color = rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.highlight_color = self.color.tint(0.2)
        self.pressed_color = self.color.tint(-0.2)
        self.scene = scene
        self.text = Text(parent=self, text=target, scale=5, color= color.black)
        self.target = target


    def on_click(self):
        self.scene.game.change_scene(self.target)

class MenuButton2(Button):
    def __init__(self, position, game, target):
        super().__init__()
        self.position = position
        self.scale = 0.1
        self.disabled = False
        self.color = rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.highlight_color = self.color.tint(0.2)
        self.pressed_color = self.color.tint(-0.2)
        self.text = Text(parent=self, text=target, scale=5, color= color.black)
        self.target = target
        self.game = game


    def on_click(self):
        self.game.change_scene(self.target)