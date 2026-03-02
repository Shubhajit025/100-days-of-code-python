from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, paddle_goto):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_goto)

    def paddle_up(self):
        up_y = self.ycor() + 20
        self.goto(self.xcor(), up_y)

    def paddle_down(self):
        down_y = self.ycor() - 20
        self.goto(self.xcor(), down_y)

