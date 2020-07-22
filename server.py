#Imports Modules
import socket
import time

#Defines Server Values
listensocket = socket.socket()
Port = 8000
maxConnections = 999
IP = socket.gethostname() #Gets Hostname Of Current Macheine

listensocket.bind(('',Port))
running = True
#Opens Server
print("Server started at " + IP + " on port " + str(Port))
listensocket.listen(maxConnections)
#Accepts Incomming Connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")   
while running:
    message = clientsocket.recv(1024).decode() #Receives Message
    print(message) #Prints Message
    x=input()
    clientsocket.send(x.encode())
