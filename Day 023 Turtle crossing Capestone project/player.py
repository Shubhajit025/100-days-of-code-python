from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        """Player movement only forward."""
        self.forward(MOVE_DISTANCE)

    def go_back_to_start(self):
        """After reaching end go back to start position."""
        self.goto(STARTING_POSITION)

    def end_touch(self):
        """When touches end should go back to start or end the game."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
