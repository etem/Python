import socket
import time

HOST = "localhost"
PORT = 5454
data = "Happy Hacking"

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    s.sendto(data,(HOST,PORT))
    print "sent : " +data
    time.sleep(1)

