# https://www.youtube.com/watch?v=JOCdGLmQJE0&ab_channel=PratangsuDev

from ursinanetworking import *

server = UrsinaNetworkingServer("localhost", 22626)

app = Ursina()

@server.event
def onClientConnected(Client):
    Client.send_message("HelloFromServer","Welcome to the server!")

@server.event
def onClientDisconnected(Client):
    print(f"{Client} disconnected from the server!")

@server.event
def ClientConnected(user):
    print(f"{user} just connected!")

def update():
    server.process_net_events()

app.run()