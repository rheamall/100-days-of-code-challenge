from obtaining_colours import final_colours
import turtle as t
import random

dots = t.Turtle()
t.colormode(255)
dots.speed(0)
dots.penup()
dots.hideturtle()
dots.setposition(-170,-160)

for i in range(10):
    for _ in range(10):
        dots.dot(15, random.choice(final_colours))
        dots.forward(40)
    if i % 2 == 0:
        dots.left(90)
        dots.forward(40)
        dots.left(90)
    else:
        dots.right(90)
        dots.forward(40)
        dots.right(90)
    dots.forward(40)

screen = t.Screen()
screen.exitonclick()