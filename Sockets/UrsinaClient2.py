import socket
import threading
from ursina import *

# Choosing Nickname
nickname = input("Choose your nickname: ")
other_players = {}

app = Ursina()

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.


player = Entity(model="cube", color=rgb(random.randrange(255), random.randrange(255), random.randrange(255)))

# Connecting To Server
client = socket.socket()
host = "10.154.198.74"
port = 1337
client.connect((host, port))


# Listening to Server and Sending Nickname
def receive():
    threading.Timer(1, receive).start()
    message = client.recv(1024).decode()
    print(message)
    if message == 'NICK':
        client.send(bytes(nickname, "utf-8"))

    elif (msg := message.split(","))[0][5:] != nickname:
        if msg[0][5:] in other_players:
            other_players[msg[0][5:]].position = (float(msg[1][2:]), float(msg[2][2:]), float(msg[3][2:]))

        else:
            other_players[msg[0][5:]] = Entity(model="cube", color=rgb(random.randrange(255), random.randrange(255),
                                                                random.randrange(255)))


# Sending Messages To Server
def send_info():
    threading.Timer(1, send_info).start()
    message = f"name:{nickname},x:{player.position.x},y:{player.position.y},z:{player.position.z}"
    client.send(bytes(message, "utf-8"))


def uuu():
    threading.Timer(1 / 60, uuu).start()
    player.x += (held_keys["d"] - held_keys["a"]) * time.dt
    player.y += (held_keys["w"] - held_keys["s"]) * time.dt


receive()
send_info()
uuu()

app.run()
