import pytest
import pygame
from src.player import play_song, stop_song

def test_play_song():
    pygame.init()
    pygame.mixer.init()
    song_path = "path/to/song.mp3"
    play_song(song_path)
    assert pygame.mixer.music.get_busy() == True

def test_stop_song():
    pygame.init()
    pygame.mixer.init()
    song_path = "path/to/song.mp3"
    play_song(song_path)
    stop_song()
    assert pygame.mixer.music.get_busy() == False

if __name__ == "__main__":
    pytest.main()