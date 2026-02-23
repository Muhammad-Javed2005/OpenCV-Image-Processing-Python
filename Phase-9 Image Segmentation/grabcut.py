# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
GRABCUT SEGMENTATION
Used to extract foreground object from background
with minimal user input.
"""

import cv2
import numpy as np

# Load image
img = cv2.imread("man.png")

# Mask initialization
mask = np.zeros(img.shape[:2], np.uint8)

# Background and foreground models
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Rectangle around foreground object (x, y, width, height)
rect = (50, 50, 300, 400)

# Apply GrabCut
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Modify mask
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Extract foreground
result = img * mask2[:, :, np.newaxis]

cv2.imshow("Original Image", img)
cv2.imshow("GrabCut Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
