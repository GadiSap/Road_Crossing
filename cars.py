from turtle import Turtle
import random

colors = ["black", "yellow", "pink", "red", "gold", "green", "orange"]
CAR_STEP = 20

class Car (Turtle):

    def __init__(self):
        """creates the cars"""
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        col = colors[random.randint(0, 6)]
        self.color(col)
        self.speed("fastest")
        yloc = random.randint(-9, 10)*20
        self.goto(250, yloc)


    def move_car(self):
        self.forward(CAR_STEP)