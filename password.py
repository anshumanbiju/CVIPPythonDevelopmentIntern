import tkinter as tk
import random
import string


def generate_password():
    length_str = length_entry.get()

    if not length_str.isdigit():
        password_label.config(text="Please enter a valid number")
        return
    
    length = int(length_str)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)


root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack(pady=10)


root.mainloop()
