import json
import socket
from othello_game import *


#fichier json avec les données du joueur
with open('ai.json', 'r') as file:
    data=file.read()

hostAddress=('localhost',3000)

weighted_board = [0,7,56,63,2,5,58,61,16,23,40,47,3,4,24,31,       
                32,39,59,60,18,21,42,45,19,20,26,29,34,37,43,
                44,11,12,25,27,28,30,33,35,36,38,51,52,10,13,17,
                22,41,46,50,53,1,6,8,15,48,55,57,62,9,14,49,54]


#requête faite par le client au serveur
def client(data):
    with socket.socket() as s:
        s.connect(hostAddress)                     #se connecte au server 
        s.send(data.encode('UTF8'))                #send fichier json
        response=json.loads(s.recv(2048).decode()) #json.loads pour avoir en dico

    #réponse du serveur si tous est ok:
    if response=={"response": "ok"}:
        print('Let\'s play!')
        return True
    else:
        return False


def giveMove(request, board):
    the_move_played = int
    response_coup_W = {"response": "move","move": the_move_played,"message": "Don't let them know your next move"}

    if len(possibleMoves(request['state'])) != 0:
        for elem in board:
            if elem in possibleMoves(request['state']):
                response_coup_W['move']=elem
                break                                 #empeche de refaire la boucle quand le premier elem est trouvé 

        print("Le coup joué est {} \n".format(response_coup_W['move']))

        return response_coup_W

    elif len(possibleMoves(request['state'])) == 0:
        response_coup_W['move'] = None
        
        print("Le coup joué est {} , car il n'y a plus de coups possibles \n".format(response_coup_W['move']))
        
        return response_coup_W

def initializeSocket():
    playerAddress=('0.0.0.0',json.loads(data)['port'])
    s= socket.socket()
    s.bind(playerAddress) #Il s’agit du port sur lequel les clients vont pouvoir se connecter
    s.listen()
    return s


def handleRequest(request,client):
    print("La requête faite par l'hôte est {}".format(request))
    pong = {"response": "pong"}
    ping = {"request": "ping"}

    #une requête ping du serveur au port mentionné dans la requête d'inscription
    if request==ping:
        client.send(json.dumps(pong).encode())           #json.dumps pour envoyer en json
        print("La réponse du client est {}".format(pong))
        return pong
    
    #requête de coup
    elif request['request']=='play':
        print(str(request['state']['players'][0])+' has '+str(len(request['state']['board'][0])))
        print(str(request['state']['players'][1])+' has '+str(len(request['state']['board'][1])))
        print("Les coups possibles sont {}".format(possibleMoves(request['state'])))

        result = giveMove(request,weighted_board)
        client.send(json.dumps(result).encode())

        return result


#La requête faite par le serveur au client:
def server():
    s=initializeSocket()
    while True:
        client, Address=s.accept() #Attente d’un client
        host_request=json.loads(client.recv(2048).decode()) #reçoit la requete

        handleRequest(host_request,client)
        client.close()

if __name__ == "__main__":
    if client(data)==True: server()