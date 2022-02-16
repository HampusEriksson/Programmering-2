# https://www.ursinaengine.org/cheat_sheet.html
# Import everything from my file UrsinaClasses.py so ursina and all my classes are imported
from UrsinaClasses import *
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
def createworld():
    for x in range(-5,6,2):
        for y in range(-2,3,2):
            buttons.append(ReactionButton((x/10,y/10,0),mygame ))

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    if all(button.color == color.red for button in buttons):
        random.choice(buttons).activate()

    score_text.text = str(mygame.score)


window.color = rgb(119,141,226)
#Call the createworld function
createworld()
score_text = Text(text=str(mygame.score))
app.run()