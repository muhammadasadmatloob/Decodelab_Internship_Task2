import secrets
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        # Step 1: Input & Validation [cite: 89, 90]
        # User se length lena
        length = int(entry_length.get())
        
        if length < 8:
            messagebox.showwarning("Security Alert", "NIST guidelines ke mutabiq kam az kam 8 characters zaroori hain! [cite: 94]")
            return

        # Step 2: Process (Building the Engine) [cite: 96, 102]
        # Character sets define karna
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # secrets.choice() aur .join() ka istemal [cite: 121, 146]
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        # Step 3: Output [cite: 79]
        # Password ko screen par dikhana
        label_result.config(text=password, fg="#2ecc71")
        
    except ValueError:
        messagebox.showerror("Error", "Bhai, sirf numbers (integers) enter karein! [cite: 87, 90]")

# --- UI Setup ---
root = tk.Tk()
root.title("DecodeLabs Password Generator")
root.geometry("400x300")
root.configure(bg="#2c3e50")

# Title
label_title = tk.Label(root, text="Enterprise Password Generator", font=("Arial", 14, "bold"), bg="#2c3e50", fg="white")
label_title.pack(pady=20)

# Input Field
label_prompt = tk.Label(root, text="Password Length Dalein:", bg="#2c3e50", fg="white")
label_prompt.pack()
entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack(pady=10)

# Generate Button
btn_generate = tk.Button(root, text="Generate Secure Password", command=generate_password, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
btn_generate.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Courier", 12, "bold"), bg="#2c3e50", fg="#f1c40f", wraplength=350)
label_result.pack(pady=20)

root.mainloop()