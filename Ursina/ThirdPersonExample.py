# Import everything from my file UrsinaClasses.py so ursina and all my classes are imported
from Ursina.UrsinaClasses import *
# In Ursina you can work with 2D and 3D.

#Create our Ursina-app
app = Ursina()

#This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = False

# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    pass

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    player.position += player.forward * time.dt

    if held_keys["d"]:
        player.rotation_y += 5

    if held_keys["a"]:
        player.rotation_y -= 5

    for obstacle in obstacles:
        if player.intersects(obstacle).hit:
            print("Game over")
            sys.exit()

#Call the createworld function
createworld()

player = Entity(parent=scene,
            position=(0,0,0),
            model="cube",
            texture = "/Images/barbar.jpg",
            collider='box')

camera.parent = player
camera.position = (0, 11, -15)
camera.rotation = (30, 0, 0)


obstacles = [
    Ground(position = (5,0,0)),
    Ground(position = (3,0,0)),
    Ground(position = (7,0,0)),
    Ground(position = (4,0,0))
]

app.run()