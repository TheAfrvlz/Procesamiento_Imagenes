import cv2 as cv
import numpy as np

img = cv.imread('imagenes/Log.png')
img = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('logo',img)
cv.waitKey(0)