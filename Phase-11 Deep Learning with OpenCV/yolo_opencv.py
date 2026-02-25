# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

"""
YOLOv3 OBJECT DETECTION
Uses YOLOv3 with OpenCV DNN module.
"""

import cv2
import numpy as np

img = cv2.imread("scene.png")
(h, w) = img.shape[:2]


# Load YOLO
net = cv2.dnn.readNet(
    r"Phase-11 Deep Learning with OpenCV\models\yolov3.weights",
    r"Phase-11 Deep Learning with OpenCV\models\yolov3.cfg"
)

# Load class labels
with open("Phase-11 Deep Learning with OpenCV\models\coco.names", "r") as f:
    classes = f.read().strip().split("\n")

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]


 
# Create blob
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True)
net.setInput(blob)
outputs = net.forward(output_layers)

for output in outputs:
    for det in output:
        scores = det[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:
            center_x, center_y, w_box, h_box = (det[:4] * [w, h, w, h]).astype("int")
            x = int(center_x - w_box / 2)
            y = int(center_y - h_box / 2)

            cv2.rectangle(img, (x, y), (x + w_box, y + h_box), (0, 0, 255), 2)
            cv2.putText(img, classes[class_id], (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

cv2.imshow("YOLO Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

