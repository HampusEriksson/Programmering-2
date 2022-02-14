# https://www.ursinaengine.org/cheat_sheet.html
# Import everything from my file UrsinaClasses.py so ursina and all my classes are imported
from UrsinaClasses import *
# In Ursina you can work with 2D and 3D.


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
    for i in range(-2,3):
        print("hej")
        WordleButton((i/8,0.4,0))

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    pass


#Call the createworld function
createworld()

app.run()