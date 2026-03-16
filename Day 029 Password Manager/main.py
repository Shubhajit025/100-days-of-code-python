from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():


    if (len(web_entry.get()) == 0
            or len(password_entry.get()) == 0
            or len(username_entry.get()) == 0):
        messagebox.showinfo(title="Oops",
                            message="Please don't leave any field empty!")

    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(),
                               message=f"These are the details entered: "
                                       f"\n{username_entry.get()} "
                                       f"\n{password_entry.get()} "
                                       f"\nIs it ok to save?")
        if is_ok:

            with open("data.txt", mode="a") as file:
                file.write(f"{web_entry.get()} | "
                           f"{username_entry.get()} | "
                           f"{password_entry.get()}\n")

            web_entry.delete(0, END)
            web_entry.focus()
            username_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# The main window:
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Img handling with Canvas:
canvas = Canvas(width=200, height=200)

my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

# Website label:
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Communication Address label:
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# Password label:
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry bar:
# 1. web entry:
web_entry = Entry(width=51)
web_entry.focus() # -> Focus to start blink the cursor to start typing.
web_entry.grid(column=1, row=1, columnspan=2)

# 2. username entry:
username_entry = Entry(width=51)
username_entry.insert(0, "indie@gmail.com") # -> To start with an email or user_id.
username_entry.grid(column=1, row=2, columnspan=2)

# 3. password entry:
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Password Generator Button:
gen_pass = Button(text="Generate Password", command=password_generator)
gen_pass.grid(column=2, row=3)

# Add button:
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
