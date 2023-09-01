#################################################################
# SPLIT, MERGE, RESIZE, ADD, ADDWEIGHTED, ROI
#################################################################

import numpy as np
import cv2

img = cv2.imread('kratos.jpg')
img2 = cv2.imread('logo.png')

print(img.shape)  # returns a tuple with number of rows, columns and channels -> extracts resolution
print(img.size)  # returns total number of pixels
print(img.dtype)  # returns image datatype
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# ROI - Region of Interest - Stands for the region of the image that is useful to the work you're doing.

# CROPPING IMAGE AND PASTING
face = img[0:578, 473:830]  # [height1:height2, width1:width2]
black_bg = np.zeros((578, (830-473), 3), np.uint8)
img[0:578, 0:(830-473)] = face
img[0:578, 473:830] = black_bg

img = cv2.resize(img, (512, 512))  # resize the two images to a defined res
img2 = cv2.resize(img2, (512, 512))

# ADDING TWO IMAGES
# dst = cv2.add(img, img2)  # won't work if images are different sizes -> needs resizing
dst = cv2.addWeighted(img, .7, img2, .3, 0)  # src alpha src beta + gamma

cv2.imshow('image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()