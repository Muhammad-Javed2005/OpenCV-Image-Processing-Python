# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
MOBILENET SSD OBJECT DETECTION
Fast object detection using MobileNet-SSD.
"""

import cv2

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person"]

img = cv2.imread("scene.png")
(h, w) = img.shape[:2]

net = cv2.dnn.readNetFromCaffe(
    r"Phase-11 Deep Learning with OpenCV\models\MobileNetSSD_deploy.prototxt.txt",
    r"Phase-11 Deep Learning with OpenCV\models\MobileNetSSD_deploy.caffemodel"
)

blob = cv2.dnn.blobFromImage(img, 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.4:
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * [w, h, w, h]
        x1, y1, x2, y2 = box.astype("int")
        label = CLASSES[idx]
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("MobileNet SSD", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
