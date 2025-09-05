from tkinter import *

# Label = widget used to display text and/or images

window = Tk()  # create main window

photo = PhotoImage(file='jiol.png')  # load image file

# create a label with text + image
label = Label(window,
              text="Welcomes You!",   # text to display
              font=('Arial', 40, 'bold'),  # font style
              fg='#00FF00',   # text color
              bg='black',     # background color
              relief=RAISED,  # border style
              bd=10,          # border width
              padx=20,        # padding x
              pady=20,        # padding y
              image=photo,    # attach image
              compound='top') # place text above image

label.pack()  # automatically position label in window

# label.place(x=0, y=0) # manual positioning at (x, y) here 

window.mainloop()  # run the window loop