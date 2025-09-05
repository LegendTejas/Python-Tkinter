# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

# create a frame (container) with background, border width, and sunken effect
frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.pack()

# buttons placed inside the frame
Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)   # top button
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)  # left button
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)  # middle button
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)  # right button

window.mainloop()