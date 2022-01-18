# TODO: 1. Make menu list for all types of coffee drinks made by the machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

# TODO: 2. List out money made by the machine and resources it has
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 3. Write a function that checks ingredients availability
# This function checks whether we have enough ingredients to run an order
def is_resources_enough(order_ingredients):
    """This checks the order ingredients and see if we have enough resources to make the coffee"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry, there is not enough {item}.')
            return False

        else:
            return True


# TODO: 4. Write a function that processes payments
def process_payment():
    """Calculates the total coins inserted in the machine"""
    print('Please insert coins to pay for your drink:')
    total_amount = int(input('How many quarters: ')) * 0.25
    total_amount += int(input('How many dimes: ')) * 0.10
    total_amount += int(input('How many nickles: ')) * 0.05
    total_amount += int(input('How many pennies: ')) * 0.01
    return total_amount


# TODO: 5. Write a function that checks if there if customer paid enough money
def successful_transaction(received, drink_cost):
    """This function returns true if the received amount is greater than the drink cost, false
    if it is lesser than the drink cost"""
    if received >= drink_cost:
        change = round(received - drink_cost, 2)
        print(f'Here is your change: {change}')
        global profit
        profit += drink_cost
        return True

    else:
        print(f'That is not enough money. Payment of ${received} refunded.')
        return False


# TODO: 6. Make a function that checks if there is enough ingredients to make the coffee
def make_a_coffee(drink_name, order_ingredients):
    """This function calculates the ingredients needed to make a drink.
    Returns true if there is enough ingredients, false if any of the ingredients is
    not enough and refunds the customer."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕☕☕. Enjoy!')


machine_on = True

while machine_on:
    choice = input('What would you like to drink? [espresso/latte/cappuccino]: ').lower()

    if choice == 'off':
        machine_on = False

    elif choice == 'report':
        print(f'water: {resources["water"]}ml')
        print(f'milk: {resources["milk"]}ml')
        print(f'coffee: {resources["coffee"]}g')
        print(f'profit: ${profit}')

    else:
        drink = MENU[choice]
        if is_resources_enough(drink['ingredients']):
            payment = process_payment()
            if successful_transaction(payment, drink['cost']):
                make_a_coffee(choice, drink['ingredients'])
