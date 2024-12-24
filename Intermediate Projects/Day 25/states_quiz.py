import pandas as pd
import turtle

screen = turtle.Screen()
screen.title('Indian States Game')
image_path = 'india28.gif'
screen.addshape(image_path)
turtle.shape(image_path)

# def get_mouse_click_coor(x,y):
#     ''' to get the coordinates of each state from the image '''
#     print(f'{x},{y}')
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

df = pd.read_csv('indian_states.csv')
correct_guesses = []

t1 = turtle.Turtle()
t1.penup()
t1.hideturtle()

while len(correct_guesses) < 28:

    answer = screen.textinput(title=f'{len(correct_guesses)}/28 states correct!', prompt='Name as many states as you can. (Type "exit" to quit)')
    answer = answer.title()

    if answer == 'Exit':
        break

    row = df[df['State'] == answer]
    if not row.empty:
        correct_guesses.append(answer)
        t1.goto(row['x'].item(), row['y'].item())
        t1.write(f'{answer}', font=("Arial", 10, "normal"))

t1.goto((66.0,-132.0))
if len(correct_guesses) == 28:
    t1.write(f'Wow. You got it all!', font=("Arial", 15, "normal"))
else:
    t1.write(f'Well played.', font=("Arial", 15, "normal"))

screen.exitonclick()
