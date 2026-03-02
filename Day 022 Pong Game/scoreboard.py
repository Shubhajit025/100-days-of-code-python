from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() # clearing the scoreboard to update the score for players
        self.goto(-100, 200)
        self.write(self.left_player_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_player_score, align="center", font=("Courier", 80, "normal"))

    def score_for_left_player(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def score_for_right_player(self):
        self.right_player_score += 1
        self.update_scoreboard()
