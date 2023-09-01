########################################################################
# ANIMATING THE SNAKE SEGMENTS ON SCREEN
########################################################################

from turtle import Screen, Turtle
import constants as const
import time

screen = Screen()
screen.setup(width=const.SCRSIZE_WIDTH, height=const.SCRSIZE_HEIGHT)
screen.bgcolor(const.COLOR_B)
screen.title("Snake Game")
# setting tracer off, so we can use update method to refresh and redraw
screen.tracer(0)


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color(const.COLOR_C)
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    # loop will make snake segments go to the last position of the next snake segment, starting from tail.
    # then the head will move forwards
    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)

    time.sleep(0.1)  # one-second delay after each refresh
    screen.update()  # turtle method that updates the screen, should come after all updates are made.

screen.exitonclick()
