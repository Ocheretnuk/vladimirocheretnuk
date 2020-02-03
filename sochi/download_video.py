#!/usr/bin/env python
# coding: utf-8

#Скрипт скачивает видео с Youtube

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=ieqlySC2M-Y')
yt.streams.first().download()




