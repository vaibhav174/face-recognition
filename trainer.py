# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:05:22 2019

@author: bittu
"""

import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()# create recogniser from opencv
path = 'dataSet'

def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #os.path.join(path,f) appent f to path with /
    #for f in os.listdir(path) stores all files name in dataSet in f
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        #get the image
        faceImg = Image.open(imagePath);
        #covert it to numpy array coz opencv works only with numpy array
        faceNp=np.array(faceImg,'uint8')
        #get the id from file name by spliting the name [-1] gives last word in name
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)#store numpy array
        IDs.append(ID)#store id of each image
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return np.array(IDs), faces
#now call the function to get the images and ids
Ids, faces=getImagesWithID(path)
#now train recogniser
recognizer.train(faces,Ids)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()