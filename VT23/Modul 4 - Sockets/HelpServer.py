import socket
import threading
import os

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
help = []

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            message = client.recv(1024).decode().lower()

            if (
                message in ["help", "yes", "ja"]
                and nicknames[clients.index(client)] not in help
            ):
                help.append(nicknames[clients.index(client)])
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Hjälplista: ", *help, sep="\n")

            if message in ["no help", "no", "nej"]:
                help.remove(nicknames[clients.index(client)])
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Hjälplista: ", *help, sep="\n")


        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        client, address = server.accept()

        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
