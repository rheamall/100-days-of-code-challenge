from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        one_in_six_chance = random.randint(1,6) # to regulate creation of cars
        if one_in_six_chance == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.left(180)
            new_car.color(random.choice(COLORS))
            y_cor = random.randrange(-240, 250, 5)
            new_car.goto(320, y_cor)
            self.all_cars.append(new_car)

    def cars_movement(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_increment(self):
        self.car_speed += MOVE_INCREMENT


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color(COLORS[0])
        self.penup()
        self.left(90)
        self.turtle_reset()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def turtle_reset(self):
        self.goto(STARTING_POSITION)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-270, 250)
        self.write('Level: ' + str(self.level), align='left', font=FONT)

    def point_inc(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write('Game Over', align='center', font=FONT)