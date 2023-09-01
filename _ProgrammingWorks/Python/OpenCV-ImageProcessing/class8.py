################################################################
# CANNY EDGE DETECTION
################################################################

# The Canny Edge Detector is a multi-stage algorithm that detects a wide range of edges in images.
# 5 steps:
# 1- Noise Reduction -- Gaussian Filter
# 2- Gradient Calculation -- Find the intensity gradient
# 3- Non-Maximum Suppression
# 4- Double Threshold -- Determine potential edges
# 5- Edge Tracking by Hysteresis -- Suppress all weak edges that are not connected to strong edges

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 0)
canny = cv.Canny(img, 100, 200, )

titles = ['images', 'canny']
images = [img, canny]
for i in range(len(images)):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
