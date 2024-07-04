import random

logo = '''
░█▀█░█░█░█▄█░█▀▄░█▀▀░█▀▄░░░█▀▀░█░█░█▀▀░█▀▀░█▀▀░▀█▀░█▀█░█▀▀░░░█▀▀░█▀█░█▄█░█▀▀
░█░█░█░█░█░█░█▀▄░█▀▀░█▀▄░░░█░█░█░█░█▀▀░▀▀█░▀▀█░░█░░█░█░█░█░░░█░█░█▀█░█░█░█▀▀
░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀
'''

print(logo)
print('Welcome! I am thinking of an integer between 1 to 100 - your job is to guess it.')

playagain = 'y'
while playagain == 'y':
    level = input('Choose your difficulty level - type "easy" or "hard" here: ').lower()
    
    num = random.randint(1,100)
    attempts = {
        "easy" : 10,
        "hard" : 5,
    }
    a = attempts[level]
    gameover = 0
    print(f'You have {a} attempts in total.')
    
    while a > 0:
        guess = int(input("\nMake your guess: "))
        if guess > num:
            print('Too high!')
        elif guess < num:
            print('Too low!')
        else:
            print(f'Bravo, you got it! The number was indeed {num}.')
            gameover = 1
            break
        a -= 1
        print(f'You now have {a} attempts remaining.')
    
    if gameover == 0:
        print(f'\nGame over. The number was {num}')
    
    playagain = input('\nType "y" if you would like to play again, else type "n": ')

if playagain == 'n':
    print('\nThanks for playing!')