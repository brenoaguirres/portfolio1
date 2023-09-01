from turtle import Turtle
import constants as const

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = [0, 0]
        self.color(const.SCRCOLOR_C)
        self.hideturtle()
        self.goto(0, 250)
        self.write_score_text()

    def p1_increase_score(self):
        self.score[0] += 1
        self.clear()
        self.write_score_text()

    def p2_increase_score(self):
        self.score[1] += 1
        self.clear()
        self.write_score_text()

    def write_score_text(self):
        self.write(f"{self.score[0]} | {self.score[1]}", align=ALIGNMENT, font=FONT)

