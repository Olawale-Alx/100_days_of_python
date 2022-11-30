import tkinter


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tkinter.Tk()
window.title('Pomodoro')
window.minsize(height=450, width=500)
window.config(padx=80, pady=50, bg=YELLOW)

# Label
timer = tkinter.Label(text='Timer', fg=GREEN, font=(FONT_NAME, 30, 'bold'), bg=YELLOW)
timer.grid(column=1, row=0)

# Canvas
canvas = tkinter.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
photo = tkinter.PhotoImage(file='./tomato.png')
canvas.create_image(103, 112, image=photo)
canvas.create_text(103, 122, text='00:00', fill='white', font=('Mono Space', 26, 'bold'))
canvas.grid(column=1, row=1)

# Start Button
start_button = tkinter.Button(text='Start', font=(FONT_NAME, 12, 'italic'))
start_button.config(fg='red', bg=YELLOW, highlightthickness=0, activebackground='white',
                    activeforeground='red')
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tkinter.Button(text='Reset', font=(FONT_NAME, 12, 'italic'))
reset_button.config(fg='red', bg=YELLOW, highlightthickness=0, activebackground='white',
                    activeforeground='red')
reset_button.grid(column=2, row=2)

# CheckMark
check_marks = tkinter.Label(text='✔', fg=GREEN, font=(FONT_NAME, 30, 'bold'), bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
