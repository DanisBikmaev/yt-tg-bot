from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=0mh5d2a8wp0')
streams = yt.streams

for stream in streams:
    print(stream)
    print('---'*20)
    
video = streams.get_by_itag(251)
video.download()