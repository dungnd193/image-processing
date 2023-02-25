import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilenames
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from PIL import Image, ImageTk
import numpy as np
import math
from Convolutions import *


def set_image(filepath, lbl):
        if not filepath:
            return

        img = Image.open(filepath)
        img = img.convert("L")
        img.thumbnail((350, 350))
        img = ImageTk.PhotoImage(img)

        if lbl == lbl1:
            global image1
            image1 = cv2.imread(filepath, 0)
        else:
            global image2
            image2 = cv2.imread(filepath, 0)

        lbl.configure(image=img)
        lbl.image = img


def open_image():
    """Open a file for editing."""
    filepaths = askopenfilenames(
        initialdir=os,
        title="SelectImage File",
        filetypes=[("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg"), ("PNG Files", "*.png"), ("All Files", "*.*")]
    )

    if len(filepaths) == 1:
        set_image(filepaths[0], lbl1)
        lbl2.configure(image=None)
        lbl2.image = None
    elif len(filepaths) == 2:
        set_image(filepaths[0], lbl1)
        set_image(filepaths[1], lbl2)


def hpf():
    # try:
        result_path, sharpen_image = apply_filtering(image1, sharpen_kernel)
        show_input_output_image(image1, sharpen_image, 'The image of applying HPF')
        set_image(result_path, lbl1)
    # except:
        # print("An exception occurred")


def lpf():
    try:
        result_path, blur_image = apply_filtering(image1, blur_kernel)
        show_input_output_image(image1, blur_image, 'The image of applying LPF')
        set_image(result_path, lbl1)
    except:
        print("An exception occurred")


def gradient_filter():
    try:
        kernel_x = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        kernel_y = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        sobel_x = cv2.filter2D(image1, -1, kernel_x)
        sobel_y = cv2.filter2D(image1, -1, kernel_y)
        result_image = sobel_x + sobel_y
        plt.imshow(np.abs(result_image), cmap='gray')
        plt.show()
    except:
        print("An exception occurred")

def makeGaussianFilter(numRows, numCols, sigma, highPass=True):
   centerI = int(numRows/2) + 1 if numRows % 2 == 1 else int(numRows/2)
   centerJ = int(numCols/2) + 1 if numCols % 2 == 1 else int(numCols/2)
 
   def gaussian(i,j):
      coefficient = math.exp(-1.0 * ((i - centerI)**2 + (j - centerJ)**2) / (2 * sigma**2))
      return 1 - coefficient if highPass else coefficient
 
   return np.array([[gaussian(i,j) for j in range(numCols)] for i in range(numRows)])

def filterDFT(imageMatrix, filterMatrix):
   shiftedDFT = fftshift(fft2(imageMatrix))
   filteredDFT = shiftedDFT * filterMatrix
   return ifft2(ifftshift(filteredDFT))

def hybrid_filter():
    try:
        n1,m1 = image1.shape
        n2,m2 = image2.shape
        sigmaHigh = 15
        sigmaLow = 15
        highPassed = filterDFT(image1, makeGaussianFilter(n1, m1, sigmaHigh, highPass=True))
        lowPassed = filterDFT(image2, makeGaussianFilter(n2, m2, sigmaLow, highPass=False))
        result_image = highPassed + lowPassed
        plt.imshow(np.abs(result_image), cmap='gray')
        plt.show()
    except:
        print("An exception occurred")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Image Processing")

    window.rowconfigure(0, minsize=350, weight=1)
    window.columnconfigure(1, minsize=350, weight=1)

    lbl1 = tk.Label(window)
    lbl2 = tk.Label(window)
    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

    btn_open = tk.Button(frm_buttons, text="Open", command=open_image)
    btn_hpf = tk.Button(frm_buttons, text="High Pass Filter", command=hpf)
    btn_lpf = tk.Button(frm_buttons, text="Low Pass Filter", command=lpf)
    btn_gf = tk.Button(frm_buttons, text="Gradient Filter", command=gradient_filter)
    btn_hf = tk.Button(frm_buttons, text="Hybrid Filter", command=hybrid_filter)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_hpf.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    btn_lpf.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    btn_gf.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    btn_hf.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

    frm_buttons.grid(row=0, column=0, sticky="ns")
    lbl1.grid(row=0, column=1, sticky="nsew")
    lbl2.grid(row=0, column=2, sticky="nsew")

    window.mainloop()
