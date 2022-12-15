from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data = {}

# --------- NEW WORD GENERATOR --------- #
# Read csv_file and convert to a dictionary
try:
    data_file = pandas.read_csv('data/new_french_data.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    data = original_data.to_dict(orient='records')
else:
    data = data_file.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(title_text, text=data_file.keys()[0], fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_image, image=front_photo)
    flip_timer = window.after(3000, func=back_card)
    # canvas.after(3000, next_card)


def back_card():
    canvas.itemconfig(title_text, text=data_file.keys()[1], fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')
    canvas.itemconfig(canvas_image, image=back_photo)


def known_card():
    data.remove(current_card)
    new_data = pandas.DataFrame(data)
    new_data.to_csv('data/new_french_data.csv', index=False)
    next_card()


# ------------- INTERFACE -------------- #
# Tkinter Window
window = Tk()
window.title('Flash Card Project')
window.minsize(width=670, height=560)
window_photo = PhotoImage(file='images/right.png')
window.iconphoto(False, window_photo)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, back_card)

# Canvas to set on the window
canvas = Canvas(width=880, height=560, highlightthickness=0, bg=BACKGROUND_COLOR)
front_photo = PhotoImage(file='images/card_front.png')
back_photo = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(450, 290, image=front_photo)
title_text = canvas.create_text(440, 200, text='', font=('Arial', 25, 'italic'), justify='center')
word_text = canvas.create_text(440, 320, text='', font=('Arial', 38, 'bold'), justify='center')
canvas.grid(row=0, column=0, columnspan=2)

# Right button
right_button_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_button_image, highlightthickness=0,
                      bg=BACKGROUND_COLOR, cursor='hand2', command=next_card)
right_button.grid(row=1, column=1)

# Wrong button
wrong_button_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_button_image, highlightthickness=0,
                      bg=BACKGROUND_COLOR, cursor='hand2', command=known_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
