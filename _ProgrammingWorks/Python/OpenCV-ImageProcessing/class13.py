################################################################
# DETECT SIMPLE GEOMETRIC SHAPES
################################################################

import cv2 as cv
import numpy as np

# get the contours
img = cv.imread('shapes.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imgGray, 240, 255, cv.THRESH_BINARY)  # 255 stands for the max value possible for threshold
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    # approximates a polygonal curve with the specified precision
    # params = curve, max distance between curve and approximation, true/false is the curve closed?
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)

    # draw contours - the index is 0 because we're passing the contours individually.
    cv.drawContours(img, [approx], 0, (0, 0, 0), 5)

    # this ravel method gets the x,y coordinates to put the text
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 20

    # estimating the shape by the number of vertexes in approx
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        # bounding rect to detect if its square or rectangle
        x, y, w, h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        if 0.95 <= aspectRatio <= 1.05:  # 1 aspectRatio is a square, but we're leaving room for noise
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv.imshow('shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()
