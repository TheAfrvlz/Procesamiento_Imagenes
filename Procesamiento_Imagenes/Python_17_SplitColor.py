import cv2
import numpy as np

im = cv2.imread('imagenes/Spiral.png')
image = cv2.resize(im,(500,500),interpolation = cv2.INTER_AREA)

(B,G,R) = cv2.split(image)
merg = cv2.merge([B,G,R])
cv2.imshow("r",R)
cv2.imshow("g",G)
cv2.imshow("b",B)
cv2.imshow("merge",merg)
cv2.waitKey(0)

