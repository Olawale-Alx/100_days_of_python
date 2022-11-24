import tkinter


window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(height=400, width=600)
window.config(padx=40, pady=60, bg='white')

# First Widget, entry
entry = tkinter.Entry(width=14, bg='white', bd=2, justify='center',
                      font=('Mono Space', 14, 'italic'))
entry.grid(column=1, row=0)
# entry.config(-padx=2, -pady=3)

# Second Widget, label
label_one = tkinter.Label(text='Miles', font=('Mono Space', 16, 'bold'), bg='white')
label_one.grid(column=2, row=0)
label_one.config(padx=15)

# Third Widget, label
label_two = tkinter.Label(text='is equal to', font=('Mono Space', 16, 'bold'), bg='white')
label_two.grid(column=0, row=1)
label_two.config(padx=5, pady=18)

# Fourth Widget, label
label_three = tkinter.Label(text=0, font=('Mono Space', 16, 'bold'), bg='white')
label_three.grid(column=1, row=1)

# Fifth Widget, label
label_four = tkinter.Label(text='Km', font=('Mono Space', 16, 'bold'), bg='white')
label_four.grid(column=2, row=1)


# Sixth Widget, Button
def converter():
    try:
        num = float(entry.get())
        mile_to_km = num * 1.609344
        label_three.config(text=round(mile_to_km, 2))
    except ValueError:
        label_three.config(text='Value must be int')


calculator_button = tkinter.Button(text='Calculate', bg='white', fg='black',
                                   font=('Mono Space', 13, 'bold'), command=converter)
calculator_button.grid(column=1, row=3)

window.mainloop()
