import cv2
import numpy as np
import matplotlib.pyplot as plt

# original image
original_image = cv2.imread('images/femme.png',0)

plt.imshow(original_image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.axis('off')
plt.show()

# image in frequency domain
# Implement Fourier Transform to original_image
F = np.fft.fft2(original_image)
# plt.imshow(np.log1p(np.abs(F)), 
#            cmap='gray')
# plt.title('Image in Frequency domain'), plt.xticks([]), plt.yticks([])
# plt.axis('off')
# plt.show()

Fshift = np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)), 
           cmap='gray')
plt.title('The spectrum of image after transforming Fourier'), plt.xticks([]), plt.yticks([])
plt.axis('off')
plt.show()


# Filter: Low pass filter
M,N = original_image.shape
H = np.zeros((M,N), dtype=np.float32)
# D0: Tần số cắt của bộ lọc, D0 càng bé, lọc càng ít tần số thấp => ảnh càng mờ so với ảnh gốc
D0 = 50

# u: 0 -> M-1
# v: 0 -> N-1
# H(u,v) = 1 if D(u,v) <= D0 else H(u,v) = 0
for u in range(M):
    for v in range(N):
        # Calculate D(u,v)
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2) 
        if D <= D0:
            H[u,v] = 1
        else:
            H[u,v] = 0
            
# plt.imshow(H, cmap='gray')
# plt.title('Low pass filter'), plt.xticks([]), plt.yticks([])
# plt.axis('off')
# plt.show()

# # Ideal Low Pass Filtering
# Gshift = Fshift * H
# plt.imshow(np.log1p(np.abs(Gshift)), 
#            cmap='gray')
# plt.title('The spectrum of image after filtering by Low pass filter'), plt.xticks([]), plt.yticks([])
# plt.axis('off')
# plt.show()

# # Inverse Fourier Transform
# G = np.fft.ifftshift(Gshift)
# # plt.imshow(np.log1p(np.abs(G)), 
# #            cmap='gray')
# # plt.axis('off')
# # plt.show()

# g = np.abs(np.fft.ifft2(G))
# plt.imshow(g, cmap='gray')
# plt.title('The result after using Low pass filter'), plt.xticks([]), plt.yticks([])
# plt.axis('off')
# plt.show()


# Filter: High pass filter
H = 1 - H

plt.imshow(H, cmap='gray')
plt.title('High pass filter'), plt.xticks([]), plt.yticks([])
plt.axis('off')
plt.show()

# Ideal High Pass Filtering
Gshift = Fshift * H
plt.imshow(np.log1p(np.abs(Gshift)), 
           cmap='gray')
plt.title('The spectrum of image after filtering by High pass filter'), plt.xticks([]), plt.yticks([])
plt.axis('off')
plt.show()

# Inverse Fourier Transform
G = np.fft.ifftshift(Gshift)
# plt.imshow(np.log1p(np.abs(G)), 
#            cmap='gray')
# plt.axis('off')
# plt.show()

g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.title('The result after using High pass filter'), plt.xticks([]), plt.yticks([])
plt.axis('off')
plt.show()