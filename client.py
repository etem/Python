import socket

HOST = "localhost"
PORT = 5454


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((HOST,PORT))
while True:
    print s.recv(1024)

