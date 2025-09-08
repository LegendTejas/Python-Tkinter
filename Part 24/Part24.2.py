# Move an image on a Canvas using WASD keys + Arrow keys
from tkinter import *

# Movement functions (shift the image by 10 pixels per key press)
def move_up(event):
    canvas.move(myimage, 0, -10)

def move_down(event):
    canvas.move(myimage, 0, 10)

def move_left(event):
    canvas.move(myimage, -10, 0)

def move_right(event):
    canvas.move(myimage, 10, 0)

# Main window
window = Tk()

# Bind keys for movement (WASD + Arrow keys)
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# Create canvas with light grey background
canvas = Canvas(window, width=500, height=500, bg="lightgrey")
canvas.pack()

# Load and scale image, then place it at top-left corner
photoimage = PhotoImage(file='Part 24/raceCar.png').subsample(13, 13)
myimage = canvas.create_image(0, 0, image=photoimage, anchor=NW)

window.mainloop()