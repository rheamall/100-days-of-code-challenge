from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_money = MoneyMachine()
my_coffee = CoffeeMaker()


def main():
    option = ''

    while option != 'off':
        print('\nWelcome ☕ What would you like to do?\n1. To make an order, type "order"')
        print('2. To check the coffee machine report, type "report"\n3. To turn off the machine, type "off"')
        option = input('Type here: ').lower()

        if option == 'order':
            print('What would you like to order?')
            coffee = input(f'{my_menu.get_items()} Type here: ').lower()
            tmp = my_menu.find_drink(coffee)
            if tmp is not None:
                available = my_coffee.is_resource_sufficient(tmp)
                if available:
                    enough_money = my_money.make_payment(tmp.cost)
                    if enough_money:
                        my_coffee.make_coffee(tmp)
                    else:
                        continue
        elif option == 'report':
            print('Currently, this is the state of the coffee machine:')
            my_coffee.report()
        elif option == 'off':
            print('Machine turned off.')
            break
        else:
            print('Invalid option')

main()