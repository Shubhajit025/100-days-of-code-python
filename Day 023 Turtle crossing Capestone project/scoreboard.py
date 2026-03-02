from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        """Increase score when player touch end point."""
        self.level += 1
        self.update_score()

    def game_over(self):
        """When player failed to touch endpoint and hit by a car."""
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)
