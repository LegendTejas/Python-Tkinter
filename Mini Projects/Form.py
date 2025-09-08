# Grid Layouts

from tkinter import *
from tkinter import ttk

# Create main window
window = Tk()
window.title("User Information Form")
window.geometry("400x400")
window.configure(bg="#f5f5f5")

# Title
titleLabel = Label(window, text="Enter Your Information",
                   font=("Arial", 20, "bold"),
                   bg="#f5f5f5", fg="#333")
titleLabel.grid(row=0, column=0, columnspan=2, pady=15)

# Labels & Entries
Label(window, text="First Name:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, sticky=E, padx=10, pady=5)
firstNameEntry = Entry(window, width=25, font=("Arial", 12))
firstNameEntry.grid(row=1, column=1, padx=10, pady=5)

Label(window, text="Last Name:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, sticky=E, padx=10, pady=5)
lastNameEntry = Entry(window, width=25, font=("Arial", 12))
lastNameEntry.grid(row=2, column=1, padx=10, pady=5)

Label(window, text="Email:", font=("Arial", 12), bg="#f5f5f5").grid(row=3, column=0, sticky=E, padx=10, pady=5)
emailEntry = Entry(window, width=25, font=("Arial", 12))
emailEntry.grid(row=3, column=1, padx=10, pady=5)

Label(window, text="Phone:", font=("Arial", 12), bg="#f5f5f5").grid(row=4, column=0, sticky=E, padx=10, pady=5)
phoneEntry = Entry(window, width=25, font=("Arial", 12))
phoneEntry.grid(row=4, column=1, padx=10, pady=5)

Label(window, text="Address:", font=("Arial", 12), bg="#f5f5f5").grid(row=5, column=0, sticky=E, padx=10, pady=5)
addressEntry = Entry(window, width=25, font=("Arial", 12))
addressEntry.grid(row=5, column=1, padx=10, pady=5)

# Gender (Radio Buttons)
Label(window, text="Gender:", font=("Arial", 12), bg="#f5f5f5").grid(row=6, column=0, sticky=E, padx=10, pady=5)
genderVar = StringVar(value="None")
Radiobutton(window, text="Male", variable=genderVar, value="Male", bg="#f5f5f5").grid(row=6, column=1, sticky=W)
Radiobutton(window, text="Female", variable=genderVar, value="Female", bg="#f5f5f5").grid(row=6, column=1, sticky=E)

# Country (Dropdown)
Label(window, text="Country:", font=("Arial", 12), bg="#f5f5f5").grid(row=7, column=0, sticky=E, padx=10, pady=5)
countryCombo = ttk.Combobox(window, values=["India", "USA", "Germany", "Canada", "UK"], width=22, font=("Arial", 12))
countryCombo.grid(row=7, column=1, padx=10, pady=5)

# Submit Button
submitButton = Button(window, text="Submit", font=("Arial", 12, "bold"),
                      bg="#4CAF50", fg="white", padx=10, pady=5)
submitButton.grid(row=8, column=0, columnspan=2, pady=20)

window.mainloop()
