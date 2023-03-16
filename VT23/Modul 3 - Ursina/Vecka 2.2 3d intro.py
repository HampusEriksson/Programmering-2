# https://www.ursinaengine.org/documentation.html
# Om du inte kan köra ursina måste du öppna en terminal och skriva in "pip install ursina", klicka sedan på enter.
from UrsinaClasses import *
from ursina.prefabs.first_person_controller import FirstPersonController


# Create our Ursina-app. Choose size.
app = Ursina(size=(1600, 900))

# This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = True
window.exit_button.enabled = False


# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    for x in range(20):
        for z in range(20):
            Brick(position=(x, 0, z))


# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
counter = 0


def update():
    global counter
    counter += 1

    if counter % 120 == 0:
        Stone(player=player)

    if player.y < -10:
        player.position = (10, 30, 10)


def input(key):

    if key == "q":
        quit()


player = FirstPersonController(collider="cube", position=(10, 30, 10))

# Call the createworld function
createworld()

Sky()
app.run()
