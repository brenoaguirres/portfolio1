################################################################
# ADAPTIVE THRESHOLDING
################################################################

# adp. thresholding -> thresholding smaller areas with different values

import numpy as np
import cv2 as cv
import pydicom
from matplotlib import pyplot as plt

im = pydicom.dcmread("513_1783_20170307160758.0.dcm")

im = im.pixel_array.astype(float)

rescaled_image = (np.maximum(im, 0)/im.max())*255
final_image = np.uint8(rescaled_image)
final_image = np.array(final_image)

img = final_image

# _, th = cv.threshold(img, 165, 255, cv.THRESH_TOZERO_INV)

# ADAPTIVE_THRESH_MEAN_C -> threshold value is the mean of the neighborhood area.
# params -> image, max-value, callback-method, thresh-type, blockSize, C, (optional)destination

th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 2)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)

titles = ['ADP THRESH MEAN C', 'ADP_THRESH_GAUSSIAN_C']
images = [th1, th2]

for i in range(2):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')  # rows, columns, img-index, image, grayscale
    plt.title(titles[i])  # adds defined titles
    plt.xticks([]), plt.yticks([])  # removes image hor e ver rulers.

plt.show()  # show imgs

# cv.imshow("Image", img)
# res = cv.bitwise_and(th1, img)
# cv.imshow("res", res)

cv.waitKey(0)
cv.destroyAllWindows()
