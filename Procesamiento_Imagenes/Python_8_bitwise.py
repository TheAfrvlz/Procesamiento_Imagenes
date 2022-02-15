import numpy as np
import cv2 as cv

rectangle = np.zeros ((300,300),dtype="uint8")
cv.rectangle(rectangle,(25,25),(275,275),255,-1)
cv.imshow("rectangulo",rectangle)

circle = np.zeros((300,300),dtype="uint8")
cv.circle(circle,(150,150),150,255,-1)
cv.imshow("circulo",circle)

BitWiseAnd = cv.bitwise_and(rectangle,circle)
#cv.imshow("Operacion And",BitWiseAnd)


BitWiseOr = cv.bitwise_or(rectangle,circle)
#cv.imshow("Operacion Or",BitWiseOr)


BitWiseXor = cv.bitwise_xor(rectangle,circle)
#cv.imshow("Operacion Xor",BitWiseXor)

BitWiseNot = cv.bitwise_not(rectangle,circle)
#cv.imshow("Operacion Not",BitWiseNot)

Adder =  cv.add(rectangle,circle)
cv.imshow("Operacion Suma",Adder)

Rest =  cv.subtract(rectangle,circle)
cv.imshow("Operacion Resta",Rest)

Multi =  cv.multiply(rectangle,circle)
cv.imshow("Operacion Multiplicacion",Multi)

div =  cv.divide(rectangle,circle)
cv.imshow("Operacion division",div)



cv.waitKey(0)

