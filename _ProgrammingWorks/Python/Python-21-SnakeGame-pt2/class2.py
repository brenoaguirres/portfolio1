########################################################################
# DETECT COLLISIONS WITH FOOD
########################################################################

from turtle import Screen
import constants as const
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=const.SCRSIZE_WIDTH, height=const.SCRSIZE_HEIGHT)
screen.bgcolor(const.COLOR_B)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:

    snake.move()

    # detect collision
    if snake.head.distance(food) <= 14:
        food.refresh_position()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
