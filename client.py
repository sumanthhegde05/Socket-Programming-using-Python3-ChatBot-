import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost',8000))

while True:
    x=input()
    sock.send(x.encode())
    message = sock.recv(1024).decode() #Receives Message\
    print(message)
