# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
HOG PERSON DETECTION
Detects humans in images using Histogram of Oriented Gradients.
Used before deep learning era.
"""

import cv2

# Load image (use people / street image)
img = cv2.imread("people.png")

# Initialize HOG descriptor with pre-trained people detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Detect people
(rects, _) = hog.detectMultiScale(
    img,
    winStride=(8, 8),
    padding=(16, 16),
    scale=1.05
)

# Draw bounding boxes
for (x, y, w, h) in rects:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("HOG Person Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
