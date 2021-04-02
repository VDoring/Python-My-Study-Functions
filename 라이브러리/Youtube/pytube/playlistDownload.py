# https://www.youtube.com/watch?v=UJZVmeV8hAA
from pytube import Playlist

# 재생목록 지정
pl = Playlist('https://www.youtube.com/playlist?list=PLP7Xvm2GzBZlmv26857MSNQeXKzlZw6Dw')

# 재생목록 영상 다운로드
pl.download_all('./pytube downloader/Video') # 2021-03-29 AM10:36 기준 작동안됨