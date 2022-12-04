import random


word = []
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '&', '*', ';', '/', '?', '>']

# nl_letters = random.randint(8, 10)
# nl_numbers = random.randint(3, 6)

nl_letters = [word.append(random.choice(letters)) for char in range(random.randint(8, 10))]
nl_numbers = [word.append(random.choice(numbers)) for num in range(random.randint(3, 6))]
nl_symbols = [word.append(random.choice(symbols)) for sym in range(random.randint(2, 5))]
# for char in range(nl_letters):
#     word += (random.choice(letters))

# for char in range(nl_numbers):
#     word += random.choice(numbers)

random.shuffle(word)
words = ''.join(word)
print(words)
