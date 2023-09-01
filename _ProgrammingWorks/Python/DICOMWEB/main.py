import numpy as np
import cv2 as cv
import pydicom

# new test importing and converting
im = pydicom.dcmread("513_1783_20170307160758.0.dcm")

im = im.pixel_array.astype(float)

rescaled_image = (np.maximum(im, 0)/im.max())*255
final_image = np.uint8(rescaled_image)
final_image = np.array(final_image)

img = final_image

_, th = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow("Image", img)

res = cv.bitwise_and(th, img)

cv.imshow("res", res)

cv.waitKey(0)
cv.destroyAllWindows()
