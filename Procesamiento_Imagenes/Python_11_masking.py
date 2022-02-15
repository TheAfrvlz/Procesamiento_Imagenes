import cv2
import numpy as np
im = cv2.imread('imagenes/IMA1.jpg')
image = cv2.resize(im,(500,500),interpolation = cv2.INTER_AREA)

cv2.imshow("Original", image)

mask = np.ones(image.shape[:2], dtype = "uint8")
print(mask)
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255,-1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)