# animations
from tkinter import *
import time

# Window/canvas size
WIDTH = 600
HEIGHT = 300

# UFO velocity
xVelocity = 1
yVelocity = 1

# Create main window
window = Tk()
window.title("UFO in Space")

# Create canvas
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# Load and scale background to fit canvas
background_photo = PhotoImage(file='Part 25/space.png')
background_photo = background_photo.subsample(
    max(1, background_photo.width() // WIDTH),
    max(1, background_photo.height() // HEIGHT)
)
canvas.create_image(0, 0, image=background_photo, anchor=NW)

# Load UFO image and resize it to be clearly visible
photo_image = PhotoImage(file='Part 25/ufo.png')
scale_factor = max(1, photo_image.width() // 80)  # UFO width ≈ 80px
photo_image = photo_image.subsample(scale_factor, scale_factor)

# Place UFO at starting position
my_image = canvas.create_image(50, 50, image=photo_image, anchor=NW)

# Get UFO dimensions
image_width = photo_image.width()
image_height = photo_image.height()

# Animation loop
while True:
    coordinates = canvas.coords(my_image)

    # Bounce horizontally
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] <= 0:
        xVelocity = -xVelocity

    # Bounce vertically
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] <= 0:
        yVelocity = -yVelocity

    # Move UFO
    canvas.move(my_image, xVelocity, yVelocity)

    # Update screen
    window.update()
    time.sleep(0.01)

window.mainloop()