# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
TEMPLATE MATCHING
Used to find a small template image inside a larger image.
Works best for logos and symbols.
"""

import cv2

# Load images
img = cv2.imread("scene.png")
template = cv2.imread("logo.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_temp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Template matching
result = cv2.matchTemplate(gray_img, gray_temp, cv2.TM_CCOEFF_NORMED)

# Get best match location
_, max_val, _, max_loc = cv2.minMaxLoc(result)

# Draw bounding box
h, w = gray_temp.shape
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)

cv2.imshow("Template Matching Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
