# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2

image = cv2.imread(
    "Phase 1 Getting Start With OpenVC/Python_Image.png"
)

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    cv2.imshow("Display Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
