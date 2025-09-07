# how to add window tabs
from tkinter import *
from tkinter import ttk  # ttk = themed tkinter (modern looking widgets)

window = Tk()

# Notebook widget = manages multiple tabs (like a tabbed interface)
notebook = ttk.Notebook(window)

# Create two frames, each will be a separate tab
tab1 = Frame(notebook)  
tab2 = Frame(notebook)  

# Add frames as tabs in the notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# expand=True → take up all unused space
# fill="both" → fill space in both X and Y directions
notebook.pack(expand=True, fill="both")

# Add content inside each tab
Label(tab1, text="Hello, this is tab #1", width=50, height=25).pack()
Label(tab2, text="Goodbye, this is tab #2", width=50, height=25).pack()

window.mainloop()