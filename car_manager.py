from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len = 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.place_cars()
        self.setheading(180)

    def place_cars(self):
        random_y = random.randrange(-250, 280)
        self.goto(280, random_y)

    def move_cars(self):
        self.forward(STARTING_MOVE_DISTANCE)