print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
player_name = input('Hello, Enter player name here:\n').capitalize()
print(f"Welcome to Treasure Island {player_name}.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print('\nYou\'re at a crossroad. Where do you want to go\n')

action_1 = input('Type "left" or "right":\n').lower()
# print(action_1)

if action_1 == 'right':
    print('You\'ve come to a lake.')
    action_2 = input('Type "wait" to wait for a boat. Type "swim" to swim across:\n').lower()

    if action_2 == 'wait':
        print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue')
        action_3 = input('Which color do you choose:\n').lower()

        if action_3 == 'red':
            print('It\'s a room full of fire. Game Over')

        elif action_3 == 'yellow':
            print('You found the treasure! You Win!')

        elif action_3 == 'blue':
            print('You enter a room of beasts. Game Over')

        else:
            print('You choose a door that doesn\'t exist. Game Over')

    elif action_2 == 'swim':
        print('You try to swim across and got eaten by a crocodile')

    else:
        print('Invalid Input')


elif action_1 == 'left':
    print('You took left and passed through the desert. You got eaten by a Lion before getting past the crossroad')

else:
    print('Invalid Input')
