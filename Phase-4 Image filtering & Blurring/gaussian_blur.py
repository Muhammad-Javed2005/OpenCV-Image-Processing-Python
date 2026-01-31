# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2
import numpy as np

image = cv2.imread("Image Tree.jpg")

blurred = cv2.GaussianBlur(image , (15 , 15), 4) 

cv2.imshow("Original Image" , image)
cv2.imshow("Gaussian Blurred Image" , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()




