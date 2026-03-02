from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


# Creating screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# making left and right paddle object from Paddle class
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

# making ball object from Ball class
ball = Ball()

# making scoreboard object from Scoreboard class
scoreboard = Scoreboard()

# Up & Down by Up & Down arrow of keyboard
screen.listen()

# for right paddle movement
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")

# for left paddle movement
screen.onkey(left_paddle.paddle_down, "s")
screen.onkey(left_paddle.paddle_up, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_the_ball()

    # Detecting the collision with the wall top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # Detecting the collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_ball_x()

    # Detecting is the ball miss right paddle collision
    if ball.xcor() > 380:
        ball.reset_ball_position()
        scoreboard.score_for_left_player()

    # Detecting is the ball miss left paddle collision
    if ball.xcor() < -380:
        ball.reset_ball_position()
        scoreboard.score_for_right_player()


screen.exitonclick()
