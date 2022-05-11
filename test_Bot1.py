import Bot1


def test_client():
    with open('ai.json', 'r') as file:
        data1=file.read()
    with open('BadAi.json', 'r') as file:
        data2=file.read()
    assert Bot1.client(data1) == True
    assert Bot1.client(data2) == False

def test_giveMove():
    board = [0,7,56,63,2,3,4,5,10,13,16,17,18,21,22,23,24,31,32,39,40,41,42,45,46,47,50,53,58,59,60,61,11,12,19,20,25,26,27,28,29,30,33,34,35,36,37,38,43,44,51,52,1,6,8,9,14,15,48,49,54,55,57,62]
    request1 = {'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Stephanie', 'Elise'], 'current': 0, 'board': [[35, 19, 27], [36, 20, 28]]}}
    request2 = {'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Elise', 'Stephanie'], 'current': 0, 'board': [[44, 46, 45, 36, 11, 13, 10, 35, 29, 33, 26, 12, 34, 20, 27, 51, 42,
                                                                                                                                   14, 21, 28, 30, 22, 25, 9, 17], [24, 18, 19, 0, 16, 8, 23, 32, 39, 31, 7, 1, 2, 4, 5, 3, 6]]}}
    request3 = {'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Stephanie', 'Elise'], 'current': 1, 'board': [[3, 40, 56, 48, 0, 1, 2, 4, 31, 47, 24, 32, 63, 55, 54, 58, 34, 16, 8
                                                                                                                                  , 25, 17, 30, 26, 61, 37, 45, 53, 7, 15, 23, 39, 46, 59, 60, 35, 41, 19, 27, 11, 33, 42, 38, 20, 29], [5, 13, 36, 49, 9, 10, 18, 12, 22, 14, 21, 28, 57, 43, 50, 52, 51]]}}
    request4 = {'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Elise', 'Stephanie'], 'current': 1, 'board': [[19, 16, 18, 43, 26, 58, 50, 32, 33, 24, 36, 28, 44, 35, 45, 51, 49,
                                                                                                                        22, 25, 34], [2, 56, 0, 1, 60, 47, 63, 55, 3, 10, 17, 7, 14, 42, 53, 54, 37, 23, 30, 39, 46, 40, 41, 48, 13, 20, 27, 21, 29]]}}
    request5 = {'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Elise', 'Stephanie'], 'current': 1, 'board': [[28, 35, 19, 26, 27], [36, 18]]}}
    request6 = {'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Stephanie', 'Elise'], 'current': 0, 'board': [[3, 2, 0, 1, 23, 4, 56, 42, 5, 7, 6, 19, 27, 18, 29, 20, 60, 39, 63,
                                                                                                                        55, 47, 26, 33, 58, 57, 31, 13, 22, 30, 36, 59, 38, 45, 35, 43], [9, 10, 8, 17, 62, 44, 37, 46, 25, 61, 53, 14, 21, 28, 11, 12, 34, 48, 50, 32, 49, 16, 52, 41, 24, 40, 51]]}}


    assert Bot1.giveMove(request1, board) == {"response": "move", "move": 13, "message": "Don't let them know your next move"}
    assert Bot1.giveMove(request2, board) == {"response": "move", "move": None, "message": "Don't let them know your next move"}
    assert Bot1.giveMove(request3, board) == {"response": "move", "move": 62, "message": "Don't let them know your next move"}
    assert Bot1.giveMove(request4, board) == {"response": "move", "move": 31, "message": "Don't let them know your next move"}
    assert Bot1.giveMove(request5, board) == {"response": "move", "move": 20, "message": "Don't let them know your next move"}
    assert Bot1.giveMove(request6, board) == {"response": "move", "move": 15, "message": "Don't let them know your next move"}


def test_initializeSocket():
    s = Bot1.initializeSocket()
    assert type(s) == Bot1.socket.socket


def test_handleRequest():
    client, Address = Bot1.initializeSocket().accept()
    request1 = {"request": "ping"}
    request2 = {'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Stephanie', 'Elise'], 'current': 0, 'board': [[35, 19, 27], [36, 20, 28]]}}
    assert Bot1.handleRequest(request1, client) == {"response": "pong"}
    assert Bot1.handleRequest(request2, client) == {"response": "move", "move": 21, "message": "Don't let them know your next move"}

def test_isGameOver():
    state1 = {'players': ['Stephanie', 'Elise'], 'current': 0, 'board': [[35, 19, 27], [36, 20, 28]]}
    state2 = {'players': ['Elise', 'Stephanie'], 'current': 1, 'board': [[4, 1, 2, 3, 34, 43, 21, 52, 6, 5, 51, 37
                                                                    , 55, 50, 17, 25, 9, 33, 41, 48, 49], [16, 0, 8, 23, 24, 39, 31, 7, 27, 28, 44, 32, 40, 19, 26, 12, 10, 11, 18, 35, 42, 47, 20, 29, 63, 45, 36, 15, 14, 22, 13, 56, 62, 57, 58, 59, 60, 61, 53, 54, 46, 38, 30]]}
    assert Bot1.isGameOver(state1) == False
    assert Bot1.isGameOver(state2) == True










