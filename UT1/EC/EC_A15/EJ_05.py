class PlayMixin:
    @staticmethod
    def play(artis: str, song_name: str):
        print(f'Playing {artis} - {song_name}')


class Song(PlayMixin):
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def play(self, **kwargs):
        super().play(self.artist, self.title)


class Playlist(PlayMixin):
    def __init__(self, name: str, songs: list[Song]):
        self.name = name
        self.songs = songs

    def play(self, **kwargs):
        for song in self.songs:
            song.play()


song1 = Song("Bohemian Rhapsody", "Queen")
song1.play()

song2 = Song("Stairway to Heaven", "Led Zeppelin")
song3 = Song("Hotel California", "The Eagles")

playlist = Playlist("My playlist", [song1, song2, song3])
playlist.play()
