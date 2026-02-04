# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2 

image = cv2.imread("flower.png" , cv2.IMREAD_GRAYSCALE) 
edge = cv2.Canny(image , 50 , 150)

cv2.imshow("Original Image" , image)
cv2.imshow("Canny Edge Detection" , edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
 

