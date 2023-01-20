from Scenes import *

class Game:

    def __init__(self):
        self.active_scene_name = "Menu"
        self.active_scene = Menu(self)
        self.fpc = FirstPersonController(position = (0,0,5), enabled = False)

    def change_scene(self,scene):
        print(scene)
        self.active_scene_name = scene
        self.active_scene.delete_scene()

        match scene:
            case "Menu":
                self.active_scene = Menu(self)
                self.fpc.enabled = False

            case "FirstScene":
                self.active_scene = FirstScene(self)
                self.fpc.enabled = False

            case "SecondScene":
                self.active_scene = SecondScene(self)
                self.fpc.enabled = True

app = Ursina()

def update():
    match mygame.active_scene_name:
        case "Menu":
            pass

        case "FirstScene":
            if held_keys["q"]:
                mygame.change_scene("Menu")

        case "SecondScene":
            if held_keys["q"]:
                mygame.change_scene("Menu")

mygame = Game()

app.run()