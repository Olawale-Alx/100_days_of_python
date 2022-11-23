import tkinter


# Window
window = tkinter.Tk()
window.title('GUI App')
window.minsize(width=600, height=600)

# Label
myLabel = tkinter.Label(text='\n\nWelcome, Olawale Olaleye', font=('Mono Space', 28, 'bold'),
                        fg='green', bg='yellow')
myLabel.pack()


# Button
def onclick():
    print('Button got clicked.')
    myLabel.config(text='Button got clicked')


my_button = tkinter.Button(text='Click Me!', fg='blue', bg='white', font=('Sans Serif', 18, 'bold'),
                           command=onclick)
my_button.pack()


window.mainloop()
