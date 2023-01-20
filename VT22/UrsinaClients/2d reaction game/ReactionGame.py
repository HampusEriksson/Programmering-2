from random import randrange
from ursina import *
from ursinanetworking import *

class ReactionButton(Button):
    def __init__(self, client, c, name, position):
        super().__init__()
        self.position = position
        self.scale = 0.1
        self.disabled = False
        self.color = color.red if c == "red" else color.green
        self.highlight_color = self.color.tint(0.2)
        self.pressed_color = self.color.tint(-0.2)
        self.client = client
        self.name = name

    def on_click(self):
        click_audio = Audio('click2.mp3', pitch=1)
        click_audio.play()
        if self.color == color.green:
            Client.send_message("Score", self.name)


    def change_color(self, new_color):
        if new_color == "green":
            self.color = color.green

        elif new_color == "red":
            self.color = color.red

        self.highlight_color = self.color.tint(0.2)
        self.pressed_color = self.color.tint(-0.2)


Client = UrsinaNetworkingClient("10.154.198.74", 25120)
Easy = EasyUrsinaNetworkingClient(Client)
Buttons = {}
username = input("What is your name?")

window.borderless = False


@Easy.event
def onReplicatedVariableCreated(variable):

    if variable.content["Type"] == "Button":
        Buttons[variable.name] = ReactionButton(Client,variable.content["Color"], name = variable.name, position=variable.content["Position"])

@Easy.event
def onReplicatedVariableUpdated(variable):
    Buttons[variable.name].change_color(variable.content["Color"])

@Easy.event
def onReplicatedVariableRemoved(variable):
    destroy(Buttons[variable.name])

App = Ursina()
sky = Sky()

def update():

    Easy.process_net_events()

Client.send_message("Username", username)

App.run()
