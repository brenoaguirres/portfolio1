#################################################################
# HOW TO BIND TRACKBAR
#################################################################

import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

# create a black image and a window
# img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

# create 3 sliders
cv.createTrackbar('B', 'image', 0, 255, nothing)  # name, window, min, max, function to pass the value
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

font = cv.FONT_HERSHEY_SIMPLEX

# track position of trackbar and switch to greyscale
cv.createTrackbar('CP', 'image', 10, 400, nothing)
switch2 = 'color/gray'
cv.createTrackbar(switch2, 'image', 0, 1, nothing)

# create a trackbar with two states called switch
switch = '0: OFF\n 1: ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

# using while to update the window
while(1):
    img = cv.imread('kratos.jpg')  # img must be read inside the loop to work properly

    # print trackbar value on screen
    pos = cv.getTrackbarPos('CP', 'image')
    cv.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255), 10)

    k = cv.waitKey(1) & 0xff  # 0xff caps listened key to 8 bits
    if k == 27:
        break

    # stores trackbar position
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    g = cv.getTrackbarPos(switch2, 'image')

    if s:
        # sets all pixels to trackbar values
        img[:] = [b, g, r]

    if g:
        # sets to grayscale
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('image', img)

cv.destroyAllWindows()
