import os
import cv2 as cv
import numpy as np

people =['Batman','Elton']
DIR = r'C:/'
haar_cascade = cv.CascadeClassifier('Haar_Cascade/haarcascade_frontalface_default.xml')

features = []
Labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR,person) 
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)

            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade
