from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = 0
        self.update_level()
        
    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align= "center", font= FONT)
