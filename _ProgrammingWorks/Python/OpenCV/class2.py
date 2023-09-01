###################################################################
# HOW TO READ, WRITE, SHOW IMAGES IN OPENCV FROM CAMERA IN OPENCV
###################################################################

import cv2

# How to read video from default camera
cap = cv2.VideoCapture(0)  # 0 or -1 for default device index. 1, 2, 3... and so on for more cameras
# cap = cv2.VideoCapture('myFile.avi') // read video from file

# stores the fourcc video code for codex of .avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# stores the output path to the video, passing fourcc codex, frame-rate and size of video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# infinite capture loop until 'q' is pressed
# cap.isOpened() returns True if cap address or index was correct, otherwise it returns False
while cap.isOpened():
    # returned bool and frame
    ret, frame = cap.read()

    if ret:
        # capture frame width and height // not necessary for capturing the video
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # writing frame to output path variable
        out.write(frame)

        # convert color of the frame to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()  # releases variable
out.release()
cv2.destroyAllWindows()
