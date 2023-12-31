###################################################################
# SETTING CAMERA PARAMETERS IN OPENCV PYTHON
###################################################################

import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# sets camera resolution.
# If it's an unavailable resolution it will set it to the next default res.
cap.set(3, 1080)  # 3 means CAP_PROP_FRAME_WIDTH
cap.set(4, 720)  # 4 means CAP_PROP_FRAME_HEIGHT

print(cap.get(3))
print(cap.get(4))

font = cv2.FONT_HERSHEY_SIMPLEX

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        # print resolution on video.
        text = "Width: " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + " x Height: " \
               + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # print date and time on video
        dateT = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        frame = cv2.putText(frame, dateT, (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()