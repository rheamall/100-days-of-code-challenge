import random
from replit import clear
from art import logo, vs
from game_data import data

def play():
    B = random.choice(data)
    score = 0
    loss = False
    
    while loss == False:
        print(logo)
        if score > 0:
            print(f'You\'re right! Current score: {score}')
        A = B
        B = random.choice(data)
        if A['follower_count'] != B['follower_count']:
            print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} \n")
            print(vs)
            print(f"\nCompare B: {B['name']}, a {B['description']}, from {B['country']}")
            guess = input('\nWho has more followers? Type "A" or "B": ').upper()
            if guess == 'A' and A['follower_count'] > B['follower_count']:
                score += 1
            elif guess == 'B' and A['follower_count'] < B['follower_count']:
                score += 1
            else:
                loss = True
        else:
            B = A
        clear()
    
    if loss == True:
        print(logo)
        print(f'Sorry, that\'s wrong. Final score: {score}')

playagain = 'yes'
while playagain != 'no':
    if playagain == 'yes':
        clear()
        play()
    playagain = input('\nWould you like to play again? Type "yes" or "no": ').lower()
    if playagain == 'yes':
        continue
    elif playagain == 'no':
        print('\nThanks for playing!')
    else:
        print('\nIncorrect input.')