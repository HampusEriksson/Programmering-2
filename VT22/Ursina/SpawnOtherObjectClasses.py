from ursina import *

class MyButton(Button):
    def __init__(self, position):
        super().__init__(position=position, scale=0.1, color=color.green, highlight_color=color.green.tint(0.2),
                         pressed_color=color.green.tint(-0.2))

    def on_click(self):
        click_audio = Audio('click2.mp3', pitch=1)
        click_audio.play()
        if random.random() > 0.5:
            RandomMovingObject()
        else:
            Projectile()

class RandomMovingObject(Entity):

    def __init__(self):
        super().__init__(position=(0, 0, 0), model="cube", color=color.red)

    def update(self):
        self.x += random.randint(-1, 1) / 10
        self.y += random.randint(-1, 1) / 10

        if abs(self.x) > 5 or abs(self.y) > 5:
            destroy(self)

class Projectile(Entity):
    def __init__(self):
        super().__init__(position=(0, 0, 0), model="cube", color=color.blue)
        self.speed = (random.randint(-1, 1) / 10, random.randint(-1, 1) / 10,0)

    def update(self):
        self.position += self.speed

        if abs(self.x) > 5 or abs(self.y) > 5:
            destroy(self)
