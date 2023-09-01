##########################################################
# OBJECT TRACKING MEANSHIFT METHOD
##########################################################

# follows an object on video
# limitations:
# size of the object window doesn't change
# we have to give the initial position

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('traffic.mp4')

# take first frame of the video
ret, frame = cap.read()

# setup initial location of the window
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

# set up ROI for tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# this will help finding the ROI
# cv.imshow('first-frame', frame)
# cv.imshow('roi', roi)

# set up the termination criteria, either 10 iterations or move by atleast 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while(1):
    ret, frame = cap.read()
    if ret == True:
        # convert frame to hsv and get its back projection
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)  # hsv img, channels, histogram, ranges, scale

        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x, y, w, h = track_window
        final_image = cv.rectangle(frame, (x, y), (x+width, y+height), 255, 3)

        cv.imshow('back-projected', dst)
        cv.imshow('final_image', final_image)
        k = cv.waitKey(30) & 0xff
        if k == ord('q'):
            break
    else:
        break
