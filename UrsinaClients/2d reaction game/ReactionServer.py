from ursina import *
from ursinanetworking import *

Server = UrsinaNetworkingServer("10.154.198.74", 25120)
Easy = EasyUrsinaNetworkingServer(Server)
App = Ursina()
sky = Sky()

players = {}
usernames = {}

@Server.event
def onClientConnected(Client):
    players[Client.name] = 0

@Server.event
def onClientDisconnected(Client):
    pass

@Server.event
def Score(Client, button_name):
    players[Client.name] += 1
    Easy.update_replicated_variable_by_name(button_name, "Color", "red")
    Easy.update_replicated_variable_by_name("Button" + str(random.randint(1, 18)), "Color", "green")
    new_score = ""
    for key, value in usernames.items():
        new_score += value + " : " + str(players[key]) + "\n"
    scores.text = new_score



@Server.event
def Username(Client, username):
    usernames[Client.name] = username
    new_score = ""
    for key, value in usernames.items():
        new_score += value + " : " + str(players[key]) + "\n"
    scores.text = new_score

def createworld():
    i = 0
    for x in range(-5, 6, 2):
        for y in range(-2, 3, 2):
            i += 1
            Easy.create_replicated_variable("Button" + str(i),
                                            {"Type": "Button", "Position": (x / 10, y / 10, 0), "Color": "red"})


def start_game():
    createworld()
    b1.visible = False
    Easy.update_replicated_variable_by_name("Button" + str(random.randint(1, 18)), "Color", "green")


def update():
    Easy.process_net_events()

b1 = Button(scale=0.1, text="Start")
b1.on_click = start_game
scores = Text(position=(-0.5,0.5,0))
App.run()
