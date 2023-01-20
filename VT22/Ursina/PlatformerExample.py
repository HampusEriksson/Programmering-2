from UrsinaClasses import *
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

counter = 0
speed = 1
def update():
    global counter, speed
    counter += 1
    player.scale = (1,2,1) if held_keys["s"] else (1,4,1)
    """for o in obstacles:
        o.x -= time.dt*5*speed"""

    for o in obstacles:
        if o.x < player.x-5:
            o.x += 200
            speed *= 1.05

    origin = player.world_position + (0,player.scale_y,)
    hit_info = raycast(origin, (1,0,0), ignore=(player,),  distance=0.55, debug=True)
    hit_info2 = raycast(player.world_position+ (0,player.scale_y/2,), (1,0,0), ignore=(player,),  distance=0.55, debug=True)

    if hit_info.hit or hit_info2.hit:
        player.x -= time.dt*5*speed

    """for o in obstacles:
        if player.intersects(o).hit:
            print("Game over"""

player = PlatformerController2d(scale = (1,4,1))
camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))

for x in range(20):
    obstacles.append(
        Obstacle(
            x*10
        ))

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')



app.run()