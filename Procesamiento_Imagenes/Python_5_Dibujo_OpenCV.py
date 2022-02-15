import numpy as np 
import cv2 
canvas= np.zeros((300,300,3),dtype="uint8")
green = (0,255,255)
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)

red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red,3)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)

cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canv = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canv.shape[1] // 2, canv.shape[0] // 2)

white = (255, 255, 255)
for r in range(0, 175, 25):
    cv2.circle(canv, (150,150), r, white)

cv2.imshow("Canvas", canv)
cv2.waitKey(0)

for i in range (0,25):
    radius =  np.random.randint(5,high= 50)
    color = np.random.randint(0, high=255,size=(3,)).tolist()
    pt = np.random.randint(0,high=150,size=(2,))
    cv2.circle(canv , tuple(pt),radius,color, -1)

cv2.imshow("canvas",canv)
cv2.waitKey(0)


