from pytube import YouTube


class VideoDownloader:
    def __init__(self, url) -> None:
        self.url = url
        self._yt = YouTube(self.url)
        self._streams = self._yt.streams

    def download_video(self):
        try:
            video = self._streams.get_highest_resolution()
            video.download("downloads/")
            print("success")
        except Exception as e:
            print("error {e}")
