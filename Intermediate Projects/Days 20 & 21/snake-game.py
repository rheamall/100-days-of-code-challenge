from turtle import Screen
from game_classes import Snake, Food, ScoreBoard
import time

screen = Screen()

# SCREEN SETUP
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

# CONTROLLING THE SNAKE BY 'LISTENING' TO KEYSTROKES
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# MOVING THE SNAKE
game_on = True
my_score = 0
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detecting collision with food and updating score
    if snake.head.distance(food) < 20:
        food.new_loc()
        snake.extend_snake()
        my_score += 1
        score.update_score(my_score)
    # Detecting collision with wall
    if abs(snake.head.xcor()) > 285 or abs(snake.head.ycor()) > 285:
        game_on = False
        score.game_over()
    # Detecting collision with tail
    for i in snake.snake_body[1:]:
        if snake.head.distance(i) < 5:
            game_on = False
            score.game_over()

screen.exitonclick()
