from prettytable import PrettyTable

# import turtle
#
# tim = turtle.Turtle()
# print(tim)
# tim.shape('turtle')
# tim.color('red', 'green')
# tim.forward(100)
#
#
# show_screen = turtle.Screen()
# print(show_screen.canvheight)
# show_screen.exitonclick()

table = PrettyTable()
table.add_column('Pokemon Name',
                 ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type',
                 ['Electric', 'Water', 'Fire'])
table.align = 'r'

print(table)
