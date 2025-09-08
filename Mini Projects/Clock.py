# Digital Clock

from tkinter import *
from time import strftime

# Function to update time, day, and date
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)  # update every 1 second


# Main Window
window = Tk()
window.title("Digital Clock")
window.geometry("600x400")
window.config(bg="black")

# Title
title_label = Label(window, text="⏰ Digital Clock", font=("Arial", 24, "bold"),
                    fg="#FFD700", bg="black")
title_label.pack(pady=10)

# Time Label
time_label = Label(window, font=("Arial", 60, "bold"), fg="#00FF00", bg="black")
time_label.pack(pady=20)

# Day Label
day_label = Label(window, font=("Ink Free", 28, "bold"), fg="cyan", bg="black")
day_label.pack()

# Date Label
date_label = Label(window, font=("Ink Free", 26), fg="orange", bg="black")
date_label.pack(pady=10)

update()
window.mainloop()
