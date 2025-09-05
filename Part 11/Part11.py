# text widget = multi-line text area (can enter multiple lines)

from tkinter import *

def submit():
    # get all text from start (line 1, char 0) to end
    input = text.get("1.0", END)
    print(input)

window = Tk()

# text area widget
text = Text(
    window,
    bg="light yellow",
    font=("Ink Free", 25),
    height=8,    # number of text rows
    width=20,    # number of text columns
    padx=20,     # inner padding (x-axis)
    pady=20,     # inner padding (y-axis)
    fg="purple"  # text color
)
text.pack()

# submit button
button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()