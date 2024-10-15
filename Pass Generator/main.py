import tkinter as tk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    length = int(length_entry.get())
    new_password = generate_password(length)
    password_var.set(new_password)


root = tk.Tk()
root.title("Password Generator")


password_var = tk.StringVar()

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Default length

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, textvariable=password_var, state='readonly', width=40)
password_entry.pack(pady=5)

root.mainloop()
