import json
import socket
from secrets import choice
from othello_game import *


#fichier json avec data des joueurs
with open('player1.json', 'r') as file: 
    data=file.read()


#Adresses
hostAddress=('localhost',3000)
playerAddress=('0.0.0.0',json.loads(data)['port'])

######################  la requête d'inscription  #####################################

#requête faite par le client au serveur:
def client():

    with socket.socket() as s:
        s.connect(hostAddress) #se connecte au server du prof
        s.send(data.encode('UTF8')) #send fichier json
        response=json.loads(s.recv(2048).decode()) #json.loads : dico
    #réponse du serveur si tous est ok:
    if response=={"response": "ok"}:
        print('Let\'s play!')
        return True
    else:
        raise ValueError

########  une requête ping du serveur au port mentionné dans la requête d'inscription  ########
#################################  requête de coup  ###########################################

#La requête faite par le serveur au client:
def server():
    pong = {"response": "pong"}
    ping = {"request": "ping"}
    
    with socket.socket() as s:
        s.bind(playerAddress) #Il s’agit du port sur lequel les clients vont pouvoir se connecter
        s.listen()

        #variables
        the_move_played = int

        #dicos coup
        response_coup_W = {"response": "move","move": the_move_played,"message": "goodluck!"}
        giveup_response = {"response": "giveup",}

        while True:
            client, hostAddress=s.accept() #Attente d’un client
            host_request=json.loads(client.recv(2048).decode()) #reçoit la requete
            print(host_request)

            #La réponse que le client doit renvoyer (pong)
            if host_request==ping:
                client.send(json.dumps(pong).encode())
                print(pong)
            
            elif host_request['request']=='play':
                print(possibleMoves(host_request['state']))

                if len(possibleMoves(host_request['state'])) != 0:
                    response_coup_W['move'] = choice(possibleMoves(host_request['state']))
                    client.send(json.dumps(response_coup_W).encode())
                    print(str(response_coup_W['move']))

                elif len(possibleMoves(host_request['state'])) == 0:
                    response_coup_W['move'] = None
                    client.send(json.dumps(giveup_response).encode())
                    print(giveup_response)


if client()==True:
    server()