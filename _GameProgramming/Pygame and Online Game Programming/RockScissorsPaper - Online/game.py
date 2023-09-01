# -------------------------------------------------------------------------------------------------------------
# Game Class
# -------------------------------------------------------------------------------------------------------------
# Author: Breno Freitas Aguirres
# Date: 27/07/23
# Follow my work:
# ---> instagram.com/combo.pixel
# ---> linkedin.com/in/brenoaguirres
# ---> github.com/Kohisoft-Breno
# ---> behance.net/brenofreitas5
# -------------------------------------------------------------------------------------------------------------
# Description: This class handles logic and behaviour for "rock, scissors, paper" game's correct functioning.
# -------------------------------------------------------------------------------------------------------------

class Game:
    def __init__(self, id):
        self.p1Played = False
        self.p2Played = False
        self.isGameReady = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        """

        :param p: [0, 1]
        :return: Move
        """
        return self.moves[p]

    def set_player_move(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Played = True
        else:
            self.p2Played = True

    def connected(self):
        return self.isGameReady

    def both_went(self):
        return self.p1Played and self.p2Played

    def winner(self):
        p1 = self.moves[0].upper()[0]  # first letter uppercase
        p2 = self.moves[1].upper()[0]

        winner = -1

        if p1 == "R":
            if p2 == "S":
                winner = 0
            if p2 == "P":
                winner = 1

        if p1 == "P":
            if p2 == "S":
                winner = 1
            if p2 == "R":
                winner = 0

        if p1 == "S":
            if p2 == "P":
                winner = 0
            if p2 == "R":
                winner = 1

        return winner

    def reset_went(self):
        self.p1Played = False
        self.p2Played = False

