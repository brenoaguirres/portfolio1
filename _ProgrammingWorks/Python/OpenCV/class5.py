###################################################################
# HANDLE MOUSE EVENTS IN OPENCV
###################################################################

import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

# List all cv2 methods that contain the 'EVENT' keyword on its name
# dir is a built-in function that lists all functions and methods inside module
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# HANDLE CLICK EVENT
# callback function (receives function as argument) that will handle click event
# common syntax for this type of function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = "x: " + str(x) + ", y: " + str(y)
        print(strXY)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]  # 0 = blue channel, 1 = green channel, 2 = red channe; BGR
        green = img[y, x, 1]
        red = img[y, x, 2]
        strBGR = "Blue: " + str(blue) + " Green: " + str(green) + " Red: " + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)  # window name should match on callback function; ex: 'image'

cv2.setMouseCallback('image', click_event)  # window name should match on callback function; ex: 'image'

cv2.waitKey(0)
cv2.destroyAllWindows()