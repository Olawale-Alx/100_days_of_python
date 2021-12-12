# Password Generator Project
# Import the random module
import random

# Create lists for your letters, symbols and numbers
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Ask the user to enter the amount of characters they need to make their unique password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty string variable to store the password
password = ''

# first, add random letters to the password string based on number of characters from the user
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
    # This makes use of the random module to randomly choose among letters

# Next, add random numbers to the password string based on number of characters from the user
for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)
    # This makes use of the random module to randomly choose among numbers

# Next, add random symbols to the password string based on number of characters from the user
for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)
    # This makes use of the random module to randomly choose among symbols

print(f'Password: {password}')

# To make the password arrange the numbers, letters and symbols randomly
# Again, I make use of random.choice to randomly rearrange the strings in the password variable

# Initializes an empty string
hard_password = ''

for hard in range(1, len(password)):
    hard_password += random.choice(password)

print(f'Hard Password: {hard_password}')
