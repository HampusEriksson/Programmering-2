from random import randrange

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursinanetworking import *
from SimpleClasses import *

Client = UrsinaNetworkingClient("localhost", 25565)
Easy = EasyUrsinaNetworkingClient(Client)

Players = {}

window.borderless = False

@Client.event
def onConnectionEstablished():
    print("Connected")

@Easy.event
def onReplicatedVariableCreated(variable):
    print(variable)
    Players[variable.name] = Player(name = variable.name, position = variable.content["Position"])

@Easy.event
def onReplicatedVariableUpdated(variable):
    Players[variable.name].position = variable.content["Position"]

@Easy.event
def onReplicatedVariableRemoved(variable):
    destroy(Players[variable.name])

def Move(Vec):
    Speed = 5
    NewVec = tuple(e * (time.dt * Speed) for e in Vec)
    Client.send_message("Move", NewVec)

App = Ursina()
sky = Sky()
ground = Entity(collider="sphere", model="cube", position=(0,-5,0), scale=(10,1,10))
player = Player(name=input("Name?"))

def update():
    if player.position[1] < -5:
        player.position = (randrange(0, 15), 10, randrange(0, 15))
    Client.process_net_events()
    Easy.process_net_events()


App.run()
