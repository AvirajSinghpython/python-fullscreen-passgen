import random
import string
import tkinter as tk
from tkinter import messagebox

# 1. Main Window Setup
window = tk.Tk()
window.title("🔐 Super Safe Password Generator!")

# Make the app launch in full-screen mode
window.attributes("-fullscreen", True)
window.configure(bg="#E0F7FA")  # Cool light blue background

# Function to exit full-screen mode if they press the 'Escape' key
def exit_fullscreen(event=None):
    window.attributes("-fullscreen", False)
    window.geometry("600x500")

window.bind("<Escape>", exit_fullscreen)

# 2. Logic to Generate Passwords
def generate_password():
    letters = string.ascii_letters  
    digits = string.digits          
    symbols = "!@#$%^&*()_+"        
    all_characters = letters + digits + symbols
    
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Oops!", "Short passwords are easy to guess! Make it 4 or more. 🤔")
            return
    except ValueError:
        length = 12  
        
    password = "".join(random.choice(all_characters) for _ in range(length))
    
    password_display.config(state="normal")  
    password_display.delete(0, tk.END)       
    password_display.insert(0, password)     
    password_display.config(state="readonly") 

# 3. Logic to Copy to Clipboard
def copy_to_clipboard():
    password = password_display.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Success! 🎉", "Password copied to your Mac clipboard!")
    else:
        messagebox.showwarning("Empty!", "Generate a password first! ⚡")

# 4. Design the Screen Layout (Centered with padding)
main_frame = tk.Frame(window, bg="#E0F7FA")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(
    main_frame, 
    text="🦸‍♂️ Spy Password Maker 🦸‍♀️", 
    font=("Arial", 24, "bold"), 
    bg="#E0F7FA", 
    fg="#006064"
)
title_label.pack(pady=20)

hint_label = tk.Label(
    main_frame, 
    text="(Press 'Esc' key on your keyboard to leave full screen)", 
    font=("Arial", 10, "italic"), 
    bg="#E0F7FA",
    fg="#555555"
)
hint_label.pack(pady=5)

length_label = tk.Label(
    main_frame, 
    text="How long do you want it? (Try 12):", 
    font=("Arial", 14), 
    bg="#E0F7FA"
)
length_label.pack(pady=10)

length_entry = tk.Entry(main_frame, font=("Arial", 14), width=5, justify="center")
length_entry.insert(0, "12")  
length_entry.pack(pady=5)

generate_btn = tk.Button(
    main_frame, 
    text="⚡ Generate Secret Password ⚡", 
    font=("Arial", 14, "bold"), 
    highlightbackground="#E0F7FA",  
    fg="#00838F", 
    command=generate_password
)
generate_btn.pack(pady=20)

password_display = tk.Entry(
    main_frame, 
    font=("Courier", 18, "bold"), 
    width=22, 
    justify="center", 
    state="readonly"
)
password_display.pack(pady=10)

copy_btn = tk.Button(
    main_frame, 
    text="📋 Copy to Clipboard", 
    font=("Arial", 12, "bold"), 
    highlightbackground="#E0F7FA",  
    fg="#2E7D32", 
    command=copy_to_clipboard
)
copy_btn.pack(pady=15)

exit_btn = tk.Button(
    main_frame, 
    text="❌ Quit App", 
    font=("Arial", 11), 
    highlightbackground="#E0F7FA",  
    fg="#C62828", 
    command=window.destroy
)
exit_btn.pack(pady=10)

# 5. Turn On the App Loop
window.mainloop()
