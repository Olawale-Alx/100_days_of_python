from art import logo, vs
from game_data import data
import random
from replit import clear

# The logo and vs import are to import the ASCII images from the art.py file
# The data import imports data from game_data.py file for the game
# The random import is used to randomize data file selections for the game
# clear() is imported from replit to clear game data in order to avoid scrolling on game screen


def format_data(account):
    """Take account input and Format the account data into a printable format"""

    # This takes data from the game_data so it can be converted to human readable format
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f'{account_name}, {account_description}, {account_country}'


def check_answer(guess, a_follow_count, b_follow_count):
    """Use if statement to check if guess is right or wrong"""
    if a_follow_count > b_follow_count:
        if player_guess == 'A':
            return True

        else:
            return False

    else:
        if player_guess == 'B':
            return True

        else:
            return False


# Display art files
print(logo)
player_score = 0
game_should_continue = True
# Generate a random account from the game data
second_account = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Make the account at position B to be moved to position A if player guess is correct
    first_account = second_account
    # Generate a random account from the game data
    second_account = random.choice(data)
    # print(first_account)
    # print(second_account)
    while second_account == first_account:
        second_account = random.choice(data)

    account_a = format_data(first_account)
    account_b = format_data(second_account)

    # This compares game data A and game data B and ask the user to guess who has more followers
    print(f'Compare A: {account_a}')
    print(f'\n{vs}\n')
    print(f'Compare B: {account_b}')

    # Ask user for a guess
    player_guess = input('Who has more followers: A or B: ').upper()

    # Check answer to see if it is right or wrong
    # Get follower account of each account
    a_follower_count = first_account['follower_count']
    b_follower_count = second_account['follower_count']

    is_correct_answer = check_answer(player_guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # Keep scores
    # Clear the screen between rounds
    if is_correct_answer:
        player_score += 1
        clear()
        print(logo)
        print('You are right')
        print(f'Current Score: {player_score}')

    else:
        game_should_continue = False
        print('Sorry, that\'s wrong')
        print(f'Final Score: {player_score}')
