# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2

image = cv2.imread("E:\AI and Data Science\Open CV With Engr.Muhammad Javed\Output_python.png")

if image is not None:
    cropped = image[50:200, 100:300]

    cv2.imshow("Cropped Image", cropped)
    cv2.imshow("Original Image", image)

    cv2.imwrite("Cropped_Image.png", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found, please check the path.")
    