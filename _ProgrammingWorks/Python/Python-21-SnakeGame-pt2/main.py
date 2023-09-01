########################################################################
# SLICE LISTS & TUPLES IN PYTHON
########################################################################

from turtle import Screen
import constants as const
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=const.SCRSIZE_WIDTH, height=const.SCRSIZE_HEIGHT)
screen.bgcolor(const.COLOR_B)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:

    snake.move()

    if snake.head.distance(food) <= 15:
        food.refresh_position()
        scoreboard.increase_score()
        snake.extend_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
