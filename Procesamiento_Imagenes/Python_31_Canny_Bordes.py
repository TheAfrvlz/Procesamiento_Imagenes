import numpy as np
import cv2

image = cv2.imread('imagenes/Mosaico.jpg')
image = cv2.resize(image,(500,500),interpolation=cv2.INTER_AREA)
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("blurred",image)

canny = cv2.Canny(image,30,150)
cv2.imshow("Canny",canny)
cv2.waitKey(0)