from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_haven = []
        self.create_snake()
        self.head = self.snake_haven[0]


    def create_snake(self):
        """Body of the snake."""
        for position in STARTING_POSITION:
            self.add_snake_body(position)

    def add_snake_body(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake_haven.append(snake_body)

    def extend(self):
        # add a new snake_body to the snake.
        self.add_snake_body(self.snake_haven[-1].position())

    def move(self):
        """Movement of the snake."""
        for snakes in range(len(self.snake_haven) - 1, 0, -1):
            new_x = self.snake_haven[snakes - 1].xcor()
            new_y = self.snake_haven[snakes - 1].ycor()
            self.snake_haven[snakes].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
