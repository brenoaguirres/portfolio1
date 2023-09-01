################################################################
# IMAGE PYRAMIDS
################################################################

# Technique that uses repeated smoothing and subsampling to reduce or upscale image resolution.
# This process is used to blend and reconstruct images.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')
# Gaussian Pyramids
# lr = cv.pyrDown(img)
# llr = cv.pyrDown(lr)
# hr = cv.pyrUp(llr)  # when you decrease the res using pyrDown you lose information, so hr will look worse than lr
# #                       because its up-scaling llr.

# Gaussian Pyramid array
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i), layer)

# Laplacian Pyramid
# A level in Laplacian Pyramid is formed by the difference between the level in gaussian pyramid and the extended
#       version of its upper level in gaussian pyramid.
layer = gp[5]
cv.imshow('upper level GP', layer)
lp = [layer]
for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)


cv.imshow("Original Image", img)
# cv.imshow("pyrDown 1", lr)
# cv.imshow("pyrDown 2", llr)
# cv.imshow("pyrUp 1", hr)
cv.waitKey(0)
cv.destroyAllWindows()
