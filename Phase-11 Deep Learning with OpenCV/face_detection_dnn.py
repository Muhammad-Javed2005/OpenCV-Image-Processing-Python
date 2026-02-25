# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
FACE DETECTION USING DNN
Uses Caffe-based face detector.
"""

import cv2

img = cv2.imread("people.png")
(h, w) = img.shape[:2]

net = cv2.dnn.readNetFromCaffe(
    r"Phase-11 Deep Learning with OpenCV\models\deploy.prototxt.txt",
    r"Phase-11 Deep Learning with OpenCV\models\res10_300x300_ssd_iter_140000.caffemodel"
)

blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300))
net.setInput(blob)
detections = net.forward()

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
        box = detections[0, 0, i, 3:7] * [w, h, w, h]
        x1, y1, x2, y2 = box.astype("int")
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Face Detection DNN", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
