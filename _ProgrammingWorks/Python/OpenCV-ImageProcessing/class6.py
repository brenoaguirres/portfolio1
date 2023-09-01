################################################################
# SMOOTHING IMAGES
################################################################

# images can be filtered with various low-pass filters(LPF), high-pass filters(HPF), etc.
# LPF -> helps to remove noises, blurring the images.
# HPF -> helps to find edges in the images.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread('logo.png')  # to test the filter2D/blur smoothing
# img = cv.imread('halftone.png')  # to test the gaussian blur smoothing
# img = cv.imread('water.png')  # to test median filtering s&p noise
img = cv.imread('lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25  # array of ones divided by rows * columns
# homogeneous filter - image, desired-depth, kernel
dst = cv.filter2D(img, -1, kernel)

# blur filter algorithm - image, kernel - 5,5 kernel (same kind of filter2D because of same kernel)
blur = cv.blur(img, (5, 5))

# gaussian blur filter - image, kernel, sigmaX - different weights on the neighboring pixels.
gblur = cv.GaussianBlur(img, (5, 5), 0)

# median filter - replace each pixel's value with the median of its neighboring pixels - GREAT FOR SALT AND
#   PEPPER NOISE. - kernel must be odd, except 1.
median = cv.medianBlur(img, 5)

# bilateral filter - good for smoothing but preserving edges.
# image, diameter(each pixel's neighborhood),sigma-color, sigma-space
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'gblur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
