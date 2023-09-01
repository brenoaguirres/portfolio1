import socket
import pickle
from _thread import *
import sys
from Player import Player

server = "192.168.15.4"
port = 5555  # typically open port

# params = socket type we'll have to use, related to the way the server string comes in
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# using try except because we don't know if connection will work
try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)  # s.listen(2) -> only two people will be able to connect.
print("Waiting for a connection, Server Started.")


players = [Player(0, 0, 25, 25, (255, 0, 0)), Player(300, 300, 25, 25, (0, 0, 255))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:  # in case data is not received, disconnect and break -- finish
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))

        except:  # avoid freezing if some error occurs
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0


while True:

    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

