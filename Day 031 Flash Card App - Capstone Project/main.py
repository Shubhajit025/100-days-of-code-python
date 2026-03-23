from tkinter import  *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
cards = {}
data_dict ={}

# --------------- FUNCTIONALITY SETUP --------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def card_swap():
    global cards, flip_timer
    window.after_cancel(flip_timer)
    cards = random.choice(data_dict)
    quis = cards["French"]
    canvas.itemconfig(title_flscrd, text="French 👇", fill="black")
    canvas.itemconfig(qsn_flscrd, text=quis, fill="black")
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer = window.after(5000, func=flip)


def flip():

    ans = cards["English"]
    canvas.itemconfig(title_flscrd, text="English 👇", fill="white")
    canvas.itemconfig(qsn_flscrd, text=ans, fill="white")
    canvas.itemconfig(card_background, image= card_back_img)

def is_known():
    data_dict.remove(cards)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    card_swap()


# --------------- UI SETUP --------------- #
window = Tk()
window.title("Flash Card App - Python")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="assets/card_front.png")
card_back_img = PhotoImage(file="assets/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_flscrd = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
qsn_flscrd = canvas.create_text(400, 280, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_img = PhotoImage(file="assets/right.png")
wrong_img = PhotoImage(file="assets/wrong.png")


right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=card_swap)
wrong_button.grid(column=0, row=1)

card_swap()

window.mainloop()
