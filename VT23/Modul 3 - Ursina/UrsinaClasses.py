from ursina import *


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

    def input(self, key):
        if self.hovered and key == "left mouse down":
            destroy(self)
