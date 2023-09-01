# -------------------------------------------------------------------------------------------------------------
# Server Class
# -------------------------------------------------------------------------------------------------------------
# Author: Breno Freitas Aguirres
# Date: 27/07/23
# Follow my work:
# ---> instagram.com/combo.pixel
# ---> linkedin.com/in/brenoaguirres
# ---> github.com/Kohisoft-Breno
# ---> behance.net/brenofreitas5
# -------------------------------------------------------------------------------------------------------------
# Description: N/A
# -------------------------------------------------------------------------------------------------------------

import socket
from _thread import *
import pickle
from game import Game


server = "192.168.1.107"
port = 5555

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sckt.bind((server, port))
except socket.error as e:
    str(e)

sckt.listen(2)
print("Waiting for a connection, Server Started...")

# handles a list of game connections
connected = set()
games = {}
idCount = 0


def threaded_client(connection, p, gameId):
    global idCount

    # sends to connection which player they are.
    connection.send(str.encode(str(p)))

    reply = ""
    while True:
        data = connection.recv(4096).decode()
        try:
            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    # if the game hasn't been disconnected we're going to check for get, reset or move
                    if data == "reset":
                        game.reset_went()
                    elif data != "get":
                        game.set_player_move(p, data)

                    reply = game
                    connection.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    connection.close()


while True:
    connection, addr = sckt.accept()  # this line waits, so the following stuff will run only if conn is accepted.
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2  # stores every two people on the same gameId.
    if idCount % 2 == 1:  # every odd iteration of idCount will create a new Game in games list
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (connection, p, gameId))

