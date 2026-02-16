from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    # tim.shape("turtle")
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner.")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# def red_turtle():
#     tim = Turtle(shape="turtle")
#     tim.color("red")
#     tim.penup()
#     # tim.shape("turtle")
#     tim.goto(x=-230, y= -100)
#
# def orange_turtle():
#     tim = Turtle(shape="turtle")
#     tim.color("orange")
#     tim.penup()
#     # tim.shape("turtle")
#     tim.goto(x=-230, y=-50)
#
# def yellow_turtle():
#     tim = Turtle(shape="turtle")
#     tim.color("yellow")
#     tim.penup()
#     # tim.shape("turtle")
#     tim.goto(x=-230, y=0)
#
# def green_turtle():
#     tim = Turtle(shape="turtle")
#     tim.color("green")
#     tim.penup()
#     # tim.shape("turtle")
#     tim.goto(x=-230, y=50)
#
# def blue_turtle():
#     tim = Turtle(shape="turtle")
#     tim.color("blue")
#     tim.penup()
#     # tim.shape("turtle")
#     tim.goto(x=-230, y=100)
#
# def purple_turtle():
#     tim = Turtle(shape="turtle")
#     tim.color("purple")
#     tim.penup()
#     # tim.shape("turtle")
#     tim.goto(x=-230, y=150)

# red_turtle()
# orange_turtle()
# yellow_turtle()
# green_turtle()
# blue_turtle()
# purple_turtle()


screen.exitonclick()
