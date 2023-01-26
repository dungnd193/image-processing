import sys

sys.path.append('/Users/dungnd/Library/Python/3.8/lib/python/site-packages')

import cv2
import numpy as np

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