#se agregan las librerias numpy  y cv2
import numpy as np
import cv2 as cv

#lectura la imagen IMA1
im = cv.imread('imagenes/IMA1.jpg')

#cambio de tamaño a 500x500 pixeles
im1 = cv.resize(im,(500,500),interpolation = cv.INTER_AREA)


print("max of 255: {}".format(cv.add(np.uint8([50]), np.uint8([50]))))
print("min of 0: {}".format(cv.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around: {}".format(np.uint8([50]) + np.uint8([50])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([50])))

#creacion de matriz de unos multiplicados por 170
M =  np.ones(im1.shape,dtype="uint8") * 50

#suma de la variable imagen y la matriz de unos
added = cv.add(im1,M)
cv.imshow("Added",added)

#resta de la variable imagen y la matriz de unos
M =  np.ones(im1.shape,dtype="uint8") *50
subtrac = cv.subtract(im1,M)
cv.imshow("subtrac",subtrac)

#multiplicacion de la variable imagen y la matriz de unos
mu = cv.multiply(im1,M)
cv.imshow("multiplicacion",mu)

#division de la variable imagen y la matriz de unos
div = cv.divide(im1,M)
cv.imshow("division",div)


cv.imshow("imag",im1)
cv.waitKey(0)

