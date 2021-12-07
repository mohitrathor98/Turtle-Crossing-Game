import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

'''
TODO:

1) Create random coloured cars at random locations == done
2) Move cars from right to left
3) Create a turtle and move it upward
4) Detect turtle's collision with top
    --> Turtle goes back to original position
    --> player levels up
    --> car's speed increases
5) Detect turtle's collision with cars
    --> Everything stops
    --> Game over flashes
    --> exit on click
'''


# car creation
car = CarManager()
car_list = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # generate random number of cars
    for car in range(random.randint(1, 3) + 1):
        car_list.append(CarManager())
    


screen.exitonclick()
