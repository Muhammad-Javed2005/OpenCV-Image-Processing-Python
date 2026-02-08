import cv2

face_cascade = cv2.CascadeClassifier("Phase-7 Face & Object Detection\haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier("Phase-7 Face & Object Detection\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("Phase-7 Face & Object Detection\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            cv2.putText(frame, 'Eye Detected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
            cv2.putText(frame, 'Smile Detected', (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)


    cv2.imshow("Face, Eye and Smile Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
cap.release()
cv2.destroyAllWindows()
