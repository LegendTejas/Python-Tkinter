# Grid Layouts - Improved Appearance
from tkinter import *

# Create window
window = Tk()
window.title("User Information Form")
window.geometry("400x300")
window.configure(bg="#f5f5f5")

# Title
titleLabel = Label(window, text="Enter Your Info",
                   font=("Arial", 22, "bold"),
                   bg="#f5f5f5", fg="#333")
titleLabel.grid(row=0, column=0, columnspan=2, pady=15)

# First Name
firstNameLabel = Label(window, text="First Name:", font=("Arial", 12),
                       bg="#f5f5f5", fg="#444")
firstNameLabel.grid(row=1, column=0, sticky=E, padx=10, pady=8)

firstNameEntry = Entry(window, width=25, font=("Arial", 12), bd=2, relief="groove")
firstNameEntry.grid(row=1, column=1, padx=10, pady=8)

# Last Name
lastNameLabel = Label(window, text="Last Name:", font=("Arial", 12),
                      bg="#f5f5f5", fg="#444")
lastNameLabel.grid(row=2, column=0, sticky=E, padx=10, pady=8)

lastNameEntry = Entry(window, width=25, font=("Arial", 12), bd=2, relief="groove")
lastNameEntry.grid(row=2, column=1, padx=10, pady=8)

# Email
emailLabel = Label(window, text="Email:", font=("Arial", 12),
                   bg="#f5f5f5", fg="#444")
emailLabel.grid(row=3, column=0, sticky=E, padx=10, pady=8)

emailEntry = Entry(window, width=25, font=("Arial", 12), bd=2, relief="groove")
emailEntry.grid(row=3, column=1, padx=10, pady=8)

# Submit Button
submitButton = Button(window, text="Submit",
                      font=("Arial", 12, "bold"),
                      bg="#4CAF50", fg="white",
                      activebackground="#45a049",
                      padx=10, pady=5)
submitButton.grid(row=4, column=0, columnspan=2, pady=20)

window.mainloop()