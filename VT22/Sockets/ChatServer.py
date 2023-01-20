import socket
import threading

# Connection Data
host = "10.154.198.74"
port = 1337

# Starting Server
server = socket.socket()
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
   for client in clients:
       client.send(message)

# Handling Messages From Clients
def handle(client):
   while True:
       try:
           # Broadcasting Messages
           message = client.recv(1024)
           broadcast(message)
       except:
           # Removing And Closing Clients
           index = clients.index(client)
           clients.remove(client)
           client.close()
           nickname = nicknames[index]
           broadcast(bytes(nickname + ' left!', "utf-8"))
           nicknames.remove(nickname)
           break

# Receiving / Listening Function
def receive():
   while True:
       # Accept Connection
       client, address = server.accept()
       print("Connected with " + str(address))

       # Request And Store Nickname
       client.send(bytes('NICK', "utf-8"))
       nickname = client.recv(1024).decode()
       nicknames.append(nickname)
       clients.append(client)

       # Print And Broadcast Nickname
       print("Nickname is", nickname)
       broadcast(bytes(nickname + " joined!\n", "utf-8"))
       client.send(bytes('Connected to server!', "utf-8"))

       # Start Handling Thread For Client
       thread = threading.Thread(target=handle, args=(client,))
       thread.start()

receive()
