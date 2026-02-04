# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2
import numpy as np

image = cv2.imread("man.png" , cv2.IMREAD_GRAYSCALE)

ret , thresholded = cv2.threshold(image , 120 , 255 , cv2.THRESH_BINARY)

cv2.imshow("Original Image" , image)
cv2.imshow("Thresholded Image" , thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(image , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 11 , 2)
cv2.imshow("Adaptive Thresholded Image" , adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
