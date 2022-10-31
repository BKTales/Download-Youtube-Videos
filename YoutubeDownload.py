import pytube
from pytube import exceptions

path = "C:"

url = input("Enter video URL: ")

try:
    yt = pytube.YouTube(url)
except exceptions.VideoUnavailable:
    print("This video is unavailable")
except exceptions.VideoPrivate:
    print("Sadly, this video is private =(")
else:
    yt.streams.get_highest_resolution().download()
    print("Your video is downloading")

