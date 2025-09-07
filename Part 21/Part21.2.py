# This program detects key presses in Tkinter and shows
# any single key or key combination (e.g., Ctrl + i, Shift + a) on the screen.

from tkinter import *

# Set to keep track of pressed keys
pressed_keys = set()

def key_press(event):
    pressed_keys.add(event.keysym)  # add key to set
    
    # If at least 2 keys are pressed, show combo
    if len(pressed_keys) >= 2:
        combo = " + ".join(sorted(pressed_keys))  # join pressed keys
        label.config(text=combo)
    else:
        label.config(text=event.keysym)  # single key display

def key_release(event):
    # remove released key
    pressed_keys.discard(event.keysym)

window = Tk()
window.title("Key Combination Detector")

# Bind key press and release
window.bind("<KeyPress>", key_press)
window.bind("<KeyRelease>", key_release)

label = Label(window, font=("Helvetica", 40))
label.pack(pady=50)

window.mainloop()