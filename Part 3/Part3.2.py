from tkinter import *

count = 0

def click():
    global count
    count+=1
    label.config(text=count)

window = Tk()
button = Button(window,text='Click me!!!')
button.config(command=click) #performs call back of function
button.config(font=('Ink Free',50,'bold'))
button.config(bg='#ff6200')
button.config(fg='#fffb1f')
button.config(activebackground='#FF0000')
button.config(activeforeground='#fffb1f')
img = PhotoImage(file='clickEmoji.png')
button.config(image=img)
button.config(compound='bottom')
label = Label(window,text=count)
label.config(font=('Monospace',50))
label.pack()
button.pack()

window.mainloop()