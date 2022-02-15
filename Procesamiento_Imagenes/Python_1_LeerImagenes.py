#se agrega la libreria OPENCV
import cv2 as cv

#se hace lectura de la imagen que esta en la carpeta de imagenes y se guarda en la variable img
img = cv.imread('imagenes/IMA1.jpg')

#se cambia el tamaño de la imagen de 250x250 la imagen img
img_r = cv.resize(img,(250,250),interpolation=cv.INTER_AREA)

#se muestra la imagen original y la imagen escalada en la pantalla
cv.imshow('escala_imagen',img_r)
cv.imshow('imagen',img)

#se espera a que se presione una tecla
cv.waitKey(0)
