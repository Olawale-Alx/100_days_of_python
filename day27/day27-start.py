import tkinter


# Window
window = tkinter.Tk()
window.title('GUI App')
window.minsize(width=600, height=600)

# Label
myLabel = tkinter.Label(text='\n\nWelcome, Olawale Olaleye', font=('Mono Space', 28, ['italic', 'bold']),
                        fg='green', bg='yellow')
myLabel.grid(column=0, row=0)


# Button
def onclick():
    print('Button got clicked.')
    myLabel.config(text=entry.get())


my_button = tkinter.Button(text='Click Me!', fg='blue', bg='white', font=('Sans Serif', 18, 'bold'),
                           command=onclick)
my_button.grid(column=1, row=1)

# Entry - Something like an input field
entry = tkinter.Entry(bg='violet', bd=2, font=('Mono Space', 16, 'italic'), width=18)
entry.get()
entry.grid(column=3, row=2)

# Big text box
# text_box = tkinter.Text(height=12, width=50, font=('Sans Serif', 12))
# text_box.grid(column=2, row=3)

# New Button
new_button = tkinter.Button(text='New Button', bg='yellow', fg='blue', font=('Serif', 18, 'italic'),
                            highlightcolor='red')
new_button.grid(column=2, row=0)

window.mainloop()
