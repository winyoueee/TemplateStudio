import pytest
from src.song import Song, SongSchema

def test_song_creation():
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "album": "Test Album",
        "duration": 180
    }
    song = Song(song_data)
    assert song.title == "Test Song"
    assert song.artist == "Test Artist"
    assert song.album == "Test Album"
    assert song.duration == 180

def test_song_schema():
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "album": "Test Album",
        "duration": 180
    }
    schema = SongSchema()
    result = schema.load(song_data)
    assert result.title == "Test Song"
    assert result.artist == "Test Artist"
    assert result.album == "Test Album"
    assert result.duration == 180

def test_song_duration():
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "album": "Test Album",
        "duration": 180
    }
    song = Song(song_data)
    assert song.duration == 180

def test_song_artist():
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "album": "Test Album",
        "duration": 180
    }
    song = Song(song_data)
    assert song.artist == "Test Artist"