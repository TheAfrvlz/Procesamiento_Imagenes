from matplotlib import pyplot as plt
import cv2 as cv

image = cv.imread('imagenes/image.jpg')
scale = cv.resize(image,(400,400),interpolation=cv.INTER_AREA)
GrayImage = cv.cvtColor(scale,cv.COLOR_BGR2GRAY)
cv.imshow('gray',GrayImage)

hist = cv.calcHist([image],[0],None,[256],[0,256])
plt.figure()
plt.title("grayscale")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()

chans = cv.split(scale)
colors = ("b","g","r")
plt.figure()
plt.title("Escala Colores")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
for (chan, color) in zip (chans, colors):
    hist1 = cv.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist1, color = color)
    plt.xlim([0, 256])
cv.imshow('Imagen Original',scale)
plt.show()

cv.waitKey(0)