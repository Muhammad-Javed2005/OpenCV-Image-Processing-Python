# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
FEATURE MATCHING USING ORB
Matches features between two images.
Used in object recognition and panorama stitching.
"""

import cv2

img1 = cv2.imread("flower.png", 0)
img2 = cv2.imread("man.png", 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Brute Force Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw matches
result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None)

cv2.imshow("Feature Matching", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
