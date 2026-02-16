# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
HARRIS CORNER DETECTION
This technique is used to detect corners in an image.
Corners are important features where image intensity changes in two directions.
"""

import cv2
import numpy as np

# Load image
img = cv2.imread("flower.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to float32 as required by Harris
gray = np.float32(gray)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate result to mark corners clearly
corners = cv2.dilate(corners, None)

# Mark detected corners in red
img[corners > 0.01 * corners.max()] = [0, 0, 255]

cv2.imshow("Harris Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
