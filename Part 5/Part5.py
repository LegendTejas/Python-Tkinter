# checkbox = you can select multiple options
from tkinter import *

def display():
    # check combinations of checkbox values
    if (x.get() == 1) & (y.get() == 0):
        print("I like Python")
    elif (x.get() == 0) & (y.get() == 1):
        print("I like Java")
    elif (x.get() == 1) & (y.get() == 1):
        print("I like both Python & Java")
    else:
        print("I don't like either")

window = Tk()
window.configure(bg="#000000")

x = IntVar()  # variable to track Python checkbox state
y = IntVar()  # variable to track Java checkbox state

# load and resize images for checkboxes
python_logo = PhotoImage(file="Part 5\python_logo.png").subsample(8, 8)  # reduce size by 8 (use 9,9 for smaller)
java_logo = PhotoImage(file="Part 5\Java_logo.png").subsample(8, 8)      # reduce size by 8 (use 9,9 for smaller)

# Python checkbox
checkbox = Checkbutton(
    window, text="Python", variable=x, onvalue=1, offvalue=0, command=display,
    font=("Arial", 18), fg="#00FF00", bg="#000000",
    activeforeground="#0000FF", activebackground="#000000",
    image=python_logo, compound="left", padx=10, pady=5, anchor="w"
)
checkbox.pack(fill="x", padx=20, pady=10)

# Java checkbox
checkbox2 = Checkbutton(
    window, text="Java", variable=y, onvalue=1, offvalue=0, command=display,
    font=("Arial", 18), fg="#0B9CF5", bg="#000000",
    activeforeground="#0000FF", activebackground="#000000",
    image=java_logo, compound="left", padx=10, pady=5, anchor="w"
)
checkbox2.pack(fill="x", padx=20, pady=10)

window.mainloop()