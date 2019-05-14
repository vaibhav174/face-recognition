# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:49:42 2019

@author: bittu
"""

import cv2
import numpy as np
import sqlite3
# we are using cascade classifier
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#load the web cam
cam=cv2.VideoCapture(0); #for web cam the capture id is generally 0
#load recognizer from cv2
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/trainingData.yml")

def getProfile(id):
    conn=sqlite3.connect("facebase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

id=0
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 0, 0)
#camera code
while(True):
    ret,img=cam.read();#return two variables one flag and another image
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting the returned colored image to grayscale
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)#detect faces in image and return its coordinates
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#draw rectangle around face. (x,y),(x+w,y+h) are 2 points of rectangle.(255,0,0) is the RGB value for rectangle and 2 is thickness
        id, conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile!=None):
            cv2.putText(img,str(profile[1]),(x,y+h),font,fontscale, fontcolor)
            cv2.putText(img,str(profile[2]),(x,y+h+30),font,fontscale, fontcolor)
    cv2.imshow("face",img);#open window
    if(cv2.waitKey(1) == ord('q')):
        break;#ord return unicode of q we exit on pressing q
cam.release()
cv2.destroyAllWindows()