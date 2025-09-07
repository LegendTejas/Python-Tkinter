# canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()
window.title("Beautiful Canvas Art")

# Create a canvas area where we can draw shapes
canvas = Canvas(window, height=600, width=600, bg="lightblue")
canvas.pack()  # place the canvas on the window

# Draw two diagonal lines forming a cross (X shape)
canvas.create_line(0, 0, 600, 600, fill="blue", width=6)   # from top-left to bottom-right
canvas.create_line(0, 600, 600, 0, fill="red", width=6)    # from bottom-left to top-right

# Draw a rectangle
canvas.create_rectangle(50, 50, 200, 200, fill="purple", outline="white", width=6)
# (x1, y1, x2, y2) → (50,50) is top-left corner, (200,200) is bottom-right corner

# Draw an oval inside the rectangle
canvas.create_oval(50, 50, 200, 200, fill="pink", outline="black", width=5)
# The oval will fit exactly inside the rectangle's boundary

# Draw a circle in the middle
canvas.create_oval(250, 250, 350, 350, fill="orange", outline="black", width=6)
# Since width and height are equal, this oval becomes a perfect circle

# Draw a triangle (polygon with 3 points)
canvas.create_polygon(300, 130, 400, 300, 200, 300,
                      fill="yellow", outline="black", width=6)
# Each pair (x, y) is a vertex: top (300,130), bottom-right (400,300), bottom-left (200,300)

# Draw a hexagon (6-sided polygon)
canvas.create_polygon(450, 100, 520, 150, 520, 230,
                      450, 280, 380, 230, 380, 150,
                      fill="lightgreen", outline="black", width=6)
# Coordinates are given in clockwise order to form a closed hexagon

# Draw a semi-circle (arc)
canvas.create_arc(150, 20, 450, 250, style=PIESLICE, start=0, extent=180,
                  fill="cyan", outline="blue", width=6)
# (x1,y1,x2,y2) defines the bounding box for the arc
# start=0 means it starts from the right side, extent=180 means half-circle


# Keep the window open until user closes it
window.mainloop()