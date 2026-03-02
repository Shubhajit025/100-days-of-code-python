from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.all_spawned_car = []
        self.initial_car_speed = STARTING_MOVE_DISTANCE

    def car_spawn(self):
        """Spawning cars."""
        random_car = random.randint(1, 6)
        if random_car == 1:
            porsche_911 = Turtle(shape="square")
            porsche_911.shapesize(stretch_wid=1, stretch_len=2)
            porsche_911.penup()
            porsche_911.color(random.choice(COLORS))
            porsche_911.setheading(180)
            porsche_911.goto(280, random.randint(-240, 240))
            self.all_spawned_car.append(porsche_911)


    def car_move(self):
        """Movement of player."""
        for car in self.all_spawned_car:
            car.forward(self.initial_car_speed)

    def upgrade_levels(self):
        """Upgrading levels when player reaches end point successfully."""
        self.initial_car_speed += MOVE_INCREMENT
