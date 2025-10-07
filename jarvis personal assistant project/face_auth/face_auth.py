# face_auth/face_auth.py
import cv2
import sys

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

recognized = False
print("🔐 Face Authentication Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        recognized = True
        break

    cv2.imshow('Face Authentication', frame)

    if recognized or cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if recognized:
    print("✅ Face recognized. Access granted.")
    sys.exit(0)
else:
    print("🚫 Face not recognized. Access denied.")
    sys.exit(1)
