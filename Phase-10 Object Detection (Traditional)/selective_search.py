# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
SELECTIVE SEARCH
Generates region proposals for object detection.
Used before YOLO / Faster-RCNN.
"""

import cv2

# Load image
img = cv2.imread("E:\AI and Data Science\Open CV With Engr.Muhammad Javed\object.jpg")

# Create Selective Search object
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(img)
ss.switchToSelectiveSearchFast()

# Get region proposals
rects = ss.process()

# Draw first few proposals
for i, rect in enumerate(rects[:100]):
    x, y, w, h = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

cv2.imshow("Selective Search", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
