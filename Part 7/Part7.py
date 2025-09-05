from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ "")

window = Tk()

hotImage = PhotoImage(file='Part 7\hot.png').subsample(20,20)
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,to=0,
              length=600,
              orient=VERTICAL, #orientation of scale
              font = ('Consolas',15),
              tickinterval = 10, #adds numeric indicators for value
              #showvalue = 0, #hide current value
              resolution = 5, #increment of slider
              troughcolor = '#69EAFF',
              fg = '#FF1C00',
              bg = '#111111'
              )

scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set current value of slider

scale.pack()

coldImage = PhotoImage(file='Part 7\cold.png').subsample(5,5)
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()