import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_list = []
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
loop_count = 0
while game_is_on:
    loop_count += 1
    time.sleep(0.1)
    screen.update()
    
    # generate cars
    if loop_count%6 == 0:
        car_list.append(CarManager())
    # move cars
    for car in car_list:
        car.move_cars()
        
    # turtle collision with top
    if player.finish():
        player.goto_start()
        score.update_level()
        CarManager.increase_speed()
        
    # detect turtle's collision with cars
    for car in car_list:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()
            break

screen.exitonclick()
