from art import logo

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

operators = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
}

cont = 'new'
solution = 0
print(logo)

def calculator():
    op = input('\nWhat operation would you like to do? \n+\n-\n*\n/\nType your input: ')
    num2 = float(input('\nInput the second number: '))
    ans = operators[op]
    solution = ans(num1,num2)
    print(f'\n{num1} {op} {num2} = {solution}')
    return solution

while True:
    if cont == 'new':
        num1 = float(input('\nInput the first number: '))
        solution = calculator()
    elif cont == 'continue':
        num1 = solution
        solution = calculator()
    elif cont == 'stop':
        print('\nThank you for using the calculator!')
        break
    else:
        print('Invalid input.')
    cont = input(f'\nWhat would you like to do?\n1. Type "new" to begin a new calculation\n2. Type "continue" to continue calculations with {solution}\n3. Type "stop" to stop using the calculator.\nType your input: ').lower()