from abc import abstractproperty
import pytube
import os
import pathlib
from moviepy.editor import *

url = 'https://www.youtube.com/watch?v=gBT84ogoiWg'
youtube = pytube.YouTube(url)

print('Downloading...')

video = youtube.streams.get_highest_resolution()
video.download('.', 'download')

print('Successfully Downloaded: ' + video.title)

print('Converting to mp3...')

video_to_convert = VideoFileClip(os.path.join(pathlib.Path().absolute(), 'download.mp4'))
audio_clip = video_to_convert.audio.write_audiofile('download.mp3')
video_to_convert.close()
os.remove('download.mp4')

print('Finished!')