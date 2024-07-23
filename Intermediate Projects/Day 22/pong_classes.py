from turtle import Turtle
import time

DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, my_start_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5)
        self.penup()
        self.goto(my_start_pos)
        self.setheading(90)

    def move_up(self):
        self.forward(DISTANCE)

    def move_down(self):
        self.backward(DISTANCE)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.home()
        self.x_dist = 10
        self.y_dist = 10

    def movements(self):
        new_x = self.xcor() + self.x_dist
        new_y = self.ycor() + self.y_dist
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_dist *= -1

    def paddle_bounce(self):
        self.x_dist *= -1

    def ball_reset(self):
        self.home()
        time.sleep(0.5)
        self.x_dist *= -1


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-40, 200)
        self.write(self.left_score, align='center', font=('Courier', 32, 'normal'))
        self.goto(40, 200)
        self.write(self.right_score, align='center', font=('Courier', 32, 'normal'))

    def right_point(self):
        self.right_score += 1
        self.update_scores()

    def left_point(self):
        self.left_score += 1
        self.update_scores()
