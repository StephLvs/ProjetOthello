import socket
import threading
import json

#fichier json avec data du joueur
with open('player1.json') as file:
    data=file.read()
#Addresses
address=('localhost',3000)
player1_Address=('0.0.0.0',json.loads(data)['port'])

######################  la requête d'inscription  #####################################

#requête faite par le client au serveur:
def client():
    with socket.socket() as s:
        s.connect(address) #se connecte au server du prof
        s.send(data.encode('UTF8')) #send fichier json
        response=json.loads(s.recv(2048).decode()) #json.loads : dico
    #réponse du serveur si tous est ok:
    if response=={"response": "ok"}:
        print(response)
        return True
    else:
        print(response)
        return False

    
   
########  une requête ping du serveur au port mentionné dans la requête d'inscription  ########
#################################  requête de coup  ###########################################

#La requête faite par le serveur au client:
def server():
    response_player1={"response": "pong"}

    #variables
    list_of_errors=[]
    players=[]
    state_of_the_game={'players': players,'current': 0,'board': [[28, 35], [27, 36]]}
    the_move_played=int

    #dicos coup
    dico_state={"request": "play","lives": 3,"errors": list_of_errors,"state": state_of_the_game}
    response_coup_W={"response": "move","move": 37,"message": "goodluck"}
    response_coup_L={"response": "giveup",}

    #testing
    '''players.append()
    black=players[0]
    white=players[1]
    board.append() '''

    with socket.socket() as s:
        s.bind(player1_Address )#Il s’agit du port sur lequel les clients vont pouvoir se connecter
        s.listen()
        while True:
            client, address=s.accept() #Attente d’un client
            request=json.loads(client.recv(2048).decode()) #reçoit la requete
            print(request)

            #La réponse que le client doit renvoyer (pong)
            if request=={"request": "ping"}:
                client.send(json.dumps(response_player1).encode())
                print(response_player1)
            
            if dico_state['request']=='play':
                #if possible
                #response_coup_W["move"]=int(input())
                client.send(json.dumps(response_coup_W).encode())
                print(response_coup_W)
            
            

if client()==True:
    server()
