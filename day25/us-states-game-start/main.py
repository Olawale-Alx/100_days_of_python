import turtle
import pandas


# TODO: Project: Guess the name of the State
# Use the screen method in the turtle import to create the screen for the game
screen = turtle.Screen()
screen.title('U.S States Game')
screen_image = './blank_states_img.gif'
screen.addshape(screen_image)
turtle.shape(screen_image)

# Read the data from the csv file
data = pandas.read_csv('./50_states.csv')
states_data = data.state.to_list()
total_correct_guesses = 0
correct_guess_list = []

# Use a while loop to keep the game running
while len(correct_guess_list) < 50:
    answer = screen.textinput(title=f'{total_correct_guesses}/50 States Guessed',
                              prompt='What is another state?').title()

    # check if answer == exit. if yes, quit the game
    if answer == 'Exit'.title():
        missing_states = []
        for state in states_data:
            # Use an if loop to check for missing states from the correctly guessed states
            if state not in correct_guess_list:
                missing_states.append(state)
            csv_data = pandas.DataFrame(missing_states)
            csv_data.to_csv('./missing_states.csv')
        break

    # TODO: If answer is one of the states in all the states of the 50_states_CSV
    if answer in states_data:
        correct_guess_list.append(answer)
        # Use turtle to write the name of the state on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        xy_cord = data[data.state == answer]
        t.goto(int(xy_cord.x), int(xy_cord.y))
        t.write(answer)
