from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("Tejas first GUI Program")

icon = PhotoImage(file="jiol.png")

window.iconphoto(True, icon)
window.config(background="aqua")

window.mainloop() # place window on computer screen, listen for events