import cv2
import numpy as np


EyeClassif = cv2.CascadeClassifier('Haar_Cascade/haarcascade_eye.xml') 

image = cv2.imread('imagenes/Team.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ojos = EyeClassif.detectMultiScale(gray,1.1,10)

for (x,y,w,h) in ojos:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()