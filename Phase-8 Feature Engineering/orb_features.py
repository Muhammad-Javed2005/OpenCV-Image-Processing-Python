# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
ORB FEATURE DETECTION
Fast and free alternative to SIFT.
Used in real-time applications.
"""

import cv2

img = cv2.imread("flower.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create ORB detector
orb = cv2.ORB_create(nfeatures=500)

keypoints, descriptors = orb.detectAndCompute(gray, None)

# Draw keypoints
result = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0))

cv2.imshow("ORB Features", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
