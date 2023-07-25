import sqlite3
import pytest

from src.database import Database
from src.settings import UserSchema, SongSchema, PlaylistSchema

def setup_module(module):
    global db
    db = Database()

def teardown_module(module):
    db.close()

def test_create_users_table():
    db.create_table("users", UserSchema)
    assert "users" in db.get_table_names()

def test_create_songs_table():
    db.create_table("songs", SongSchema)
    assert "songs" in db.get_table_names()

def test_create_playlists_table():
    db.create_table("playlists", PlaylistSchema)
    assert "playlists" in db.get_table_names()

def test_insert_user():
    user = {"username": "test", "password": "test"}
    db.insert("users", user)
    assert db.select_one("users", {"username": "test"}) == user

def test_insert_song():
    song = {"title": "test", "artist": "test", "album": "test", "path": "test.mp3"}
    db.insert("songs", song)
    assert db.select_one("songs", {"title": "test"}) == song

def test_insert_playlist():
    playlist = {"name": "test", "songs": ["test.mp3"]}
    db.insert("playlists", playlist)
    assert db.select_one("playlists", {"name": "test"}) == playlist

def test_update_user():
    user = {"username": "test", "password": "newtest"}
    db.update("users", {"username": "test"}, user)
    assert db.select_one("users", {"username": "test"})["password"] == "newtest"

def test_update_song():
    song = {"title": "test", "artist": "newtest", "album": "newtest", "path": "newtest.mp3"}
    db.update("songs", {"title": "test"}, song)
    assert db.select_one("songs", {"title": "test"})["artist"] == "newtest"

def test_update_playlist():
    playlist = {"name": "test", "songs": ["newtest.mp3"]}
    db.update("playlists", {"name": "test"}, playlist)
    assert db.select_one("playlists", {"name": "test"})["songs"] == ["newtest.mp3"]

def test_delete_user():
    db.delete("users", {"username": "test"})
    assert db.select_one("users", {"username": "test"}) is None

def test_delete_song():
    db.delete("songs", {"title": "test"})
    assert db.select_one("songs", {"title": "test"}) is None

def test_delete_playlist():
    db.delete("playlists", {"name": "test"})
    assert db.select_one("playlists", {"name": "test"}) is None