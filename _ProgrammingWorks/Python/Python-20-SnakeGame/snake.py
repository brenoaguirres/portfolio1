from turtle import Turtle
import constants as const

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_LEFT = 180
HEADING_RIGHT = 360


# in Python class names are PascalCase
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # direction for setHeading()
        self.head = HEADING_RIGHT

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color(const.COLOR_C)
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        self.segments[0].setheading(self.head)
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head != HEADING_DOWN:
            self.head = HEADING_UP

    def move_down(self):
        if self.head != HEADING_UP:
            self.head = HEADING_DOWN

    def move_left(self):
        if self.head != HEADING_RIGHT:
            self.head = HEADING_LEFT

    def move_right(self):
        if self.head != HEADING_LEFT:
            self.head = HEADING_RIGHT
