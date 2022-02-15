#Se agrega la libreria opencv
import cv2 as cv

#se define la funcion reescale, permite cambiar el tamaño del frame 
#al cual se le asigna el frame y el tamaño deseado
def rescaleFrame(frame, scale):
    
    #se obtiene el ancho y alto de la imagen y se multiplica por su valor de escala
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    #se crea una variable a la que se le asigna el ancho y alto
    dimensions = (width,height)
    
    #se hace un retorno de la imagen con el tamaño deseado
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)


#se hace una captura de video del archivo en la carpeta en imagenes
capture = cv.VideoCapture('imagenes/PM.mp4')

#se hace un bucle infinito 
while True:

    #se hace una lectura de cada frame del video
    isTrue, frame = capture.read()

    #al frame del video se le aplica un cambio de de escala
    fScale = rescaleFrame(frame,0.2)

    #se muestra el video en pantalla
    cv.imshow('Video',fScale)

    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()