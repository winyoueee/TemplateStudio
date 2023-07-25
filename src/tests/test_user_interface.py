import pytest
from src.user_interface import UserInterface
from src.song import Song
from src.playlist import Playlist

def test_user_interface_initialization():
    ui = UserInterface()
    assert ui.current_user is None
    assert ui.current_song is None
    assert ui.current_playlist is None

def test_user_interface_play_song():
    ui = UserInterface()
    song = Song("Test Song", "Test Artist", "Test Album", "test.mp3")
    ui.play_song(song)
    assert ui.current_song == song

def test_user_interface_stop_song():
    ui = UserInterface()
    song = Song("Test Song", "Test Artist", "Test Album", "test.mp3")
    ui.play_song(song)
    ui.stop_song()
    assert ui.current_song is None

def test_user_interface_load_playlist():
    ui = UserInterface()
    playlist = Playlist("Test Playlist")
    ui.load_playlist(playlist)
    assert ui.current_playlist == playlist

def test_user_interface_save_playlist():
    ui = UserInterface()
    playlist = Playlist("Test Playlist")
    ui.load_playlist(playlist)
    ui.save_playlist()
    assert ui.current_playlist is None

def test_user_interface_load_library():
    ui = UserInterface()
    ui.load_library()
    assert ui.library is not None

def test_user_interface_save_library():
    ui = UserInterface()
    ui.load_library()
    ui.save_library()
    assert ui.library is None

def test_user_interface_update_settings():
    ui = UserInterface()
    ui.update_settings({"volume": 50})
    assert ui.settings["volume"] == 50

def test_user_interface_load_settings():
    ui = UserInterface()
    ui.load_settings()
    assert ui.settings is not None
