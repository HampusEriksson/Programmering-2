# https://www.ursinaengine.org/cheat_sheet.html
# Import everything from my file UrsinaClasses.py so ursina and all my classes are imported
from UrsinaClasses import *
# In Ursina you can work with 2D and 3D.

# Import the FirstPersonController is you want to do a first person game
from ursina.prefabs.first_person_controller import FirstPersonController

# Import the PlatformerController2d is you want to do a platform game
from ursina.prefabs.platformer_controller_2d import PlatformerController2d



#Create our Ursina-app
app = Ursina()

#This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = False

# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    ClickerButton("Go to bridge",0,0, load_bridge)

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    pass

def load_bridge():
    sky = Sky()
    player = FirstPersonController(collider="cube", position=(10, 30, 10))
#Call the createworld function
createworld()

# Creates a sky with the variable name sky. This is a prefab in Ursina

# If you want a first person game you have to create a player with a given position

app.run()