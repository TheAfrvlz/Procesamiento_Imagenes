import numpy as np
import cv2


image = cv2.imread('imagenes/newIMA.png')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image,(0,0),10)
cv2.imshow("desenfoque",image)



(T,thresh) = cv2.threshold(blurred,140,255,cv2.THRESH_BINARY)
cv2.imshow("umbral binario",thresh)


(T,threshinv) = cv2.threshold(blurred,140,255,cv2.THRESH_BINARY_INV)
cv2.imshow("umbral binario inverso",threshinv)



cv2.imshow("cir",cv2.bitwise_and(image,image,mask=thresh))


cv2.waitKey(0)