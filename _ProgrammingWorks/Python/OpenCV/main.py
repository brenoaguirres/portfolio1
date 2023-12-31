###################################################################
# MORE MOUSE EVENTS IN OPENCV
###################################################################

import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # CREATING LINES FROM POINTS
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # creates a point
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 5)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        # SHOW COLOR OF THE PIXEL FILLED ON OTHER WINDOW
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        myColorImage = np.zeros((512, 512, 3), np.uint8)
        myColorImage[:] = [blue, green, red]  # this notation means every point on the list

        cv2.imshow('color', myColorImage)  # displays color on new window.


img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
