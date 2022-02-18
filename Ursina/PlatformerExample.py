from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
camera.orthographic = True
camera.fov = 20
obstacles = []
ground = Entity(
    model = 'cube',
    color = color.olive.tint(-.4),
    z = -.1,
    y = -1,
    origin_y = .5,
    scale = (1000, 100, 10),
    collider = 'box',
    ignore = True,
    )
def update():
    global counter
    counter += 1
    player.scale = (1,2,1) if held_keys["s"] else (1,4,1)
    for o in obstacles:
        o.x -= time.dt*5
    if counter % 60 == 0:
        obstacles.append(
            Entity(
                model='cube',
                color=color.red,
                collider='box',
                position = (player.x + 10, random.choice([0.5,3]), 0)
            )
    )

    for o in obstacles:
        if player.intersects(o).hit:
            print("Game over")
            sys.exit()

player = PlatformerController2d(scale = (1,4,1))
camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))
counter = 0

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')



app.run()