import socket
import threading
import json
from unicodedata import name

with open('player1.json') as file:   #lire fichier json (data du player 1)
    data=file.read()

serverAddress=('localhost',3000)    #server prof

def client(Player):
    with socket.socket() as s:
        s.connect((serverAddress)) #on se connecte au serveur du prof
        s.send(data.encode('UTF8')) #e nvoie notre data encodé
        response=json.loads(s.recv(2048).decode()) #message du prof en dico

    if response=={"response": "ok"}:
        print(response)
        print(json.loads(Player)['name'], response)
        return True
    else:
        print(response)
        print(json.loads(Player)['name'], response)
        return False

#requete de ping
def server(Player):
    player1_Address= ('0.0.0.0',json.loads(data)['port'])
    
    with socket.socket() as s0:
        s0.bind(player1_Address) #on bind au server
        s0.listen()
        response_player = {"response": "pong"}

        while True:
            lur, address = s0.accept()
            response_lur=json.loads(lur.recv(2048).decode())
            print(response_lur)
            
            if response_lur=={"request": "ping"}:
                lur.send(json.dumps(response_player).encode())
                print(json.loads(Player)['name'], response_player)
            

if client()== True:
    server()