# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh?")

window = Tk()

x = IntVar()

colors = ["red", "green", "orange"]  # assign a color to each food option

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],       #adds text to radio buttons
                              variable=x,             #groups radiobuttons together if they share the same variable
                              value=index,            #assigns each radiobutton a different value
                              padx=25,                #adds padding on x-axis
                              font=("Impact", 30),
                              fg=colors[index],       # text color
                              command=order           #set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)

window.mainloop()