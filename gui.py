import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import os
from convolutions import *

def set_image(filepath): 
    if not filepath:
        return
        
    img=Image.open(filepath)
    img.thumbnail((350,350))
    img=ImageTk.PhotoImage(img)
    global image 
    image = cv2.imread(filepath, 0)
    lbl.configure(image=img)
    lbl.image=img

def open_image():
    """Open a file for editing."""
    filepath = askopenfilename(
        initialdir=os, 
        title="SelectImage File",
        filetypes=[("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg"), ("PNG Files", "*.png"), ("All Files", "*.*")]
    )
    set_image(filepath)

def save_image():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    # with open(filepath, mode="w", encoding="utf-8") as output_file:
    #     text = lbl.get("1.0", tk.END)
    #     output_file.write(text)
    # window.title(f"Simple Text Editor - {filepath}")

def hpf():
    try:
        result_path, sharpen_image = apply_filtering(image, sharpen_kernel)  
        # show_input_output_image(image, sharpen_image, 'The image of applying HPF')
        set_image(result_path)
    except:
        print("An exception occurred")

def lpf():
    try:
        result_path, blur_image = apply_filtering(image, blur_kernel)  
        # show_input_output_image(image, sharpen_image, 'The image of applying HPF')
        set_image(result_path)
    except:
        print("An exception occurred")

def gradient_filter():
    try:
        result_path, laplacian_image = apply_filtering(image, laplacian_kernel)  
        # show_input_output_image(image, sharpen_image, 'The image of applying HPF')
        set_image(result_path)
    except:
        print("An exception occurred")

window = tk.Tk()
window.title("Image Processing")

window.rowconfigure(0, minsize=350, weight=1)
window.columnconfigure(1, minsize=350, weight=1)

lbl = tk.Label(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open = tk.Button(frm_buttons, text="Open", command=open_image)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_image)
btn_hpf = tk.Button(frm_buttons, text="High Pass Filter", command=hpf)
btn_lpf = tk.Button(frm_buttons, text="Low Pass Filter", command=lpf)
btn_gf = tk.Button(frm_buttons, text="Gradient Filter", command=gradient_filter)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_hpf.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_lpf.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_gf.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
lbl.grid(row=0, column=1, sticky="nsew")



window.mainloop()