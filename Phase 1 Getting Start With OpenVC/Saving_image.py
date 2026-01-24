# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************


import cv2

image = cv2.imread(
    "Phase 1 Getting Start With OpenVC/Python_Image.png"
)

if image is not None:
    success = cv2.imwrite("Output_python.png" , image)

    if success:
        print("Image saved successfully as 'output_pythin.png'")

    else:
        print("Failed to save the image")

else:
    print("Image not found , cannot save the image")