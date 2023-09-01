################################################################
# HOUGH LINE TRANSFORM (HOUGHLINES METHOD)
################################################################

# see class1 for more explanation <<<<<<<<<<<<<<<

import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # convert to grayscale for canny edge detection - preferable
edges = cv.Canny(gray, 50, 150, apertureSize=3)  # canny edge detection - image, 1st. thresh, 2nd. thresh,
#                                                       apertureSize for Sobel operator.
lines = cv.HoughLines(edges, 1, np.pi / 180, 200)  # HoughLines - img, rho, theta, threshold
#                                                       rho - distance resolution of accumulator in pixels (normally 1)
#                                                       theta - angle res. of the accumulator in radians (normally pi/8)
#                                                    threshold - Accumulator thld param. - returns lines > threshold
# lines - Output vector. Each line is represented by a 2 or 3 element vector (rho, theta) or
#       (rho, theta, votes)
#       rho - distance from the coordinate origin (0, 0) (top-left corner of an image).
#       theta - is the line rotation angle in radians.
#       votes - value of the accumulator.

for line in lines:
    rho, theta = line[0]  # first element of line contains rho and theta
    a = np.cos(theta)  # converting polar coordinates to cartesian system
    b = np.sin(theta)
    x0 = a * rho  # x0, y0 are the origin (0,0)
    y0 = b * rho
    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y1 = int(y0 + 1000 * a)
    # x2 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * a)
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
