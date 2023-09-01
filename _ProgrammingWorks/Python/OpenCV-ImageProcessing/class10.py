################################################################
# IMAGE BLENDING USING PYRAMIDS
################################################################

# steps to completely blend two images
# 1- Load the two images
# 2- Find the Gaussian Pyramids for the two images, in this particular case the level is 6
# 3- From gaussian pyramids, find laplassian pyramids
# 4- Now join the left half of img1 with right half of img2 in each level of laplassian pyramid
# 5- From this joint image pyramids, reconstruct the original image

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

apple = cv.imread('apple.jpg')
orange = cv.imread('orange.jpg')

# merge/blend half of two images
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# gaussian pyramid apple_layer
apple_layer = apple.copy()
gp1 = [apple_layer]
for i in range(6):
    apple_layer = cv.pyrDown(apple_layer)
    gp1.append(apple_layer)

# gaussian pyramid orange_layer
orange_layer = orange.copy()
gp2 = [orange_layer]
for i in range(6):
    orange_layer = cv.pyrDown(orange_layer)
    gp2.append(orange_layer)

# laplassian pyramid apple
apple_layer = gp1[-1]
lp1 = [apple_layer]
for i in range(6, 0, -1):
    gaussian_extended = cv.pyrUp(gp1[i])
    laplacian = cv.subtract(gp1[i-1], gaussian_extended)
    lp1.append(laplacian)

# laplassian pyramid orange
orange_layer = gp2[-1]
lp2 = [orange_layer]
for i in range(6, 0, -1):
    gaussian_extended = cv.pyrUp(gp2[i])
    laplacian = cv.subtract(gp2[i-1], gaussian_extended)
    lp2.append(laplacian)

# halves
apple_orange_pyramid = []
n = 0
for lp1, lp2 in zip(lp1, lp2):
    n += 1
    cols, rows, chnls = lp1.shape
    laplacian = np.hstack((lp1[:, 0:int(cols/2)], lp2[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# reconstruction
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 7):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv.imshow("apple-orange", apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()
