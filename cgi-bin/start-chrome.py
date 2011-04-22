#!"C:\Python26\python.exe"
import os
from optparse import OptionParser

song_list = {'london': 'vTvNwAT29Lo',
             'mcdonald': '1oVoT9CnjK0',
             'spider': 'doyv0fL0YJw',
             'monkeys': 'tkXOKkxc0BA',
             'rain': 'KAYZo8a8AHg',
             'mary': 'u_K9hFxSvDM',
             'polly': 'nZQGDi1w2U',
             'bus': '7nKBKPcycFE'}
             

if '__main__' == __name__:
    parser = OptionParser()
    args = parser.parse_args()[1]

    song_name = args[0]
    os.system("Taskkill /IM chrome.exe /F")
    os.system("start http://www.youtube.com/watch_popup?v=%s&vq=medium" % song_list[song_name])

    
