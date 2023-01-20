from Ursina.UrsinaClasses import *


app = Ursina()


def createworld():

    grounds.append(Entity(model="cube", position=(0,-3.5,48),  texture="brick", scale=(10,0.1,100), collider="cube"))
    grounds.append(Entity(model="cube", position=(0,3.5,48),  texture="brick", scale=(10,0.1,100),collider="cube"))
    grounds.append(Entity(model="cube", position=(5,0,48),  texture="brick", scale=(0.1,7,100),collider="cube"))
    grounds.append(Entity(model="cube", position=(-5,0,48),  texture="brick", scale=(0.1,7,100),collider="cube"))
    grounds.append(Entity(model="cube", position=(0,0,150),  texture="white_cube", scale=(10,7,100), color=color.rgba(255,69,0,75),collider="cube"))



# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    global count
    count += 1
    global speed
    ball.position += ball.forward * time.dt * speed



    player.x = mouse.x * 8
    player.y = mouse.y * 8

    if player in ball.intersects().entities or grounds[4] in ball.intersects().entities:
        speed *= -1.1
        print(ball.rotation)

count = 0
grounds = []
#Call the createworld function
createworld()
ball = Entity(model="sphere", position=(0,0,50), color=color.blue, collider = "sphere")
player = Entity(model="cube", position=(0,0,0),  texture="white_cube", scale=(1,1,1), color=color.rgba(124,252,0,50),collider="cube")
speed = -20

app.run()