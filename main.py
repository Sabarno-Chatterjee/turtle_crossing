import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
cars = []
screen = Screen()
scoreboard = Scoreboard()
# car1 = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# car2 = CarManager()

print(cars)


player = Player()
screen.onkey(fun=player.move, key="Up")
game_is_on = True
while game_is_on:
    for car in range(random.randint(0,1)):
        time.sleep(1)
        car1 = CarManager()
        cars.append(car1)
    for car in cars:
        car.car_move()
    time.sleep(0.2)
    screen.update()
    if player.ycor() > 280:
        player.new_level()
        scoreboard.level_up()





screen.exitonclick()