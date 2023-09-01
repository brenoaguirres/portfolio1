################################################################
# IMAGES GRADIENTS AND EDGE DETECTION
################################################################

# An image gradient is a directional change in the intensity or color in an image.
# We can use image gradients to find edges in images.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', cv.IMREAD_GRAYSCALE)

# gradients
# the 64Float supports the negative numbers which we will be dealing by using Laplacian method
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)  # image, dtype
# get the absolute value and convert back to unsigned 8-bit
lap = np.uint8(np.absolute(lap))

# sobelx & sobely gradients - get the horizontal or vertical gradients
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)  # image, dtype, dx, dy, kernelsize
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelCombined = cv.bitwise_or(sobelX, sobelY)

titles = ['image', 'laplacian', 'sobelX', 'sobelY', 'sobel-combined']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
