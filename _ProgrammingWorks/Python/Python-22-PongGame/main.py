from turtle import Screen
import constants as const
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=const.SCRSIZE_WIDTH, height=const.SCRSIZE_HEIGHT)
screen.bgcolor(const.SCRCOLOR_B)
screen.title("Pong Game")
screen.tracer(0)

paddle_1 = Paddle()
paddle_2 = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_1.move_up, "w")
screen.onkeypress(paddle_1.move_down, "s")
screen.onkeypress(paddle_2.move_up, "Up")
screen.onkeypress(paddle_2.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(1/60)
    screen.update()

    ball.move()

    # collision detection
    ball.collision()
    ball.paddle_collision(paddle_1)
    ball.paddle_collision(paddle_2)
    if ball.p1_score_collision():
        scoreboard.p1_increase_score()
    if ball.p2_score_collision():
        scoreboard.p2_increase_score()

screen.exitonclick()
