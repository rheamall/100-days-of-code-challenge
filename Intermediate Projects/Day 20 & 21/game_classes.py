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
        self.color('white')
        self.hideturtle()
        self.goto(0, 275)
        self.update_score(0)

    def update_score(self, score):
        """ Displaying score """
        self.clear()
        self.write(f"Score: {score}", align="center", font=('Courier', 16, 'normal'))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=('Courier', 16, 'normal'))