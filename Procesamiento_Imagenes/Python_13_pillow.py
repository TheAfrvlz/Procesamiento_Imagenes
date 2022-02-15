from PIL import Image
import matplotlib.pyplot as plt
from PIL  import ImageOps



image =  Image.open('imagenes/IMA1.jpg')
type(image)

plt.figure(figsize=(10,10))
plt.imshow(image)
#plt.show()

#image = Image.open('imagenes/IMA1.jpg')
print(image.size)
print(image.mode)
#image.show()

imageG = ImageOps.grayscale(image)
print(imageG.mode)

#cuantizacion: numero de valores unicos de intensidad en cada pixel
imageG.quantize(256//2)

r,g,b = imageG.split()

#ImageOps.get_concat_h(image,r)

imageG.show()

