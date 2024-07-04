import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
restart = 'y'

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(mylist):
    score = sum(mylist)
    if len(mylist) == 2 and 11 in mylist and 10 in mylist:
        score = 0
    elif (score > 21) and (11 in mylist):
        mylist.remove(11)
        mylist.append(1)
        score = sum(mylist)
    return score    

def the_end(u_c, c_c):
    gameend = False
    u_sc = calculate_score(u_c)
    c_sc = calculate_score(c_c)
    if u_sc > 21 or u_sc == 0 or c_sc == 0:
        gameend = True
    return gameend

def compare(a, b):
    if a == b:
        return "Draw"
    elif b == 0:
        return "The dealer had a blackjack! You lose."
    elif a > 21:
        return "A bust! You went over 21. You lose."
    elif a == 0:
        return "Congratulations, you win with a blackjack!"
    elif b > 21:
        return "The dealer went over 21. You win!"
    elif a > b:
        return "Yay, you win!"
    else:
        return "You lost."

def play_game():
    for i in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card()) 
    gameend = the_end(user_cards, comp_cards)
    u_sc = calculate_score(user_cards) 

    print(f'Your cards: {user_cards}; Current score: {u_sc}')
    print(f'Dealer\'s first card: {comp_cards[0]}') 

    while gameend == False and u_sc < 21:
        another = input('\nType "y" to get another card and "n" to pass: ')
        if another == 'y':
            user_cards.append(deal_card())
            gameend = the_end(user_cards, comp_cards)
            u_sc = calculate_score(user_cards)
            if gameend == False and u_sc < 21:
                print(f'Your cards: {user_cards}; Current score: {u_sc}')
        else:
            gameend = True

    while calculate_score(comp_cards) < 17 and u_sc <= 21:
        comp_cards.append(deal_card())

    u_sc = calculate_score(user_cards) 
    c_sc = calculate_score(comp_cards)
    print(f'Your final hand: {user_cards}; Final score: {u_sc}')
    print(f'Dealer\'s final hand: {comp_cards}; Dealer\'s score: {c_sc}')
    print('\n',compare(u_sc, c_sc))

while restart == 'y':
    if restart == 'y':
        print(logo)
        user_cards = []
        comp_cards = []
        play_game()
    restart = input('\nType "y" if you want to restart the game, else type "n": ')

print('\nHope you had fun playing!')