################################################################
# MORPHOLOGICAL TRANSFORMATIONS
################################################################

# Morphological transformations are simple operations based on img shape.
# Morphological transformations are commonly performed on binary imgs.
# These ops need the original img and a Kernel.
# A Kernel tells you how to change the value of any pixel by combining it with
#   different amounts of the neighboring pixels.
# A Kernel is normally a square or some shape you want to apply on the image.

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("smarties.png", cv.IMREAD_GRAYSCALE)  # IMREAD_GRAYSCALE same as 0
_, mask = cv.threshold(img, 225, 255, cv.THRESH_BINARY_INV)

# we will create a square of white (ones) to apply to our morphological transforms.
kernel = np.ones((3, 3), np.uint8)  # 3x3 square shape -> best result I got for this img.
# dilation will apply 1 if at least 1 pixel under the kernel is 1
dilation = cv.dilate(mask, kernel, iterations=3)  # src/mask, kernel, iterations(default=1)
# erosion will apply 1 only if every pixel in the kernel is 1
erosion = cv.erode(mask, kernel, iterations=3)
# opening -> erosion followed by dilation
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)  # src/mask, operation type, kernel
# closing -> dilation followed by dilation
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
# gradient -> difference between dilation and erosion
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
# topHat -> difference between image and it's opening
topHat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

titles = ["image", "mask", "dilation", "erosion", "opening", "closing", "gradient", "top-hat"]
images = [img, mask, dilation, erosion, opening, closing, gradient, topHat]

for i in range(len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
