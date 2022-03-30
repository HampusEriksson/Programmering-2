from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursinanetworking import *

Client = UrsinaNetworkingClient("localhost", 25565)
Easy = EasyUrsinaNetworkingClient(Client)

Players = {}

window.borderless = False


class Player(FirstPersonController):
    def __init__(self, position, name):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            texture="white_cube",
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(0.9, 1)),
        )
        self.name = name


@Easy.event
def onReplicatedVariableCreated(variable):
    print(variable)
    Players[variable.name] = Player(variable.content["Position"], variable.name)

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

def update():
    Move(player.position)

    Easy.process_net_events()


App.run()
