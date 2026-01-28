# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2

image = cv2.imread("E:\AI and Data Science\Open CV With Engr.Muhammad Javed\Output_python.png")

if image is None:
    print("Image not found, please check the path.")

else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped = cv2.flip(image, -1)

    cv2.imshow("Flipped Horizontal", flipped_horizontal)
    cv2.imshow("Flipped Vertical", flipped_vertical)
    cv2.imshow("Flipped Both", flipped)
    cv2.imshow("Original Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


