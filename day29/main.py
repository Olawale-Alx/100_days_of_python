from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_on_click():
    acc_name = account_entry.get()
    user_name = email_entry.get()
    secret = password_entry.get()

    account_info = f'Account Name: {acc_name}, User Name: {user_name}, Secret: {secret}\n'

    with open('/home/vagrant/Desktop/password_generator.txt', mode='a') as pass_gen:
        pass_gen.write(account_info)

    account_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
YELLOW = "#f7f5dd"

window = Tk()
window.title('Password Generator')
window.minsize(height=450, width=300)
window_photo = PhotoImage(file='./logo.png')
window.iconphoto(False, window_photo)
window.config(padx=40, pady=20, bg=YELLOW)

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
account_entry = Entry(width=41, bd=2, highlightthickness=0)
account_entry.focus()
account_entry.grid(column=1, row=1, columnspan=2)

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
generate_button = Button(text='Generate Password', width=15, bd=1, highlightthickness=0, cursor='hand2', bg='white')
generate_button.grid(column=2, row=3)

# Add button
add_button = Button(text='Add', width=39, bd=1, highlightthickness=0, cursor='hand2', bg='white',
                    command=add_on_click)
add_button.grid(pady=15, column=1, row=4, columnspan=2)

window.mainloop()
