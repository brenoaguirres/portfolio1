########################################################################
# CREATE A SNAKE CLASS AND MOVE TO OOP
########################################################################

# separate behaviour for snake class

from turtle import Screen, Turtle
import constants as const
import time
from snake import Snake

screen = Screen()
screen.setup(width=const.SCRSIZE_WIDTH, height=const.SCRSIZE_HEIGHT)
screen.bgcolor(const.COLOR_B)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    snake.move()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()