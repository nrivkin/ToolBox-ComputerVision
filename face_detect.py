""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ret
cap.isOpened()
cap.open(0)
cap.release()
cv2.destroyAllWindows()
cap