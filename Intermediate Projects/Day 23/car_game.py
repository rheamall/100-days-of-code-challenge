import time
from turtle import Screen
from game_classes import Player, CarManager, Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

t1 = Player()
cars = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(t1.move_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.cars_movement()

    # detecting collision with car
    for car in cars.all_cars:
        if t1.distance(car) < 10:
            game_is_on = False
            level.game_over()

    # detecting that the turtle has reached the wall i.e. passed this level
    if t1.ycor() > 280:
        level.point_inc()
        t1.turtle_reset()
        cars.speed_increment()

screen.exitonclick()
