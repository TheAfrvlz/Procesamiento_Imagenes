
import cv2 as cv

#lectura imagenes
image1 = cv.imread('imagenes/IMA1.jpg')

#escala de imagenes
image = cv.resize(image1,(500,500),cv.INTER_LINEAR)


#informacion de la imagenes
print ("width: {} pixels".format(image.shape[1]))
print ("height: {} pixels".format(image.shape[0]))
print ("channels: {} pixels".format(image.shape[2]))


#crea nueva imagenes escaladas
cv.imshow("image",image)

(b,g,r) =  image[150,150]
print("pixel al (0,0)- Red:{},Green:{},Blue:{}".format(r,g,b))

image [0:100,0:100]= (255,255,255)
(b,g,r) =  image[200,200]
print("pixel al (0,0)- Red:{},Green:{},Blue:{}".format(r,g,b))
cv.imshow("image11",image)

cv.waitKey(0)