import pytest
from src.playlist import Playlist
from src.song import Song

def test_playlist_creation():
    playlist = Playlist("My Playlist")
    assert playlist.name == "My Playlist"
    assert playlist.songs == []

def test_add_song():
    playlist = Playlist("My Playlist")
    song = Song("Song Title", "Song Artist", "Song Album", "Song Path")
    playlist.add_song(song)
    assert len(playlist.songs) == 1
    assert playlist.songs[0] == song

def test_remove_song():
    playlist = Playlist("My Playlist")
    song = Song("Song Title", "Song Artist", "Song Album", "Song Path")
    playlist.add_song(song)
    playlist.remove_song(song)
    assert len(playlist.songs) == 0

def test_load_playlist():
    playlist = Playlist("My Playlist")
    song1 = Song("Song Title 1", "Song Artist 1", "Song Album 1", "Song Path 1")
    song2 = Song("Song Title 2", "Song Artist 2", "Song Album 2", "Song Path 2")
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.save_playlist()
    loaded_playlist = Playlist.load_playlist("My Playlist")
    assert loaded_playlist.songs == [song1, song2]

def test_save_playlist():
    playlist = Playlist("My Playlist")
    song1 = Song("Song Title 1", "Song Artist 1", "Song Album 1", "Song Path 1")
    song2 = Song("Song Title 2", "Song Artist 2", "Song Album 2", "Song Path 2")
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.save_playlist()
    loaded_playlist = Playlist.load_playlist("My Playlist")
    assert loaded_playlist.songs == [song1, song2]