# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
THRESHOLDING VS SEGMENTATION
This file explains the difference between simple thresholding
and proper image segmentation techniques.
"""

import cv2

# Load image
img = cv2.imread("flower.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", img)
cv2.imshow("Threshold Result", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
