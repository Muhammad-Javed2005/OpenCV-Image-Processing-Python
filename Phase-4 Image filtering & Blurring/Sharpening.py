# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************


import cv2
import numpy as np


image = cv2.imread("Image Tree.jpg")

sharpening_kernel =  np.array([[0, -1, 0],
                               [-1,  5, -1],
                                 [0, -1, 0]])


sharpened = cv2.filter2D(image, -1, sharpening_kernel)

cv2.imshow("Original Image" , image)
cv2.imshow("Sharpened Image" , sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
