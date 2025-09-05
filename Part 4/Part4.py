# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()  # get text from entry
    print("Hello", username)

def delete():
    entry.delete(0, END)  # delete all text in entry

def backspace():
    entry.delete(len(entry.get()) - 1, END)  # delete last character

window = Tk()

submit = Button(window, text="Submit", command=submit)
submit.pack(side=BOTTOM)

delete = Button(window, text="Delete", command=delete)
delete.pack(side=RIGHT)

backspace = Button(window, text="Backspace", command=backspace)
backspace.pack(side=RIGHT)

entry = Entry()
entry.config(font=('Ink Free', 50))   # font styling
entry.config(bg='black', fg='#00FF00')  # background and text color
# entry.insert(0, 'Hello Bro')  # pre-fill text
# entry.config(state=DISABLED)  # disable button (un-clickable)
entry.config(width=10)  # width of textbox
# entry.config(show='$')  # mask input (like password field)
entry.pack()

window.mainloop()