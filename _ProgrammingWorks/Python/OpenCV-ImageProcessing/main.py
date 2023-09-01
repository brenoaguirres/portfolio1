################################################################
# TEMPLATE MATCHING USING OPENCV
################################################################

# Template matching - A method of searching and finding a template image inside a larger image.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('messi-cortado.jpg', 0)

# image, template, template match mode alg
# this will return an array of very small values, the biggest of them (closest to 1) is the brightest point, which
#   we will find next.
res = cv.matchTemplate(gray_img, template, cv.TM_CCOEFF_NORMED)

# different template algorithms will result in different behaviours for the points

# filtering out values greater than 'certain' value
# filtering out "where" res is greater or equal than "threshold"
threshold = 0.95  # for filtering, not for threshold method
loc = np.where(res >= threshold)

# draw square on template of original image, iterating for the case in which we have multiple
#   results from our loc filter.
w, h = template.shape[::-1]  # -1 will get columns and rows in the reverse order w, h instead of h, w.
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)  # pt is the filtered point

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
