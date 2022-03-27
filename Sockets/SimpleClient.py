import socket

c = socket.socket()

host = "192.168.0.105"
port = 1337

c.connect((host,port))

c.send(bytes(input("Write your name "), "utf-8"))

print(c.recv(1024).decode())