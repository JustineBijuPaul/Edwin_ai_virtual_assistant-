import re
import urllib
import webbrowser

from speak import speak
from speak import takecommand


def yt():
    speak("opening youtube")
    speak("what should i play on youtube")
    song = takecommand()
    words = song.split()
    search_link = "http://www.youtube.com/results?search_query=" + '+'.join(words)
    html = urllib.request.urlopen(search_link)
    video_id = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    link = "https://www.youtube.com/watch?v=" + video_id[0]
    webbrowser.open_new(link)
    exit()
