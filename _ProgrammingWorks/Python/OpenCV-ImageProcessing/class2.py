################################################################
# SIMPLE IMAGE THRESHOLDING
################################################################

# thresholding -> technique for separating image from bg by comparing each pixel with a predefined
#       threshold value.

import numpy as np
import cv2 as cv
import pydicom

# new test importing and converting
im = pydicom.dcmread("513_1783_20170307160758.0.dcm")

im = im.pixel_array.astype(float)

rescaled_image = (np.maximum(im, 0)/im.max())*255
final_image = np.uint8(rescaled_image)
final_image = np.array(final_image)

#img = cv.imread(final_image, 0)
img = final_image
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # THRESH_BINARY type: if the pixel is lesser than 127(thresh)
#                                                           it will be black, if it's greater it will be white(255).
#                                                           Binary -> either one or zero
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)  # Inverse of thresh binary.
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)       # caps < 127 to same ; > 127 to 127
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)      # < 127 to 0; > 127 to same
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow("Image", img)
cv.imshow("TH", th5)

# res = cv.bitwise_not(th4)
res = cv.bitwise_and(th5, img)

cv.imshow("res", res)

cv.waitKey(0)
cv.destroyAllWindows()
