from typing import List


class PlayMixin:
    song_name = None
    @staticmethod
    def play(song_name: str):
        return f'Playing {song_name}'

class Song(PlayMixin)
    def __init__(self, title: str, artist: str, song_name=None):
        self.title = title
        self.artist = artist
        self.song_name = self.title + ' - ' + self.artist
        super().__init__(song_name)

class Playlist(PlayMixin):
    def __init__(self, name: str, songs: List, songs_name=None):
        self.name = name
        self.songs = songs
        super().__init__(songs_name)
#
