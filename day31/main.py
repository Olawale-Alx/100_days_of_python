from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

# --------- INTERFACE --------- #
# Tkinter Window
window = Tk()
window.title('Flash Card Project')
window.minsize(width=670, height=560)
window_photo = PhotoImage(file='images/right.png')
window.iconphoto(False, window_photo)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

# Canvas to set on the window
canvas = Canvas(width=880, height=560, highlightthickness=0, bg=BACKGROUND_COLOR)
photo = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(450, 290, image=photo)
canvas.create_text(440, 200, text='Title', font=('Arial', 25, 'italic'), justify='center')
canvas.create_text(440, 320, text='Word', font=('Arial', 38, 'bold'), justify='center')
canvas.grid(row=0, column=0, columnspan=2)

# Right button
right_button_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_button_image, highlightthickness=0,
                      bg=BACKGROUND_COLOR, cursor='hand2')
right_button.grid(row=1, column=1)

# Wrong button
wrong_button_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_button_image, highlightthickness=0,
                      bg=BACKGROUND_COLOR, cursor='hand2')
wrong_button.grid(row=1, column=0)

window.mainloop()
