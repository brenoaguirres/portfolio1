from turtle import Turtle
import constants as const

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color(const.COLOR_C)
        self.hideturtle()  # hides turtle to show only text
        self.goto(0, 250)
        self.write_score_text()

    def increase_score(self):
        self.score += 1
        self.clear()  # clears previous written turtle
        self.write_score_text()

    def write_score_text(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)