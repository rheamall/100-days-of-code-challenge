import random
from symbols import rock, paper, scissors

rounds = int(input('How many rounds would you like to play?\n'))
wins = 0
for i in range(rounds):
    print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')
    choice = int(input())
    comp = random.randint(0,2)
    play = [rock, paper, scissors]

    print(play[choice])

    print('Computer chose:')
    print(play[comp])

    if choice == comp:
        print('Draw')
    elif choice == 0 and comp == 1:
        print('You lose')
    elif choice == 0 and comp == 2:
        print('You win')
        wins += 1
    elif choice == 1 and comp == 0:
        print('You win')
        wins += 1
    elif choice == 1 and comp == 2:
        print('You lose')
    elif choice == 2 and comp == 0:
        print('You lose')
    elif choice == 2 and comp == 1:
        print('You win')
        wins += 1
    else:
        print('Invalid input')

if wins > rounds/2:
    print('You won the game!')