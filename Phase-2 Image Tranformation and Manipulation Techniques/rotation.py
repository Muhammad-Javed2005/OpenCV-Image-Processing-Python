# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************


import cv2

image = cv2.imread("E:\AI and Data Science\Open CV With Engr.Muhammad Javed\Output_python.png")


if image is None:
    print("Image not found, please check the path.")

else:
    (h ,w) = image.shape[:2]

    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center , 90 , 1.0)
    rotated = cv2.warpAffine(image, M, (w, h) )
    cv2.imshow("Rotated Image", rotated)
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    