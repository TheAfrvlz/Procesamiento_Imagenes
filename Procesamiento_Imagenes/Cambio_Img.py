import numpy as np
import cv2 

dimension = (35,35)

#Escala Deadpool

for x in range(1,11):
    #print(x)
    #image = cv2.imread('conteo_{}.png'.format(x))
    image = cv2.imread('IMAGENES_OPENCV/PositivasDeadpool/{}.jpg'.format(x))
    image = cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
    cv2.imwrite('IMAGENES_OPENCV/Deadpool/P/{}.jpg'.format(x),image)

for x in range(12,28):
    #print(x)
    #image = cv2.imread('conteo_{}.png'.format(x))
    image = cv2.imread('IMAGENES_OPENCV/PositivasDeadpool/{}.jpg'.format(x))
    image = cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
    cv2.imwrite('IMAGENES_OPENCV/Esc_Deadpool/P/{}.jpg'.format(x),image)

#Escala Batman

for x in range(1,11):
    #print(x)
    #image = cv2.imread('conteo_{}.png'.format(x))
    image = cv2.imread('IMAGENES_OPENCV/PositivasBatman/{}.jpg'.format(x))
    image = cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
    cv2.imwrite('IMAGENES_OPENCV/Batman/P/{}.jpg'.format(x),image)

for x in range(12,27):
    #print(x)
    #image = cv2.imread('conteo_{}.png'.format(x))
    image = cv2.imread('IMAGENES_OPENCV/PositivasBatman/{}.jpg'.format(x))
    image = cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
    cv2.imwrite('IMAGENES_OPENCV/Batman/P/{}.jpg'.format(x),image)

#Escala Negativos

for x in range(1,11):
    #print(x)
    #image = cv2.imread('conteo_{}.png'.format(x))
    image = cv2.imread('IMAGENES_OPENCV/Negativas/{}.jpg'.format(x))
    image = cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
    cv2.imwrite('IMAGENES_OPENCV/Batman/N/{}.jpg'.format(x),image)
    cv2.imwrite('IMAGENES_OPENCV/Deadpool/N/{}.jpg'.format(x),image)

for x in range(12,13):
    #print(x)
    #image = cv2.imread('conteo_{}.png'.format(x))
    image = cv2.imread('IMAGENES_OPENCV/Negativas/{}.jpg'.format(x))
    image = cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
    cv2.imwrite('IMAGENES_OPENCV/Batman/N/{}.jpg'.format(x),image)
    cv2.imwrite('IMAGENES_OPENCV/Deadpool/N/{}.jpg'.format(x),image)