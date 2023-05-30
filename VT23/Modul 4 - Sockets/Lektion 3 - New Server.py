import socket

s = socket.socket()
print("Socket created")

# cmd - ipconfig - IPv4 Address
host = "10.158.78.100"
port = 1337

# Bind säger var socketen "läggs"
s.bind((host, port))

# Socketen lyssnar inkommande connections
s.listen()
print("Waiting for connection")

while True:
    client, addr = s.accept()
    name = client.recv(1024).decode()
    print("Connected  to", addr, name)

    client.send(bytes("Welcome " + name + " !", "utf-8"))

    client.close()
