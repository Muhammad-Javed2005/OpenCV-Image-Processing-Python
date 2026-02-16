# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
HOMOGRAPHY TRANSFORMATION
Used to map one image plane onto another.
Important for panorama stitching and perspective correction.
"""

import cv2
import numpy as np

img1 = cv2.imread("Image Tree.jpg", 0)
img2 = cv2.imread("Image Tree.jpg", 0)

orb = cv2.ORB_create(1000)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    print("Homography Matrix:\n", H)
else:
    print("Not enough matches found.")
