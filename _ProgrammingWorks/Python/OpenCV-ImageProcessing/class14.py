################################################################
# UNDERSTANDING IMAGE HISTOGRAMS USING OPENCV
################################################################

# Histogram is a graph that shows the overall intensity of an image.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 0)

# # CALCULATE HISTOGRAM WITH OPENCV <<<<<<<<<<<<<<<<<<
# params = image, index-of-channels, optional-mask
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# img = np.zeros((200, 200), np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), 255, -1)


# # CREATE HISTOGRAM WITH MATPLOTLIB <<<<<<<<<<<<<<<<<<<<<<<
# # ravel() returns a flattened array
# separating channels
# b, g, r = cv.split(img)
#
# cv.imshow("img", img)
# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)
#
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])


plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
