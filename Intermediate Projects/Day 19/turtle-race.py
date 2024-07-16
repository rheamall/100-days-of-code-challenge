from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
mybet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour: ")
colours = ['pink', 'purple', 'blue', 'green', 'yellow', 'orange', 'red']
turtles = []

y = 160
for i in colours:
    tim = Turtle(shape='turtle')
    tim.color(i)
    tim.penup()
    tim.goto(-235, y)
    y -= 50
    turtles.append(tim)

race_on = False
winner = ''
if mybet in colours:
    race_on = True

while race_on:
    for i in turtles:
        movement = random.randint(0, 10)
        i.forward(movement)
        if i.xcor() > 230:
            winner = i.pencolor()
            race_on = False

if mybet == winner:
    print(f'The winner is {winner}. You won!')
else:
    print(f'The winner is {winner}. Better luck next time!')

screen.exitonclick()