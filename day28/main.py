import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
repetition = 0
timer_window = None
marks = ''


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global marks
    window.after_cancel(timer_window)
    canvas.itemconfig(canvas_text, text='00:00')
    timer.config(text='Timer')
    marks = ''


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetition
    repetition += 1

    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if repetition % 8 == 0:
        counter(long_break_sec)
        timer.config(text='Long Break', fg=RED)
    elif repetition % 2 == 0:
        counter(short_break_sec)
        timer.config(text='Short Break', fg=PINK)
    else:
        counter(work_sec)
        timer.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    global marks
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer_window
        timer_window = window.after(1000, counter, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(repetition / 2)
        for _ in range(work_sessions):
            marks += '✅'
        check_marks.config(text=marks)


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
canvas_text = canvas.create_text(103, 122, text='00:00', fill='white', font=('Mono Space', 26, 'bold'))
canvas.grid(column=1, row=1)

# Start Button
start_button = tkinter.Button(text='Start', font=(FONT_NAME, 12, 'italic'))
start_button.config(fg='red', bg=YELLOW, highlightthickness=0, activebackground='black',
                    activeforeground='red', command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tkinter.Button(text='Reset', font=(FONT_NAME, 12, 'italic'))
reset_button.config(fg='red', bg=YELLOW, highlightthickness=0, activebackground='black',
                    activeforeground='red', command=reset_timer)
reset_button.grid(column=2, row=2)

# CheckMark
check_marks = tkinter.Label(fg='white', font=(FONT_NAME, 30, 'bold'), bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
