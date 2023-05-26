#server_side
import threading
from socket import * 
host='127.0.0.1'
port=59000
server = socket(AF_INET, SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handel_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index= clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'this {alias} left the chatroom'.encode('utf-8'))
            aliases.remove(alias)
            break
    
def recieve():
    while True:
        print("the server is listening")
        client , addr = server.accept()
        print(f'connection is established with {str(addr)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'the alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'the{alias} has coneceted to chatroom'.encode('utf-8'))
        client.send('you are connected successfuly'.encode('utf-8'))
        thread = threading.Thread(target=handel_client,args=(client,))
        thread.start()
        
if __name__ == '__main__': recieve()       