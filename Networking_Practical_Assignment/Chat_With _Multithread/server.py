import socket 
from socket import *
from _thread import *
import threading

 
def thread_receive(c):
    while True:
        x=c.recv(500)
        print(x.decode('UTF-8'))
 
def client_thread(c):
        receive = threading.Thread(target=thread_receive, args=(c,))
        receive.start()
        while True:
            c.send(input("Server:").encode("UTF-8"))

s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host ="127.0.0.1"
port = 7000
s.bind((host,port))
s.listen(5)
try:
 while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
        print('Connected to :', addr[0]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(client_thread, (c,)) 
except KeyboardInterrupt:
    s.close() 