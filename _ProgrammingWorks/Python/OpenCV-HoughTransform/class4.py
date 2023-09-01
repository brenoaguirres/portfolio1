################################################################
# HOUGH CIRCLE TRANSFORM
################################################################

# see class1 for more explanation <<<<<<<<<<<<<<<

# A circle is represented mathematically by -> (x-x_center)^2 + (y-y_center)^2 = r^2
#       (x_center, y_center) is the center, r is the radius

import cv2 as cv
import numpy as np

img = cv.imread('smarties.png')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
m_blur = cv.medianBlur(gray, 5)

# image, method, dp -> inverse ratio of the accumulator res. to the image res. ex: if 2, then 1/2 of img res.
# minDist -> min distance between the centers of the detected circles
# param1 -> First method specific parameter. In case of HOUGH_GRADIENT, it is the higher threshold of the two
#   passed to the Canny edge detector (the lower one is twice smaller).
# param2 -> Second method specific parameter. In case of HOUGH_GRADIENT, it is the accumulator threshold for the
#   circle centers at the detection stage.
# minRadius -> Minimum circle radius.
# maxRadius -> Maximum circle radius. If <= 0, uses the maximum image dimension. If < 0, returns centers without
#   finding the radius.
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 255, 0), 3)
    cv.circle(output, (x, y), 2, (0, 255, 255), 3)

cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()
