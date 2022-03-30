from ursina.prefabs.first_person_controller import FirstPersonController
from ursinanetworking import *
from ursina.shaders import basic_lighting_shader
from random import *


class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mouse_sensitivity = (155, 155)

class PlayerRepresentation(Entity):
    def __init__(self, position = (5,5,5)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            texture = "white_cube",
            origin_y = .5,
            color = color.white,
            highlight_color = color.white,
            scale = (0.5, 1, 0.5)
        )
        print("HELLO !")

BLOCKS_PARENT = Entity()


class Grass(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            parent=BLOCKS_PARENT,
            position=position,
            model="block",
            origin_y=.5,
            color=color.white,
            highlight_color=color.white,
            scale=1,
            collider="cube"
        )





class BreakParticle(Entity):

    def __init__(self, texture, position=(0, 0, 0)):
        super().__init__(
            position=position,
            model="block",
            texture=texture,
            origin_y=.5,
            billboard=True,
            color=color.white,
            highlight_color=color.white,
            scale=(
                uniform(0.01, 0.25),
                uniform(0.01, 0.25),
                uniform(0.0, 0.0)
            ),
            shader=basic_lighting_shader
        )

        self.s = 0.05
        self.velx = uniform(-self.s, self.s)
        self.vely = uniform(0, 0.1)
        self.velz = uniform(-self.s, self.s)
        self.animate_scale(0, uniform(0.75, 1))
        destroy(self, 1)

    def update(self):
        r = raycast(self.position, (0, -1, 0), ignore=(self,), distance=0.1, debug=False).hit
        if not r:
            self.position += (self.velx, self.vely, self.velz)
            self.vely -= 0.009