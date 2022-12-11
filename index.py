import numpy as np
import cv2
from matplotlib import pyplot as plt


# #read image
img_src = cv2.imread('images/femme.png',0)


# using numpy library
def fourier_transform_numpy(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 50*np.log(np.abs(fshift))
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

# using OpenCV library
def fourier_transform_opencv(img):
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 50*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

def LPF(img):
    rows, cols = img.shape

    nrows = cv2.getOptimalDFTSize(rows)
    ncols = cv2.getOptimalDFTSize(cols)
    nimg = np.zeros((nrows,ncols))
    nimg[:rows,:cols] = img

    # Implement Fourier Transform 
    dft = cv2.dft(np.float32(nimg),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    crow,ccol = int(rows/2) , int(cols/2)

    # create a kernel, center square is 1, remaining all zeros
    kernel = np.zeros((rows,cols,2),np.uint8)
    kernel[crow-30:crow+30, ccol-30:ccol+30] = 1

    # apply kernel
    fshift = dft_shift*kernel

    # inverse Fourier Transform
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
    plt.title('Output Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    fourier_transform_opencv(img)
    fourier_transform_opencv(img_back)

LPF(img_src)


# #prepare the 5x5 shaped filter
# Bo loc thong cao
high_pass_filter = np.array([[1, 1, 1], 
                             [1, 12, 1], 
                             [1, 1, 1]])
high_pass_filter = high_pass_filter/sum(high_pass_filter)

low_pass_filter = np.array([[1, 1, 1],
                           [1, 1, 1],
                           [1, 1, 1]], 
                           dtype=np.float32)

# filter the source image
img_src = cv2.filter2D(img_src, -1, low_pass_filter)

# save result image
cv2.imwrite('result.jpg',img_src)

# fourier_transform_opencv(img_src)


