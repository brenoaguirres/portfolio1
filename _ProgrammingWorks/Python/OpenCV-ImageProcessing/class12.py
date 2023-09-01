################################################################
# MOTION DETECTION AND TRACKING USING OPENCV CONTOURS
################################################################

import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')

# reads first two frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # find absolute difference between the first two frames
    diff = cv.absdiff(frame1, frame2)
    # convert to grayscale, is easier to find the contours.
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    # apply gaussian blur
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    # threshold
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    # dilate threshold image to fill all the holes
    dilated = cv.dilate(thresh, None, iterations=3)
    # find contours
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # draw rectangles on frame1
    for contour in contours:
        # returns the x,y,w,h coordinates for creating a rectangle bounding the object
        (x, y, w, h) = cv.boundingRect(contour)

        # if contour area is too small the skip this iteration
        if cv.contourArea(contour) < 700:
            continue

        # otherwise draw the rectangle
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame1, "Status: {}".format("Movement"), (10, 20), cv.FONT_HERSHEY_SIMPLEX,
                   1, (0, 0, 255), 3)

    # draw contours on frame1
    #cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # display frame
    cv.imshow("feed", frame1)

    # update frames
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(40) == 32:
        break

cv.destroyAllWindows()
cap.release()
