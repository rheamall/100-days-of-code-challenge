from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(20)
def backwards():
    tim.backward(20)
def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def myclear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="W", fun=forwards)  # higher order function i.e. a function that can work with other functions
screen.onkey(key="S", fun=backwards)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=myclear)

screen.exitonclick()
