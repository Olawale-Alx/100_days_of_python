from random import randint
from art import logo
from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's
# answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard
# mode).

# Task 1: Take player name and print greetings
# Task 2: Ask player for difficulty levels
# Task 3: Pick a random number using random.randint
# Task 4: Add two variables to track player attempts and remaining attempts
# Task 5: Ask player to make a guess
# Task 6: There can be four options: Too low, Too high, Win or Lose.
# player_attempt against answer and return to guess if answer is incorrect and player still has more
# attempts, lose if none or win if attempt = answer


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    def greeting():
        player_name = input('Enter player name to continue: ')
        clear()
        print(logo)
        print(f'Welcome to the Number Guessing Game, {player_name.title()}')

    greeting()

    # Choosing a random number between 1 and 100.
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f'The correct answer is {answer}')

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

