import socket

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket()
host = "10.151.212.111"
port = 1337
client.connect((host, port))

# Sending Messages To Server
def write():
    while True:
        message = nickname + " : " + input("")
        client.send(bytes(message, "utf-8"))


write()
