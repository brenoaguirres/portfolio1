# -------------------------------------------------------------------------------------------------------------
# Network Class
# -------------------------------------------------------------------------------------------------------------
# Author: Breno Freitas Aguirres
# Date: 27/07/23
# Follow my work:
# ---> instagram.com/combo.pixel
# ---> linkedin.com/in/brenoaguirres
# ---> github.com/Kohisoft-Breno
# ---> behance.net/brenofreitas5
# -------------------------------------------------------------------------------------------------------------
# Description: This class handles client side's implementation of connection and data transfer to the server.
# -------------------------------------------------------------------------------------------------------------

import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.107"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            # when connected receives which player we are
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

