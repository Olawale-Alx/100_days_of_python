import random
 

word_list = ["aardvark", "baboon", "camel"]
lives = 6
display = []

chosen_word = random.choice(word_list)
# print(chosen_word)

#TODO1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

for _ in chosen_word:
  display += '_'

print(display)

#TODO1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while True:

  guess = input('Make a letter guess: ').lower()
  # print(guess)

  #TODO3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

  for letters in chosen_word:
    if guess == letters:
      print('right')

    else:
      print('wrong')

  #Testing code
  print(f'Pssst, the solution is {chosen_word}.')

  #TODO2: - Loop through each position in the chosen_word;
  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  print(display)

  if '_' not in display:
    print('You win')
    break

  #TODO2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

  if guess not in chosen_word:
    lives -= 1

    if lives == 0:
      print('You lost')


  #Join all the elements in the list and turn it into a String.

  print(f"{' '.join(display)}")

#Check if user has got all letters.

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

#TODO-2: - Import the stages from hangman_art.py and make this error go away.

#TODO-2: - Import the stages from hangman_art.py and make this error go away.
    # print(stages[lives])
