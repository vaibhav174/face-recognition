# -*- coding: utf-8 -*-
"""
Created on Sun May 12 09:11:29 2019

@author: bittu
"""

import cv2
import numpy as np
import sqlite3
# we are using cascade classifier
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#load the web cam
cam=cv2.VideoCapture(0); #for web cam the capture id is generally 0

def insertOrUpdate(Id,Name,Age):
    conn=sqlite3.connect("facebase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecord=0
    for row in cursor:
        isRecord=1
    if(isRecord==1):
        cmd="UPDATE People SET Name="+str(Name)+",Age="+str(Age)+"Where ID="+str(Id)
    else:
        cmd="INSERT INTO People VALUES("+str(Id)+","+str(Name)+","+str(Age)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id = input('enter user id')
name = input('enter name')
# include "" while entering name
age = input('enter age')
insertOrUpdate(id,name,age)
sampleNum =0
#camera code
while(True):
    ret,img=cam.read();#return two variables one flag and another image
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting the returned colored image to grayscale
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)#detect faces in image and return its coordinates
    for(x,y,w,h) in faces:
        sampleNum+=1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])#writing data to database file
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#draw rectangle around face. (x,y),(x+w,y+h) are 2 points of rectangle.(255,0,0) is the RGB value for rectangle and 2 is thickness
        cv2.waitKey(100);
    cv2.imshow("face",img);#open window
    cv2.waitKey(1);
    if(sampleNum>20):
        break;
cam.release()
cv2.destroyAllWindows()