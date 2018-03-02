#!/usr/bin/python

import cv2
import numpy
import random
import sys

cascade_src = 'haarcascade_upperbody.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

cascade_src1 = 'haarcascade_fullbody.xml'
car_cascade1 = cv2.CascadeClassifier(cascade_src1)

cascade_src2 = 'haarcascade_lowerbody.xml'
car_cascade2 = cv2.CascadeClassifier(cascade_src2)

video = cv2.VideoCapture('personas.avi')
video.set(5,35)
print video.get(5)
for i in range(20):
    print i, video.get(i)

while True:
    r, frame=video.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(640,480))
    upper = car_cascade.detectMultiScale(frame,3,2)
    full = car_cascade1.detectMultiScale(frame,5,2)
    lower = car_cascade2.detectMultiScale(frame,4,2)
    for (x, y, w, h) in upper:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    for (x, y, w, h) in full:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)
    for (x, y, w, h) in lower:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 8)
    cv2.imshow("hola",frame)
    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        video.release()


