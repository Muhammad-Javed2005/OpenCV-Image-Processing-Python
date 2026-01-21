# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************


import cv2

image = cv2.imread("Phase 1 Getting Start With OpenVC\Python_Image.png")

if image is not None:
    height, width, channels = image.shape
    print(f"Image Dimensions: Width={width}, Height={height}, Channels={channels}")

else:
    print("Image not found, cannot retrieve dimensions")
