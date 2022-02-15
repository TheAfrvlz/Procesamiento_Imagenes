#deteccion de bordes, encuentra puntor en una imagenes, donde el brillo cambia de forma diferente, 
from __future__ import print_function
from mahotas import thresholding
import numpy as np
import mahotas
import cv2

image = cv2.imread('imagenes/newIMA.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("original",image)

#se obtiene el gradiente()
#cv2.CV_64F - tipo de dato de salida para la imagen
lap = cv2.Laplacian(image, cv2.CV_64F)
#para poder obtener todos los bordes, se utiliza datos de tipo flotante, se obtiene su valor absoluto del gradiente de la imagen y se convierte en 
#en un tipo de archivo entero de 8 bits sin signo, 
lap = np.uint8(np.absolute(lap))
cv2.imshow("laplacian",lap)
cv2.waitKey(0)

sobelX = cv2.Sobel(image,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelComb = cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("sobelX",sobelX)
cv2.imshow("sobelY", sobelY)
cv2.imshow("sobel combi",sobelComb)
cv2.waitKey(0)

