#!/usr/bin/env python
# coding: utf-8


from IPython.display import Audio
import spleeter #  эффективно отделяют вокал от музыки
Audio('audio_example.mp3')

get_ipython().system('spleeter separate -h')
get_ipython().system('spleeter separate -i audio_example.mp3 -o output/')
get_ipython().system('ls output/audio_and_instrument')

Audio('output/audio_and_instrument/videoalla_vocals.mp3')
Audio('output/audio_and_instrument/videoalla_accompaniment.mp3.mp3)







