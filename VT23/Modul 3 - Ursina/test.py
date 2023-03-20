from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time

app = Ursina()


class Bullet(Entity):
    def __init__(self):
        super().__init__()
        self.model = "cube"
        self.scale = 0.4
        self.speed = 50
        self.collider = "box"
        self.x = player.x
        self.y = player.y + 2
        self.z = player.z
        self.color = color.blue
        self.rotation = player.rotation
        self.rotation_x = player.camera_pivot.rotation_x
        self.ahead = Entity(
            model="cube",
            color=color.red,
            rotation=self.rotation,
            collider="box",
            scale=self.scale,
        )

    # an error is occuring here on the bullet class
    def update(self):
        self.ahead.position = self.position
        i = 0
        precollide = False
        while i < self.speed:
            i += 1
            self.ahead.position = self.ahead.position + self.forward * i * time.dt
            ray2 = raycast(
                self.ahead.position,
                (self.forward * i * time.dt),
                ignore=(
                    self,
                    player,
                    self.ahead,
                ),
                distance=0.5,
                debug=False,
            )
            if ray2.hit:
                precollide = True
        direction = self.forward * self.speed * time.dt
        self.position += direction
        ray = raycast(
            self.position,
            direction,
            ignore=(
                self,
                player,
                self.ahead,
            ),
            distance=0.5,
            debug=False,
        )
        if ray.hit or precollide:
            destroy(self)


def input(key):
    global bullets
    if key == "b":
        Bullet()
    if key == "q":
        quit()


player = FirstPersonController()

ground = Entity(model="plane", scale_x=100, scale_z=100, collider="box")

dummy = Entity(model="cube", position=(0, 1, -4), color=color.red, collider="box")

bullets = []

app.run()
