# from turtle import Turtle, Screen
# import random

# timmy = Turtle()
#
# timmy.shape('turtle')
# timmy.color('coral')

# CHALLENGE: Make a square shape
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# CHALLENGE: Make a dashed line
# for i in range(10):
#     timmy.forward(10)
#     timmy.pencolor('white')
#     timmy.forward(10)
#     timmy.pencolor('coral')
# OR:
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# CHALLENGE: Make a triangle up to a decagon overlaid on each other, each drawn with a random color
# colours = ["tomato", "light coral", "crimson", "dark magenta", "deep pink", "indigo",
#            "dark orange", "firebrick", "medium violet red", "royal blue", "pale green",
#            "teal", "light sea green", "pale green"]  # obtained from https://trinket.io/docs/colors
#
# for i in range(3,11):
#     sides = i
#     timmy.color(random.choice(colours))
#     while sides > 0:
#         angle = ((i - 2) * 180) / i  # formula
#         timmy.forward(100)
#         timmy.right(180-angle)
#         sides -= 1

# CHALLENGE: Generate a random walk
# directions = [0, 90, 180, 270]
# # Using the earlier defined colours list
# timmy.pensize(15)
# timmy.speed(0)
#
# for _ in range(150):
#     timmy.forward(20)
#     timmy.color(random.choice(colours))
#     timmy.setheading(random.choice(directions))

# CHALLENGE: Generate a random walk while generating random RGB colours
# import turtle as t
#
# tim = t.Turtle()
# t.colormode(255)
#
# def gen_colours():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed(0)
#
# for _ in range(150):
#     tim.forward(20)
#     tim.color(gen_colours())
#     tim.setheading(random.choice(directions))


# CHALLENGE: Generate a spirograph
# tim.speed(0)
#
# def gen_colours():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple
#
# def spirograph(gap):
#     for i in range(360//gap):
#         tim.color(gen_colours())
#         tim.circle(100)
#         # tim.setheading(tim.heading() + gap)
#         tim.left(gap)
#
# spirograph(5)
#
# screen = Screen()
# screen.exitonclick()