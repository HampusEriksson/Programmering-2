# https://www.ursinaengine.org/cheat_sheet.html
# Import everything from my file UrsinaClasses.py so ursina and all my classes are imported
from Ursina.UrsinaClasses import *
# In Ursina you can work with 2D and 3D.

class Game:

    def __init__(self):
        self.score = 0
#Create our Ursina-app
app = Ursina()
mygame = Game()
#This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = False
buttons = []
# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts

count = 0
# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    global count
    count += 1
    activebrick.y -= 0.01 + 0.02*held_keys["s"]
    if count > 5:
        activebrick.rotation_z += held_keys["d"]*90-held_keys["a"]*90

        count = 0




window.color = rgb(119,141,226)
#Call the createworld function
activebrick = TetrisBrick((0,5,0))

Entity(model="cube", scale=(100,1,1), position=(0,-4,0))

app.run()