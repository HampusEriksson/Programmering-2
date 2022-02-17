from UrsinaClasses import *

class Scene:

    def __init__(self, name, game):
        self.name = name
        self.entities = []
        self.game = game

    def delete_scene(self):
        for e in self.entities:
            destroy(e)

class FirstScene(Scene):

    def __init__(self, game):
        super(FirstScene, self).__init__("FirstScene", game)
        self.entities.append(MenuButton((0, 0, 0), self, "Menu"))


class SecondScene(Scene):

    def __init__(self, game):
        super(SecondScene, self).__init__("SecondGame", game)
        self.entities.append(MenuButton((0, 0, 0), self, "Menu"))


class Menu(Scene):

    def __init__(self, game):
        super(Menu, self).__init__("Menu" , game)
        self.scenenames = ["FirstScene", "SecondScene"]
        for x in range(2):
            self.entities.append(MenuButton((x/10,0,0), self, self.scenenames[x]))


