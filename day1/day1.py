# 1. Create a greeting for your program.

print('Hello and welcome to the band name generator!')

# 2. Ask the user for the city that they grew up in.

city_name = input('What is the name of the city you grew up in?\n')

# 3. Ask the user for the name of a pet.

pet_name = input('What is the name of your faorite pet?\n')

# 4. Combine the name of their city and pet and show them their band name.

print(f'\nIf the name of the city you grew up in is {city_name} and the name of your favorite pet is {pet_name}, then the name of your band will be: {city_name.capitalize()}{pet_name.capitalize()}')

# 5. Make sure the input cursor shows on a new line, see the example at:
# https://replit.com/@appbrewery/band-name-generator-end
