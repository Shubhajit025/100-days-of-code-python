from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

# W = Forwards
def move_forward():
    tim.forward(10)

# S = Backwards
def move_backward():
    tim.backward(10)

# A = Counter - Clockwise
def move_counter_clockwise():
    tim.right(10)

# D = Clockwise
def move_clockwise():
    tim.left(10)

# C = Clear drawing
def clear_page():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear_page)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)

screen.exitonclick()
