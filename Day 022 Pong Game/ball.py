from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_value = 10
        self.y_value = 10


    def move_the_ball(self):
        goto_x = self.xcor() + self.x_value
        goto_y = self.ycor() + self.y_value
        self.goto(goto_x, goto_y)

    def bounce_ball_y(self):
        self.y_value *= -1

    def bounce_ball_x(self):
        self.x_value *= -1

    def reset_ball_position(self):
        self.goto(0, 0)
        self.bounce_ball_x()

