# Import everything from my file UrsinaClasses.py so ursina and all my classes are imported
from Ursina.UrsinaClasses import *
# In Ursina you can work with 2D and 3D.

# Import the FirstPersonController is you want to do a first person game
from ursina.prefabs.first_person_controller import FirstPersonController

# Import the PlatformerController2d is you want to do a platform game


#Create our Ursina-app
app = Ursina()

#This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = False

# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    Ground(scale = (30,1,30))

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    if sun.x > 15 or sun.z > 15:
        sun.speed = -1
    if sun.x < -15 or sun.z < -15:
        sun.speed = 1
    sun.x += sun.speed * time.dt
    sun.z += sun.speed * time.dt

    for s in suns:
        if s.x > 15 or s.z > 15:
            sun.speed = -1
        if s.x < -15 or s.z < -15:
            s.speed = 1
        s.x += s.speed * time.dt
        s.z += s.speed * time.dt


#Call the createworld function
createworld()

# Creates a sky with the variable name sky. This is a prefab in Ursina
sky = Sky()

# If you want a first person game you have to create a player with a given position
player = FirstPersonController(position = (0,0,0))
suns = [Sun(position = (5,5,5)), Sun(position = (8,8,8))]
sun = Sun()
wall = Entity(model="cube", scale=(1,3,1), collider="cube")
app.run()