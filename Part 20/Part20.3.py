from tkinter import *

window = Tk()
window.title("Pokéball")

canvas = Canvas(window, height=500, width=500, bg="lightgray")
canvas.pack()

# Outer circle (black border of Pokéball)
canvas.create_oval(50, 50, 450, 450, outline="black", width=12)

# Top half (red)
canvas.create_arc(50, 50, 450, 450, fill="red", outline="black", start=0, extent=180, width=5)

# Bottom half (white)
canvas.create_arc(50, 50, 450, 450, fill="white", outline="black", start=180, extent=180, width=5)

# Center black line (horizontal divider)
canvas.create_line(50, 250, 450, 250, fill="black", width=15)

# Outer button circle (black)
canvas.create_oval(190, 190, 310, 310, fill="black", outline="white", width=5)

# Inner button circle (white)
canvas.create_oval(210, 210, 290, 290, fill="white", outline="black", width=5)

window.mainloop()