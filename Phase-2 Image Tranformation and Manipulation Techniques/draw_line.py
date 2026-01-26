# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2

image = cv2.imread("E:\AI and Data Science\Open CV With Engr.Muhammad Javed\Output_python.png")

if image is None:
    print("Image not found, please check the path.") 

else:
    print("Image loaded successfully.")

    plt1 = (50 , 100)
    plt2 = (300 , 100)
    color = (0 , 255 , 0)
    thickness = 4

    cv2.line(image , plt1 , plt2 , color , thickness)

    cv2.imshow("Line on Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
