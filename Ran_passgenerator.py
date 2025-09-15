import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError
        characters = ''
        if letters_var.get():
            characters += string.ascii_letters
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation
        if not characters:
            messagebox.showwarning("Warning", "Select at least one character type.")
            return
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive number for length.")

def copy_to_clipboard():
    pwd = entry_password.get()
    if pwd:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x450")
root.resizable(False, False)
root.configure(bg="#2E3F4F")

tk.Label(root, text="Random Password Generator", bg="#2E3F4F", fg="white",
         font=("Helvetica", 16, "bold")).pack(pady=10)

frame_length = tk.Frame(root, bg="#2E3F4F")
frame_length.pack(pady=5)
tk.Label(frame_length, text="Password Length:", bg="#2E3F4F", fg="white",
         font=("Arial", 12)).pack(side="left")
entry_length = tk.Entry(frame_length, width=10, font=("Arial", 12))
entry_length.pack(side="left", padx=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

frame_check = tk.Frame(root, bg="#2E3F4F")
frame_check.pack(pady=10, fill="x", padx=20)

tk.Checkbutton(frame_check, text="Include Letters", variable=letters_var,
               font=("Arial", 12), bg="white").pack(anchor="w", pady=2)
tk.Checkbutton(frame_check, text="Include Numbers", variable=numbers_var,
               font=("Arial", 12), bg="white").pack(anchor="w", pady=2)
tk.Checkbutton(frame_check, text="Include Symbols", variable=symbols_var,
               font=("Arial", 12), bg="white").pack(anchor="w", pady=2)

tk.Button(root, text="Generate Password", command=generate_password,
          bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=15)

tk.Label(root, text="Generated Password:", bg="#2E3F4F", fg="white",
         font=("Arial", 12)).pack()
entry_password = tk.Entry(root, width=40, font=("Arial", 12))
entry_password.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,
          bg="#2196F3", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

root.mainloop()

