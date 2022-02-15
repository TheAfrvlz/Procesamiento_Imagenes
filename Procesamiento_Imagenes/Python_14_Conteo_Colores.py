import cv2 as cv
import numpy as np
import math
Color =(255,255,255)
Objetos = 0
Rojo_L = np.array([175, 100, 20], np.uint8)
Rojo_H = np.array([180, 255, 255], np.uint8)

Azul_L = np.array([100,100,20],np.uint8)
Azul_H = np.array([121,255,255],np.uint8)

Amarillo_L = np.array([15,100,20],np.uint8)
Amarillo_H = np.array([45,255,255],np.uint8)

Verde_L = np.array([52,52,72],np.uint8)
Verde_H = np.array([102,255,255],np.uint8)

Morado_L = np.array([130, 100, 20], np.uint8)
Morado_H = np.array([145, 255, 255], np.uint8)

Naranja_L = np.array([11,234,255], np.uint8)
Naranja_H = np.array([2,234,255], np.uint8)


Mosaic = cv.imread('imagenes/Mosaico.jpg')
Mos_Res = cv.resize(Mosaic,(700,700),interpolation=cv.INTER_AREA)
Mos_HSV = cv.cvtColor(Mos_Res,cv.COLOR_BGR2HSV)

MskM = cv.inRange(Mos_HSV,Morado_L,Morado_H)
MskR = cv.inRange(Mos_HSV,Rojo_L,Rojo_H)
MskV = cv.inRange(Mos_HSV,Verde_L,Verde_H)
MskA = cv.inRange(Mos_HSV,Azul_L,Azul_H)
MskAm = cv.inRange(Mos_HSV,Amarillo_L,Amarillo_H)
MskN = cv.inRange(Mos_HSV,Naranja_L,Naranja_H)

ConMo,s = cv.findContours(MskM,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
ConR,z = cv.findContours(MskR,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
ConV,s = cv.findContours(MskV,cv.RETR_CCOMP,cv.CHAIN_APPROX_SIMPLE)
ConA,s = cv.findContours(MskA,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
ConAm,s = cv.findContours(MskAm,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

Img_Mask = cv.bitwise_and (Mos_Res, Mos_Res, mask=MskR)

for Con in ConR:
       area = cv.contourArea(Con)
       if area > 20:
          Objetos += 1
          cv.drawContours(Mos_Res,[Con],0,Color,2)

for Con in ConMo:
       area = cv.contourArea(Con)
       if area > 20:
          Objetos += 1
          cv.drawContours(Mos_Res,[Con],0,Color,2)   


for Con in ConV:
       area = cv.contourArea(Con)
       if area > 20:
          Objetos += 1
          cv.drawContours(Mos_Res,[Con],0,Color,2)        


cv.imshow('Mosaico',Mos_Res)
cv.waitKey(0)
cv.destroyAllWindows()

