import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    _,frame = cap.read()
    cv2.imshow('test', frame)