########################################################################
# SETUP SCREEN AND CREATING A SNAKE BODY
########################################################################

# Breaking the problem in steps:
# 1- Create a Snake body
# 2- Move the Snake
# 3- Create Snake food
# 4- Detect collision with food
# 5- Create a scoreboard
# 6- Detect collision with wall
# 7- Detect collision with tail

from turtle import Screen, Turtle

screen = Screen()  # Screen object
screen.setup(width=600, height=600)  # setup screen size, good to explicitly define attributes for reading
screen.bgcolor("#8bac0f")  # setup background color - gameboy screen color
screen.title("Snake Game")

# Turtles are Turtle's graphic objects.
# When we create a turtle, it's dimensions are 20x20.



# will quit the screen only when receiving a click
screen.exitonclick()
