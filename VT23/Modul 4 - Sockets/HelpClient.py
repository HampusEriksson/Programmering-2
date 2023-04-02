import socket

# Choosing Nickname
nickname = input("Choose your nickname: ")

client = socket.socket()
host = "10.154.198.74"
port = 1337
client.connect((host, port))
client.send(bytes(nickname,"utf-8"))
# Listening to Server and Sending Nickname

# Sending Messages To Server
while True:
    message = input('Help?')
    client.send(bytes(message, "utf-8"))
    if message in ["quit", "q"]:
        break