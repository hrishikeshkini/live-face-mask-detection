import cv2
import os



cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def detect(img):
    coods = faceCascade.detectMultiScale(img)
    return coods

while True:
    ret, frame = cap.read()
    coods = detect(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    for(x, y, w, h) in coods:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('live', frame)
    if cv2.waitKey(1) &  0xFF == ord('x'):
        break
cv2.destroyAllWindows() 