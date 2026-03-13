from tkinter import *

from click import command

window = Tk()
window.title("My first GUI programme.")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label:
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# Buttons:
def button_clicked():
    my_label.config(text=input_.get())
    print("I got clicked.")

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()

# new_button
new_button = Button(text="I am new button")
new_button.grid(column=2, row=0)

# Entry:
input_ = Entry(width=10)
# input_.pack()
input_.get()
input_.grid(column=3, row=2)

window.mainloop()
