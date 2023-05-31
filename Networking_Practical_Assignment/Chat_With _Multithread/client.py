from socket import *
from _thread import *
import threading 


def thread_receive(s):
    while True:
        x=s.recv(500)
        print(x.decode('UTF-8'))

s= socket(AF_INET,SOCK_STREAM)
host ="127.0.0.1"
port = 7000
s.connect((host,port))
    

receive = threading.Thread(target=thread_receive, args=(s,))
receive.start()
while True:
          s.send(input("Client:").encode("UTF-8"))