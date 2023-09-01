##########################################################
# BACKGROUND SUBTRACTION METHODS IN OPENCV
##########################################################

# Background subtraction is a technique for generating foreground mask which is a.k.a. the binary image containing
#   the pixels belonging to a moving object of a scene.

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('vtest.avi')

# creating a background object of the funcion using createBackgroundSubtractorMOG()
# require pip install opencv-contrib-python

# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
# fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True)
# fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)

# required for GMG
# params -> shape and size of kernel
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    # getting foreground mask
    fgmask = fgbg.apply(frame)
    # Subtractor GMG needs morphological opening to work properly
    # fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)

    cv.imshow('feed', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == ord('q') or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()
