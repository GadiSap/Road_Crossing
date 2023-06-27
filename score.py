from turtle import Turtle

FONT = ('Courier', 16, 'normal')

class Score (Turtle):

    def __init__(self):
        """counts the score"""
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 200)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)


    def update(self):
        self.level +=1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=('Courier', 30, 'bold'))

