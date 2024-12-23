from turtle import Turtle
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COORD = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """ Creating the snake's body """
        for i in COORD:
            self.add_part(i)

    def extend_snake(self):
        self.add_part(self.snake_body[-1].position())

    def add_part(self, coord):
        """ Add a new part to the snake """
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(coord)
        self.snake_body.append(snake)

    def move(self):
        """ Moves the snake's body automatically """
        for part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # moving the first part forward

    def up(self):
        """ Moves the snake up """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ Moves the snake down """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ Moves the snake left """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ Moves the snake right """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        """ resets the snake once the game is over """
        for part in self.snake_body:
            part.goto(1000,1000)  # moving the current snake body off the screen
        self.snake_body.clear()  # this will remove all elements (turtles) in the snake list
        self.create_snake()  # will trigger the creation of a new snake
        self.head = self.snake_body[0]


class Food(Turtle):
    def __init__(self):
        """ Creating a dot of food """
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color('red')
        self.speed(0)
        self.new_loc()

    def new_loc(self):
        """ Generating food at a random spot on the screen """
        self.goto(random.randint(-270, 270), random.randint(-270, 270))


class ScoreBoard(Turtle):
    def __init__(self):
        """ Making a score count """
        super().__init__()
        self.score = 0
        with open('high_score_data.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.hideturtle()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        """ Displaying score """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 16, 'normal'))
        with open('high_score_data.txt', 'w') as file:
            file.write(str(self.high_score))

    def inc_score(self):
        self.score += 1
        self.update_score()

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
