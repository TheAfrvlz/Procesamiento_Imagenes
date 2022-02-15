import cv2
import numpy as np

faceClassif = cv2.CascadeClassifier('Haar_Cascade/haarcascade_frontalface_default.xml')

image = cv2.imread('imagenes/Team.jpeg')
image = cv2.resize(image, (500,500),interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30,30),
	maxSize=(600,600))

for (x,y,w,h) in faces:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()