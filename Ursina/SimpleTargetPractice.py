# Cheat sheet for ursina : https://www.ursinaengine.org/cheat_sheet.html#Entity

# Import ursina so we can use the module
from ursina import *
from UrsinaClasses import *
from UrsinaConstants import *
# In Ursina you can work with 2D and 3D.

# Import the FirstPersonController if you want to do a first person game
from ursina.prefabs.first_person_controller import FirstPersonController

# Import the PlatformerController2d is you want to do a platform game
# from ursina.prefabs.platformer_controller_2d import PlatformerController2d



#Create our Ursina-app
app = Ursina()

#This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = False

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    for t in targets:
        t.update()


# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    for z in range(20):
        for x in range(20):
            Ground(position=(x, 0, z))

    return [
        Target(i)
        for i in range(10)
    ]
#Call the createworld function
targets = createworld()

# Creates a sky with the variable name sky. This is a prefab in Ursina
sky = Sky()

# If you want a first person game you have to create a player with a given position
player = FirstPersonController(position = (10,10,10))


app.run()
