import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import os

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        initialdir=os, 
        title="SelectImage File",
        filetypes=[("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg"), ("PNG Files", "*.png"), ("All Files", "*.*")]
    )

    if not filepath:
        return
        
    img=Image.open(filepath)
    img.thumbnail((350,350))
    img=ImageTk.PhotoImage(img)

    lbl.configure(image=img)
    lbl.image=img

def convolution():
    filepath = askopenfilename(
        initialdir=os, 
        title="Select kernel",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )


    file= open(filepath,'r')
    txt= file.read()
    print(txt)
    file.close()

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = lbl.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Image Processing")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

lbl = tk.Label(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

# lbl=Label(window)
# lbl.pack()


btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)
convolution = tk.Button(frm_buttons, text="Convolution", command=convolution)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
convolution.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
lbl.grid(row=0, column=1, sticky="nsew")



window.mainloop()