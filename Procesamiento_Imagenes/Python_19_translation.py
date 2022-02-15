import numpy as np
import cv2

image = cv2.imread('imagenes/newIMA.jpg')


#definicion de funcion que permite mover una imagen
def translate (image,x,y):
    #se crea una matriz que va a tener un tamaño de x y y
    M = np.float32([[1,0,x],[0,1,y]])
    
    #se crea una imagen ya desplazada
    shif = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
    return shif

M = np.float32([[1,0,100],[0,1,150]])
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
#desplazamiento derecha, abajo
cv2.imshow("image shift",shifted)
cv2.imshow("shift function",translate(image,150,100))

(h,w) = image.shape[:2]
center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("rotacion 45 grad",rotated)

#implementacion de metodo que permite rotar una imagen
M = cv2.getRotationMatrix2D(center,-90,1.0)
rotated1 = cv2.warpAffine(image,M,(w,h))
#cv2.imshow("rotacion 90 grados",rotated1)

def rotate (image,angle,center,scale=1.0):
    (h,w) = image.shape[:2]
    center = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center,angle,scale)
    rotated = cv2.warpAffine(image,M,(w,h))
    return rotated

#cv2.imshow("rotacion 45",rotate(image,45,1.0))


#vertical flip
#cv2.imshow("flip image",cv2.flip(image,0))
#horizontal flip
cv2.imshow("flip image",cv2.flip(image,1))
cv2.waitKey(0)

