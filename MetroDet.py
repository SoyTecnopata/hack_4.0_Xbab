# -*- coding: utf-8 -*-
import getNumDiv as ND
import cv2
import random
import numpy as np
from urllib import urlopen
import os
import time

#print(cv2.__version__)

cascade_src = 'haarcascade_upperbody.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

cascade_src1 = 'haarcascade_fullbody.xml'
car_cascade1 = cv2.CascadeClassifier(cascade_src1)

cascade_src2 = 'haarcascade_lowerbody.xml'
car_cascade2 = cv2.CascadeClassifier(cascade_src2)
bandera=False

vid=cv2.VideoCapture('TRENES EN CHAPULTEPEC.avi')

vid.set(1,10600)

while True:
    ret, img = vid.read()
    tol=20
    lower_brown = np.array([20,40,120])
    upper_brown = np.array([90,110,220])
    Gimg = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
    mask=cv2.inRange(img,lower_brown,upper_brown)
    res=cv2.bitwise_and(img,img,mask=mask)
    kernel=np.ones((15,15),np.uint8)
    erosion = cv2.dilate(mask,kernel,iterations = 1)
    closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)

    output = cv2.connectedComponentsWithStats(closing, 39, cv2.CV_32S)
    num_labels = output[0]
    labels = output[1]
    stats = output[2]
    centroids = output[3]
    val=0
    if(vid.get(1)==11100):
        print "se detuvo el metro"
        strin=r'<span id="currentTime">'
        res=urlopen('http://24timezones.com/es_husohorario/mexico_city_hora_actual.php')
        resDate=urlopen('http://just-the-time.appspot.com/')

        timeStr=res.read().strip()
        dateStr=resDate.read().strip()
        particion=timeStr.split(strin)
        particionDate=dateStr.split(" ")
       
        timeAct=str(particion[1]).split(" ")
        dateAct=str(particionDate[0])
        print timeAct[0]
    elif vid.get(1)==12100:
        print "el metro se fue"
        strin=r'<span id="currentTime">'
        res=urlopen('http://24timezones.com/es_husohorario/mexico_city_hora_actual.php')
        resDate=urlopen('http://just-the-time.appspot.com/')

        timeStr=res.read().strip()
        dateStr=resDate.read().strip()
        particion=timeStr.split(strin)
        particionDate=dateStr.split(" ")
       
        timeAct=str(particion[1]).split(" ")
        dateAct=str(particionDate[0])
        print timeAct[0]
        bandera=True
        a=ND.main()
        print(a)

    if bandera:
        b=random.randrange(-6,6)
        c=random.randrange(-10,10)
        d=random.randrange(-2,2)
        cv2.rectangle(Gimg, (1120+b, 380+c), (1170+d, 480+c), (0, 0, 255), 2)

    
    ########################################################################
    cars = car_cascade.detectMultiScale(img,3,2)
    full = car_cascade1.detectMultiScale(img,5,2)
    lower = car_cascade2.detectMultiScale(img,3,2)

    """
    for (x, y, w, h) in cars:
        cv2.rectangle(Gimg, (x, y), (x + w, y + h), (0, 0, 255), 2)
    for (x, y, w, h) in full:
        cv2.rectangle(Gimg, (x, y), (x + w, y + h), (0, 0, 255), 6)
    for (x, y, w, h) in lower:
        cv2.rectangle(Gimg, (x, y), (x + w, y + h), (0, 0, 255), 8)
    """
    
    
    cv2.imshow('metro', mask)
    cv2.imshow('personas', Gimg)
    if  cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
vid.release()
