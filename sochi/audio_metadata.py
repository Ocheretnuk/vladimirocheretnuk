#!/usr/bin/env python
# coding: utf-8

# In[28]:


# выведем и запишем методанные для аудио 

import mutagen 
import datetime 

file = "videoalla.mp3"
audiofile = mutagen.File(file) 
l = datetime.timedelta(seconds=audiofile.info.length)
lm = audiofile.info.length
song_title = audiofile.tags.getall('TIT2') #Получаем название трека
singer_title = audiofile.tags.getall('TPE2') #Получаем исполнителя
bit = audiofile.info.bitrate


print('Продолжительность трека:', l) #Выводим продолжительность трека
print('Битрейт:', bit) #Выводим битрейт трека
print('Исполнитель:', singer_title) 
print('Название песни:', song_title, '\n')
#получаем словарь с данными и сохраняем в формате Json
v = {
    "Продолжительность трека": lm,
    "Битрейт": bit,
    "Исполнитель": singer_title,
    "Название песни": song_title
}   
    
with open("audio_metadata.json", "w") as write_file:
    json.dump(v, write_file)

      

