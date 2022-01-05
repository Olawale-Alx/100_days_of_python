from logo import logo
from replit import clear

# Calculator


# Addition
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


def modulo(n1, n2):
    return n1 % n2


def exponential(n1, n2):
    return n1 ** n2


math_operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
  '%': modulo,
  '**': exponential,
}


def calculator():
    """
    This function takes inputs from the user in form of numbers and math symbols to perform a
    mathematical operation
    """
    print(logo)
    input1 = float(input('Enter the first number? '))

    start = True

    while start:
        for ops in math_operations:
            print(ops)

    ops_symbol = input('Pick an operation from the above operations symbols: ')

    input2 = float(input('Enter the next number? '))

    if ops_symbol == '+':
        answer = add(input1, input2)
        print(f'{input1} {ops_symbol} {input2} = {answer}')

    elif ops_symbol == '-':
        answer = subtract(input1, input2)
        print(f'{input1} {ops_symbol} {input2} = {answer}')

    elif ops_symbol == '*':
        answer = multiply(input1, input2)
        print(f'{input1} {ops_symbol} {input2} = {answer}')

    elif ops_symbol == '/':
        answer = divide(input1, input2)
        print(f'{input1} {ops_symbol} {input2} = {answer}')

    elif ops_symbol == '%':
        answer = modulo(input1, input2)
        print(f'{input1} {ops_symbol} {input2} = {answer}')

    elif ops_symbol == '**':
        answer = exponential(input1, input2)
        print(f'{input1} {ops_symbol} {input2} = {answer}')

    else:
        print('\nERROR: INVALID OPERAND FOR THE OPERATION YOU ARE TRYING TO PERFORM!')

    cont = input('Enter y to continue your calculation or n to to start a new calculation: '
                 '').lower()

    if cont == 'y':
        input1 = answer

    else:
        start = False
        clear()
        calculator()


calculator()
