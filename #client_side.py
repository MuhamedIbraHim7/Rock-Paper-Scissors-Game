#client_side

import threading
from socket import *
host='127.0.0.1'
port = 59000
alias = input('insert an alias >>>')
client= socket(AF_INET,SOCK_STREAM)
client.connect((host,port))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print("errror")
            client.close()
            break

def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
send_thread = threading.Thread(target=client_send)
send_thread.start()