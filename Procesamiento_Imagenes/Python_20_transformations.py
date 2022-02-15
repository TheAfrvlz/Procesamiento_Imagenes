import cv2 as cv
import numpy as np
img = cv.imread('imagenes/IMA1.jpg')
img1 = cv.resize(img,(700,700))
cv.imshow("imag",img1)

def translate (img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension =  (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

translated = translate(img1,100,100)
cv.imshow("translated",translated)

cv.waitKey(0)