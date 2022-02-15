import cv2
url="http://192.168.1.67:8080/shot.jpg"
cap=cv2.VideoCapture(url)

while(True):
    cap .open(url)
    _,frame=cap.read()
    cv2.imshow('video',frame)
    if(cv2.waitKey(1) & 0xFF==27):
        break
cap.release()
cv2.destroyAllWindows()