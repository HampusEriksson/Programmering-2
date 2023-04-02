import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket()
host = "10.154.198.74"
port = 1337
client.connect((host, port))

# Listening to Server and Sending Nickname
def receive():
   while True:
       try:
           # Receive Message From Server
           # If 'NICK' Send Nickname
           message = client.recv(1024).decode()
           if message == 'NICK':
               client.send(bytes(nickname,"utf-8"))
           else:
               print(message)
       except:
           # Close Connection When Error
           print("An error occured!")
           client.close()
           break

# Sending Messages To Server
def write():
   while True:
       message = nickname + " : " + input('')
       client.send(bytes(message, "utf-8"))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
