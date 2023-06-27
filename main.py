from turtle import Screen
import time
from player import Player
from cars import Car
from score import Score
import random


# a game where the player needs to cross the road. Every level it get harder
#parameters
car_speed = 0.5
car_volume = -0.5

#set up screen
screen = Screen()
screen.title("Crossing")
screen.setup(width = 600, height=500)
screen.bgcolor("white")
screen.tracer(0)

#sets player, car and score objects
player = Player()
score =Score()
all_cars = []
screen.update()
#sets screen listen method to follow user input
screen.listen()
screen.onkey(player.move, "Up")

#runs game
game_on = True
while game_on:
    car_speed *= 0.95  #increases difficulty by decreasing the wait time between steps
    car_volume += 0.5  # increases difficulty by increasing the number of cars
    for ca in all_cars: #clears cars from screen
        ca.goto(400, 0)
    all_cars = []
    score.update()
    screen.update()
    next_level = False
    #run each level
    while not next_level:
        number_of_cars = int(random.normalvariate(car_volume, 1))
        for _ in range (number_of_cars):
            new_car = Car()
            all_cars.append(new_car)
        for ca in all_cars:
            ca.move_car()
            # test collision with car
            if player.distance(ca) < 30 and abs(player.ycor() - ca.ycor()) < 20:
                score.game_over()
                next_level = True
                game_on = False
        screen.update()
        time.sleep(car_speed)

        #test finish level
        if player.ycor() > 230:
            next_level = True
            player.re_set()




screen.exitonclick()


