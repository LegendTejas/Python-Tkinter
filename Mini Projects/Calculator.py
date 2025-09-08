# Python Calculator
from tkinter import *

# ----- Logic -----
def button_press(ch):
    global expr
    expr += str(ch)
    _set_display(expr)

def equals():
    global expr
    try:
        result = str(eval(expr))
        expr = result
        _set_display(result)
    except Exception:
        expr = ""
        _set_display("Error")

def clear_all():
    global expr
    expr = ""
    _set_display("")

def backspace():
    global expr
    expr = expr[:-1]
    _set_display(expr)

def _set_display(text):
    # update readonly entry
    display_entry.config(state="normal")
    display_var.set(text)
    display_entry.config(state="readonly")

# ----- Window + Layout -----
root = Tk()
root.title("Calculator")
root.geometry("360x480")   # good default
root.minsize(300, 380)    # allow resize but keep usable minimum
root.config(bg="#1e1e1e")

# make root grid expandable
root.grid_rowconfigure(1, weight=1)   # button_frame row expands
root.grid_columnconfigure(0, weight=1)

expr = ""
display_var = StringVar()

# Outer padding frame (gives space at boundary)
outer = Frame(root, bg="#1e1e1e", padx=14, pady=14)
outer.grid(sticky="nsew")
outer.grid_rowconfigure(1, weight=1)
outer.grid_columnconfigure(0, weight=1)

# Top: display + small backspace/clear row
top_row = Frame(outer, bg="#1e1e1e")
top_row.grid(row=0, column=0, sticky="ew", pady=(0, 10))
top_row.grid_columnconfigure(0, weight=1)

display_entry = Entry(top_row, textvariable=display_var, font=("Consolas", 20),
                      justify="right", relief="sunken", bd=3, state="readonly",
                      readonlybackground="white", fg="black")
display_entry.grid(row=0, column=0, sticky="ew")

# small controls to the right of display (backspace)
ctrls = Frame(top_row, bg="#1e1e1e")
ctrls.grid(row=0, column=1, padx=(8,0))
Button(ctrls, text="⌫", command=backspace, width=3, height=1,
       font=("Arial", 12, "bold"), bg="#3a3a3a", fg="white",
       activebackground="#555").grid(padx=2, pady=0)

# ----- Buttons Frame (grid that expands) -----
btn_frame = Frame(outer, bg="#1e1e1e")
btn_frame.grid(row=1, column=0, sticky="nsew")
# configure 4 columns and 4 rows to expand equally
for c in range(4):
    btn_frame.grid_columnconfigure(c, weight=1, uniform="col")
for r in range(4):
    btn_frame.grid_rowconfigure(r, weight=1, uniform="row")

# button style (do not include bg here to avoid duplicate kwargs)
base_style = {"font": ("Arial", 14, "bold"), "bd": 2, "relief": "raised", "fg": "white"}

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
]

for (text, r, c) in buttons:
    if text == "=":
        btn = Button(btn_frame, text=text, command=equals, bg="#2ea44f",
                     activebackground="#23823b", **base_style)
    elif text in {"+", "-", "*", "/"}:
        btn = Button(btn_frame, text=text, command=lambda t=text: button_press(t),
                     bg="#ff8c42", activebackground="#d77a2d", **base_style)
    else:
        btn = Button(btn_frame, text=text, command=lambda t=text: button_press(t),
                     bg="#2e2e2e", activebackground="#444444", **base_style)

    btn.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)

# ----- Clear button (spans full width at bottom) -----
# give it its own row that expands minimally
outer.grid_rowconfigure(2, weight=0)
clear_btn = Button(outer, text="CLEAR", command=clear_all,
                   font=("Arial", 13, "bold"), bg="#d9534f", fg="white",
                   activebackground="#b52b27", pady=8)
clear_btn.grid(row=2, column=0, sticky="ew", pady=(12,0))

# allow top-level expansion behavior for nicer resizing
root.update_idletasks()
root.mainloop()