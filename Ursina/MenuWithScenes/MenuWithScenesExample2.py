from Ursina.UrsinaClasses import *

class Game:

    def __init__(self):
        self.fpc = FirstPersonController(position = (0,0,5), enabled = False)
        self.entities = []

    def change_scene(self,scene):
        self.active_scene_name = scene
        for e in self.entities:
            destroy(e)

        match scene:
            case "Menu":
                self.scenenames = ["FirstScene", "SecondScene"]
                for x in range(2):
                    self.entities.append(MenuButton2((x / 10, 0, 0), self, self.scenenames[x]))
                self.fpc.enabled = False

            case "FirstScene":
                self.entities = [
                    MenuButton2((0, 0, 0), self, "Menu"),
                ]
                self.fpc.enabled = False

            case "SecondScene":
                self.entities = [
                    Ground(position=(0, 0, 0), scale=(20, 1, 20)),
                    Sky()
                ]
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
mygame.change_scene("Menu")
app.run()