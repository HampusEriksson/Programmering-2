# https://www.ursinaengine.org/documentation.html
# In Ursina you can work with 2D and 3D.
# Om du inte kan köra ursina måste du öppna en terminal och skriva in "pip install ursina", klicka sedan på enter.
from ursina import *

PLAYER_SPEED = 5

# Create our Ursina-app. Choose size of the game window.
app = Ursina(size=(1600, 900))

# This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = True
window.exit_button.enabled = True


# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    for _ in range(10):
        Entity(
            model="sphere",
            position=(random.randint(-7, 7), random.randint(-4, 4)),
            color=rgb(171, 0, 255),
            collider="sphere",
        )


counter = 0
score = 0
# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    global counter, score
    counter += 1
    if counter % 120 == 0:
        pass

    player.y += held_keys["w"] * PLAYER_SPEED * time.dt
    player.y -= held_keys["s"] * PLAYER_SPEED * time.dt
    player.x += held_keys["d"] * PLAYER_SPEED * time.dt
    player.x -= held_keys["a"] * PLAYER_SPEED * time.dt

    if abs(player.x) >= 7:
        player.x *= -1

    if abs(player.y) > 4:
        player.y *= -1

    pos_text.text = f"x: {round(player.x, 1)} y: {round(player.y, 1)}"
    score_text.text = f"Score: {score}"

    if apple in player.intersects().entities:
        apple.position = (random.randint(-7, 7), random.randint(-4, 4))
        score += 1
        player.scale *= 1.05

    if player.intersects().entities != [] and apple not in player.intersects().entities:
        player.position = (0, 0)
        score -= 1


# Bakgrundsfärg
# rgb = red, green, blue. Blandning mellan 0 och 255
window.color = rgb(255, 0, 0)
window.color = color.blue

# Call the createworld function
createworld()

player = Entity(model="cube", position=(0, 0), color=color.red, collider="box")
apple = Entity(
    model="sphere",
    position=(random.randint(-7, 7), random.randint(-4, 4)),
    color=color.green,
    collider="sphere",
)
pos_text = Text(position=(-0.65, 0.45))
score_text = Text(position=(-0.65, 0.35))
app.run()

"""
Built in models
quad	
wireframe_cube	
plane	
circle	
diamond	
wireframe_quad	
sphere	
cube	
icosphere	
cube_uv_top	
arrow	
sky_dome	"""
