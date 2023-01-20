from Ursina.UrsinaClasses import *

class Game:

    def __init__(self):
        self.fpc = FirstPersonController(position = (0,0,5), enabled = False)
        self.entities = []

    def change_scene(self,scene_selection):
        self.active_scene_name = scene_selection

        for o in self.entities:
            destroy(o)

        match scene_selection:
            case "Menu":
                self.scenenames = ["FirstScene", "SecondScene"]
                for x in range(len(self.scenenames)):
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

def update_menu():
    pass

def update_first_scene():
    if held_keys["q"]:
        mygame.change_scene("Menu")

def update_second_scene():
    if held_keys["q"]:
        mygame.change_scene("Menu")

def update():


    match mygame.active_scene_name:
        case "Menu":
            update_menu()

        case "FirstScene":
            update_first_scene()

        case "SecondScene":
            update_second_scene()

mygame = Game()
mygame.change_scene("Menu")
app.run()