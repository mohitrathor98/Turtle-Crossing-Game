from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len = 4)
        self.color(random.choice(COLORS))
        self.penup()
        self.place_cars()

    def place_cars(self):
        random_y = random.randrange(-280, 280)
        self.goto(280, random_y)
