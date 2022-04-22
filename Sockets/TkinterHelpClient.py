import sys
import tkinter as tk
import socket

nickname = input("Name? ")

client = socket.socket()
host = "10.154.198.74"
port = 1337
client.connect((host, port))
client.send(bytes(nickname,"utf-8"))

app = tk.Tk()
def help():
   client.send(bytes("help", "utf-8"))

def no_help():
   client.send(bytes("no help", "utf-8"))

help_button = tk.Button(app, text ="Help", command = help)
nohelp_button = tk.Button(app, text ="No Help", command = no_help)
quit_button = tk.Button(app, text ="Quit", command = sys.exit)

help_button.pack()
nohelp_button.pack()
quit_button.pack()

app.mainloop()