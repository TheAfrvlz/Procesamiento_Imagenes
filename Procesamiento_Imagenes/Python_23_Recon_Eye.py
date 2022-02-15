import numpy as np
import cv2

EyeClassif = cv2.CascadeClassifier('Haar_Cascade/haarcascade_eye.xml') 

cap = cv2.VideoCapture(0)


while(True):
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ojos = EyeClassif.detectMultiScale(gray,1.2,10)

    for (x,y,w,h) in ojos:
	    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Reconocimiento de Ojos',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()