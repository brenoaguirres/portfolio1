from turtle import Turtle
import constants as const

STARTING_POSITIONS = [(-350, 0), (350, 0)]
SPEED = 20
paddles = 0


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(const.SCRCOLOR_D)
        self.set_starting_pos()

    def set_starting_pos(self):
        global paddles
        if paddles < 1:
            self.goto(STARTING_POSITIONS[0])
            paddles += 1
        else:
            self.goto(STARTING_POSITIONS[1])

    def move_up(self):
        new_y = self.ycor() + SPEED
        if new_y < (const.SCRSIZE_HEIGHT // 2) - 50:
            self.goto(self.xcor(), new_y)
        else:
            new_y = (const.SCRSIZE_HEIGHT // 2) - 50
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - SPEED
        if new_y > (-const.SCRSIZE_HEIGHT // 2) + 50:
            self.goto(self.xcor(), new_y)
        else:
            new_y = (-const.SCRSIZE_HEIGHT // 2) + 50
            self.goto(self.xcor(), new_y)
