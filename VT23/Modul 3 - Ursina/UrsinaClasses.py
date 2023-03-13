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
