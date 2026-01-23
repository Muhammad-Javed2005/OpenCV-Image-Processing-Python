# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************


import cv2

image = cv2.imread("Phase 1 Getting Start With OpenVC\Python_Image.png")

if image is None:
    print("Image is not found")
else:
    print("Image load successfully")
