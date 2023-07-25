```python
import os
import pygame

class Song:
    def __init__(self, song_id, title, artist, album, duration, file_path):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.file_path = file_path

    def play_song(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()

    def get_song_details(self):
        return {
            'song_id': self.song_id,
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            'duration': self.duration,
            'file_path': self.file_path
        }

    def is_file_exists(self):
        return os.path.isfile(self.file_path)
```