from turtle import Turtle
import constants as const

X_VEL = 5
Y_VEL = 5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(const.SCRCOLOR_D)
        self.shape("square")
        self.penup()
        self.x_velocity = X_VEL
        self.y_velocity = Y_VEL

    def move(self):
        new_x = self.xcor() + self.x_velocity
        new_y = self.ycor() + self.y_velocity
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_velocity *= -1

    def bounce_x(self):
        self.x_velocity *= -1

    def collision(self):
        if self.ycor() >= (const.SCRSIZE_HEIGHT // 2) - 10:
            self.goto(self.xcor(), (const.SCRSIZE_HEIGHT // 2) - 10)
            self.bounce_y()

        if self.ycor() <= (-const.SCRSIZE_HEIGHT // 2 + 10):
            self.goto(self.xcor(), (-const.SCRSIZE_HEIGHT // 2) + 10)
            self.bounce_y()

    def paddle_collision(self, paddle):
        if self.distance(paddle) <= 51 and self.xcor() > (const.SCRSIZE_WIDTH // 2) - 60:
            self.bounce_x()
        elif self.distance(paddle) <= 51 and self.xcor() < (-const.SCRSIZE_WIDTH // 2) + 60:
            self.bounce_x()

    def p1_score_collision(self):
        if self.xcor() > const.SCRSIZE_WIDTH // 2:
            self.reset_ball()
            return True

    def p2_score_collision(self):
        if self.xcor() < -(const.SCRSIZE_WIDTH // 2):
            self.reset_ball()
            return True

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
