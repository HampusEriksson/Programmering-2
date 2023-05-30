import socket

client = socket.socket()

host = "10.158.78.100"
port = 1337

client.connect((host, port))

client.send(bytes(input("Write your name"), "utf-8"))

print(client.recv(1024).decode())
