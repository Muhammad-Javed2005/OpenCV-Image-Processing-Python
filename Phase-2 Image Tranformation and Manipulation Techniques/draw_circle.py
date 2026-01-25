# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2

image = cv2.imread("E:\AI and Data Science\Open CV With Engr.Muhammad Javed\Output_python.png")

if image is None:
    print("Image not found, please check the path.") 

else:
    print("Image loaded successfully.")

    center = (150 , 150)
    radius = 75
    color = (0 , 255 , 0)
    thickness = -1

    cv2.circle(image , center , radius , color , thickness  )

    cv2.imshow("Draw Circle on Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
