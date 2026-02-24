# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
DNN OBJECT DETECTION (Generic)
Demonstrates how OpenCV DNN processes an image.
"""

import cv2

img = cv2.imread("object.jpg")

net = cv2.dnn.readNetFromCaffe(
    r"Phase-11 Deep Learning with OpenCV\models\MobileNetSSD_deploy.prototxt.txt",
    r"Phase-11 Deep Learning with OpenCV\models\MobileNetSSD_deploy.caffemodel"
)

blob = cv2.dnn.blobFromImage(img, 0.007843, (300, 300), 127.5)
net.setInput(blob)

detections = net.forward()

print("Detections shape:", detections.shape)
