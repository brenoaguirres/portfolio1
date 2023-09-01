###################################################################
# DRAW GEOMETRIC SHAPES ON IMAGES USING OPENCV
###################################################################

import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)

# creating black img with numpy
# img = np.zeros([512, 512, 3], np.uint8)

# drawing lines and arrows
img = cv2.arrowedLine(img, (0, 0), (255, 255), (147, 96, 44), 10)
img = cv2.line(img, (0, 0), (255, 255), (255, 255, 255), 5)  # color is given in BGR and not RGB

# drawing rectangle and circle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)  # -1 thickness means fill

# drawing text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)  # 4 is size, cv2.LINE_AA is
#                                                                                           line type.

cv2.imshow('lena.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()