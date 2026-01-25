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
    color = (0 , 255 , 0)
    thickness = 4

    cv2.putText(image , "Open CV with Engr.Muhammad Javed" , plt1 , cv2.FONT_HERSHEY_SIMPLEX , 0.7 , color , thickness)
    cv2.imshow("Draw rectangle on Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
