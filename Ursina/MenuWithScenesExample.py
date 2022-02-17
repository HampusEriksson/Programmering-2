from Scenes import *

class Game:

    def __init__(self):
        self.active_scene_name = "Menu"
        self.active_scene = Menu(self)

    def change_scene(self,scene):
        print(scene)
        self.active_scene_name = scene
        self.active_scene.delete_scene()

        match scene:
            case "Menu":
                self.active_scene = Menu(self)

            case "FirstScene":
                self.active_scene = FirstScene(self)

            case "SecondScene":
                self.active_scene = SecondScene(self)

app = Ursina()

def update():
    match mygame.active_scene_name:
        case "Menu":
            pass

        case "FirstScene":
            pass

        case "SecondScene":
            if held_keys["q"]:
                mygame.change_scene("Menu")

mygame = Game()

app.run()