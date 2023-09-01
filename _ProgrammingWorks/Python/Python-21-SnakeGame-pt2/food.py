from turtle import Turtle
import random
import constants as const


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # stretch the Turtle along its length and width from 20x20 to 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(const.COLOR_D)
        # related to animation rendering
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        random_x = random.randint((-const.SCRSIZE_WIDTH//2)+15, (const.SCRSIZE_WIDTH//2)-15)
        random_y = random.randint((-const.SCRSIZE_HEIGHT//2)+15, (const.SCRSIZE_HEIGHT//2)-15)
        self.goto(random_x, random_y)