import random


codes = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

booking = []
for code in range(8):
    booking.append(random.choice(codes))

books = ''.join(booking)
print(books)

