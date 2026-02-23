# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
K-MEANS IMAGE SEGMENTATION
Segments an image into K clusters based on color similarity.
Used in object separation and region analysis.
"""

import cv2
import numpy as np

# Load image
img = cv2.imread("flower.png")
data = img.reshape((-1, 3))
data = np.float32(data)

# Define number of clusters
K = 3

# K-means criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Apply K-means
_, labels, centers = cv2.kmeans(
    data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
)

# Convert centers to uint8
centers = np.uint8(centers)

# Map labels to center values
segmented = centers[labels.flatten()]
segmented = segmented.reshape(img.shape)

cv2.imshow("Original Image", img)
cv2.imshow("K-Means Segmentation", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
