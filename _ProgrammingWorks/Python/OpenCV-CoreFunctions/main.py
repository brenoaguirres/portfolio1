import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    global selection
    global copy
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(selection) == 0:
            selection.append((x, y))
        elif len(selection) == 1:
            selection.append((x, y))
            copy = []
            copy = np.array(img[selection[0][1]:selection[1][1], selection[0][0]:selection[1][0]])
            selection = []
            cv2.imshow('copy', copy)
        elif len(selection) == 2:
            selection = []
            copy = []
            selection.append((x, y))

    if event == cv2.EVENT_RBUTTONDOWN:
        if len(copy) > 0:
            rows, columns, m = copy.shape
            img[y:y+rows, x:x+columns] = copy
            cv2.imshow('image', img)

selection = []
copy = []
img = cv2.imread('kratos.jpg')

cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

# select two points with left click to copy, paste with right click, display instructions on screen, use scroll to
#   change rgb channels, add open cv logo
# open img2 on a second window