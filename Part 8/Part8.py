from tkinter import *

def submit():
    # get selected items from listbox
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    # add new item from entry box
    item = entryBox.get().strip()
    if item == "":
        error_label.config(text="Please enter the item you want to add in list")
    else:
        listbox.insert(listbox.size(), item)  # insert at end
        listbox.config(height=listbox.size())  # adjust height
        entryBox.delete(0, END)  # clear entry box
        error_label.config(text="")  # clear error message

def delete():
    # delete selected items (reverse order to avoid shifting issues)
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

# main window
window = Tk()

# listbox widget
listbox = Listbox(
    window,
    bg="#f7ffde",
    font=("Constantia", 35),
    width=12,
    selectmode=MULTIPLE  # allow multiple selections
)
listbox.pack()

# default items
listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())  # set height based on items

# entry box for adding items
entryBox = Entry(window)
entryBox.pack()

# error label
error_label = Label(window, text="", fg="red", font=("Arial", 12))
error_label.pack()

# frame to group buttons
frame = Frame(window)
frame.pack()

# buttons
submitButton = Button(frame, text="submit", command=submit)
submitButton.pack(side=LEFT)

addButton = Button(frame, text="add", command=add)
addButton.pack(side=LEFT)

deleteButton = Button(frame, text="delete", command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()