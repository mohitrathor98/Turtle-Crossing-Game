from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 20
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
        CarManager.car_speed = MOVE_DISTANCE

    def place_cars(self):
        random_y = random.randrange(-250, 280)
        self.goto(280, random_y)

    def move_cars(self):
        self.forward(CarManager.car_speed)
    
    @classmethod
    def increase_speed(self):
        CarManager.car_speed += MOVE_INCREMENT