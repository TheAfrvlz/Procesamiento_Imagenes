import numpy as np
import cv2
import tkinter as tk
from numpy.lib.function_base import flip

xPos = 25
yPos = 25
ColorB = (255,0,0)
ColorG = (0,255,0)
ColorR = (0,0,255)
Color = (0,0,0)
Offset = 40
Malla = 3
Img_A = []

Rojo_L = np.array([0,50,20],np.uint8)
Rojo_H = np.array([5,255,255],np.uint8)

Azul_L = np.array([100,100,20],np.uint8)
Azul_H = np.array([121,255,255],np.uint8)

Amarillo_L = np.array([15,100,20],np.uint8)
Amarillo_H = np.array([45,255,255],np.uint8)

Verde_L = np.array([52,52,72],np.uint8)
Verde_H = np.array([102,255,255],np.uint8)

Negro_L = np.array([0, 0, 0],np.uint8)
Negro_H = np.array([180,255,30],np.uint8)

Blanco_L = np.array([0, 0, 200],np.uint8)
Blanco_H = np.array([180,255,255],np.uint8)

cap = cv2.VideoCapture(0)

#def Set_Malla(frame):
    #for i in range(0,Malla):
        #for j in range(0, Malla):
            #cv2.rectangle(frame,(xPos+(Offset*i),yPos+(Offset*j)),((xPos+Offset+(Offset*i),yPos+Offset+(Offset*j))),Color,2)         
            #Img_A.append(frame[yPos+(Offset*i): yPos+Offset+(Offset*i) , xPos+(Offset*j) : xPos+Offset+(Offset*j)])

while(True):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    
    #Set_Malla(frame)

    #for i in range(9):
        #Img_A[i] = cv2.cvtColor(Img_A[i],cv2.COLOR_BGR2HSV)
        
    Img_HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    MsKN = cv2.inRange(Img_HSV,Negro_L,Negro_H)
    MskR = cv2.inRange(Img_HSV,Rojo_L,Rojo_H)
    MskV = cv2.inRange(Img_HSV,Verde_L,Verde_H)
    MskA = cv2.inRange(Img_HSV,Azul_L,Azul_H)
    MskAm = cv2.inRange(Img_HSV,Amarillo_L,Amarillo_H)
    MskBl = cv2.inRange(Img_HSV,Blanco_L,Blanco_H)

    Msk = MskAm + MskR + MskA + MskV + MsKN + MskBl
    
    Img_Mask = cv2.bitwise_and (frame, frame, mask=MskV)

    C1,s1 = cv2.findContours(MskV, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    
    for Con in C1:
       area = cv2.contourArea(Con)
       if area > 2500:
          cv2.drawContours(frame,[Con],0,Color,1)


    cv2.imshow('Cubo Rubic',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()