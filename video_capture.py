import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture(0)
while cap.isOpened():

    # Read feed
    ret, frame = cap.read()

    # Show to screen
    cv2.imshow('OpenCV Feed', frame)

    # Break gracefully
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
