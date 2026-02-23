# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
WATERSHED SEGMENTATION
Used to separate touching or overlapping objects.
Commonly used in medical and industrial image analysis.
"""

import cv2
import numpy as np

# Load image
img = cv2.imread("shape.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold
_, thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Noise removal using morphology
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform,
                           0.7 * dist_transform.max(), 255, 0)

# Unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labeling
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Apply watershed
markers = cv2.watershed(img, markers)
img[markers == -1] = [0, 0, 255]

cv2.imshow("Watershed Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
