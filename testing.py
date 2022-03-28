import socket
import threading

import numpy as np
from ursina import *



app = Ursina()


# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.






def update():
    print((held_keys["d"] - held_keys["a"]))
    player.x += (held_keys["d"] - held_keys["a"])*time.dt
    player.y += (held_keys["w"] - held_keys["s"])*time.dt



player = Entity(model="cube", position=(0,0,0),color=rgb(random.randrange(255),random.randrange(255),random.randrange(255)))

app.run()
