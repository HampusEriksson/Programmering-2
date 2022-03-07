from UrsinaClasses import *

app = Ursina()



def update():
    controller.animations[controller.state].rotation_z += 5 * time.dt


def input(key):
    if key == "1":
        controller.state = "red"

    elif key == "2":
        controller.state = "green"

    elif key == "3":
        controller.state = "elmo"
EditorCamera()

controller = Animator(
    animations= {
        "red":Entity(model="cube", color=color.red),
        "green":Entity(model="cube", color=color.green, collider="cube"),
        "elmo":Animation("/images/elmo.gif")
    }
)
app.run()