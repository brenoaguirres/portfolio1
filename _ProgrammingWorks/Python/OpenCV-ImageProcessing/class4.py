################################################################
# MATPLOTLIB AND OPENCV
################################################################

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# advantages of matplot lib:
# -> in imshow() method you can see the x,y coordinates of the image
# -> you can save the image, zoom, config plot
# ->

img = cv.imread("smarties.png", -1)
cv.imshow("image", img)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # opencv reads in bgr, and image needs to be changed to rgb.

plt.imshow(img)  # imshow from pyplot
plt.xticks([]), plt.yticks([])  # this'll hide horizontal and vertical rules of the graph/img
plt.show()  # display matplotlib stuff

# SOME CONTENT OF MATPLOTLIB IN CLASS3

cv.waitKey(0)
cv.destroyAllWindows()
