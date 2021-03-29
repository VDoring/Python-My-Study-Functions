# https://www.youtube.com/watch?v=54EjMLjxuhQ
from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=54EjMLjxuhQ').streams.first().download('./pytube downloader/Video')