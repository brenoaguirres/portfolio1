###################################################################
# HOW TO READ, WRITE, SHOW IMAGES IN OPENCV
###################################################################

import cv2

# read image as pixel dataset
img = cv2.imread('lena.jpg', 0)  # 0 (greyscale), 1 (color), -1 (search on the img, including alpha channel)
# print(img)

# display image
cv2.imshow('image-name', img)
key = cv2.waitKey(0) & 0xFF  # keyboard binding function // 5000 milliseconds to show the image // if '0' ms, would show
#                                   img until close button press

if key == 27:
    cv2.destroyAllWindows()  # I think closes all opened windows
elif key == ord('s'):
    cv2.imwrite('lena_copy.png', img)  # write image to file

