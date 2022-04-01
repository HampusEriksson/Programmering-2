import socket
import threading

import numpy as np
from ursina import *



app = Ursina()


# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.






def update():
    player.y -= player.speed* time.dt

    if player.y <-3 and player.speed>0:
        player.speed = -1

    elif player.speed < 0:
        player.speed += 0.01

def spawn_ent():
    Entity(model="cube", position=(random.random()),color=rgb(random.randrange(255),random.randrange(255),random.randrange(255)))

player = Entity(model="cube", position=(0,0,0),color=rgb(random.randrange(255),random.randrange(255),random.randrange(255)), speed = 1)

b = WindowPanel(
    title="Options",

)

b.on_click = spawn_ent
app.run()
