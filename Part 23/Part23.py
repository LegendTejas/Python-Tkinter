# drag & drop 
from tkinter import *

# Save the starting mouse position when left button is clicked
def drag_start(event):
    widget = event.widget          # the widget being clicked (label in this case)
    widget.startX = event.x        # x-coordinate inside the widget
    widget.startY = event.y        # y-coordinate inside the widget

# Update widget position while dragging
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x   # new x position
    y = widget.winfo_y() - widget.startY + event.y   # new y position
    widget.place(x=x, y=y)                           # move widget

# Create main window
window = Tk()

# First draggable label (red)
label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)

# Second draggable label (blue)
label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100, y=100)

# Bind drag events to both labels
label.bind("<Button-1>", drag_start)      # left click to start drag
label.bind("<B1-Motion>", drag_motion)    # move while holding left button

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()