import json
import socket
from othello_game import *

######################  la requête d'inscription  #####################################
hostAddress=('localhost',3000)
#fichier json avec data des joueurs
with open('ai.json', 'r') as file:
    data=file.read()
#Adresses
playerAddress=('0.0.0.0',json.loads(data)['port'])
#requête faite par le client au serveur:
def client(data):

    with socket.socket() as s:
        s.connect(hostAddress) #se connecte au server du prof
        s.send(data.encode('UTF8')) #send fichier json
        response=json.loads(s.recv(2048).decode()) #json.loads : dico
    #réponse du serveur si tous est ok:
    if response=={"response": "ok"}:
        print('Let\'s play!')
        return True
    else:
        return False

########  une requête ping du serveur au port mentionné dans la requête d'inscription  ########
#################################  requête de coup  ###########################################

def giveMove(request, board):
    the_move_played = int
    response_coup_W = {"response": "move","move": the_move_played,"message": "Don't let them know your next move"}
    if len(possibleMoves(request['state'])) != 0:
        for elem in board:
            if elem in possibleMoves(request['state']):
                response_coup_W['move']=elem

                break #empeche de refaire la boucle
        return response_coup_W

    elif len(possibleMoves(request['state'])) == 0:
        response_coup_W['move'] = None
        
        return response_coup_W

def handleRequest(request,client,board):
    pong = {"response": "pong"}
    ping = {"request": "ping"}

    if request==ping:
        client.send(json.dumps(pong).encode())
        print(pong)
        return "pong"
    elif request['request']=='play':
        result = giveMove(request,board)
        client.send(json.dumps(result).encode())

        print(possibleMoves(request['state']))
        return "{}".format(possibleMoves(request['state']))



#La requête faite par le serveur au client:
def server():
    
    s= socket.socket()
    s.bind(playerAddress) #Il s’agit du port sur lequel les clients vont pouvoir se connecter
    s.listen()

    #board
    weighted_board=[0,7,56,63,2,3,4,5,10,13,16,17,18,21,22,23,24,31,32,39,40,41,42,45,46,47,50,53,58,59,60,61,11,12,19,20,25,26,27,28,29,30,33,34,35,36,37,38,43,44,51,52,1,6,8,9,14,15,48,49,54,55,57,62]

    while True:
        client, Address=s.accept() #Attente d’un client
        host_request=json.loads(client.recv(2048).decode()) #reçoit la requete
        print(host_request)

        handleRequest(host_request,client, weighted_board)

if __name__ == "__main__":
    if client(data)==True:
        server()