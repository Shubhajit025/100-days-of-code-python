from tkinter import *


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def calculation():
    miles = float(value_to_convert.get())
    km = miles * 1.60934
    result.config(text=round(km, 2))


# miles label:
miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.config(padx=20, pady=20)
miles_label.grid(column=2, row=0)

# Comparison label:
compare_label = Label(text="is equal to", font=("Arial", 16, "bold"))
compare_label.config(padx=20, pady=20)
compare_label.grid(column=0, row=1)

# Km label:
km_label = Label(text="KM", font=("Arial", 16, "bold"))
km_label.config(padx=20, pady=20)
km_label.grid(column=2, row=1)

# result label:
result = Label(text=0, font=("Arial", 16, "bold"))
result.config(padx=20, pady=20)
result.grid(column=1, row=1)

# Calculate click button:
button = Button(text="Calculate", width=10, command=calculation)
button.config(padx=20, pady=20)
button.grid(column=1, row=2)

# Enter value:
value_to_convert = Entry(width=20)
value_to_convert.get()
value_to_convert.grid(column=1, row=0)



window.mainloop()
