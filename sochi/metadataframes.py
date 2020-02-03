#!/usr/bin/env python
# coding: utf-8


#получаем метаданные по всем изображениям

import json
from wand.image import Image
import os 


os.chdir(r"frames") #заходим в папку, где хранятся все изображения
os.listdir(path=".")
print (len(os.listdir(path="."))) # кол-во получившихся кадров


#os.chdir(r"frames")
data_frame = [] # этот список будет заполнятся словарями с данными ко каждому изображению
for i in range(1, len(os.listdir(path="."))): 
# для каждой картинки заполняем словарь данными о ней: 
  #  'date:create':
  #  'date:modify': 
  #  'jpeg:colorspace': 
  #  'jpeg:sampling-factor': 
   # 'frame_number:': 
   # 'width:': 
   # 'height:': 
   # 'type:': 

    with Image(filename="frame " + str(i)+ ".jpg") as img:

        data1 = {
            'frame_number:': str(i),
            'width:': img.width,
            'height:': img.height,
            'type:': img.type,
        }
        data = {}
        for k, v in img.metadata.items():
            data[k] = v
        data.update(data1) # Словарь с данными для одной картинки
        
        data_frame.append(data) # заполняем список

with open('metadataframes.json', 'w') as f: #записываем в json
    json.dump(data_frame , f)

