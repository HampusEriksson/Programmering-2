import socket
import threading

# Connection Data
# windows - cmd - ipconfig - IPv4 Address
host = "10.158.78.100"
port = 1337

# Starting Server
server = socket.socket()
server.bind((host, port))
server.listen()

# Handling Messages From Clients
def handle(client):
    while True:
        message = client.recv(1024)
        message = message.decode("utf-8")
        print(message)


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with " + str(address))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
