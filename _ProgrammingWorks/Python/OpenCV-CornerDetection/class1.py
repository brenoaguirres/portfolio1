##########################################################
# DETECT CORNERS WITH HARRIS CORNER DETECTION
##########################################################

# method proposed by Chris Harris and Mike Steffens
# 1) Determine which windows produce very large variations in intensity when moved in both x and y directions.
# 2) With each such window found, a score R is computed.
# 3) After applying a threshold to this score, important corners are selected & marked.


import numpy as np
import cv2 as cv

img = cv.imread('chessboard.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)  # must cvt to float32, because cv.cornerHarris takes float32 format image

# params -> image, blockSize, ksize, k
# image ->  grayscale, float32 input img
# blockSize -> size of the neighbourhood considered for corner detection (pixel block sizes)
# ksize -> aperture parameter of Sobel derivative used
# k -> harris detector free parameter in the equation
dst = cv.cornerHarris(gray, 2, 3, 0.1)

dst = cv.dilate(dst, None)  # dilate to get better results

# reverting back to original img with optimal threshold value && marking the corners as red
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imshow('dst', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()
