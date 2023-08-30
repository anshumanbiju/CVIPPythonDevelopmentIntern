import tkinter as tk

def add_to_expression(value):
    current_expression.set(current_expression.get() + str(value))
    update_label()

def append_operator(operator):
    current_expression.set(current_expression.get() + operator)
    total_expression.set(total_expression.get() + current_expression.get())
    current_expression.set("")
    update_total_label()
    update_label()

def clear():
    current_expression.set("")
    total_expression.set("")
    update_label()
    update_total_label()

def square():
    current_expression.set(str(eval(f"{current_expression.get()}**2")))
    update_label()

def sqrt():
    current_expression.set(str(eval(f"{current_expression.get()}**0.5")))
    update_label()

def evaluate():
    total_expression.set(total_expression.get() + current_expression.get())
    update_total_label()
    try:
        current_expression.set(str(eval(total_expression.get())))
        total_expression.set("")
    except Exception as e:
        current_expression.set("Error")
    finally:
        update_label()

def update_label():
    label.config(text=current_expression.get()[:11])

def update_total_label():
    expression = total_expression.get()
    for operator, symbol in operations.items():
        expression = expression.replace(operator, f' {symbol} ')
    total_label.config(text=expression)

app = tk.Tk()
app.geometry("375x667")
app.title("Calculator")

current_expression = tk.StringVar()
total_expression = tk.StringVar()
current_expression.set("")
total_expression.set("")

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

display_frame = tk.Frame(app, height=221, bg=LIGHT_GRAY)
display_frame.pack(expand=True, fill="both")

total_label = tk.Label(display_frame, textvariable=total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                       fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
total_label.pack(expand=True, fill='both')

label = tk.Label(display_frame, textvariable=current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                 fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
label.pack(expand=True, fill='both')

digits = {
    7: (1, 1), 8: (1, 2), 9: (1, 3),
    4: (2, 1), 5: (2, 2), 6: (2, 3),
    1: (3, 1), 2: (3, 2), 3: (3, 3),
    0: (4, 2), '.': (4, 1)
}

operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

buttons_frame = tk.Frame(app)
buttons_frame.pack(expand=True, fill="both")

buttons_frame.rowconfigure(0, weight=1)
for x in range(1, 5):
    buttons_frame.rowconfigure(x, weight=1)
    buttons_frame.columnconfigure(x, weight=1)

for digit, grid_value in digits.items():
    button = tk.Button(buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                       borderwidth=0, command=lambda x=digit: add_to_expression(x))
    button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

i = 0
for operator, symbol in operations.items():
    button = tk.Button(buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                       borderwidth=0, command=lambda x=operator: append_operator(x))
    button.grid(row=i, column=4, sticky=tk.NSEW)
    i += 1

clear_button = tk.Button(buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                         borderwidth=0, command=clear)
clear_button.grid(row=0, column=1, sticky=tk.NSEW)

square_button = tk.Button(buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                          borderwidth=0, command=square)
square_button.grid(row=0, column=2, sticky=tk.NSEW)

sqrt_button = tk.Button(buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                        borderwidth=0, command=sqrt)
sqrt_button.grid(row=0, column=3, sticky=tk.NSEW)

equals_button = tk.Button(buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                          borderwidth=0, command=evaluate)
equals_button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

app.mainloop()
