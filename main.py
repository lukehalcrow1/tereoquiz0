import tkinter as tk

from tkinter import messagebox

def button1clicked():
    messagebox.showinfo("Button 1", "Ydrt")
def button2clicked():
    messagebox.showinfo("Button 2", "test")

root = tk.Tk()
root.title("Testers")
root.geometry("300x150")

button1 = tk.Button(root, text="Button 1", command=button1clicked)
button1.pack(pady=10)

button2 = tk.Button(root, text="Button 2", command=button2clicked)
button2.pack(pady=10)

root.mainloop()