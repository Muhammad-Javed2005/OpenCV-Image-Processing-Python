# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
DNN IMAGE CLASSIFICATION
Uses a pretrained Caffe model to classify an image.
"""

import cv2

# Load image
img = cv2.imread("object.jpg")

# Load model
net = cv2.dnn.readNetFromCaffe(
    r"Phase-11 Deep Learning with OpenCV\models\deploy.prototxt.txt",
    r"Phase-11 Deep Learning with OpenCV\models\res10_300x300_ssd_iter_140000.caffemodel"
)

# Prepare input
blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300))
net.setInput(blob)

# Forward pass
detections = net.forward()

print("Image processed successfully")
