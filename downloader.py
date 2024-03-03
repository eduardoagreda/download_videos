"""
    Script to download YouTube videos.
    With this script, we can check if a single video or a playlist 
    and proceed to download all videos.
"""

import os

from pytube import YouTube
from pytube import Playlist

from pytube.exceptions import PytubeError


class DownloadVideos:
    """
        Class to download youtube videos.
    """
    def __init__(self, url):
        self.url = url

    def check_url_type(self) -> bool:
        """
            Function to check if the URL contain a video
            or a playlist.

            Return (bool): True or False
        """
        try:
            if 'playlist' in self.url:
                return True
            return False
        except PytubeError as e:
            raise f"An error occurred! The error is: {e}"

    def download_video(self):
        """
            Function to download single video or a playlists videos
            from YouTube.
        """
        if self.check_url_type():
            playlist = Playlist(self.url)
            abs_path = os.getcwd()
            for video in playlist.videos:
                print(video.title)
                video.streams.filter(progressive=True,
                                     file_extension='mp4').desc().first()\
                                        .download(output_path=f'{abs_path}/{playlist.title}')
        else:
            video = YouTube(self.url)
            video.streams.filter(progressive=True,
                                 file_extension='mp4').desc().first().download()

print("Enter YouTube URL:")
url_ = input()
test = DownloadVideos(url=url_)
test.download_video()
