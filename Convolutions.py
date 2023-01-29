import matplotlib.pyplot as plt

from kernel import *

sys.path.append('/Users/dungnd/Library/Python/3.8/lib/python/site-packages')

# original image
original_image = cv2.imread('images/femme.png', 0)


def fourier_transform(img, title='Input'):
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 50 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title(title + ' Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title(title + ' Image Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()


def show_input_output_image(input_image, output_image, kernel_name):
    plt.subplot(121), plt.imshow(input_image, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(output_image, cmap='gray')
    plt.title(kernel_name), plt.xticks([]), plt.yticks([])
    plt.show()
    fourier_transform(input_image)
    fourier_transform(output_image, title='Output')


def apply_filtering(img, kernel):
    output_image = cv2.filter2D(src=img,
                                ddepth=-1,
                                kernel=kernel)
    result_path = 'images/result.png'
    cv2.imwrite(result_path, output_image)
    return (result_path, output_image)


def add_image(x, y):
    output_image = cv2.add(x, y)
    result_path = 'images/result_hybrid.png'
    cv2.imwrite(result_path, output_image)
    return (result_path, output_image)
# apply the covolution
# blur_image = apply_filtering(original_image, blur_kernel) 
# show_input_output_image(original_image, blur_image, 'The image of applying Blur kernel')

# sharpen_image = apply_filtering(original_image, sharpen_kernel) 
# show_input_output_image(original_image, sharpen_image, 'The image of applying Sharpen kernel')

# laplacian_image = apply_filtering(original_image, laplacian_kernel) 
# show_input_output_image(original_image, laplacian_image, 'The image of applying Laplacian kernel')

# mean_image = apply_filtering(original_image, mean_kernel) 
# show_input_output_image(original_image, mean_image, 'The image of applying Mean kernel')

# gaussian_image = apply_filtering(original_image, gaussian_kernel) 
# show_input_output_image(original_image, gaussian_image, 'The image of applying Gaussian kernel')
