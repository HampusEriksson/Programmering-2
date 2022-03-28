import socket

s = socket.socket()
print("Socket created")

host = "10.154.198.74"
port = 1337

#Bind säger var socketen "läggs"
s.bind((host, port))

#Socketen lyssnar inkommande connections
s.listen()
print("Waiting for connection")

while True:
   c, addr = s.accept()
   name = c.recv(1024).decode()
   print("Connected to", addr, name)

   c.send(bytes("Welcome " + name +" !", "utf-8)"))

   c.close()
