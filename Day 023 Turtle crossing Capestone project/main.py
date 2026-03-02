from turtle import Screen

from scoreboard import ScoreBoard
from car_management import CarManager
from player import Player
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player object from Player class.
player = Player()
# Total 6 cars object from CarManagement class.
car = CarManager()
# creating scoreboard object from ScoreBoard class.
scoreboard = ScoreBoard()

# event listener.
screen.listen()

# player moving by keyboard Up arrow press.
screen.onkey(player.move, "Up")


game_ongoing = True
while game_ongoing:
    time.sleep(0.1)
    screen.update()

    car.car_spawn()
    car.car_move()

    for cars in car.all_spawned_car:
        if cars.distance(player) < 20:
            game_ongoing = False
            scoreboard.game_over()

    if player.end_touch():
        player.go_back_to_start()
        car.upgrade_levels()
        scoreboard.increase_score()


screen.exitonclick()
