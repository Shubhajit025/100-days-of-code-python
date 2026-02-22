from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# starting_position = [(0,0), (-20,0), (-40,0)]

# snake_haven = []

# for position in starting_position:
#     snake_body = Turtle(shape="square")
#     snake_body.color("white")
#     snake_body.penup()
#     snake_body.goto(position)
#     snake_haven.append(snake_body)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    # Detecting collision with tail
    for snake_body in snake.snake_haven[1:]:
        # if snake_body == snake.head:
        #     pass
        if snake.head.distance(snake_body) < 10:
            game_is_on = False
            scoreboard.game_over()


    # About score board


    # for snakes in range(len(snake_haven) - 1, 0, -1):
    #     new_x = snake_haven[snakes - 1].xcor()
    #     new_y = snake_haven[snakes - 1].ycor()
    #     snake_haven[snakes].goto(new_x, new_y)
    # snake_haven[0].forward(20)
    # snake_haven[0].right(90)



screen.exitonclick()
