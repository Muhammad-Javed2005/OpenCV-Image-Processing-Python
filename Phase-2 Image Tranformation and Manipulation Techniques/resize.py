# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************


import cv2

image = cv2.imread("E:\AI and Data Science\Open CV With Engr.Muhammad Javed\Output_python.png")


if image is None:
    print("Image not found, please check the path.")

else:
    print("Image loaded successfully.")

    resized = cv2.resize(image, (300, 300) )

    cv2.imshow("Resized Image", resized)
    cv2.imshow("Original Image", image)

    cv2.imwrite("Resized_Image.png", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
