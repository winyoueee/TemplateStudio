import pytest
from src.library import load_library, save_library
from src.song import Song

def test_load_library():
    # Assuming the library is empty at the start
    library = load_library()
    assert library == []

    # Add a song to the library
    song = Song("Test Song", "Test Artist", "Test Album", "test.mp3")
    library.append(song)
    save_library(library)

    # Load the library again and check if the song is there
    library = load_library()
    assert len(library) == 1
    assert library[0].title == "Test Song"
    assert library[0].artist == "Test Artist"
    assert library[0].album == "Test Album"
    assert library[0].file_path == "test.mp3"

def test_save_library():
    # Create a new library with one song
    song = Song("Test Song", "Test Artist", "Test Album", "test.mp3")
    library = [song]
    save_library(library)

    # Load the library and check if the song is there
    library = load_library()
    assert len(library) == 1
    assert library[0].title == "Test Song"
    assert library[0].artist == "Test Artist"
    assert library[0].album == "Test Album"
    assert library[0].file_path == "test.mp3"