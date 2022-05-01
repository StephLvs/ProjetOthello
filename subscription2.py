import socket
import threading
import json

#fichier json avec data du joueur
with open('player2.json') as file:
    data2=file.read()

#Addresses
address=('localhost',3000)
player2_Address=('0.0.0.0',json.loads(data2)['port'])

######################  la requête d'inscription  #####################################

#requête faite par le client au serveur:
def client():
    with socket.socket() as s:
        s.connect(address) #se connecte au server du prof
        s.send(data2.encode('UTF8')) #send fichier json
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
    response_player2={"response": "pong"}

    #variables
    list_of_errors=[]
    players=[]
    state_of_the_game={'players': players,'current': 0,'board': [[28, 35], [27, 36]]}
    the_move_played=int

    #dicos coup
    dico_state={"request": "play","lives": 3,"errors": list_of_errors,"state": state_of_the_game}
    response_coup_W={"response": "move","move": the_move_played,"message": "ima beat yo ass"}
    response_coup_L={"response": "giveup",}
   

    with socket.socket() as s:
        s.bind(player2_Address)#Il s’agit du port sur lequel les clients vont pouvoir se connecter
        s.listen()
        #une requête ping du serveur au port mentionné dans la requête d'inscription
        while True:
            client, address=s.accept() #Attente d’un client
            request=json.loads(client.recv(2048).decode()) #reçoit la requete
            print(request)
            #La réponse que le client doit renvoyer (pong)
            if request=={"request": "ping"}:
                client.send(json.dumps(response_player2).encode())
                print(response_player2)
            if dico_state['request']=='play':
                print('test')
            

if client()==True:
    server()
