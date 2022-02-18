# Cheat sheet for ursina : https://www.ursinaengine.org/cheat_sheet.html#Entity
import sys
sys.path.append('/Programmering 2/Ursina')
# Import ursina so we can use the module

from Ursina.UrsinaClasses import *
from dataclasses import dataclass

# Import the FirstPersonController if you want to do a first person game
from ursina.prefabs.first_person_controller import FirstPersonController

@dataclass
class Game:
    targets = []
    level = 1


    def spawntargets(self):
        self.targets = [
            Target(self)
            for _ in range(10)
        ]


mygame = Game()
#Create our Ursina-app
app = Ursina()

#This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = False

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    for t in mygame.targets:
        t.update()
        if distance(t,mygame.player) < 1.5:
            print("Game over")
            app.quit()

    if not mygame.targets:
        mygame.level += 1
        mygame.spawntargets()
        mygame.player.position = (10,25,10)


# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    for x in range(20):
        for z in range(20):
            Ground(position=(x, 0, z))

createworld()
#Call the createworld function

# Creates a sky with the variable name sky. This is a prefab in Ursina
sky = Sky()
mygame.player = FirstPersonController(collider = "cube", position=(10, 30, 10))
# If you want a first person game you have to create a player with a given position
mygame.spawntargets()


app.run()
