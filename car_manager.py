from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.starting_position()
        self.showturtle()
        self.car_move()

    def starting_position(self):
        y_position = random.randint(-280, 280)
        self.goto(x=310, y=y_position)

    def car_move(self):
        self.forward(MOVE_INCREMENT)
