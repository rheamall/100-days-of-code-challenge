# TODO: Coffee machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "dollars",
}


def my_order(order):
    output = "0"
    for i in MENU:
        if order == i:
            output = calc_resources(MENU[i]['ingredients'], MENU[i]['cost'])
    if output == "0":
        print('Invalid order.')
    elif output == "1":
        process_coins(order)
    else:
        print(output)


def process_coins(order):
    print('Enter the number of pennies, nickels, dimes and quarters you have.')
    pennies = int(input('Number of pennies: '))
    nickels = int(input('Number of nickels: '))
    dimes = int(input('Number of dimes: '))
    quarters = int(input('Number of quarters: '))
    money = round(0.01 * pennies + 0.05 * nickels + 0.1 * dimes + 0.25 * quarters, 2)
    if money < MENU[order]['cost']:
        print('Sorry, that\'s not enough money. Money refunded.')
        resources['water'] += mydic['water']
        resources['milk'] += mydic['milk']
        resources['coffee'] += mydic['coffee']
        resources['money'] -= money
    elif money > MENU[order]['cost']:
        change = money - MENU[order]['cost']
        print(f'Here\'s your change: ${change:.2f}. ')
        print(f'Your {order} will be ready within a minute. Enjoy!')
    else:
        print(f'Your {order} will be ready within a minute. Enjoy!')


def calc_resources(mydic, cost):
    if resources['water'] >= mydic['water'] and resources['milk'] >= mydic['milk'] and resources['coffee'] >= mydic['coffee']:
        resources['water'] -= mydic['water']
        resources['milk'] -= mydic['milk']
        resources['coffee'] -= mydic['coffee']
        resources['money'] += cost
        return "1"
    elif resources['water'] < mydic['water']:
        return 'Sorry, there\'s not enough water.'
    elif resources['milk'] < mydic['milk']:
        return 'Sorry, there\'s not enough milk.'
    elif resources['coffee'] < mydic['coffee']:
        return 'Sorry, there\'s not enough coffee.'
    else:
        return 'Invalid entry.'


def main():
    option = ''

    while option != 'off':
        print('\nWelcome ☕ What would you like to do?\n1. To make an order, type "order"')
        print('2. To check the coffee machine report, type "report"\n3. To turn off the machine, type "off"')
        option = input('Type here: ').lower()

        if option == 'order':
            coffee = input('What would you like to order: latte, espresso or cappuccino? Type here: ').lower()
            my_order(coffee)
        elif option == 'report':
            print('Currently, this is the state of the coffee machine:')
            for i in resources:
                print(f'{i.title()}: {resources[i]} {units[i]}')
        elif option == 'off':
            print('Machine turned off.')
            break
        else:
            print('Invalid option')

main()