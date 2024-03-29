from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                   'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '/', '?']

    nl_cap_letters = [random.choice(cap_letters) for char in range(random.randint(2, 4))]
    nl_small_letters = [random.choice(small_letters) for char in range(random.randint(3, 5))]
    nl_numbers = [random.choice(numbers) for num in range(random.randint(3, 5))]
    nl_symbols = [random.choice(symbols) for sym in range(random.randint(2, 5))]

    word = nl_cap_letters + nl_small_letters + nl_numbers + nl_symbols
    random.shuffle(word)
    suggested_password = ''.join(word)
    password_entry.insert(0, suggested_password)
    pyperclip.copy(suggested_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_on_click():
    acc_name = account_entry.get()
    user_name = email_entry.get()
    secret = password_entry.get()

    if acc_name == '' or len(secret) < 8 or user_name == '':
        messagebox.showinfo(title=acc_name, message='Username cannot be empty and password cannot be less than '
                                                    'eight')
    else:
        proceed = messagebox.askokcancel(title=acc_name, message=f'Login Details:\nUser Name: {user_name}\n'
                                                                 f'Password: {secret}\n Okay to proceed?')
        if proceed:
            json_data = {acc_name: {
                'Username': user_name,
                'Password': secret
            }}

            try:
                # Here, we read the json data and update with the new data
                with open('/home/vagrant/Desktop/password_data_list.json', mode='r') as pass_gen:
                    # Load the data
                    data = json.load(pass_gen)
                    # Update the data
                    data.update(json_data)

                # Here, we write the updated data to the existing file
                with open('/home/vagrant/Desktop/password_data_list.json', mode='w') as pass_gen:
                    json.dump(data, pass_gen, indent=4)

            except FileNotFoundError:
                with open('/home/vagrant/Desktop/password_data_list.json', mode='w') as pass_gen:
                    json.dump(json_data, pass_gen, indent=4)

            finally:
                account_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SEARCH BUTTON FUNCTIONALITY ------------ #
def find_password():
    acc_name = account_entry.get()

    try:
        with open('/home/vagrant/Desktop/password_data_list.json', mode='r') as pass_gen:
            data = json.load(pass_gen)

            if acc_name in data:
                messagebox.showinfo(title=f'{acc_name}', message=f'Username: {data[acc_name]["Username"]}\n'
                                                                 f'Secret: {data[acc_name]["Password"]}')

            else:
                messagebox.showinfo(title=f'{acc_name}', message=f'No details exist for {acc_name}!')

    except FileNotFoundError:
        messagebox.showinfo(title='File', message='No Data File Found!!!')


# ---------------------------- UI SETUP ------------------------------- #
YELLOW = "#f7f5dd"

window = Tk()
window.title('Password Generator')
window.minsize(height=450, width=300)
window_photo = PhotoImage(file='./logo.png')
window.iconphoto(False, window_photo)
window.config(padx=60, pady=20, bg=YELLOW)

# Layout is 3col and 5row
# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=YELLOW)
photo = PhotoImage(file='./logo.png')
image = canvas.create_image(100, 120, image=photo)
canvas.grid(pady=20, padx=0, column=0, row=0, columnspan=3)

# Label for account name
account_name = Label(text='Account Name:', justify='left', bg=YELLOW)
account_name.grid(pady=4, column=0, row=1)

# Entry for account name
account_entry = Entry(width=22, bd=2, highlightthickness=0)
account_entry.focus()
account_entry.grid(column=1, row=1, columnspan=1)

# Button for account search
account_search = Button(text='Search', width=15, bd=1, highlightthickness=0, cursor='hand2',
                        bg='white', command=find_password)
account_search.grid(column=2, row=1)

# Label for email/username
email_user = Label(text='Email/Username:', justify='left', bg=YELLOW)
email_user.grid(pady=4, column=0, row=2)

# Entry for email/username
email_entry = Entry(width=41, bd=2, highlightthickness=0)
email_entry.insert(0, 'olaleyeolawale2020@outlook.com')
email_entry.grid(column=1, row=2, columnspan=2)

# Label for password
password = Label(text='Password:', justify='left', bg=YELLOW)
password.grid(pady=4, column=0, row=3)

# Entry for password
password_entry = Entry(width=22, bd=2, highlightthickness=0)
password_entry.grid(column=1, row=3)

# Generate Password button
generate_button = Button(text='Generate Password', width=15, bd=1, highlightthickness=0, cursor='hand2',
                         bg='white', command=password_generator)
generate_button.grid(column=2, row=3)

# Add button
add_button = Button(text='Add', width=39, bd=1, highlightthickness=0, cursor='hand2', bg='white',
                    command=add_on_click)
add_button.grid(pady=15, column=1, row=4, columnspan=2)

window.mainloop()
