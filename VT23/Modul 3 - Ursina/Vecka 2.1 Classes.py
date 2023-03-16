# https://www.ursinaengine.org/documentation.html
# In Ursina you can work with 2D and 3D.
# Om du inte kan köra ursina måste du öppna en terminal och skriva in "pip install ursina", klicka sedan på enter.
from UrsinaClasses import *

PLAYER_SPEED = 5

# Create our Ursina-app. Choose size of the game window.
app = Ursina(size=(1600, 900))

# This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = True


# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    pass


counter = 0
score = 0
# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    global counter, score
    counter += 1
    if counter % 30 == 0:
        x = Obstacle(player.x, player.y)
        destroy(x, delay=2)

    player.y += held_keys["w"] * PLAYER_SPEED * time.dt
    player.y -= held_keys["s"] * PLAYER_SPEED * time.dt
    player.x += held_keys["d"] * PLAYER_SPEED * time.dt
    player.x -= held_keys["a"] * PLAYER_SPEED * time.dt

    if apple in player.intersects().entities:
        apple.position = (
            player.x + random.randint(-7, 7),
            player.y + random.randint(-4, 4),
        )
        score += 1
        player.scale *= 1.05

    if player.intersects().entities != [] and apple not in player.intersects().entities:
        player.position = (0, 0)
        score -= 1


# Bakgrundsfärg
# rgb = red, green, blue. Blandning mellan 0 och 255
window.color = rgb(255, 0, 0)
window.color = color.pink

# Call the createworld function
createworld()

player = Entity(model="cube", position=(0, 0), color=color.red, collider="box")
apple = Apple()

camera.parent = player


app.run()
