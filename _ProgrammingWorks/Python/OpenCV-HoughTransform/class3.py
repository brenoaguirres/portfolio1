################################################################
# PROBABILISTIC HOUGH LINE TRANSFORM (HOUGHLINESP METHOD)
################################################################

# see class1 for more explanation <<<<<<<<<<<<<<<

import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow('edges', edges)

# params - img, rho, theta, threshold, line lengths < 100 are rejected, max allowed gap to treat as a single line
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]  # HoughLinesP will output directly the x1y1x2y2
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv.imshow('image', img)
k = cv.waitKey(0)
cv.destroyAllWindows()
