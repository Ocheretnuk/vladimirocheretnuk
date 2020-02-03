#!/usr/bin/env python
# coding: utf-8


# Раскладываем видео по кадрам

import numpy as np
import cv2
import time
import os
from wand.image import Image


cap = cv2.VideoCapture('Алла Пугачева - Миллион алых роз.mp4')
i = 0
data_frame = []

try:
    os.mkdir("frames") # создаем и пререходим в папку, где будем хранить кадры
    os.chdir(r"frames")
except:
    None
    
while(True):
    ret, frame = cap.read() #cap.read() в ret возвращает значение, типа Boolean (True/False). Если frame прочитан корректно: ret = True.
    i += 1 
    cv2.imshow('frame', frame)
    cv2.imwrite("frame " + str(i)+ ".jpg",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




