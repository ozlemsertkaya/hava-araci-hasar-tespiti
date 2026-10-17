import cv2
cap = cv2.VideoCapture(0)
ok, kare = cap.read()
print(ok, kare.shape if ok else None)
cap.release()