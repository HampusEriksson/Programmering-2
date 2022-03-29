# https://www.youtube.com/watch?v=JOCdGLmQJE0&ab_channel=PratangsuDev

from ursinanetworking import *

client = UrsinaNetworkingServer("localhost", 22626)

username = input("Username: ")

app = Ursina()

@client.event
def onConnectionEstablished():
    client.send_message("ClientConnected", username)

@client.event
def onConnectionError(Reason):
    print(f"Error ! Reason : {Reason}")

@client.event
def HelloFromServer(content):
    print(f"Server says {content}.")

def update():
    client.process_net_events()

app.run()