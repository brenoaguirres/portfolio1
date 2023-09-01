##########################################################
# DETECT CORNERS WITH SHI TOMASI CORNER DETECTOR
##########################################################

# method proposed py J. Shi and C. Tomasi.
# based on Harris method

import numpy as np
import cv2 as cv

img = cv.imread('chessboard.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# image, number of corners to track, quality level, minDist
# quality level -> minimum expected quality of image corner
# minDistance -> min. possible euclidian distance between the returned corners
corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)

# int0 equals int64
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, 255, -1)

cv.imshow('dst', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()
