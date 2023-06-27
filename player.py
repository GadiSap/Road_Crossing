from turtle import Turtle

STARTING_POSITION = (0, -230)
STEP = 10
class Player(Turtle):

    def __init__(self):
        """Setting up the player"""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("blue")
        self.speed("fastest")
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(STEP)

    def re_set(self):
        self.goto(STARTING_POSITION)


