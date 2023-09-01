################################################################
# FIND AND DRAW CONTOURS
################################################################

# Contours are the curves, joining all continuous points along the boundary which have the same color or intensity.
# Useful for shape analysis, object detection, object recognition.
# For better accuracy we use binary images.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('logo.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # threshold image,
#                                                                       contour mode, contour approximation method
# the var. 'contours' will be a python list with all the contours in the image. Each individual contour is a Numpy
#       array of (x,y) coordinates and boundary points of the object.
# the var. 'hierarchy' is an optional output vector which contains info about the image topology.
print("Number of contours: " + str(len(contours)))
print(contours[0])

# draw contours on image.
# image, contours, contour index: -1 for all, color, thickness
cv.drawContours(img, contours, -1, (0, 255, 255), 3)

cv.imshow('Image', img)
cv.imshow('Image GRAY', imgray)

cv.waitKey(0)
cv.destroyAllWindows()
