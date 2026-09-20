import tkinter as tk

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()  # Create the main window
root.title("Modern Calculator made with Python 🐍") # Set the window title
root.geometry("420x650") # Set the window size to 420x650 pixels
root.resizable(True, True)  # Allow the window to be resizable
root.configure(bg="#1D3052") 

expression = "" # Initialize the expression variable to store the current input
display_var = tk.StringVar() # Create a StringVar to hold the display value of the calculator


# -----------------------------
# Functions
# -----------------------------
def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)


def clear():
    global expression
    expression = ""
    display_var.set("")


def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)


def calculate():
    global expression

    try:
        result = eval(expression)
        expression = str(result)
        display_var.set(expression)

    except:
        expression = ""
        display_var.set("Error")


# -----------------------------
# Keyboard Input
# -----------------------------
def keyboard_input(event):

    key = event.keysym

    # Numbers
    if event.char in "0123456789":
        press(event.char)

    # Operators
    elif event.char in "+-*/.":
        press(event.char)

    # Enter key
    elif key in ("Return", "KP_Enter"):
        calculate()

    # Backspace
    elif key == "BackSpace":
        backspace()

    # Escape
    elif key == "Escape":
        clear()


# -----------------------------
# Display
# -----------------------------
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 32),
    bg="#1c2940",
    fg="white",
    justify="right",
    bd=0,
    insertbackground="white"
)

display.pack(
    padx=25,
    pady=(30, 20),
    ipady=25,
    fill="x"
)


# -----------------------------
# Button Frame
# -----------------------------
button_frame = tk.Frame(
    root,
    bg="#101827"
)

button_frame.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)


# -----------------------------
# Button Styles
# -----------------------------
number_button = {
    "font": ("Arial", 20, "bold"),
    "bg": "#34445f",
    "fg": "white",
    "activebackground": "#465a7a",
    "activeforeground": "white",
    "bd": 0
}

operator_button = {
    "font": ("Arial", 20, "bold"),
    "bg": "#ff9418",
    "fg": "white",
    "activebackground": "#ffad45",
    "activeforeground": "white",
    "bd": 0
}


# -----------------------------
# Buttons
# -----------------------------
buttons = [
    ("C", 0, 0, clear),
    ("⌫", 0, 1, backspace),
    ("%", 0, 2, lambda: press("%")),
    ("÷", 0, 3, lambda: press("/")),

    ("7", 1, 0, lambda: press("7")),
    ("8", 1, 1, lambda: press("8")),
    ("9", 1, 2, lambda: press("9")),
    ("×", 1, 3, lambda: press("*")),

    ("4", 2, 0, lambda: press("4")),
    ("5", 2, 1, lambda: press("5")),
    ("6", 2, 2, lambda: press("6")),
    ("−", 2, 3, lambda: press("-")),

    ("1", 3, 0, lambda: press("1")),
    ("2", 3, 1, lambda: press("2")),
    ("3", 3, 2, lambda: press("3")),
    ("+", 3, 3, lambda: press("+")),

    ("0", 4, 0, lambda: press("0")),
    (".", 4, 2, lambda: press(".")),
    ("=", 4, 3, calculate)
]


# -----------------------------
# Create Buttons
# -----------------------------
for text, row, column, command in buttons:

    if text in ["÷", "×", "−", "+"]:
        style = operator_button

    elif text == "=":
        style = {
            "font": ("Arial", 20, "bold"),
            "bg": "#20c77a",
            "fg": "white",
            "activebackground": "#35df91",
            "bd": 0
        }

    else:
        style = number_button

    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        **style
    )

    button.grid(
        row=row,
        column=column,
        padx=6,
        pady=6,
        sticky="nsew"
    )


# Make buttons responsive
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)


# -----------------------------
# Footer
# -----------------------------
footer = tk.Label(
    root,
    text="Built with Python 🐍",
    font=("Arial", 11),
    bg="#101827",
    fg="#8da2c0"
)

footer.pack(pady=15)


# -----------------------------
# Enable Keyboard
# -----------------------------
root.bind("<Key>", keyboard_input)

# Put cursor/focus on calculator
root.focus_set()


# -----------------------------
# Run
# -----------------------------
root.mainloop()