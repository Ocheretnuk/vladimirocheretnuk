#!/usr/bin/env python
# coding: utf-8

# In[1]:


#получаем аудио дорожку

import moviepy.editor as mp
clip = mp.VideoFileClip("Алла Пугачева - Миллион алых роз.mp4")
clip.audio.write_audiofile("videoalla.mp3")


# In[2]:


#получаем только видео без звука

import moviepy.editor as mp
clip = mp.VideoFileClip("Алла Пугачева - Миллион алых роз.mp4")
clip2 = clip. set_audio ( None)
clip2.write_videofile ("videoalla_without_sound.mp4" )





