# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))


while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame")
        break

    out.write(frame)
    cv2.imshow("Recording Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stopping recording...")
        break
camera.release()
out.release()
cv2.destroyAllWindows()
