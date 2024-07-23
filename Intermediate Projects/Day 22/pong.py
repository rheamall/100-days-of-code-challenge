from turtle import Screen, Turtle
from pong_classes import Paddle, Ball, ScoreBoard
import time

screen = Screen()

# SCREEN SETUP
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

line = Turtle('square')
line.color('white')
line.shapesize(stretch_wid=0.5)
line.penup()
line.goto(0, 300)
line.setheading(270)

for i in range(60):
    if i % 2 == 0:
        line.pendown()
        line.forward(10)
    else:
        line.penup()
        line.forward(10)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'W')
screen.onkey(left_paddle.move_down, 'S')

game_on = True
sleep_time = 0.1

while game_on and sleep_time >= 0:
    screen.update()
    time.sleep(sleep_time)
    ball.movements()

    # bouncing off the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detecting collision with the paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()
        sleep_time *= 0.9

    # when the right player misses
    if ball.xcor() > 380:
        ball.ball_reset()
        sleep_time = 0.1
        scoreboard.left_point()

    # when the left player misses
    if ball.xcor() < -380:
        ball.ball_reset()
        sleep_time = 0.1
        scoreboard.right_point()

screen.exitonclick()
