# Move a widget inside the window using WASD and Arrow keys
from tkinter import *

# Movement functions (adjusts position by 10 pixels per key press)
def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)

def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())

# Create main window
window = Tk()
window.title("Tejas Racing Car")
window.geometry("500x500")

# Bind keys for movement (WASD + Arrow keys)
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# Load and scale down image, then place it at starting position
myimage = PhotoImage(file='Part 24/raceCar.png').subsample(8, 8)
label = Label(window, image=myimage)
label.place(x=0, y=0)

window.mainloop()