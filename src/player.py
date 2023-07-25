import pygame
from .song import Song

class Player:
    def __init__(self):
        pygame.mixer.init()
        self.current_song = None

    def play_song(self, song: Song):
        if self.current_song is not None:
            self.stop_song()
        self.current_song = song
        pygame.mixer.music.load(song.file_path)
        pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()
        self.current_song = None

    def pause_song(self):
        pygame.mixer.music.pause()

    def resume_song(self):
        pygame.mixer.music.unpause()

    def is_playing(self):
        return pygame.mixer.music.get_busy()