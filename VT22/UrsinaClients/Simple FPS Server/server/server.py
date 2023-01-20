from ursinanetworking import *

Server = UrsinaNetworkingServer("10.154.198.74", 25565)
Easy = EasyUrsinaNetworkingServer(Server)

# Spawn Block Function
def spawn_block(block_type, position):
    block_name = f"Block {position[0]*32+position[2]}"
    Easy.create_replicated_variable(
        f"Block {block_name}",
        { "type" : "block", "block_type" : block_type, "position" : position}
    )


# A little Hello
@Server.event
def onClientConnected(Client):
    Easy.create_replicated_variable(
        f"player_{Client.id}",
        { "type" : "player", "id" : Client.id, "position" : (0, 0, 0) }
    )
    print(f"{Client} connected !")
    Client.send_message("GetId", Client.id)

# A little goodbye
@Server.event
def onClientDisconnected(Client):
    Easy.remove_replicated_variable_by_name(f"player_{Client.id}")

# Update Player's position
@Server.event
def MyPosition(Client, NewPos):
    Easy.update_replicated_variable_by_name(f"player_{Client.id}", "position", NewPos)

# Create the world
for x in range(20):
    for z in range(20):
        spawn_block("grass", (x, 0, z))

while True:
    Easy.process_net_events()