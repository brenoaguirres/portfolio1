#########################################################################
# FACE DETECTION USING HAAR CASCADE CLASSIFIERS
#########################################################################

# Face detection method proposed by Paul Viola and Michael Jones
# Machine learning based approach, where a cascade function is trained for a lot of positive and negative images.
#
# First a classifier is trained with a few hundred sample views of a particular object, called positive examples,
# scaled to the same size (say, 20x20), and to - negative - arbitrary images of the same size.
#
# Then it can be applied to a ROI in an input image, the outputs are 1 if the region is likely to show the object or
# 0 otherwise.
#
# OpenCV comes with a built-in trainer and a detector.
# If you want to train for any object you can use these functions and you check opencv github page for pre-built objects
# https://github.com/opencv/opencv/tree/4.x/data/haarcascades

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

# read cascadeclassifier training inputs
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# read input image
# img = cv.imread('test.jpg')

cap = cv.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # parameters - image, objects, scaleFactor, minNeighbors
    # objects -> Vector of rectangles where each rectangle contains the detected object, the rectangles may be partially
    #       outside the original image.
    # scaleFactor -> Parameter specifying how much the image size reduced at each image scale.
    # minNeighbors -> Parameter specifying how many neighbors each candidate rectangle should have to retain it.
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # will draw a rectangle for each face passed in faces
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow('feed', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
