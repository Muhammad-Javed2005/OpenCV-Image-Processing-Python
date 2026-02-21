# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
SHI-TOMASI CORNER DETECTION
Improved version of Harris corner detector.
Used widely in tracking and motion analysis.
"""

import cv2
import numpy as np

img = cv2.imread("flower.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect corners
corners = cv2.goodFeaturesToTrack(
    gray,
    maxCorners=100,
    qualityLevel=0.01,
    minDistance=10
)

corners = np.int32(corners)

# Draw corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 4, (0, 255, 0), -1)

cv2.imshow("Shi-Tomasi Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
