import cv2
import numpy as np
import matplotlib.pyplot as plt

# original image
original_image = cv2.imread('images/femme.png', 0)

def fourier_transform(img):
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 50*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

def show_input_output_image(input_image, output_image, kernel_name): 
    plt.subplot(121),plt.imshow(input_image, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(output_image, cmap = 'gray')
    plt.title(kernel_name), plt.xticks([]), plt.yticks([])
    plt.show()
    fourier_transform(input_image)
    fourier_transform(output_image)

# convolution kernel
M = 3
blur_kernel = np.ones((M,M)) * 1/(M*M)

sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]], 
                           dtype=np.float32)

laplacian_kernel = np.array((
                            [0, 1, 0],
                            [1, -4, 1],
                            [0, 1, 0]), 
                            dtype="int")

mean_kernel = np.ones((3,3))

x = cv2.getGaussianKernel(5,10)
gaussian_kernel = x*x.T

# apply the covolution
blur_image = cv2.filter2D(src=original_image, 
                          ddepth=-1, 
                          kernel=blur_kernel)
show_input_output_image(original_image, blur_image, 'The image of applying Blur kernel')

sharpen_image = cv2.filter2D(src=original_image, 
                             ddepth=-1, 
                             kernel=sharpen_kernel)
# show_input_output_image(original_image, sharpen_image, 'The image of applying Sharpen kernel')

laplacian_image = cv2.filter2D(src=original_image, 
                             ddepth=-1, 
                             kernel=laplacian_kernel)
# show_input_output_image(original_image, laplacian_image, 'The image of applying Laplacian kernel')

mean_image = cv2.filter2D(src=original_image, 
                             ddepth=-1, 
                             kernel=mean_kernel)
# show_input_output_image(original_image, mean_image, 'The image of applying Mean kernel')

gaussian_image = cv2.filter2D(src=original_image, 
                             ddepth=-1, 
                             kernel=gaussian_kernel)
# show_input_output_image(original_image, gaussian_image, 'The image of applying Gaussian kernel')

