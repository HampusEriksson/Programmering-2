import socket

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
# windows - cmd - ipconfig - IPv4 Address

client = socket.socket()
host = "10.158.78.100"
port = 1337
client.connect((host, port))

# Sending Messages To Server
def write():
    while True:
        message = nickname + " : " + input("")
        client.send(bytes(message, "utf-8"))


write()
