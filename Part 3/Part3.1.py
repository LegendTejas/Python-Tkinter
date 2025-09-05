# button = you click it, then it does stuff

from tkinter import *

def click():
    print("Hello There!")  # function called when button is clicked

window = Tk()  # create main window

# create a button with initial text
button = Button(window, text='Click me!!')

button.config(command=click)             # link button to function (callback)
button.config(font=('Ink Free', 50, 'bold'))  # set font style and size
button.config(bg='#ff6200')              # background color
button.config(fg='#fffb1f')              # text color
button.config(activebackground='#FF0000')  # background color when clicked
button.config(activeforeground='#fffb1f')  # text color when clicked

image = PhotoImage(file='Part 3\clickEmoji.png')  # load button image
button.config(compound='bottom')           # place text below image

# button.config(state=DISABLED)  # disable button (un-clickable)

button.pack()  # add button to window

window.mainloop()