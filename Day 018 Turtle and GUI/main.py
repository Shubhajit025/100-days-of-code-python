from turtle import Screen
import turtle as t
import random

# from turtle import *  # This * means importing everything from that module called here turtle.
# import turtle as t # This is also importing module but making the module name as t, where t is an allies name given by us or me to shorten the given module name.
# import heroes  # Some modules are need to install from pypi. Because they are not inside the python package library but inside a python package manager a big library available on internet.


tim = t.Turtle()
# tim.shape("arrow")
# tim.color("#0B2D72")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour



# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)


# for _ in range(4):
#
#     tim.forward(100)
#     tim.right(90)

# Making Drag line like '-------' :
# for _ in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# Making triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon: By me before watching solution.

# # triangle:
# for _ in range(3):
#     tim.pencolor("orange")
#     tim.forward(100)
#     tim.right(120)
#
# # Square:
# for _ in range(4):
#     tim.pencolor("green")
#     tim.forward(100)
#     tim.right(90)
#
# # pentagon:
# for _ in range(5):
#     tim.pencolor("DeepPink2")
#     tim.forward(100)
#     tim.right(72)
#
# # hexagon:
# for _ in range(6):
#     tim.pencolor("DarkSlateGray")
#     tim.forward(100)
#     tim.right(60)
#
# # heptagon:
# for _ in range(7):
#     tim.pencolor("blue4")
#     tim.forward(100)
#     tim.right(51.43)
#
# # octagon:
# for _ in range(8):
#     tim.pencolor("goldenrod4")
#     tim.forward(100)
#     tim.right(45)
#
# # nonagon:
# for _ in range(9):
#     tim.pencolor("gray10")
#     tim.forward(100)
#     tim.right(40)
#
# # decagon:
# for _ in range(10):
#     tim.pencolor("LightCoral")
#     tim.forward(100)
#     tim.right(36)

# Making triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon: By me after watching solution.

# colour = ["cyan", "mint cream", "dark blue", "goldenrod", "magenta", "misty rose", "red", "orange", "violet red", "indigo", "gold"]
#
# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colour))
#     draw_shapes(shape_side_n)

# Making a random movement with random color and thickness of pen:

colour = ["cyan", "mint cream", "dark blue", "goldenrod", "magenta", "misty rose", "red", "orange", "violet red", "indigo", "gold"]
direction = [0, 90, 180, 270]
tim.width(1)
tim.speed(10.5)

# tim.forward(0)
# tim.circle(100)
# tim.heading()

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)












# def draw_random():
#     tim.color(random.choice(colour))
#     random.choice(direction)
#
# for random_art in range(1, 51):
#     tim.color(random.choice(colour))
#     tim.width(5)
#     tim.forward(10)
#     tim.right(90)
#     tim.backward(10)
#     tim.left(90)
#     tim.backward(10)
#     tim.forward(10)
#     tim.backward(10)
#     tim.forward(10)
#     tim.right(90)
#     tim.forward(10)
#     tim.left(90)
#     tim.forward(10)
#     tim.left(90)

    # draw_random()
# tim.width(5)
# tim.forward(10)
# tim.right(90)
# tim.backward(10)
# tim.left(90)
# tim.forward(10)
# tim.right(90)
# tim.forward(10)
# tim.left(90)
# tim.forward(10)

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))












screen = Screen()
screen.exitonclick()

