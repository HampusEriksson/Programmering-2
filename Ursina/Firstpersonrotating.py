# Import ursina so we can use the module
from ursina import *
# In Ursina you can work with 2D and 3D.

# Import the FirstPersonController is you want to do a first person game
from ursina.prefabs.first_person_controller import FirstPersonController

# Import the PlatformerController2d is you want to do a platform game
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

class Obstacle(Entity):

    def __init__(self):
        super(Obstacle, self).__init__(
            parent=scene,
            position=(random.randrange(0,20), 0.5,20),
            model="cube",
            texture="white_cube",
            color= random.choice([color.green, color.red, color.blue, color.yellow]),
            collider='box'
        )

    def upd(self):
        self.position.z = self.position.z - 1
        print(self.position.z)
        if self.position.z < -10:
            del self

#Create our Ursina-app
app = Ursina()

#This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = False
COLORS = [color.green, color.red, color.blue, color.yellow]
obstacles = []
obstacles.append(Obstacle())
# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    if player.x < 1 and player.y <1:
        player.position = (1,10,10)
        player.rotation=(90,90,0)

    for o in obstacles:
        o.upd()
    """for i, color in enumerate(world):
        for j, box in enumerate(color):
            box.color = COLORS[(i+1) % (len(world))]
    COLORS.append(COLORS.pop(0))"""



# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    world = []
    colors = []
    for z in range(20):
        for x in range(20):
            colors.append(Entity(parent=scene,
            position=(x,0,z),
            model="cube",
            texture="white_cube",
            color=color.green,
            collider='box'))
    world.append(colors)
    colors = []
    for z in range(20):
        for x in range(20):
            colors.append(Entity(parent=scene,
            position=(0,x,z),
            model="cube",
            texture="white_cube",
            color=color.red,
            collider='box'))
    world.append(colors)
    colors = []
    for z in range(20):
        for x in range(20):
            colors.append(Entity(parent=scene,
            position=(x,20,z),
            model="cube",
            texture="white_cube",
            color=color.blue,
            collider='box'))
    world.append(colors)
    colors = []
    for z in range(20):
        for x in range(20):
            colors.append(Entity(
            parent=scene,
            position=(20,x,z),
            model="cube",
            texture="white_cube",
            color=color.yellow,
            collider='box'))
    world.append(colors)
    return world

#Call the createworld function
world = createworld()

# Creates a sky with the variable name sky. This is a prefab in Ursina
sky = Sky()

# If you want a first person game you have to create a player with a given position
player = FirstPersonController(position = (10,25,10))
app.run()
