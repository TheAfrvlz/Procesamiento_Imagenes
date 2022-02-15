import numpy as np
import cv2 as cv


image = cv.imread('imagenes/IMA1.jpg')
image= cv.cvtColor(image,cv.COLOR_BGR2GRAY)
imageS = cv.resize(image,(400,400),interpolation = cv.INTER_AREA)
blurred = cv.GaussianBlur(imageS,(5,5),0)

cv.imshow("image",blurred)


(t,thresh) = cv.threshold(blurred,155,255,cv.THRESH_BINARY)
cv.imshow("threshold binary",thresh)

(t,threshinv) = cv.threshold(blurred,155,255,cv.THRESH_BINARY_INV)
cv.imshow("threshold inv",threshinv)

cv.imshow("circuit", cv.bitwise_and(imageS,imageS,mask = thresh))
cv.waitKey(0)
