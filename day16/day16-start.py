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
# table.border = False
table.header_style = 'upper'
table.align = 'l'
# table.add_column('Pokemon Name',
#                  ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type',
#                  ['Electric', 'Water', 'Fire'])
table.add_column('First Name',
                 ['Olawale', 'Anita', 'Sayo', 'Peace', 'Oyinlola'])
table.add_column('Last Name',
                 ['Olaleye', 'Bartholomew', 'Osuntokun', 'Umoren', 'Akinseinde'])


print(table)
print(table.get_string(start=2, end=4))
