import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Turtle Crossing")

player = Player()
screen.onkey(fun=player.move, key="Up")
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Collision with cars:
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Detect successful crossing:
    if player.is_at_finish_line():
        player.new_level()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
