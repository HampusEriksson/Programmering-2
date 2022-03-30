
from MinecraftClasses import *

App = Ursina()
Client = UrsinaNetworkingClient("10.154.198.74", 25565)
Easy = EasyUrsinaNetworkingClient(Client)
window.borderless = False

sky = Sky()

Blocks = {}
Players = {}
PlayersTargetPos = {}

SelfId = -1


@Client.event
def GetId(Id):
    global SelfId
    SelfId = Id
    print(f"My ID is : {SelfId}")

@Easy.event
def onReplicatedVariableCreated(variable):
    global Client
    variable_name = variable.name
    variable_type = variable.content["type"]
    if variable_type == "block":
        block_type = variable.content["block_type"]
        if block_type == "grass":
            new_block = Grass()
        else:
            print("Block not found.")
            return

        new_block.name = variable_name
        new_block.position = variable.content["position"]
        new_block.client = Client
        Blocks[variable_name] = new_block

    elif variable_type == "player":
        PlayersTargetPos[variable_name] = Vec3(0, 0, 0)
        Players[variable_name] = PlayerRepresentation()
        if SelfId == int(variable.content["id"]):
            Players[variable_name].color = color.red
            Players[variable_name].visible = False

@Easy.event
def onReplicatedVariableUpdated(variable):
    PlayersTargetPos[variable.name] = variable.content["position"]

@Easy.event
def onReplicatedVariableRemoved(variable):
    variable_name = variable.name
    variable_type = variable.content["type"]
    if variable_type == "block":
        destroy(Blocks[variable_name])
        del Blocks[variable_name]
    elif variable_type == "player":
        destroy(Players[variable_name])
        del Players[variable_name]

player = Player()

def update():

    if player.position[1] < -5:
        player.position = (randrange(0, 15), 10, randrange(0, 15))

    for p in Players:
        Players[p].position += (Vec3(PlayersTargetPos[p]) - Players[p].position) / 25

    Easy.process_net_events()

App.run()