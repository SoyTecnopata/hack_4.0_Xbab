# -*- coding: utf-8 -*-

import cv2
import numpy as np
print(cv2.__version__)

cascade_src = 'haarcascade_upperbody.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

cascade_src1 = 'haarcascade_fullbody.xml'
car_cascade1 = cv2.CascadeClassifier(cascade_src1)

cascade_src2 = 'haarcascade_lowerbody.xml'
car_cascade2 = cv2.CascadeClassifier(cascade_src2)


vid=cv2.VideoCapture('TRENES EN CHAPULTEPEC.avi')

while True:
    ret, img = vid.read()

    tol=20
    #hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #lower_brown = np.array([27,0,0])
    #upper_brown = np.array([33,100,100])
    # Only in RGB 26, 71, 170    59,96,159
    lower_brown = np.array([10,60,140])
    upper_brown = np.array([60,90,220])
    
    mask=cv2.inRange(img,lower_brown,upper_brown)
    res=cv2.bitwise_and(img,img,mask=mask)
    ##Brown R=158, G=135, B=103
    ## 138,111,82
    ## 209,177,139
    ##Brown H=22,100,90
    kernel=np.ones((15,15),np.uint8)
    erosion = cv2.dilate(mask,kernel,iterations = 1)
    closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)

    output = cv2.connectedComponentsWithStats(closing, 39, cv2.CV_32S)
    num_labels = output[0]
    labels = output[1]
    stats = output[2]
    centroids = output[3]

    cars = car_cascade.detectMultiScale(img,4,2)
    full = car_cascade1.detectMultiScale(img,8,2)
    lower = car_cascade2.detectMultiScale(img,4,2)


    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    for (x, y, w, h) in full:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 6)
    for (x, y, w, h) in lower:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 8)


    
    cv2.imshow('video', img)
    if  cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
vid.release()
