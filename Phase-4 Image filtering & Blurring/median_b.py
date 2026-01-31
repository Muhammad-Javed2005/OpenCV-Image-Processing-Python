# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************


import cv2 

image = cv2.imread("Image Tree.jpg")

median_blurred = cv2.medianBlur(image , 7)

cv2.imshow("Original Image" , image)
cv2.imshow("Median Blurred Image" , median_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
