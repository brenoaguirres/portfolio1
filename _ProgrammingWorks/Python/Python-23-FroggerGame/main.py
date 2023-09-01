import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import constants as const

screen = Screen()
screen.setup(width=const.SCRSIZE_WIDTH, height=const.SCRSIZE_HEIGHT)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(1/60)
    screen.update()
