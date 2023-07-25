import pytest
from src import utils

def test_play_song():
    song = {"title": "Test Song", "artist": "Test Artist", "album": "Test Album", "path": "test_path.mp3"}
    utils.play_song(song)
    assert utils.current_song == song

def test_stop_song():
    song = {"title": "Test Song", "artist": "Test Artist", "album": "Test Album", "path": "test_path.mp3"}
    utils.play_song(song)
    utils.stop_song()
    assert utils.current_song == None

def test_load_playlist():
    playlist = [{"title": "Test Song 1", "artist": "Test Artist 1", "album": "Test Album 1", "path": "test_path1.mp3"},
                {"title": "Test Song 2", "artist": "Test Artist 2", "album": "Test Album 2", "path": "test_path2.mp3"}]
    utils.load_playlist(playlist)
    assert utils.current_playlist == playlist

def test_save_playlist():
    playlist = [{"title": "Test Song 1", "artist": "Test Artist 1", "album": "Test Album 1", "path": "test_path1.mp3"},
                {"title": "Test Song 2", "artist": "Test Artist 2", "album": "Test Album 2", "path": "test_path2.mp3"}]
    utils.load_playlist(playlist)
    utils.save_playlist()
    assert utils.current_playlist == None

def test_load_library():
    library = [{"title": "Test Song 1", "artist": "Test Artist 1", "album": "Test Album 1", "path": "test_path1.mp3"},
               {"title": "Test Song 2", "artist": "Test Artist 2", "album": "Test Album 2", "path": "test_path2.mp3"}]
    utils.load_library(library)
    assert utils.current_library == library

def test_save_library():
    library = [{"title": "Test Song 1", "artist": "Test Artist 1", "album": "Test Album 1", "path": "test_path1.mp3"},
               {"title": "Test Song 2", "artist": "Test Artist 2", "album": "Test Album 2", "path": "test_path2.mp3"}]
    utils.load_library(library)
    utils.save_library()
    assert utils.current_library == None

def test_update_settings():
    settings = {"volume": 50, "shuffle": False, "repeat": False}
    utils.update_settings(settings)
    assert utils.current_settings == settings

def test_load_settings():
    settings = {"volume": 50, "shuffle": False, "repeat": False}
    utils.load_settings(settings)
    assert utils.current_settings == settings
