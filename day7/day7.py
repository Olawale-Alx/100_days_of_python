import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

lives = 6
display = []
end_of_game = True

print(logo)

chosen_word = random.choice(word_list)

# TODO1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_"
# representing each letter to guess.
for _ in chosen_word:
    display += '_'
# Join all the elements in the list and turn it into a String.
print(f"{' '.join(display)}")

# TODO1: - Use a while loop to let the user guess again. The loop should only stop once the user
# has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you
# can tell the user they've won.
while end_of_game:
    guess = input('\nMake a letter guess: ').lower()

    # Testing code
    # print(f'Pssst, the solution is {chosen_word}.')

    # TODO4: - If the user has entered a letter they've already guessed, print the letter and let
    # them know.
    if guess in display:
        print(f'You already guessed the word {guess} before.')

    # TODO2: - Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that
    # position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_",
    # "p", "p", "_", "_"].
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if '_' not in display:
        print('You win')
        end_of_game = False

    # TODO2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1
        # TODO5: - If the letter is not in the chosen_word, print out the letter and let them know
        # it's not in the word.
        print(stages[lives])
        print(f'Your guess: {guess} is not in the chosen word')
        if lives == 0:
            print('You lost')
            end_of_game = False
