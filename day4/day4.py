import random

# This imports the random module

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# Player name and introduction
player_name = input('Enter player name:\n').capitalize()

print(f'Welcome to the rock, paper and scissors game {player_name}')

# Game Instructions
print('''
      GAME INSTRUCTIONS

    You pick an option between rock, paper and scissors and the computer also picks its options and the program checks \
    for a winner

    Player Input = 0 for rock, 1 for paper, 2 for scissors
''')

# Convert the game options to a list
choices = [rock, paper, scissors]

# Initialize the scoreboard for the players and total games played
player_score = 0
computer_scores = 0
games_played = 0

# Loop function
while True:

    # Player choice
    player_option = int(input('What do you pick between rock, paper and scissors:\n'))
    player_option = choices[player_option]

    # Computer's choice
    computer = random.randint(0, (len(choices) - 1))
    computer_option = choices[computer]

    # If, elif and else to check the conditions of player and computer's choice
    if player_option == choices[0] and computer_option == choices[2]:
        print(f'You picked {player_option}')
        print(f'Computer picked {computer_option}')
        games_played += 1
        player_score += 1
        print('You won this round')

    elif player_option == choices[2] and computer_option == choices[1]:
        print(f'You picked {player_option}')
        print(f'Computer picked {computer_option}')
        games_played += 1
        player_score += 1
        print('You won this round')

    elif player_option == choices[1] and computer_option == choices[0]:
        print(f'You picked {player_option}')
        print(f'Computer picked {computer_option}')
        games_played += 1
        player_score += 1
        print('You won this round')

    else:
        print(f'You picked {player_option}')
        print(f'Computer picked {computer_option}')
        games_played += 1
        computer_scores += 1
        print('Computer won this round')

    # This check whether the player still wants to play or end the game
    # If yes, it goes to the top of he while loop and starts the conditions all oer again
    # If no, it ends the game and prints the scores for each player and total games played
    cont = input('Do you want to continue playing (Y/N): ').capitalize()
    if cont == 'Y':
        continue

    else:
        print(f'Computer Scores: {computer_scores}')
        print(f'Your scores: {player_score}')
        print(f'Number of games played: {games_played}')
        break

exit(0)
