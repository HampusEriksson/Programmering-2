from ursina import *

class Ground(Entity):

    def __init__(self, position=(0, 0, 0)):
        super(Ground, self).__init__(
            parent=scene,
            position=position,
            model="cube",
            texture="white_cube",
            color=color.gray,
            collider='box'
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)


            if key == 'right mouse down':
                del self


class Target(Entity):

    def __init__(self, i):
        self.speed = 1
        super(Target, self).__init__(
            parent=scene,
            model="cube",
            texture="target.png",
            position=(20, random.randrange(3, 7), 5 + i),
            collider = 'sphere')

    def input(self, key):
        if self.hovered and key == 'left mouse down':
            destroy(self)

    def update(self):
        try:
            if self.z >= 20 or self.z<=0:
                self.speed *= -1

            self.z += self.speed * time.dt
        except AssertionError:
            print("AssertionError")
