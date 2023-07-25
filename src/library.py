import os
import sqlite3
from song import SongSchema

class Library:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                title TEXT,
                artist TEXT,
                album TEXT,
                duration INTEGER
            )
        """)

    def load_library(self):
        self.cursor.execute("SELECT * FROM songs")
        rows = self.cursor.fetchall()
        return [SongSchema(*row) for row in rows]

    def save_library(self, library):
        self.cursor.execute("DELETE FROM songs")
        for song in library:
            self.cursor.execute("INSERT INTO songs VALUES (?, ?, ?, ?)",
                                (song.id, song.title, song.artist, song.album, song.duration))
        self.conn.commit()

    def add_song(self, song):
        self.cursor.execute("INSERT INTO songs VALUES (?, ?, ?, ?)",
                            (song.id, song.title, song.artist, song.album, song.duration))
        self.conn.commit()

    def remove_song(self, song_id):
        self.cursor.execute("DELETE FROM songs WHERE id=?", (song_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()