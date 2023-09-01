################################################################
# OBJECT DETECTION AND OBJECT TRACKING USING HSV COLOR SPACE
################################################################

import numpy as np
import cv2 as cv

# HSV: Hue - base pigment (0-360); Saturation - amount of color/hue (0-100%); Value - brightness (0-100%)

def nothing(x):  # dummy function for required callback
    pass

# video capture
cap = cv.VideoCapture(0)

# tracking window and trackbars
cv.namedWindow("tracking")
cv.createTrackbar("LH", "tracking", 0, 255, nothing)
cv.createTrackbar("LS", "tracking", 0, 255, nothing)
cv.createTrackbar("LV", "tracking", 0, 255, nothing)
cv.createTrackbar("UH", "tracking", 255, 255, nothing)
cv.createTrackbar("US", "tracking", 255, 255, nothing)
cv.createTrackbar("UV", "tracking", 255, 255, nothing)

while True:
    # for image
    # frame = cv.imread("smarties.png")
    # for video
    _, frame = cap.read()  # _ is a generic name for variable

    #getting trackbar input
    lowerHue = cv.getTrackbarPos("LH", "tracking")
    lowerSat = cv.getTrackbarPos("LS", "tracking")
    lowerVal = cv.getTrackbarPos("LV", "tracking")
    upperHue = cv.getTrackbarPos("UH", "tracking")
    upperSat = cv.getTrackbarPos("US", "tracking")
    upperVal = cv.getTrackbarPos("UV", "tracking")

    # conversion to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_b = np.array([lowerHue, lowerSat, lowerVal])  # lower hue for blue color detection -- HSV
    h_b = np.array([upperHue, upperSat, upperVal])  # higher hue for blue color detection -- HSV

    mask = cv.inRange(hsv, l_b, h_b)  # returns an array with the hsv options between the lower and higher boundaries

    res = cv.bitwise_and(frame, frame, mask=mask)  # applies the mask on the image

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    key = cv.waitKey(1)
    if key == 32:  # 32 for space
        break

cap.release()
cv.destroyAllWindows()
