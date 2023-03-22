from ursina import *
from ursina.prefabs.health_bar import HealthBar


class Obstacle(Entity):
    def __init__(self, player_x, player_y) -> None:
        super().__init__(
            model="sphere",
            position=(
                player_x + random.randint(-7, 7),
                player_y + random.randint(-4, 4),
            ),
            color=rgb(171, 0, 255),
            collider="sphere",
        )


class Apple(Entity):
    def __init__(self) -> None:
        super().__init__(
            model="sphere",
            position=(random.randint(-7, 7), random.randint(-4, 4)),
            color=color.green,
            collider="sphere",
        )


class Brick(Entity):
    def __init__(self, position) -> None:
        super().__init__(
            model="cube", texture="brick", position=position, collider="box"
        )


class Stone(Entity):
    def __init__(self, player) -> None:

        super().__init__(
            model="sphere",
            texture="grass",
            position=(
                random.randrange(-5, 25),
                2,
                random.randrange(-5, 25),
            ),
            collider="sphere",
            player=player,
        )

    def update(self):
        # en_entity.look_at(en annan entity)
        self.look_at(self.player)
        self.position += self.forward * time.dt

        if self.y < 0:
            destroy(self)

        if self.intersects(self.player):
            quit()

        if self.intersects().entities != []:
            for item in self.intersects().entities:
                if isinstance(item, Bullet):
                    destroy(self)


class Enemy(Entity):
    def __init__(self, player) -> None:

        super().__init__(
            model="cube",
            texture=random.choice(["skeleton.png", "sins.jpg", "among.jpg"]),
            position=(
                random.randrange(-5, 25),
                2,
                random.randrange(-5, 25),
            ),
            collider="box",
            player=player,
        )
        health = random.randrange(1, 5)
        self.health = health
        self.health_bar = HealthBar(
            parent=self,
            bar_color=color.lime.tint(-0.25),
            roundness=0.5,
            value=health,
            show_text=False,
            show_lines=False,
        )

    def update(self):
        # en_entity.look_at(en annan entity)
        self.look_at(self.player)
        self.position += self.forward * time.dt

        if self.y < 0:
            destroy(self)

        if self.intersects(self.player):
            quit()

        if self.intersects().entities != []:
            for item in self.intersects().entities:
                if isinstance(item, Bullet):
                    destroy(item)
                    self.health -= 1
                    self.health_bar.value -= 1
                    if self.health == 0:
                        destroy(self)


class Bullet(Entity):
    def __init__(self, player) -> None:

        super().__init__(
            model="sphere",
            color=color.red,
            position=player.position + (0, 2, 0) + player.forward,
            collider="sphere",
            scale=0.2,
            forward=player.forward,
            rotation=player.rotation,
            rotation_x=player.camera_pivot.rotation_x,
        )
        destroy(self, delay=3)

    def update(self):
        self.position += self.forward * time.dt * 50  # * self.acc
        # self.acc *= 1.01
        self.y -= 0.01
